function getUrlParameter(name) {
    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
    var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    var results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
};

document.getElementById('hostport').value = parseInt(getUrlParameter('hostport')) || localStorage.getItem("hostport") || "archipelago.gg:38281";
document.getElementById('name').value = getUrlParameter('name') || localStorage.getItem("name") || 'Player1';

document.getElementById("loginbutton").addEventListener("click", pressed_login);

document.getElementById("solobutton").addEventListener("click", pressed_solo);

function pressed_login(){
    localStorage.setItem("hostport", document.getElementById("hostport").value);
    localStorage.setItem("name", document.getElementById("name").value);

    login();
}

let play_solo = false;
function pressed_solo(){
    play_solo = true;
    
    window.possible_merges = [0, 0, 0, 0, 0, 0, 1, 3, 5, 5, 5, 6, 8, 9, 11, 13, 15, 16, 16, 18, 19, 20, 21, 22, 23, 24]

    window.actual_possible_merges = [0, 0, 0, 0, 0, 0, 1, 3, 5, 5, 5, 6, 8, 9, 11, 13, 15, 16, 16, 18, 19, 20, 21, 22, 23, 24]


    closeMenus();

    window.set_puzzle_dim(5, 5);


    window.unlockPiece(13);
    window.unlockPiece(1);
    window.unlockPiece(17);
    window.unlockPiece(25);
    window.unlockPiece(15);
    window.unlockPiece(8);
    window.unlockPiece(18);

    function sendCheck(numberOfMerges){
        let trans = {
            1: 20,
            2: 11,
            3: 21,
            4: 9,
            5: 6,
            6: 3,
            7: 2,
            8: 14,
            9: 16,
            10: 22,
            11: 5,
            12: 4,
            13: 24,
            14: 12,
            15: 10,
            16: 23,
            17: 19,
            18: 7
        }
        let val = trans.hasOwnProperty(numberOfMerges) ? trans[numberOfMerges] : -1;
        if(val > 0){
            setTimeout(() => {
                window.unlockPiece(val);
                playNewItemSound();
            }, 300);
        }
    }
    function sendGoal(){
        console.log("You won!")
    }


    window.sendCheck = sendCheck;
    window.sendGoal = sendGoal;

    apstatus = "Playing solo";
    document.getElementById("m6").innerText = apstatus;

    document.getElementById("n1").style.display = "none";
}

var connectionInfo = null;
function login() {
    // Create a new Archipelago client
    connectionInfo = {
        hostport: localStorage.getItem("hostport") || "archipelago.gg:38281", // Default hostpost
        game: "Jigsaw", // Replace with the game name for this player.
        name: localStorage.getItem("name") || "Player1", // Default player name
        password: document.getElementById("password").value,
        items_handling: 0b111,
    };

    document.getElementById('loginbutton').value  = "Connecting...";
    document.getElementById('loginbutton').style.backgroundColor = "orange";

    // Connect to the Archipelago server
    connectToServer();
}

// server stuff:
import {
    Client
} from "./archipelago.js";

var client = null;
var apstatus = "?";
var connected = false;

function closeMenus(){
    document.getElementById("login-container").style.display = "none";
    document.getElementById("puzzleDIV").style.display = "block";
    window.dispatchEvent(new Event("resize"));
}

function connectToServer(firsttime = true) {
    client = new Client();
    client.items.on("itemsReceived", receiveditemsListener);
    client.socket.on("connected", connectedListener);
    client.socket.on("disconnected", disconnectedListener);
    
    client.messages.on("message", jsonListener);
    
    client
    .login(connectionInfo.hostport, connectionInfo.name, connectionInfo.game, {password: connectionInfo.password})
        .then(() => {
            console.log("Connected to the server");
            document.getElementById('loginbutton').value = "Connected to the server";

            closeMenus();
        })
        .catch((error) => {
            console.log("Failed to connect", error)
            document.getElementById('loginbutton').value  = "Failed: "+error;
            document.getElementById('loginbutton').style.backgroundColor = "red";
        });
}

const receiveditemsListener = (items, index) => {
    console.log("ReceivedItems packet: ", items, index);
    newItems(items, index);
};

let puzzlePieceOrder = [];

