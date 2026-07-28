# Severed Steel Randomizer Setup Guide

## Requirements
- Windows OS (Hard required. Client is using memory reading / writing through Windows APIs)
- Severed Steel installed through Steam
- Archipelago 0.6.7+

**Hashes of expected ThankYouVeryCool-Win64-Shipping.exe**
```
Name: ThankYouVeryCool-Win64-Shipping.exe
Size: 98889216 bytes (94 MiB)
CRC32: 0691B25B
CRC64: FD1FFCCA03780C98
SHA256: 6785038b3a289054264cb057283c2553865cb73c8e1ba41a350878684202ff83
SHA1: 3ea1e1ef851cf6e3750deedf159d1d314103ff10
BLAKE2sp: b7ce2aeac45e734d78199d16f6ee34656dfe32257c8a065776aa5e61646da87f
```

## Game Setup Instructions
No manual mod installation or other configuration is required to play Severed Steel with Archipelago. The client included with the APWorld does all the work by attaching to the game process and monitoring and manipulating the game state in real-time.

**Notes**
- This was developed with the game launched using DirectX 12. It may work with DirectX 11, but no guarantees

## Joining a Multiworld Game
- Launch Severed Steel and wait until you are in the main menu
- Open the Archipelago Launcher. Find and click _Severed Steel Client_
- Using the _Severed Steel Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `Severed Steel process found!`
  - You are now ready to play Severed Steel with Archipelago. Make sure to check out the `Severed Steel` tab in the client

## Continuing a Multiworld Game
- Perform the same steps as above

## Extra Notes
- The client will automatically unlock all mutators and mirrored mode. It will also prevent any scores from sending to the leaderboards
- There is no mechanism for locking Firefight 2.0 levels in the game. As such, nothing will prevent you from loading any level, but location checks will only send in levels you have unlocked
- When playing a seed with mutators, each level will only send location checks if the required mutator is present. You are free to play with any other mutator you desire, just be mindful of the effect on your scores
- When playing a seed with mirrored levels, each level will only send location checks if the correct mirrored state is present
