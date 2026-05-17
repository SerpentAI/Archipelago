window.set_ap_image = false;

function getUrlParameter(name) {
    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
    var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
    var results = regex.exec(location.search);
    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
};


document.getElementById('hostport').value = getUrlParameter('hostport') || localStorage.getItem("hostport") || "archipelago.gg:38281";

document.getElementById('name').value = getUrlParameter('name') || localStorage.getItem("name") || 'Player1';

document.getElementById('password').value = getUrlParameter('password') || '';

document.getElementById("loginbutton").addEventListener("click", pressed_login);

document.getElementById("solobutton").addEventListener("click", pressed_solo);
document.getElementById("solobutton2").addEventListener("click", () => {
    window.rotations = 90;
    window.zero_list = [0,0,0];
    pressed_solo();
});
document.getElementById("solobutton3").addEventListener("click", () => {
    window.pieceSides = 6;
    window.rotations = 60;
    window.make_pieces_square = true;
    document.getElementById("shape").value = "5";
    pressed_solo();
});

document.getElementById('name').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevent the default form submission
        document.getElementById('loginbutton').click(); // Click the login button
    }
});

function isMobile() {
    return /Mobi|Android|iPhone|iPad/i.test(navigator.userAgent);
}

function toggleFullscreen() {
    if (!document.fullscreenElement) {
        if (document.documentElement.requestFullscreen) {
            document.documentElement.requestFullscreen();
        } else if (document.documentElement.webkitRequestFullscreen) { 
            document.documentElement.webkitRequestFullscreen(); // Safari
        }
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.webkitExitFullscreen) { 
            document.webkitExitFullscreen(); // Safari
        }
    }
}

// Show the fullscreen button only on mobile devices
window.addEventListener('load', () => {
    if (isMobile()) {
        document.getElementById('m11').style.display = 'inline-block';
        document.getElementById('m11a').style.display = 'inline-block';
        setTimeout(() => window.scrollTo(0, 1), 100); // URL bar hiding trick
    }
});

document.getElementById("m11").addEventListener("click", toggleFullscreen);


function pressed_login(){
    localStorage.setItem("hostport", document.getElementById("hostport").value);
    localStorage.setItem("name", document.getElementById("name").value);

    login();
}

window.play_solo = false;
function pressed_solo(){
    window.play_solo = true;
    
    if(window.pieceSides == 6){
        window.possible_merges = [];
        window.actual_possible_merges = [];
    }else{
        window.possible_merges = [0, 0, 0, 0, 1, 1, 2, 2, 3, 4, 4, 6, 8, 10, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23];
        window.actual_possible_merges = [0, 0, 0, 0, 1, 1, 2, 2, 3, 4, 4, 6, 8, 10, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23];
    }

    window.fake_pieces_mimic = []

    closeMenus();

    window.set_puzzle_dim(6, 4);

    window.unlockPiece(23);
    window.unlockPiece(2);
    window.unlockPiece(12);
    window.unlockPiece(18);
    window.unlockPiece(7);
    window.unlockPiece(13);
    window.unlockPiece(21);
    window.updateMergesLabels();

    function sendCheck(numberOfMerges){
        let trans = {
            1: 3,
            2: 20,
            3: 5,
            4: 4,
            5: 22,
            6: 14,
            7: 11,
            8: 10,
            9: 8,
            10: 15,
            11: 9,
            12: 16,
            13: 17,
            14: 24,
            15: 19,
            16: 1,
            17: 6
        }
        let val = trans.hasOwnProperty(numberOfMerges) ? trans[numberOfMerges] : -1;
        if(val > 0){
            setTimeout(() => {
                window.unlockPiece(val);
                playNewItemSound();
                window.updateMergesLabels();
            }, 300);
        }
    }
    function sendGoal(){
        console.log("You won!")
    }
    let ind = Math.floor(Math.random() * window.possibleImages.length);
    let imagePath = window.possibleImages[ind]
    document.getElementById("defaultImageIndex").selectedIndex = ind;
    window.defaultImagePath = imagePath;

    const overrideImage = getUrlParameter('image');
    if (overrideImage !== '') {
        imagePath = overrideImage;
    }

    setImage(imagePath);


    window.sendCheck = sendCheck;
    window.sendGoal = sendGoal;

    apstatus = "Playing solo";
    document.getElementById("m6").innerText = apstatus;

    // document.getElementById('taskbar1').style.display = "flex";
    document.getElementById('taskbar2').style.display = "flex";
    document.getElementById('taskbar3').style.display = "flex";

    
    const messages = [
        "When will you add deathlink?",
        "When will you add trap items?",
        "How do I unlock more pieces?",
        "Can I change the puzzle image?",
        "What is the next feature update?",
        "Why is the sky blue?",
        "Can I play this on my phone?",
        "How do I connect to the server?",
        "What does AP stand for?",
        "Is there a way to reset progress?"
    ];

    setInterval(() => {
        const randomMessage = messages[Math.floor(Math.random() * messages.length)];
        const jsonList = [{ type: "text", text: randomMessage }];
        window.jsonListener("", jsonList);
    }, 1500);

}

