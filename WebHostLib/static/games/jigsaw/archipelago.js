var __defProp = Object.defineProperty;
var __export = (target, all) => {
  for (var name in all)
    __defProp(target, name, {
      get: all[name],
      enumerable: true,
      configurable: true,
      set: (newValue) => all[name] = () => newValue
    });
};

// src/api/index.ts
var exports_api = {};
__export(exports_api, {
  slotTypes: () => slotTypes,
  permissions: () => permissions,
  itemsHandlingFlags: () => itemsHandlingFlags,
  itemClassifications: () => itemClassifications,
  clientStatuses: () => clientStatuses
});

// src/api/constants.ts
var clientStatuses = {
  disconnected: 0,
  connected: 5,
  ready: 10,
  playing: 20,
  goal: 30
};
var itemClassifications = {
  progression: 1,
  useful: 2,
  trap: 4,
  none: 0
};
var itemsHandlingFlags = {
  minimal: 0,
  others: 1,
  own: 2,
  starting: 4,
  all: 7
};
var permissions = {
  disabled: 0,
  enabled: 1,
  goal: 2,
  auto: 6,
  autoEnabled: 7
};
var slotTypes = {
  spectator: 0,
  player: 1,
  group: 2
};
// src/errors.ts
class SocketError extends Error {
}

class ArgumentError extends Error {
  argumentName;
  value;
  constructor(message, argumentName, value) {
    super(message);
    this.argumentName = argumentName;
    this.value = structuredClone(value);
  }
}

class LoginError extends Error {
  errors = [];
  constructor(message, errors) {
    super(message);
    this.errors = errors;
  }
}

class UnauthenticatedError extends Error {
}

// src/interfaces/ClientOptions.ts
var defaultClientOptions = {
  timeout: 1e4,
  autoFetchDataPackage: true,
  maximumMessages: 1000,
  debugLogVersions: true
};

// src/constants.ts
var targetVersion = { major: 0, minor: 5, build: 1 };
var libraryVersion = "2.0.4";

// src/utils.ts
function uuid() {
  const uuid2 = [];
  for (let i = 0;i < 36; i++) {
    uuid2.push(Math.floor(Math.random() * 16));
  }
  uuid2[14] = 4;
  uuid2[19] = uuid2[19] &= ~(1 << 2);
  uuid2[19] = uuid2[19] |= 1 << 3;
  uuid2[8] = uuid2[13] = uuid2[18] = uuid2[23] = "-";
  return uuid2.map((d) => d.toString(16)).join("");
}

// src/interfaces/ConnectionOptions.ts
var defaultConnectionOptions = {
  password: "",
  uuid: uuid(),
  tags: [],
  version: targetVersion,
  items: itemsHandlingFlags.all,
  slotData: true
};

// src/classes/Item.ts
class Item {
  #client;
  #item;
  #sender;
  #receiver;
  constructor(client, item, sender, receiver) {
    this.#client = client;
    this.#item = item;
    this.#sender = sender;
    this.#receiver = receiver;
  }
  toString() {
    return this.name;
  }
  get receiver() {
    return this.#receiver;
  }
  get sender() {
    return this.#sender;
  }
  get name() {
    return this.#client.package.lookupItemName(this.game, this.#item.item, true);
  }
  get id() {
    return this.#item.item;
  }
  get locationName() {
    return this.#client.package.lookupLocationName(this.sender.game, this.#item.location, true);
  }
  get locationId() {
    return this.#item.location;
  }
  get locationGame() {
    return this.sender.game;
  }
  get game() {
    return this.receiver.game;
  }
  get progression() {
    return (this.flags & itemClassifications.progression) === itemClassifications.progression;
  }
  get useful() {
    return (this.flags & itemClassifications.useful) === itemClassifications.useful;
  }
  get trap() {
    return (this.flags & itemClassifications.trap) === itemClassifications.trap;
  }
  get filler() {
    return this.flags === itemClassifications.none;
  }
  get flags() {
    return this.#item.flags;
  }
}

// src/classes/PackageMetadata.ts
class PackageMetadata {
  game;
  checksum;
  itemTable;
  locationTable;
  reverseItemTable;
  reverseLocationTable;
  constructor(game, _package) {
    this.game = game;
    this.checksum = _package.checksum;
    this.itemTable = Object.freeze(_package.item_name_to_id);
    this.locationTable = Object.freeze(_package.location_name_to_id);
    this.reverseItemTable = Object.freeze(Object.fromEntries(Object.entries(this.itemTable).map(([k, v]) => [v, k])));
    this.reverseLocationTable = Object.freeze(Object.fromEntries(Object.entries(this.locationTable).map(([k, v]) => [v, k])));
  }
  exportPackage() {
    return {
      checksum: this.checksum,
      item_name_to_id: { ...this.itemTable },
      location_name_to_id: { ...this.locationTable }
    };
  }
}

