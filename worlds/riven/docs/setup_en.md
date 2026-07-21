# Riven Randomizer Setup Guide

## Requirements
- Windows OS (Hard required. Client is using memory reading / writing / allocation and running remote threads through Windows APIs)
- Riven installed through Steam
- Archipelago 0.6.7+

**Hashes of expected Riven-Win64-Shipping.exe**
```
Name: Riven-Win64-Shipping.exe
Size: 138775552 bytes (132 MiB)
CRC32: 3199F0E9
CRC64: E07D2DBB706AC39D
SHA256: c988078bb2940ef2deacf57600062d3ca5ff35d2111e8ee0af92f2f0f8052969
SHA1: 21d54e33b9d6d98023fd24d2d40ec16113303bde
BLAKE2sp: d6fce30e90780b7470c55f021a2378519402f3ec1aae068cf9bd37e97f79dc48In
```

## Game Setup Instructions
No manual mod installation or other configuration is required to play Riven with Archipelago. The client included with the APWorld does all the work by attaching to the game process and monitoring and manipulating the game state in real-time.

**Notes**
- Keyboard and Mouse controls are the only supported input methods. Controllers and VR have a high chance to not work correctly
- In Input Options, set `Quick Travel on Ladders` to `Off`
- In Input Options, set `Hide Vehicle Transitions` to `Off`

## Joining a Multiworld Game
- Launch Riven and start a New Game
  - While it may be tempting to make and reuse a save once you arrive on Riven and the cage has been lowered, note that the puzzle solutions are only randomized on creating a new game. If you make and reuse that save across seeds, you will skip the intro, but your puzzle solutions will always be the same.
- Open the Archipelago Launcher. Find and click _Riven Client_
- Using the _Riven Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `Riven process found!`
  - You are now ready to play Riven with Archipelago. Make sure to check out the `Riven` tab in the client

## Continuing a Multiworld Game
- Launch Riven and load the correct save
  - Always double-check you are loading the save for the seed you intend to play. Loading the incorrect save and connecting to the client can send location checks that you haven't performed. Be aware!
- Open the Archipelago Launcher. Find and click _Riven Client_
- Using the _Riven Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `Riven process found!`
  - You are now ready to play Riven with Archipelago. Make sure to check out the `Riven` tab in the client
