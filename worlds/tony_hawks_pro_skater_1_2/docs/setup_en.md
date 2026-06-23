# Tony Hawk's Pro Skater 1 + 2 Randomizer Setup Guide

## Requirements
- Windows OS (Hard required. Client is using memory reading / writing / allocation and running remote threads through Windows APIs)
- Tony Hawk's Pro Skater 1 + 2 installed through Steam or EGS
- Archipelago 0.6.7+

**Hashes of expected THPS12.exe**

_Steam_
```
Name: THPS12.exe
Size: 66312456 bytes (63 MiB)
CRC32: 0654ECBF
CRC64: 9C97186D49CD1E46
SHA256: 1334052bb57d766ae1b4659f9c12abc7afde5fc6dd80e0457fb1885b909233e9
SHA1: 9073e99d69b2d67eb7d961a79b5b2ec95255f601
BLAKE2sp: cec37532d7fce27f4e51edc18504271fab07ec8f35a00701fc23ead7e9483ba2
```

_EGS_
```
Name: THPS12.exe
Size: 438122568 bytes (417 MiB)
CRC32: 5CC3D3A8
CRC64: 667BCD7A3604E2A4
SHA256: 5e60ff7b94ec279ac182c3c74973161dd8cced6503311e18834a9b23601774a2
SHA1: e7cf616c53b465f17345e4045b88caa2fcb38844
BLAKE2sp: ea31ac520d0b815c7492b6a228f17e105df8e1de712a11073c32d119edcddd39
```

## Game Setup Instructions
No game modding is required to play Tony Hawk's Pro Skater 1 + 2 with the Archipelago. The client included with the APWorld does all the work by attaching to the game process and monitoring and manipulating the game state in real-time.

**Note:** You will need to have at least 8 (and ideally every) level unlocked through vanilla play before playing the Archipelago implementation. The mod cannot unlock them on your behalf.

## Joining a Multiworld Game
- Launch Tony Hawk's Pro Skater 1 + 2 and advance to the main menu (where you can see a preview of the selected skater)
- Open the Archipelago Launcher. Find and click _Tony Hawk's Pro Skater 1 + 2 Client_
- Using the _Tony Hawk's Pro Skater 1 + 2 Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `Tony Hawk's Pro Skater 1 + 2 process found!`
  - You are now ready to play Tony Hawk's Pro Skater 1 + 2 with Archipelago. Make sure to check out the `Tony Hawk's Pro Skater 1 + 2` tab in the client

## Continuing a Multiworld Game
- Perform the same steps as above