// src/classes/managers/DataPackageManager.ts
class DataPackageManager {
  #client;
  #packages = new Map;
  #checksums = new Map;
  #games = new Set;
  constructor(client) {
    this.#client = client;
    this.#client.socket.on("roomInfo", (packet) => {
      this.#packages.clear();
      this.#checksums.clear();
      this.#games.clear();
      this.#packages.set("Archipelago", this.#preloadArchipelago());
      for (const game in packet.datapackage_checksums) {
        this.#checksums.set(game, packet.datapackage_checksums[game]);
        this.#games.add(game);
      }
    });
  }
  findPackage(game) {
    return this.#packages.get(game) ?? null;
  }
  async fetchPackage(games = [], update = true) {
    if (games.length === 0) {
      games = Array.from(this.#games);
    }
    games = games.filter((game) => {
      if (!this.#games.has(game))
        return false;
      if (this.#packages.get(game)?.checksum !== this.#checksums.get(game))
        return true;
      return false;
    });
    const data = { games: {} };
    for (const game of games) {
      const request = { cmd: "GetDataPackage", games: [game] };
      const [response] = await this.#client.socket.send(request).wait("dataPackage");
      data.games[game] = response.data.games[game];
    }
    if (update) {
      this.importPackage(data);
    }
    return data;
  }
  importPackage(dataPackage) {
    for (const game in dataPackage.games) {
      this.#packages.set(game, new PackageMetadata(game, dataPackage.games[game]));
      this.#checksums.set(game, dataPackage.games[game].checksum);
    }
  }
  exportPackage() {
    return {
      games: this.#packages.entries().reduce((games, [game, pkg]) => {
        games[game] = pkg.exportPackage();
        return games;
      }, {})
    };
  }
  lookupItemName(game, id, fallback = true) {
    const fallbackName = `Unknown Item ${id}`;
    const gamePackage = this.findPackage(game);
    if (!gamePackage) {
      return fallback ? fallbackName : undefined;
    }
    const name = gamePackage.reverseItemTable[id];
    if (fallback && name === undefined) {
      return fallbackName;
    }
    return name;
  }
  lookupLocationName(game, id, fallback = true) {
    const fallbackName = `Unknown Location ${id}`;
    const gamePackage = this.findPackage(game);
    if (!gamePackage) {
      return fallback ? fallbackName : undefined;
    }
    const name = gamePackage.reverseLocationTable[id];
    if (fallback && name === undefined) {
      return fallbackName;
    }
    return name;
  }
  #preloadArchipelago() {
    return new PackageMetadata("Archipelago", {
      checksum: "ac9141e9ad0318df2fa27da5f20c50a842afeecb",
      item_name_to_id: { Nothing: -1 },
      location_name_to_id: { "Cheat Console": -1, Server: -2 }
    });
  }
}

// src/classes/IntermediateDataOperation.ts
class IntermediateDataOperation {
  #client;
  #operations = [];
  #key;
  #default;
  constructor(client, key, _default) {
    this.#client = client;
    this.#key = key;
    this.#default = _default;
  }
  replace(value) {
    this.#operations.push({ operation: "replace", value });
    return this;
  }
  default() {
    this.#operations.push({ operation: "default", value: null });
    return this;
  }
  add(value) {
    this.#operations.push({ operation: "add", value });
    return this;
  }
  multiply(value) {
    this.#operations.push({ operation: "mul", value });
    return this;
  }
  power(value) {
    this.#operations.push({ operation: "pow", value });
    return this;
  }
  remainder(value) {
    this.#operations.push({ operation: "mod", value });
    return this;
  }
  floor() {
    this.#operations.push({ operation: "floor", value: null });
    return this;
  }
  ceiling() {
    this.#operations.push({ operation: "ceil", value: null });
    return this;
  }
  max(value) {
    this.#operations.push({ operation: "max", value });
    return this;
  }
  min(value) {
    this.#operations.push({ operation: "min", value });
    return this;
  }
  and(value) {
    this.#operations.push({ operation: "and", value });
    return this;
  }
  or(value) {
    this.#operations.push({ operation: "or", value });
    return this;
  }
  xor(value) {
    this.#operations.push({ operation: "xor", value });
    return this;
  }
  leftShift(value) {
    this.#operations.push({ operation: "left_shift", value });
    return this;
  }
  rightShift(value) {
    this.#operations.push({ operation: "right_shift", value });
    return this;
  }
  remove(value) {
    this.#operations.push({ operation: "remove", value });
    return this;
  }
  pop(value) {
    this.#operations.push({ operation: "pop", value });
    return this;
  }
  update(value) {
    this.#operations.push({ operation: "update", value });
    return this;
  }
  async commit(awaitReply = false) {
    const _uuid = uuid();
    const request = {
      cmd: "Set",
      default: this.#default,
      key: this.#key,
      operations: this.#operations,
      want_reply: awaitReply,
      uuid: _uuid
    };
    this.#client.socket.send(request);
    if (!awaitReply) {
      return;
    }
    const [response] = await this.#client.socket.wait("setReply", (packet) => packet.uuid === _uuid);
    return response.value;
  }
}

