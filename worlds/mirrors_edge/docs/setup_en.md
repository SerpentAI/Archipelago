# Mirror's Edge Randomizer Setup Guide

## Requirements
- Windows OS (Hard required. Client is using memory reading / writing / allocation and running remote threads through Windows APIs)
- Mirror's Edge installed through Steam. Other platforms may work, but support won't be provided for them.
- Archipelago 0.6.7+

**Hashes of expected MirrorsEdge.exe**
```
Name: MirrorsEdge.exe
Size: 31946072 bytes (30 MiB)
CRC32: D0F6BEE3
CRC64: 7176B806A647DA42
SHA256: a0f653b63b299d5d3899b8b4fa6e4d47eeb390bf26b1f020710482eabfe297f0
SHA1: 9538dd552d8acdc5498e7b37a59ea5c434a2fb08
BLAKE2sp: ec88d566bd480acb5e290546b91e4ceaa659941228ff3df657499f889f55092c
```

## Game Setup Instructions
No game modding is required to play Mirror's Edge with Archipelago. The client included with the APWorld does all the work by attaching to the game process and monitoring and manipulating the game state in real-time.

**Note:** DxWrapper (to enable borderless windowed mode and alt-tabbing among other things) is supported and won't interfere with the implementation. Setting it up correctly is left as an exercise to the player, and support will not be provided as it falls outside the scope of this implementation.

## Joining a Multiworld Game
- Launch Mirror's Edge and advance to the main menu
- Open the Archipelago Launcher. Find and click _Mirror's Edge Client_
- Using the _Mirror's Edge Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `Mirror's Edge process found!`
  - You are now ready to play Mirror's Edge with Archipelago. Make sure to check out the `Mirror's Edge` tab in the client

## Continuing a Multiworld Game
- Perform the same steps as above
