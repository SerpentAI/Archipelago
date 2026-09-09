# Peggle Deluxe Randomizer Setup Guide

## Requirements
- Windows OS (Hard required. Client is using memory reading / writing / allocation through Windows APIs)
- Peggle Deluxe installed through Steam
  - Only the English version is supported. Other languages use different executables. 
  - The language can be changed in Properties -> General on Steam
- Archipelago 0.6.7+

**Hashes of expected Peggle.exe**

```
Name: Peggle.exe
Size: 4709400 bytes (4599 KiB)
CRC32: B454DAF4
CRC64: B046A11F1C1C20A4
SHA256: d37a37e305e468dc48fd88eeb4e1056a086881e1be14f66f3590c99a88c44d4c
SHA1: 6e1c243aeea88f289e6571656fffa89aecdd6769
BLAKE2sp: b31434bfabce261ea818f9b896c67ffb03307ef0dffd5a7cc07b5ccded5be86e
```

## Game Setup Instructions
No manual mod installation or other configuration is required to play Peggle Deluxe with Archipelago. The client included with the APWorld does all the work by attaching to the game process and monitoring and manipulating the game state in real-time.

**IMPORTANT**

Once the Archipelago client is connected, hooks and patches will be set up in the game's memory. _**If the client is ever closed, Peggle Deluxe will NEED to be restarted before connecting another client**_ for everything to function as expected. If you don't restart the game, the previous hooks and patches will remain installed with no way for the new client to detect and use them.

**Note:** You don't need to have completed Adventure Mode to play. The client will be able to unlock the Quick Play levels as needed regardless of Adventure progress.

## Joining a Multiworld Game
- Launch Peggle Deluxe and either sit on the splash screen or advance to the main menu
- Open the Archipelago Launcher. Find and click _Peggle Deluxe Client_
- Using the _Peggle Deluxe Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `Peggle Deluxe process found!`
  - You are now ready to play Peggle Deluxe with Archipelago. Make sure to check out the `Peggle Deluxe` tab in the client

## Continuing a Multiworld Game
- Perform the same steps as above