// src/classes/managers/DataStorageManager.ts
class DataStorageManager {
  #client;
  #storage = {};
  #subscribers = {};
  constructor(client) {
    this.#client = client;
    this.#client.socket.on("disconnected", () => {
      this.#storage = {};
      this.#subscribers = {};
    }).on("setReply", (packet) => {
      this.#storage[packet.key] = packet.value;
      const callbacks = this.#subscribers[packet.key];
      if (callbacks) {
        callbacks.forEach((callback) => callback(packet.key, packet.value, packet.original_value));
      }
    }).on("connected", () => {
      if (this.#client.options.debugLogVersions) {
        const key = `${this.#client.game}:${libraryVersion}:${navigator?.userAgent}`;
        this.prepare("archipelago.js__runtimes", {}).default().update({ [key]: true }).commit(false);
      }
    });
  }
  get store() {
    return structuredClone(this.#storage);
  }
  async fetch(input, monitor = false) {
    let keys = typeof input === "string" ? [input] : input;
    if (monitor) {
      const monitorKeys = keys.filter((key) => this.#storage[key] === undefined);
      if (monitorKeys.length > 0) {
        this.#client.socket.send({ cmd: "SetNotify", keys: monitorKeys });
      }
    }
    let data = {};
    keys = keys.filter((key) => {
      const value = structuredClone(this.#storage[key]);
      const exists = value !== undefined;
      if (exists) {
        data[key] = value;
      }
      return !exists;
    });
    if (keys.length > 0) {
      const response = await this.#get(keys);
      data = { ...data, ...response };
    }
    if (monitor) {
      this.#storage = { ...this.#storage, ...data };
    }
    return typeof input === "string" ? data[input] : data;
  }
  async notify(keys, callback) {
    keys.forEach((key) => {
      this.#subscribers[key] ??= [];
      this.#subscribers[key].push(callback);
    });
    return this.fetch(keys, true);
  }
  prepare(key, _default) {
    if (key.startsWith("_read_")) {
      throw TypeError("Cannot manipulate read only keys.");
    }
    return new IntermediateDataOperation(this.#client, key, _default);
  }
  async fetchItemNameGroups(game) {
    return await this.fetch([`_read_item_name_groups_${game}`], true);
  }
  async fetchLocationNameGroups(game) {
    return await this.fetch([`_read_location_name_groups_${game}`], true);
  }
  async#get(keys) {
    const _uuid = uuid();
    const [response] = await this.#client.socket.send({ cmd: "Get", keys, uuid: _uuid }).wait("retrieved", (packet) => packet.uuid === _uuid);
    return response.keys;
  }
}

// src/classes/ArchipelagoEventEmitter.ts
class ArchipelagoEventEmitter {
  #events = {};
  addEventListener(event, callback, once = false) {
    this.#events[event] ??= [];
    this.#events[event].push([callback, once]);
  }
  removeEventListener(event, callback) {
    const callbacks = this.#events[event];
    if (callbacks && callbacks.length > 0) {
      this.#events[event] = callbacks.filter(([cb]) => cb !== callback);
    }
  }
  dispatchEvent(event, data) {
    const callbacks = this.#events[event] ?? [];
    for (const [callback, once] of callbacks) {
      callback(...data);
      if (once) {
        this.removeEventListener(event, callback);
      }
    }
  }
}

// src/classes/managers/EventBasedManager.ts
class EventBasedManager {
  #events = new ArchipelagoEventEmitter;
  on(event, listener) {
    this.#events.addEventListener(event, listener);
    return this;
  }
  off(event, listener) {
    this.#events.removeEventListener(event, listener);
    return this;
  }
  async wait(event, clearPredicate = () => true) {
    return new Promise((resolve) => {
      const listener = (...args) => {
        if (clearPredicate(...args)) {
          this.#events.removeEventListener(event, listener);
          resolve(args);
        }
      };
      this.#events.addEventListener(event, listener);
    });
  }
  emit(event, detail) {
    this.#events.dispatchEvent(event, detail);
  }
}

// src/classes/managers/DeathLinkManager.ts
class DeathLinkManager extends EventBasedManager {
  #client;
  #lastDeath = Number.MIN_SAFE_INTEGER;
  constructor(client) {
    super();
    this.#client = client;
    this.#client.socket.on("bounced", (packet) => {
      if (packet.tags?.includes("DeathLink") && packet.data.time && packet.data.source) {
        const deathLink = packet.data;
        if (deathLink.time === this.#lastDeath) {
          return;
        }
        this.#lastDeath = deathLink.time;
        this.emit("deathReceived", [deathLink.source, deathLink.time * 1000, deathLink.cause]);
      }
    });
  }
  get enabled() {
    return this.#client.arguments.tags.includes("DeathLink");
  }
  enableDeathLink() {
    if (this.#client.arguments.tags.includes("DeathLink")) {
      return;
    }
    this.#client.updateTags([...this.#client.arguments.tags, "DeathLink"]);
  }
  disableDeathLink() {
    if (!this.#client.arguments.tags.includes("DeathLink")) {
      return;
    }
    this.#client.updateTags(this.#client.arguments.tags.filter((tag) => tag !== "DeathLink"));
  }
  sendDeathLink(source, cause) {
    if (!this.#client.authenticated) {
      throw new UnauthenticatedError("Cannot send death links before connecting and authenticating.");
    }
    if (!this.enabled) {
      return;
    }
    this.#lastDeath = Math.ceil(Date.now() / 1000);
    const deathLink = {
      source,
      cause,
      time: this.#lastDeath
    };
    this.#client.bounce({ tags: ["DeathLink"] }, deathLink);
  }
}

// src/classes/Hint.ts
class Hint {
  #client;
  #hint;
  #item;
  constructor(client, hint) {
    this.#client = client;
    this.#hint = hint;
    this.#item = new Item(this.#client, { item: hint.item, location: hint.location, player: hint.finding_player, flags: hint.item_flags }, this.#client.players.findPlayer(hint.finding_player), this.#client.players.findPlayer(hint.receiving_player));
  }
  get item() {
    return this.#item;
  }
  get found() {
    return this.#hint.found;
  }
  get entrance() {
    return this.#hint.entrance || "Vanilla";
  }
}