const connectedListener = (packet) => {
    apstatus = "AP: Connected";

    window.apseed = packet.slot_data.seed_name;
    window.slot = packet.slot;

    let apworld = packet.slot_data.ap_world_version
    if(!apworld || ["0.0.0", "0.0.1", "0.0.2", "0.0.3", "0.0.4", "0.1.0", "0.1.1"].includes(apworld)){
        if(!localStorage.getItem("referredTo011")){
            alert("You are using an older apworld, you will be forwarded to the backup version. You will only see this message once.")
            localStorage.setItem("referredTo011", true);
        }
        window.location.href = "/index011.html";
        return;
    }else{
        console.log("This apworld version should work", packet.slot_data.ap_world_version)
    }

    connected = true;
    document.getElementById("m6").innerText = apstatus;
    

    console.log("Connected packet:",packet);
    window.set_puzzle_dim(packet.slot_data.nx, packet.slot_data.ny);

    puzzlePieceOrder = packet.slot_data.piece_order;

    window.possible_merges = packet.slot_data.possible_merges;
    window.actual_possible_merges = packet.slot_data.actual_possible_merges;
    console.log("Set merges possibilities")

    let imagePath = "color-icon2.png";
    if(packet.slot_data.orientation < 1){
        imagePath = "https://images.pexels.com/photos/1658967/pexels-photo-1658967.jpeg";
    }
    if(packet.slot_data.orientation > 1){
        imagePath = "https://images.pexels.com/photos/147411/italy-mountains-dawn-daybreak-147411.jpeg";
    }

    window.setImagePath(imagePath);
};

const disconnectedListener = (packet) => {
    connected = false;
    window.saveProgress(false);
    apstatus = "AP: Disconnected. Progress saved, please refresh.";
    document.getElementById("m6").innerText = apstatus;
    menu.open();
};

var lastindex = 0;
function newItems(items, index) {
    setTimeout(() => {
        if (items && items.length) {
            if (index > lastindex) {
                console.log("Something strange happened, you should have received more items already... Let's reconnect...");
            }
            var received_items = [];
            for (let i = lastindex - index; i < items.length; i++) {
                const item = items[i]; // Get the current item
                received_items.push(item.toString()); // Add the item name to the 'items' array
            }
            openItems(received_items)
            lastindex = index + items.length;
        } else {
            console.log("No items received in this update...");
        }
    }, 300); // Wait for one second
}

function openItems(items){
    let itemUnlocked = false;
    for (let i = 0; i < items.length; i++) {
        // console.log(items[i], puzzlePieceOrder)
        let number_of_pieces = 0;
        if(items[i] == "Puzzle Piece"){
            number_of_pieces = 1;
        }
        if(items[i] == "2 Puzzle Pieces"){
            number_of_pieces = 2;
        }
        if(items[i] == "5 Puzzle Pieces"){
            number_of_pieces = 5;
        }
        if(items[i] == "10 Puzzle Pieces"){
            number_of_pieces = 10;
        }
        for(let c = 0; c < number_of_pieces; c++){
            if(puzzlePieceOrder){
                let piece = puzzlePieceOrder.shift();
                // console.log("Unlocking piece", piece);
                if (piece !== undefined) {
                    window.unlockPiece(piece);
                    itemUnlocked = true;
                }
            }
        }
    }
    if(itemUnlocked){
        playNewItemSound();
    }
}

function playNewItemSound() {
    if(!window.gameplayStarted && !play_solo){
        return;
    }
    const soundSources = ["Sounds/p1.mp3", "Sounds/p2.mp3", "Sounds/p3.mp3", "Sounds/p4.mp3"];
    const randomSound = soundSources[Math.floor(Math.random() * soundSources.length)];
    const newItemSound = new Audio(randomSound);

    newItemSound.play().catch(function(error) {
        // Handle the error here (e.g., log it or show a warning message)
        console.log("Could not play sound because user hasn't interacted with the website yet");
    });
}
function playNewMergeSound() {
    const soundSources = ["Sounds/m1.mp3", "Sounds/m2.mp3", "Sounds/m3.mp3", "Sounds/m4.mp3", "Sounds/m5.mp3"];
    const randomSound = soundSources[Math.floor(Math.random() * soundSources.length)];
    const newItemSound = new Audio(randomSound);

    if (!window.lastMergeSoundTime || Date.now() - window.lastMergeSoundTime > 1000) {
        newItemSound.play().catch(function(error) {
            // Handle the error here (e.g., log it or show a warning message)
            console.log("Could not play sound because user hasn't interacted with the website yet");
        });
        window.lastMergeSoundTime = Date.now();
    }
}
window.playNewMergeSound = playNewMergeSound;
function playNewGameSound() {
    const soundSources = ["Sounds/b1.mp3", "Sounds/b2.mp3"];
    const randomSound = soundSources[Math.floor(Math.random() * soundSources.length)];
    const newItemSound = new Audio(randomSound);

    newItemSound.play().catch(function(error) {
        // Handle the error here (e.g., log it or show a warning message)
        console.log("Could not play sound because user hasn't interacted with the website yet");
    });
}
window.playNewGameSound = playNewGameSound;

function sendCheck(numberOfMerges){
    console.log(numberOfMerges);
    if(connected){
        client.check(234782000 + numberOfMerges);
    }
}
function sendGoal(){
    client.goal();
}