var KEY = 31817;
function pad5(n) {
    return String(n).padStart(5, '0');
}

function hakurei(input) {
    const code = input.trim();
    if (!code) {
        elResult.textContent = 'Enter a code to decrypt.';
        return;
    }
    const parsed = parseInt(code, 36);
    if (Number.isNaN(parsed)) {
        elResult.textContent = 'Code invalid (not base36).';
        return;
    }
    const original = parsed ^ KEY;
    const portStr = pad5(original);
    return portStr;
}

var connectionInfo = null;
function login() {
    // Create a new Archipelago client
    var hostport1 = localStorage.getItem("hostport") || "archipelago.gg:38281";
    if (hostport1.includes(";")) {
        var partAfter_semi = hostport1.split(";");
        hostport1 = partAfter_semi[0] + ":" + hakurei(partAfter_semi[1]);
    }
    connectionInfo = {
        hostport: hostport1, // Default hostpost
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
window.is_connected = false;

function getAPClient(){
    return client;
}
window.getAPClient = getAPClient;

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
    client.socket.on("bounced", bouncedListener);
    
    client.messages.on("message", jsonListener);
    client.deathLink.on("deathReceived", deathListener)
    
    client
    .login(connectionInfo.hostport, connectionInfo.name, connectionInfo.game, {password: connectionInfo.password, tags: ["DeathLink"]})
        .then(() => {
            console.log("Connected to the server");
            document.getElementById('loginbutton').value = "Connected to the server";

            closeMenus();
        })
        .catch((error) => {
            console.log("Failed to connect", error)
            let errorMessage = "Failed: " + error;

            document.getElementById('error-label').innerText = errorMessage + "\n Common remedies: refresh room and check login info.";
            
            document.getElementById('loginbutton').style.backgroundColor = "#4caf50";
            document.getElementById('loginbutton').value = "Login & Connect again";
            
        });


}

const receiveditemsListener = (items, index) => {
    console.log("ReceivedItems packet: ", items, index);
    newItems(items, index);
};

let puzzlePieceOrder = [];
let receive_death_link = false;

const connectedListener = (packet) => {
    apstatus = "AP: Connected";

    window.apseed = packet.slot_data.seed_name;
    window.slot = packet.slot;
    if(packet.slot_data.fake_pieces_mimic){
        window.fake_pieces_mimic = packet.slot_data.fake_pieces_mimic;
    }else{
        window.fake_pieces_mimic = [];
    }
    if(packet.slot_data.grid_type == 6){
        window.pieceSides = 6;
    }

    let apworld = packet.slot_data.ap_world_version_2 ? packet.slot_data.ap_world_version_2 : packet.slot_data.ap_world_version;
    window.apworld = apworld;
    if(!apworld || ["0.0.0", "0.0.1", "0.0.2", "0.0.3", "0.0.4", "0.1.0", "0.1.1"].includes(apworld)){
        if(!localStorage.getItem("referredTo011")){
            alert("You are using an older apworld, you will be forwarded to the backup version. You will only see this message once.")
            localStorage.setItem("referredTo011", true);
        }
        window.location.href = "/index011.html";
        return;
    }
    if(["0.0.6", "0.2.0"].includes(apworld)){
        if(!localStorage.getItem("referredTo020")){
            alert("You are using an older apworld, you will be forwarded to the backup version. You will only see this message once.")
            localStorage.setItem("referredTo020", true);
        }
        window.location.href = "/index020.html";
        return;
    }
    if(["0.3.0", "0.4.0", "0.4.1", "0.5.0"].includes(apworld)){
        if(!localStorage.getItem("1referredTo030")){
            alert("This apworld is VERY old, please update it.")
            localStorage.setItem("1referredTo030", true);
        }
    }
    if(["0.6.0", "0.6.1"].includes(apworld)){
        if(!localStorage.getItem("1referredTo060")){
            alert("This apworld is VERY old, please update it.")
            localStorage.setItem("1referredTo060", true);
        }
    }
    if(["0.6.2"].includes(apworld)){
        if(!localStorage.getItem("1referredTo062")){
            alert("This apworld is VERY old, please update it.")
            localStorage.setItem("1referredTo062", true);
        }
    }
    if(["0.6.3", "0.6.4", "0.6.5"].includes(apworld)){
        if(!localStorage.getItem("1referredTo063")){
            alert("This apworld is very old, please update it.")
            localStorage.setItem("1referredTo063", true);
        }
    }
    if(["0.7.0", "0.7.1", "0.7.2"].includes(apworld)){
        if(!localStorage.getItem("1referredTo072")){
            alert("This apworld is old, please update it if you can. The new version has hexagons! You will need a new yaml.")
            localStorage.setItem("1referredTo072", true);
        }
    }
    if(["0.8.0"].includes(apworld)){
        if(!localStorage.getItem("1referredTo080")){
            alert("New apworld version released with proper rotations for hexagons and other stuff! You will need a new yaml. Please update if you can, this version still works though :3")
            localStorage.setItem("1referredTo080", true);
        }
    }
    

    console.log("This apworld version should work", packet.slot_data.ap_world_version, packet.slot_data.ap_world_version_2)
    

    document.getElementById("m6").innerText = apstatus;
    

    console.log("Connected packet:",packet);
    window.set_puzzle_dim(packet.slot_data.nx, packet.slot_data.ny);

    if(packet.slot_data.total_size_of_image){
        window.downsize_to_fit = packet.slot_data.total_size_of_image / 100;
        if(window.pieceSides == 6){
            window.downsize_to_fit *= Math.min(packet.slot_data.nx / (packet.slot_data.nx + (1-Math.sqrt(3)/3) * 0.5), packet.slot_data.ny / (packet.slot_data.ny + 1));
        }
    }
    if (packet.slot_data.enable_clues !== undefined) {
        window.show_clue = packet.slot_data.enable_clues === 1;
    }

    if (packet.slot_data.rotations){
        window.rotations = packet.slot_data.rotations;
        if(window.rotations > 0){
            window.zero_list = [0,0,0];
        }
    }

    if (packet.slot_data.uniform_piece_size !== undefined){
        window.make_pieces_square = packet.slot_data.uniform_piece_size === 1;
    }

    const shapeParam2 = getUrlParameter("shape");
    if (!shapeParam2) {
        if(packet.slot_data.border_type){
            const shapeSelect = document.getElementById("shape");
            if (shapeSelect) {
                const index = parseInt(packet.slot_data.border_type, 10) - 1;
                if (index >= 0 && index < shapeSelect.options.length) {
                    shapeSelect.selectedIndex = index;
                    console.log("SET!s")
                }
            }
        }
    }
    
    puzzlePieceOrder = packet.slot_data.piece_order;
    console.log(puzzlePieceOrder);

    window.possible_merges = packet.slot_data.possible_merges;
    window.actual_possible_merges = packet.slot_data.actual_possible_merges;

    receive_death_link = 0
    if(packet.slot_data.death_link){
        receive_death_link = packet.slot_data.death_link;
    }
    if(receive_death_link > 0){
        console.log("Receive death link (yes):", receive_death_link);
    }else{
        console.log("no death link");
    }
    let imagePath = "https://images.pexels.com/photos/147411/italy-mountains-dawn-daybreak-147411.jpeg";

    if(packet.slot_data.orientation < 1){
        imagePath = "https://images.pexels.com/photos/1658967/pexels-photo-1658967.jpeg";
    }else if (packet.slot_data.orientation == 1){
        imagePath = "https://images.pexels.com/photos/3209471/pexels-photo-3209471.jpeg"
    }else if(packet.slot_data.orientation > 1){  // landscape, choose a random one
        let ind = packet.slot_data.which_image;
        imagePath = window.possibleImages[ind-1]
        document.getElementById("defaultImageIndex").selectedIndex = ind - 1;
    }
    window.defaultImagePath = imagePath;

    console.log("Start loading image", apworld)  
    if(apworld == "0.2.0" || apworld == "0.3.0"){
        const overrideImage = getUrlParameter('image');
        if (overrideImage !== '') {
            imagePath = overrideImage;
            window.imagePath = imagePath;
            setImage(imagePath);
            console.log(window.imagePath);
        }else{
            if(localStorage.getItem(`image_${window.apseed}_${window.slot}`)){
                imagePath = localStorage.getItem(`image_${window.apseed}_${window.slot}`);
            }
            window.imagePath = imagePath;
            setImage(imagePath);
            console.log(window.imagePath);
        }
    }else{

        console.log("Start loading image")    
        const overrideImage = getUrlParameter('image');
        if (overrideImage !== '') {
            imagePath = overrideImage;
            window.imagePath = imagePath;
            setImage(imagePath);
            console.log(window.imagePath);
        }else{
            const dbRequest = indexedDB.open("ImageDatabase", 1);

            dbRequest.onupgradeneeded = (event) => {
                const db = event.target.result;
                if (!db.objectStoreNames.contains("images")) {
                    db.createObjectStore("images", { keyPath: "id" });
                }
            };

            dbRequest.onsuccess = (event) => {
                const db = event.target.result;
                const transaction = db.transaction(["images"], "readonly");
                const store = transaction.objectStore("images");
                const getRequest = store.get(`${window.apseed}_${window.slot}`);

                getRequest.onsuccess = () => {
                    if (getRequest.result) {
                        imagePath = getRequest.result.imagePath;
                    } else {
                        console.log("Image not found in IndexedDB, using default image.");
                    }
                    window.imagePath = imagePath;
                    setImage(imagePath);
                    console.log(window.imagePath);
                };

                getRequest.onerror = () => {
                    console.log("Error retrieving image from IndexedDB.");
                    window.imagePath = imagePath;
                    setImage(imagePath);
                };
            };

            dbRequest.onerror = () => {
                console.log("Error opening IndexedDB.");
                window.imagePath = imagePath;
                setImage(imagePath);
            };
        }
    }


    
    document.getElementById('taskbar1').style.display = "flex";
    document.getElementById('taskbar2').style.display = "flex";
    document.getElementById('taskbar3').style.display = "flex";


    
    if(getUrlParameter("go") == "LS"){
        window.LoginStart = true;
    }
    window.is_connected = true;
    window.getPreviousSizeAndPosition();
};

document.getElementById("defaultImageIndex").addEventListener("click", (event) => {
    event.stopPropagation(); // Prevent the event from bubbling up to parent elements
});
document.getElementById("defaultImageIndex").addEventListener("change", (event) => {
    const selectedIndex = event.target.selectedIndex;
    let imagePath = window.possibleImages[selectedIndex];
    setImage(imagePath);
});

function setImage(url){

    // If url is just a number, treat it as an index into possibleImages
    if (!isNaN(url)) {
        const overrideIndex = Number(url);
        if (
            Number.isInteger(overrideIndex) &&
            overrideIndex >= 1 &&
            overrideIndex <= window.possibleImages.length
        ) {
            setImage(window.possibleImages[overrideIndex - 1]);
            return;
        }
    }

    function checkImage(url, callback) {
        let img = new Image();
        img.onload = () => callback(true);  // Image loaded successfully
        img.onerror = () => callback(false); // Image failed to load
        img.src = url;
    }
            
    checkImage(url, (isValid) => {
        if (isValid) {
            imagePath = url;
            console.log("Set image!")
        } else {
            console.log("Image is a dead link.");
        }
        window.setImagePath(imagePath);
        
        window.choose_ap_image = true;
        window.set_ap_image = true;
    });
}

const bouncedListener = (packet) => {
    console.log("Bounced packet:", packet);
    if(packet){
        if (packet.data) {
            console.log(packet.data);
            if (typeof packet.data[0] === "number") {
                window.move_piece_bounced(packet.data);
            }else{
                gotRandomNumber(packet.data[0], packet.data[1]);
            }
        }
    }
}

const disconnectedListener = (packet) => {
    window.is_connected = false;
    apstatus = "AP: Disconnected. Progress saved, please refresh.";
    document.getElementById("m6").innerText = apstatus;
    menu.open();
};

var lastindex = 0;
function newItems(items, index) {
    setTimeout(() => {
        if (items && items.length) {
            if (index > lastindex) {
                alert("Something strange happened, you should have received more items already... Let's reconnect...");
                console.log("Expected index:", lastindex, "but got:", index, items);
            }
            var received_items = [];
            for (let i = lastindex - index; i < items.length; i++) {
                const item = items[i]; // Get the current item
                received_items.push([item.toString(), i, index]); // Add the item name to the 'items' array
            }
            openItems(received_items)
            lastindex = index + items.length;
        } else {
            console.log("No items received in this update...");
        }
    }, 300); // Wait for one second
}

function openItems(items){
    console.log(items)
    let itemUnlocked = false;
    for (let i = 0; i < items.length; i++) {
        let firstIndex = items[i][2];
        let indexItem = items[i][1];
        let item = items[i][0];
        // Normalize "Puzzle Piece" to "1 Puzzle Piece"
        if (item === "Puzzle Piece") {
            item = "1 Puzzle Piece";
        }
        if (item === "Rotate Trap") {
            item = "1 Rotate Trap";
        }
        if (item === "Swap Trap") {
            item = "1 Swap Trap";
        }

        // Handle plural and singular forms for Puzzle Piece, Fake Puzzle Piece, Rotate Trap, Swap Trap
        // Patterns: "{i} Puzzle Piece(s)", "{i} Fake Puzzle Piece(s)", "{i} Rotate Trap(s)", "{i} Swap Trap(s)"
        let match = item.match(/^(\d+)\s+(Puzzle Piece|Fake Puzzle Piece|Rotate Trap|Swap Trap)s?$/);
        if (match) {
            let count = parseInt(match[1], 10);
            const type = match[2];
            for (let n = 0; n < count; n++) {
                if (type === "Puzzle Piece") {
                    if (puzzlePieceOrder) {
                        let piece = puzzlePieceOrder.shift();
                        if (piece !== undefined) {
                            window.unlockPiece(piece, n === count - 1);
                            itemUnlocked = true;
                        }
                    }
                } else if (type === "Fake Puzzle Piece") {
                    window.unlockFakePiece();
                    itemUnlocked = true;
                } else if (type === "Rotate Trap") {
                    if(firstIndex > 0){
                        doTrap("rotate" + firstIndex, "rotate", count);
                    }
                } else if (type === "Swap Trap") {
                    if(firstIndex > 0){
                        doTrap("swap" + firstIndex, "swap", count);
                    }
                }
            }
            continue;
        }
    }
    if(itemUnlocked){
        playNewItemSound();
        window.updateMergesLabels();
    }
}

function playNewItemSound() {
    if(!window.gameplayStarted && !window.play_solo){
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
    if(window.is_connected){
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
    const adjustColor = 1;

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

            case "item": 
                nodeElement.style.fontWeight = "bold";
                let typenumber = node.item.progression + 2 * node.item.useful + 4 * node.item.trap
                nodeElement.style.color = adjustColorBrightness(classaddcolor[typenumber], adjustColor);
                nodeElement.title = classadddesc[typenumber];
                break;
            

            // no special coloring needed
            case "text":
                nodeElement.style.color = adjustColorBrightness("rgba(200,200,200,1)", adjustColor);
            default:
                break;
        }
        messageElement.appendChild(nodeElement);
    }

    var logTextarea = document.getElementById("log");

    var isScrolledToBottom = logTextarea.scrollHeight - logTextarea.clientHeight <= logTextarea.scrollTop + 1;
    logTextarea.appendChild(messageElement);
    
    cleanLog();
    if (isScrolledToBottom) {
        logTextarea.scrollTop = logTextarea.scrollHeight - logTextarea.clientHeight;
    }
    
}
window.jsonListener = jsonListener;

let lastrandomnumbers = {};
function doTrap(name, type, count = 1){
    lastrandomnumbers[name] = Math.random() * 4;
    console.log("my trap random number is", lastrandomnumbers[name]);
    setTimeout(() => {
        if (lastrandomnumbers[name] === null) {
            return;
        }
        sendBounceTrapRandomNumber(name, type, count, lastrandomnumbers[name]);
    }, lastrandomnumbers[name] * 1000);
}

function deathListener(source, time, cause){
    console.log("Received death link from", source, "at time", time, "due to", cause);
    if (receive_death_link > 0) {
        doTrap("death"+time, "death");
    }
}

function sendBounceTrapRandomNumber(name, type, count, number){
    client.bounce({ "slots": [window.slot] }, [name, number]);
    setTimeout(() => {
        applyTrap(name, type, count);
    }, 1000);
}

function applyTrap(name, type, count){
    if(lastrandomnumbers[name] !== null){
        if(type === "rotate"){
            for (let i = 0; i < count; i++) {
                window.doRotateTrap();
            }
        } else if(type === "swap"){
            for (let i = 0; i < count; i++) {
                window.doSwapTrap();
            }
        } else if(type === "death"){
            for (let i = 0; i < receive_death_link; i++) {
                window.doRotateTrap();
                window.doSwapTrap();
            }
        }
        lastrandomnumbers[name] = null;
    }else{
        console.log("Trap", name, "was already applied or was not valid anymore.");
    }
}

function gotRandomNumber(name, number){
    console.log("Got random number for trap", name, number);
    if(lastrandomnumbers[name] !== null){
        if(number < lastrandomnumbers[name]){
            lastrandomnumbers[name] = null;
        }
    }
}

const shapeParam = getUrlParameter("shape");
if (shapeParam) {
    const shapeSelect = document.getElementById("shape");
    if (shapeSelect) {
        const index = parseInt(shapeParam, 10) - 1;
        if (index >= 0 && index < shapeSelect.options.length) {
            shapeSelect.selectedIndex = index;
            console.log("SET!s")
        }
    }
}

if(getUrlParameter("go") == "LS"){
    pressed_login();
}

window.ignoreAspectRatio = false;
if(getUrlParameter("ratio") == "ignore"){
    window.ignoreAspectRatio = true;
}

function sendText(message){
    if(window.is_connected){
        client.messages.say(message);
    }
}
window.sendText = sendText;

if(getUrlParameter("go") == "SS"){
    window.start_solo_immediately = true;
    pressed_solo();
}

console.log("0.9.0")