// src/classes/managers/ItemsManager.ts
class ItemsManager extends EventBasedManager {
  #client;
  #received = [];
  #hints = [];
  constructor(client) {
    super();
    this.#client = client;
    this.#client.socket.on("receivedItems", (packet) => {
      let index = packet.index;
      const count = packet.items.length;
      const items = [...packet.items];
      while (items.length > 0) {
        const networkItem = items.shift();
        this.#received[index++] = new Item(this.#client, networkItem, this.#client.players.findPlayer(networkItem.player), this.#client.players.self);
      }
      this.emit("itemsReceived", [this.#received.slice(packet.index, packet.index + count), packet.index]);
    }).on("connected", () => {
      this.#hints = [];
      this.#received = [];
      this.#client.storage.notify([`_read_hints_${this.#client.players.self.team}_${this.#client.players.self.slot}`], this.#receivedHint.bind(this)).then((data) => {
        const hints = data[`_read_hints_${this.#client.players.self.team}_${this.#client.players.self.slot}`];
        this.#hints = hints.map((hint) => new Hint(this.#client, hint));
        this.emit("hintsInitialized", [this.#hints]);
      }).catch((error) => {
        throw error;
      });
    });
  }
  get received() {
    return [...this.#received];
  }
  get hints() {
    return [...this.#hints];
  }
  get count() {
    return this.#received.length;
  }
  #receivedHint(_, hints) {
    for (let i = 0;i < hints.length; i++) {
      if (this.#hints[i] === undefined) {
        this.#hints[i] = new Hint(this.#client, hints[i]);
        this.emit("hintReceived", [this.#hints[i]]);
      } else if (this.#hints[i].found !== hints[i].found) {
        this.#hints[i] = new Hint(this.#client, hints[i]);
        this.emit("hintFound", [this.#hints[i]]);
      }
    }
  }
}

// src/classes/MessageNode.ts
class BaseMessageNode {
  client;
  part;
  constructor(client, part) {
    this.client = client;
    this.part = part;
  }
  toString() {
    return this.text;
  }
}

class ItemMessageNode extends BaseMessageNode {
  part;
  type = "item";
  item;
  constructor(client, part, item, receiver) {
    super(client, part);
    const player = client.players.findPlayer(part.player, receiver.team);
    this.part = part;
    this.item = new Item(client, item, player, receiver);
  }
  get text() {
    return this.item.name;
  }
}

class LocationMessageNode extends BaseMessageNode {
  #name;
  part;
  type = "location";
  id;
  constructor(client, part) {
    super(client, part);
    const player = client.players.findPlayer(part.player);
    const pkg = client.package.findPackage(player.game);
    this.part = part;
    if (part.type === "location_name") {
      this.#name = part.text;
      this.id = pkg.locationTable[part.text];
    } else {
      this.id = parseInt(part.text);
      this.#name = client.package.lookupLocationName(player.game, this.id, true);
    }
  }
  get text() {
    return this.#name;
  }
}

class ColorMessageNode extends BaseMessageNode {
  part;
  type = "color";
  color;
  constructor(client, part) {
    super(client, part);
    this.part = part;
    this.color = part.color;
  }
  get text() {
    return this.part.text;
  }
}

class TextualMessageNode extends BaseMessageNode {
  part;
  type;
  constructor(client, part) {
    super(client, part);
    this.part = part;
    if (this.part.type === "entrance_name") {
      this.type = "entrance";
    } else {
      this.type = "text";
    }
  }
  get text() {
    return this.part.text;
  }
}

class PlayerMessageNode extends BaseMessageNode {
  part;
  type = "player";
  player;
  constructor(client, part) {
    super(client, part);
    this.part = part;
    if (part.type === "player_id") {
      this.player = client.players.findPlayer(parseInt(part.text));
    } else {
      const player = client.players.teams[client.players.self.team].find((p) => p.name === part.text);
      if (!player) {
        throw new Error(`Cannot find player under name: ${part.text}`);
      }
      this.player = player;
    }
  }
  get text() {
    return this.player.alias;
  }
}

// src/classes/managers/MessageManager.ts
class MessageManager extends EventBasedManager {
  #client;
  #messages = [];
  get log() {
    return [...this.#messages];
  }
  constructor(client) {
    super();
    this.#client = client;
    this.#client.socket.on("printJSON", this.#onPrintJSON.bind(this));
  }
  async say(text) {
    if (!this.#client.authenticated) {
      throw new UnauthenticatedError("Cannot send chat messages without being authenticated.");
    }
    text = text.trim();
    const request = { cmd: "Say", text };
    this.#client.socket.send(request);
    await this.wait("chat", (message) => message === text);
  }
  #onPrintJSON(packet) {
    const nodes = [];
    for (const part of packet.data) {
      switch (part.type) {
        case "item_id":
        case "item_name": {
          const itemPacket = packet;
          let receiver;
          if (itemPacket.type === "ItemCheat") {
            receiver = this.#client.players.findPlayer(itemPacket.receiving, itemPacket.team);
          } else {
            receiver = this.#client.players.findPlayer(itemPacket.receiving);
          }
          nodes.push(new ItemMessageNode(this.#client, part, itemPacket.item, receiver));
          break;
        }
        case "location_id":
        case "location_name": {
          nodes.push(new LocationMessageNode(this.#client, part));
          break;
        }
        case "color": {
          nodes.push(new ColorMessageNode(this.#client, part));
          break;
        }
        case "player_id":
        case "player_name": {
          nodes.push(new PlayerMessageNode(this.#client, part));
          break;
        }
        default: {
          nodes.push(new TextualMessageNode(this.#client, part));
          break;
        }
      }
    }
    const text = nodes.map((node) => node.text).join();
    if (this.#client.options.maximumMessages >= 1) {
      this.log.push({ text, nodes });
      this.log.splice(0, this.log.length - this.#client.options.maximumMessages);
    }
    switch (packet.type) {
      case "ItemSend": {
        const sender = this.#client.players.findPlayer(packet.item.player);
        const receiver = this.#client.players.findPlayer(packet.receiving);
        const item = new Item(this.#client, packet.item, sender, receiver);
        this.emit("itemSent", [text, item, nodes]);
        break;
      }
      case "ItemCheat": {
        const sender = this.#client.players.findPlayer(packet.item.player, packet.team);
        const receiver = this.#client.players.findPlayer(packet.receiving, packet.team);
        const item = new Item(this.#client, packet.item, sender, receiver);
        this.emit("itemCheated", [text, item, nodes]);
        break;
      }
      case "Hint": {
        const sender = this.#client.players.findPlayer(packet.item.player);
        const receiver = this.#client.players.findPlayer(packet.receiving);
        const item = new Item(this.#client, packet.item, sender, receiver);
        this.emit("itemHinted", [text, item, packet.found, nodes]);
        break;
      }
      case "Join": {
        const player = this.#client.players.findPlayer(packet.slot, packet.team);
        this.emit("connected", [text, player, packet.tags, nodes]);
        break;
      }
      case "Part": {
        const player = this.#client.players.findPlayer(packet.slot, packet.team);
        this.emit("disconnected", [text, player, nodes]);
        break;
      }
      case "Chat": {
        const player = this.#client.players.findPlayer(packet.slot, packet.team);
        this.emit("chat", [packet.message, player, nodes]);
        break;
      }
      case "ServerChat": {
        this.emit("serverChat", [packet.message, nodes]);
        break;
      }
      case "TagsChanged": {
        const player = this.#client.players.findPlayer(packet.slot, packet.team);
        this.emit("tagsUpdated", [text, player, packet.tags, nodes]);
        break;
      }
      case "Tutorial": {
        this.emit("tutorial", [text, nodes]);
        break;
      }
      case "CommandResult": {
        this.emit("userCommand", [text, nodes]);
        break;
      }
      case "AdminCommandResult": {
        this.emit("adminCommand", [text, nodes]);
        break;
      }
      case "Goal": {
        const player = this.#client.players.findPlayer(packet.slot, packet.team);
        this.emit("goaled", [text, player, nodes]);
        break;
      }
      case "Release": {
        const player = this.#client.players.findPlayer(packet.slot, packet.team);
        this.emit("released", [text, player, nodes]);
        break;
      }
      case "Collect": {
        const player = this.#client.players.findPlayer(packet.slot, packet.team);
        this.emit("collected", [text, player, nodes]);
        break;
      }
      case "Countdown": {
        this.emit("countdown", [text, packet.countdown, nodes]);
      }
    }
    this.emit("message", [text, nodes]);
  }
}

// src/classes/Player.ts
class Player {
  #client;
  #player;
  constructor(client, player) {
    this.#client = client;
    this.#player = player;
  }
  toString() {
    return this.alias;
  }
  get name() {
    return this.#player.name;
  }
  get alias() {
    return this.#player.alias;
  }
  get game() {
    if (this.slot === 0) {
      return "Archipelago";
    }
    return this.#networkSlot.game;
  }
  get type() {
    if (this.slot === 0) {
      return slotTypes.spectator;
    }
    return this.#networkSlot.type;
  }
  get team() {
    return this.#player.team;
  }
  get slot() {
    return this.#player.slot;
  }
  get members() {
    if (this.type !== slotTypes.group) {
      return [];
    }
    return this.#client.players.teams[this.team].filter((player) => this.#networkSlot.group_members.includes(player.slot));
  }
  get groups() {
    if (this.slot === 0) {
      return [];
    }
    return this.#client.players.teams[this.team].filter((player) => player.slot !== 0 && this.#client.players.slots[player.slot].group_members.includes(this.slot));
  }
  async fetchStatus() {
    if (this.type === slotTypes.group) {
      return clientStatuses.goal;
    }
    return await this.#client.storage.fetch(`_read_client_status_${this.team}_${this.slot}`) ?? 0;
  }
  async fetchSlotData() {
    return await this.#client.storage.fetch(`_read_slot_data_${this.slot}`);
  }
  async fetchHints() {
    const hints = await this.#client.storage.fetch(`_read_hints_${this.team}_${this.slot}`);
    return hints.map((hint) => new Hint(this.#client, hint));
  }
  get #networkSlot() {
    return this.#client.players.slots[this.slot];
  }
}

// src/classes/managers/PlayersManager.ts
class PlayersManager extends EventBasedManager {
  #client;
  #players = [];
  #slots = {};
  #slot = 0;
  #team = 0;
  constructor(client) {
    super();
    this.#client = client;
    this.#client.socket.on("connected", (packet) => {
      this.#slots = Object.freeze(packet.slot_info);
      this.#players = [];
      this.#slot = packet.slot;
      this.#team = packet.team;
      for (const player of packet.players) {
        this.#players[player.team] ??= [{ team: player.team, slot: 0, name: "Archipelago", alias: "Archipelago" }];
        this.#players[player.team][player.slot] = player;
      }
    }).on("roomUpdate", (packet) => {
      if (!packet.players) {
        return;
      }
      for (const player of packet.players) {
        if (this.#players[player.team][player.slot].alias !== player.alias) {
          const oldAlias = this.#players[player.team][player.slot].alias;
          this.#players[player.team][player.slot] = player;
          this.emit("aliasUpdated", [new Player(this.#client, player), oldAlias, player.alias]);
        }
      }
    });
  }
  get self() {
    if (this.#slot === 0) {
      throw new Error("Cannot lookup own player object when client has never connected to a server.");
    }
    return new Player(this.#client, this.#players[this.#team][this.#slot]);
  }
  get slots() {
    return this.#slots;
  }
  get teams() {
    const players = [];
    for (let team = 0;team < this.#players.length; team++) {
      players[team] = [];
      for (let player = 0;player < this.#players[team].length; player++) {
        players[team].push(new Player(this.#client, this.#players[team][player]));
      }
    }
    return players;
  }
  findPlayer(slot, team) {
    if (team === undefined) {
      team = this.#client.players.self.team;
    }
    const playerTeam = this.#players[team];
    if (playerTeam) {
      return new Player(this.#client, this.#players[team][slot]);
    }
    return;
  }
}

// src/classes/managers/RoomStateManager.ts
class RoomStateManager extends EventBasedManager {
  #client;
  #serverVersion = { major: -1, minor: -1, build: -1 };
  #generatorVersion = { major: -1, minor: -1, build: -1 };
  #games = [];
  #tags = [];
  #seed = "";
  #password = false;
  #hintPoints = 0;
  #hintCost = 0;
  #locationCheckPoints = 0;
  #permissions = { release: 0, collect: 0, remaining: 0 };
  #missingLocations = [];
  #checkedLocations = [];
  #race = false;
  get serverVersion() {
    return { ...this.#serverVersion };
  }
  get generatorVersion() {
    return { ...this.#generatorVersion };
  }
  get games() {
    return [...this.#games];
  }
  get tags() {
    return [...this.#tags];
  }
  get seedName() {
    return this.#seed;
  }
  get password() {
    return this.#password;
  }
  get permissions() {
    return { ...this.#permissions };
  }
  get hintPoints() {
    return this.#hintPoints;
  }
  get hintCost() {
    if (this.hintCostPercentage > 0) {
      return Math.max(1, Math.floor(this.hintCostPercentage * this.allLocations.length * 0.01));
    }
    return 0;
  }
  get hintCostPercentage() {
    return this.#hintCost;
  }
  get locationCheckPoints() {
    return this.#locationCheckPoints;
  }
  get missingLocations() {
    return [...this.#missingLocations].sort();
  }
  get checkedLocations() {
    return [...this.#checkedLocations].sort();
  }
  get allLocations() {
    return [...this.#missingLocations, ...this.#checkedLocations].sort();
  }
  get race() {
    return this.#race;
  }
  constructor(client) {
    super();
    this.#client = client;
    this.#client.socket.on("roomInfo", (packet) => {
      this.#serverVersion = {
        major: packet.version.major,
        minor: packet.version.minor,
        build: packet.version.build
      };
      this.#generatorVersion = {
        major: packet.generator_version.major,
        minor: packet.generator_version.minor,
        build: packet.generator_version.build
      };
      this.#tags = packet.tags;
      this.#games = packet.games;
      this.#seed = packet.seed_name;
      this.#password = packet.password;
      this.#permissions = packet.permissions;
      this.#hintCost = packet.hint_cost;
      this.#locationCheckPoints = packet.location_check_points;
    }).on("connected", (packet) => {
      this.#missingLocations = packet.missing_locations;
      this.#checkedLocations = packet.checked_locations;
      this.emit("locationsChecked", [this.checkedLocations]);
      this.#hintPoints = packet.hint_points;
      this.emit("hintPointsUpdated", [0, packet.hint_points]);
    }).on("roomUpdate", (packet) => {
      if (packet.hint_cost !== undefined) {
        const [oc, op] = [this.hintCost, this.hintCostPercentage];
        this.#hintCost = packet.hint_cost;
        this.emit("hintCostUpdated", [oc, this.hintCost, op, this.hintCostPercentage]);
      }
      if (packet.hint_points !== undefined) {
        const old = this.#hintPoints;
        this.#hintPoints = packet.hint_points;
        this.emit("hintPointsUpdated", [old, this.hintPoints]);
      }
      if (packet.location_check_points !== undefined) {
        const old = this.#locationCheckPoints;
        this.#locationCheckPoints = packet.location_check_points;
        this.emit("locationCheckPointsUpdated", [old, this.locationCheckPoints]);
      }
      if (packet.password !== undefined) {
        this.#password = packet.password;
        this.emit("passwordUpdated", [this.password]);
      }
      if (packet.permissions !== undefined) {
        const old = this.#permissions;
        this.#permissions = packet.permissions;
        this.emit("permissionsUpdated", [old, this.permissions]);
      }
      if (packet.checked_locations !== undefined) {
        this.#checkedLocations = [...this.#checkedLocations, ...packet.checked_locations];
        this.#missingLocations = this.missingLocations.filter((location) => !packet.checked_locations?.includes(location));
        this.emit("locationsChecked", [packet.checked_locations]);
      }
    });
  }
}

// src/classes/managers/SocketManager.ts
class SocketManager extends EventBasedManager {
  #socket = null;
  #connected = false;
  constructor() {
    super();
  }
  get connected() {
    return this.#connected;
  }
  get url() {
    return this.#socket?.url ?? "";
  }
  send(...packets2) {
    if (this.#socket) {
      this.#socket.send(JSON.stringify(packets2));
      this.emit("sentPackets", [packets2]);
      return this;
    }
    throw new SocketError("Unable to send packets to the server; not connected to a server.");
  }
  async connect(url) {
    this.disconnect();
    if (typeof url === "string") {
      const pattern = /^([a-zA-Z]+:)\/\/[A-Za-z0-9_.~\-:]+/i;
      if (!pattern.test(url)) {
        try {
          return await this.connect(new URL(`wss://${url}`));
        } catch {
          return await this.connect(new URL(`ws://${url}`));
        }
      }
      url = new URL(url);
    }
    url.port = url.port || "38281";
    if (url.protocol !== "wss:" && url.protocol !== "ws:") {
      throw new TypeError("Unexpected protocol. Archipelago only supports the ws:// and wss:// protocols.");
    }
    try {
      return new Promise((resolve, reject) => {
        const IsomorphousWebSocket = this.#findWebSocket();
        if (IsomorphousWebSocket === null) {
          throw new SocketError("Unable to find a suitable WebSocket API in the current runtime.");
        }
        this.#socket = new IsomorphousWebSocket(url);
        this.#socket.onmessage = this.#parseMessage.bind(this);
        this.#socket.onclose = () => {
          this.disconnect();
          reject(new SocketError("Failed to connect to Archipelago server."));
        };
        this.#socket.onerror = () => {
          this.disconnect();
          reject(new SocketError("Failed to connect to Archipelago server."));
        };
        this.#socket.onopen = () => {
          this.wait("roomInfo").then(([packet]) => {
            this.#connected = true;
            if (this.#socket) {
              this.#socket.onclose = this.disconnect.bind(this);
              this.#socket.onerror = this.disconnect.bind(this);
              resolve(packet);
              return;
            }
            this.disconnect();
            reject(new SocketError("Failed to connect to Archipelago server."));
          }).catch((error) => {
            throw error;
          });
        };
      });
    } catch (error) {
      this.disconnect();
      throw error;
    }
  }
  disconnect() {
    if (!this.connected) {
      return;
    }
    this.#connected = false;
    this.#socket?.close();
    this.#socket = null;
    this.emit("disconnected", []);
  }
  #parseMessage(event) {
    const packets2 = JSON.parse(event.data);
    for (const packet of packets2) {
      switch (packet.cmd) {
        case "ConnectionRefused":
          this.emit("connectionRefused", [packet]);
          break;
        case "Bounced":
          this.emit("bounced", [packet, packet.data]);
          break;
        case "Connected":
          this.emit("connected", [packet]);
          break;
        case "DataPackage":
          this.emit("dataPackage", [packet]);
          break;
        case "InvalidPacket":
          this.emit("invalidPacket", [packet]);
          break;
        case "LocationInfo":
          this.emit("locationInfo", [packet]);
          break;
        case "PrintJSON":
          this.emit("printJSON", [packet]);
          break;
        case "ReceivedItems":
          this.emit("receivedItems", [packet]);
          break;
        case "Retrieved":
          this.emit("retrieved", [packet]);
          break;
        case "RoomInfo":
          this.emit("roomInfo", [packet]);
          break;
        case "RoomUpdate":
          this.emit("roomUpdate", [packet]);
          break;
        case "SetReply":
          this.emit("setReply", [packet]);
          break;
      }
      this.emit("receivedPacket", [packet]);
    }
  }
  #findWebSocket() {
    let IsomorphousWebSocket = null;
    if (typeof window !== "undefined") {
      IsomorphousWebSocket = window.WebSocket || window.MozWebSocket;
    } else if (typeof global !== "undefined") {
      IsomorphousWebSocket = global.WebSocket || global.MozWebSocket;
    } else if (typeof self !== "undefined") {
      IsomorphousWebSocket = self.WebSocket || self.MozWebSocket;
    } else if (typeof WebSocket !== "undefined") {
      IsomorphousWebSocket = WebSocket;
    } else if (typeof MozWebSocket !== "undefined") {
      IsomorphousWebSocket = MozWebSocket;
    }
    return IsomorphousWebSocket;
  }
}

// src/classes/Client.ts
class Client {
  #authenticated = false;
  #arguments = defaultConnectionOptions;
  #name = "";
  #game = "";
  socket = new SocketManager;
  package = new DataPackageManager(this);
  storage = new DataStorageManager(this);
  room = new RoomStateManager(this);
  players = new PlayersManager(this);
  items = new ItemsManager(this);
  messages = new MessageManager(this);
  deathLink = new DeathLinkManager(this);
  options;
  get authenticated() {
    return this.socket.connected && this.#authenticated;
  }
  get name() {
    return this.#name;
  }
  get game() {
    return this.#game;
  }
  get arguments() {
    return { ...this.#arguments };
  }
  constructor(options) {
    if (options) {
      this.options = { ...defaultClientOptions, ...options };
    } else {
      this.options = { ...defaultClientOptions };
    }
    this.socket.on("disconnected", () => {
      this.#authenticated = false;
    }).on("sentPackets", (packets2) => {
      for (const packet of packets2) {
        if (packet.cmd === "ConnectUpdate") {
          this.#arguments.tags = packet.tags;
          this.#arguments.items = packet.items_handling;
        }
      }
    });
  }
  async login(url, name, game = "", options) {
    if (name === "") {
      throw new ArgumentError("Provided slot name cannot be blank.", "name", name);
    }
    if (options) {
      this.#arguments = { ...defaultConnectionOptions, ...options };
    } else {
      this.#arguments = { ...defaultConnectionOptions };
    }
    const tags = new Set(this.arguments.tags);
    if (!game && !tags.has("HintGame") && !tags.has("Tracker") && !tags.has("TextOnly")) {
      tags.add("TextOnly");
    }
    this.#arguments.tags = Array.from(tags);
    const request = {
      cmd: "Connect",
      name,
      game,
      password: this.arguments.password,
      slot_data: this.arguments.slotData,
      items_handling: this.arguments.items,
      uuid: this.arguments.uuid,
      tags: this.arguments.tags,
      version: { ...this.arguments.version, class: "Version" }
    };
    await this.socket.connect(url);
    if (this.options.autoFetchDataPackage) {
      await this.package.fetchPackage();
    }
    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => reject(new SocketError("Server failed to respond in time.")), this.options.timeout);
      const connectedHandler = (packet) => {
        this.#authenticated = true;
        this.#game = packet.slot_info[packet.slot].game;
        this.#name = packet.slot_info[packet.slot].name;
        this.socket.off("connected", connectedHandler).off("connectionRefused", refusedHandler);
        clearTimeout(timeout);
        resolve(packet.slot_data);
      };
      const refusedHandler = (packet) => {
        this.socket.off("connected", connectedHandler).off("connectionRefused", refusedHandler);
        clearTimeout(timeout);
        reject(new LoginError(`Connection was refused by the server. Reason(s): [${packet.errors?.join(", ")}`, packet.errors ?? []));
      };
      this.socket.on("connected", connectedHandler.bind(this)).on("connectionRefused", refusedHandler.bind(this)).send(request);
    });
  }
  updateStatus(status) {
    if (!this.authenticated) {
      throw new UnauthenticatedError("Cannot update status while not connected and authenticated.");
    }
    this.socket.send({ cmd: "StatusUpdate", status });
  }
  goal() {
    this.updateStatus(clientStatuses.goal);
  }
  updateTags(tags) {
    if (!this.authenticated) {
      throw new UnauthenticatedError("Cannot update tags while not connected and authenticated.");
    }
    this.socket.send({ cmd: "ConnectUpdate", tags, items_handling: this.arguments.items });
  }
  updateItemsHandling(items) {
    if (!this.authenticated) {
      throw new UnauthenticatedError("Cannot update tags while not connected and authenticated.");
    }
    this.socket.send({ cmd: "ConnectUpdate", tags: this.arguments.tags, items_handling: items });
  }
  check(...locations) {
    if (!this.authenticated) {
      throw new UnauthenticatedError("Cannot check locations while not connected and authenticated.");
    }
    locations = locations.filter((location) => this.room.missingLocations.includes(location));
    this.socket.send({ cmd: "LocationChecks", locations });
  }
  async scout(locations, createHint = 0) {
    if (!this.authenticated) {
      throw new UnauthenticatedError("Cannot scout locations while not connected and authenticated.");
    }
    locations = locations.filter((location) => this.room.allLocations.includes(location));
    const [response] = await this.socket.send({ cmd: "LocationScouts", create_as_hint: createHint, locations }).wait("locationInfo", (packet) => {
      return packet.locations.map((location) => location.location).toSorted().join(",") === locations.toSorted().join(",");
    });
    return response.locations.map((item) => new Item(this, item, this.players.self, this.players.findPlayer(item.player)));
  }
  bounce(targets, data) {
    if (!this.authenticated) {
      throw new UnauthenticatedError("Cannot send bounces while not connected and authenticated.");
    }
    this.socket.send({
      cmd: "Bounce",
      data,
      games: targets.games ?? [],
      slots: targets.slots ?? [],
      tags: targets.tags ?? []
    });
  }
}
export {
  targetVersion,
  slotTypes,
  permissions,
  libraryVersion,
  itemsHandlingFlags,
  itemClassifications,
  defaultConnectionOptions,
  defaultClientOptions,
  clientStatuses,
  UnauthenticatedError,
  TextualMessageNode,
  SocketManager,
  SocketError,
  RoomStateManager,
  PlayersManager,
  PlayerMessageNode,
  Player,
  PackageMetadata,
  MessageManager,
  LoginError,
  LocationMessageNode,
  ItemsManager,
  ItemMessageNode,
  Item,
  IntermediateDataOperation,
  Hint,
  EventBasedManager,
  DeathLinkManager,
  DataStorageManager,
  DataPackageManager,
  ColorMessageNode,
  Client,
  BaseMessageNode,
  ArgumentError,
  exports_api as API
};
