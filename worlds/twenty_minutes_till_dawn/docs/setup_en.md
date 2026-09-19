# 20 Minutes Till Dawn Randomizer Setup Guide

## Requirements
- Windows OS (Hard required. Client is using memory reading / writing / allocation and running remote threads through Windows APIs)
- 20 Minutes Till Dawn installed through Steam
- Archipelago 0.6.7+

**Hash of expected MinutesTillDawn.exe**
```
Name: MinutesTillDawn.exe
Size: 650752 bytes (635 KiB)
CRC32: 2F162E01
CRC64: 978470214166F064
SHA256: 0ebaed5ab9b35675585c108256972aa1970253d521f0793e2bef0f3dcdaad06f
SHA1: 89d1af3ebf4df559fc926162daa88f236e3333d0
BLAKE2sp: b6413e113ee9d8ce47c89591a4b4f5ee4256483207818113d8211a2b4731bbd7
```

## Game Setup Instructions
No manual mod installation or other configuration is required to play 20 Minutes Till Dawn with Archipelago. The client included with the APWorld does all the work by attaching to the game process and monitoring and manipulating the game state in real-time.

**IMPORTANT**

Once the Archipelago client is connected, a hook will be set up in the game's memory to allow the client to safely call game functions from the main thread. _**If the client is ever closed, 20 Minutes Till Dawn will NEED to be restarted before connecting another client**_ for everything to function as expected. If you don't restart the game, the previous hook will remain installed with no way for the new client to detect and use it.

Also, if you care about the state of your vanilla save file, you will _need_ to manually back it up before playing this implementation! They can generally be found at `%USERPROFILE%\AppData\LocalLow\Flanne\MinutesTillDawn\*.json`.

## Joining a Multiworld Game
- Launch 20 Minutes Till Dawn and reach the main menu
- Open the Archipelago Launcher. Find and click _20 Minutes Till Dawn Client_
- Using the _20 Minutes Till Dawn Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `20 Minutes Till Dawn process found!`, and an `Archipelago Mod Loaded!` message should appear at the bottom right of the game's main menu
  - You are now ready to play 20 Minutes Till Dawn with Archipelago. Make sure to check out the `20 Minutes Till Dawn` tab in the client

## Continuing a Multiworld Game
- Perform the same steps as above
