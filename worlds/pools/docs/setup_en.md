# POOLS Randomizer Setup Guide

## Requirements
- Windows OS (Hard required. Client is using memory reading / writing through Windows APIs)
- POOLS installed through Steam
- Archipelago 0.6.7+

**Hashes of expected POOLS.exe**
```
Name: POOLS.exe
Size: 912512 bytes (891 KiB)
CRC32: 7E741381
CRC64: 0A3F640D82F688EE
SHA256: 3455adff0b4e90f27edf9fbbb34529e860f6b31198dda7dcdebb5666d192b29d
SHA1: 27a9cc5ec8829f285e3d6d6fb649477b8c968833
BLAKE2sp: fe569a40b8550194f70ca7000365a8844b1be285bd7bda62fef52c133e33db96
```

## Game Setup Instructions
No manual mod installation or other configuration is required to play POOLS with Archipelago. The client included with the APWorld does all the work by attaching to the game process and monitoring and manipulating the game state in real-time.

**Notes**
- The VR version is not compatible!

## Joining a Multiworld Game
- Launch POOLS and reach the main menu
- Open the Archipelago Launcher. Find and click _POOLS Client_
- Using the _POOLS Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `POOLS process found!`
  - You are now ready to play POOLS with Archipelago. Make sure to check out the `POOLS` tab in the client

## Continuing a Multiworld Game
- Perform the same steps as above

## Extra Notes / Quirks
- Location checks that require zooming on something also require the player to be touching a nearby railing to trigger
- Chair locations are triggered by 3D distance to reference coordinates. When multiple chairs are close together, sitting down on one from a weird, exaggerated angle might make the client believe it's another nearby chair.
- Special level interactions / events will not trigger their associated location checks until the autosave kicks in (up to 10 seconds)
- Wet Traps will rarely fail to trigger. Special room conditions / scripting are suspected but the real cause hasn't been found 
- Rewind Traps can make you go out-of-bounds if you've recently interacted with long slides, elevators or gravity-change sections. This will generally force you to restart the level
- The highest levels of movement speed might cause you to go out-of-bounds in gravity-change sections. Maintain responsible speeds!