window.sendCheck = sendCheck;
window.sendGoal = sendGoal;

function cleanLog() {
    var logTextarea = document.getElementById("log");
    
    // Check if logTextarea has more than 2000 children (assumed to be <span> elements)
    if (logTextarea.children.length > 2000) {
        for (var i = 0; i < 1000; i++) {
            if (logTextarea.children[0]) {
                logTextarea.removeChild(logTextarea.children[0]); // Remove the first child
            }
        }
    }
}

var classaddcolor = [
    "rgba(6, 217, 217, 1)",
    "rgba(168, 147, 228, 1)",
    "rgba(98, 122, 198, 1)",
    "rgba(255, 223, 0, 1)",
    "rgba(211, 113, 102, 1)",
    "rgba(255, 172, 28, 1)",
    "rgba(155, 89, 182, 1)",
    "rgba(128, 255, 128, 1)"]
var classaddtext = ["...", "!!", "!", "!!!", "@#!", "!?!", "@!!", "?!@"]
var classadddesc = ["Item class: normal", 
    "Item class: progression", 
    "Item class: useful", 
    "Item class: progression, useful", 
    "Item class: trap", 
    "Item class: progression, trap", 
    "Item class: useful, trap", 
    "progression, useful, trap"]
var classothercolors = [
    "rgba(100, 149, 237, 1)",
    "rgba(0, 255, 127, 1)",
    "rgba(238, 0, 238, 1)",
    "rgba(250, 250, 210, 1)"
]

function adjustColorBrightness(color, amount) {
    const colorParts = color.match(/[\d.]+/g);
    if (colorParts.length === 4) {
        // RGBA color
        let [r, g, b, a] = colorParts.map(Number);
        if(amount <= 0){
            amount = -amount;
            r = r * amount;
            g = g * amount;
            b = b * amount;
        }else{
            r = 255 - (255 - r) * amount;
            g = 255 - (255 - g) * amount;
            b = 255 - (255 - b) * amount;
        }
        return `rgba(${r}, ${g}, ${b}, ${a})`;
    } else if (colorParts.length === 3) {
        // RGB color
        let [r, g, b] = colorParts.map(Number);
        if(amount <= 0){
            amount = -amount;
            r = r * amount;
            g = g * amount;
            b = b * amount;
        }else{
            r = 255 - (255 - r) * amount;
            g = 255 - (255 - g) * amount;
            b = 255 - (255 - b) * amount;
        }
        return `rgb(${r}, ${g}, ${b})`;
    } else {
        throw new Error("Invalid color format");
    }
}

function jsonListener(text, nodes) {
    const adjustColor = 0.5;

    // Plaintext to console, because why not?
    const messageElement = document.createElement("div");
  
    let is_relevant = false;
    let contains_player = false;

    for (const node of nodes) {
        const nodeElement = document.createElement("span");
        nodeElement.innerText = node.text;

        switch (node.type) {
            case "entrance":
                nodeElement.style.color = adjustColorBrightness(classothercolors[0], adjustColor);
                break;

            case "location":
                nodeElement.style.color = adjustColorBrightness(classothercolors[1], adjustColor);
                break;

            case "color":
                // not really correct, but technically the only color nodes the server returns is "green" or "red"
                // so it's fine enough for an example.
                nodeElement.style.color = node.color;
                break;

            case "player":
                contains_player = true;
                nodeElement.style.fontWeight = "bold";
                if (node.player.slot === client.players.self.slot) {
                    // It's us!
                    nodeElement.style.color = adjustColorBrightness(classothercolors[2], adjustColor);
                    is_relevant = true;
                } else {
                    // It's them!
                    nodeElement.style.color = adjustColorBrightness(classothercolors[3], adjustColor);
                }
                nodeElement.innerText = node.player.alias;
                nodeElement.title = "Game: " + node.player.game;
                break;

            case "item": {
                nodeElement.style.fontWeight = "bold";
                let typenumber = node.item.progression + 2 * node.item.useful + 4 * node.item.trap
                nodeElement.style.color = adjustColorBrightness(classaddcolor[typenumber], adjustColor);
                nodeElement.title = classadddesc[typenumber];
            }

            // no special coloring needed
            case "text":
                nodeElement.style.color = adjustColorBrightness("rgba(126,126,126,1)", adjustColor);
            default:
                break;
        }
        messageElement.appendChild(nodeElement);
    }

    var logTextarea = document.getElementById("log");

    logTextarea.appendChild(messageElement);
    
    cleanLog();

    logTextarea.scrollTop = logTextarea.scrollHeight - logTextarea.clientHeight;
}
window.jsonListener = jsonListener;

console.log("0.2.0")