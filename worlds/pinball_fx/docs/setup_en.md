# Pinball FX Randomizer Setup Guide

## Requirements
- Windows OS (Hard required. Client is using memory reading / writing through Windows APIs)
- Pinball FX installed through Steam
- Archipelago 0.6.7+

**Hashes of expected PinballFX-Win64-Shipping.exe**
```
Name: PinballFX-Win64-Shipping.exe
Size: 102123008 bytes (97 MiB)
CRC32: DBFFA88C
CRC64: 7525D766A4FE05DA
SHA256: 952f63e5fed1de1b8e8c659c469b9f9860eda499f8d1ed262d3569632168498e
SHA1: 9b6ee89e69ce964ecb053b6d1d67a7f6e9c6fc8c
BLAKE2sp: a13a7c5d960754e433efce65e2df2ca4cc11aabc7626e252438e9474bc8f74b3

```

## Game Setup Instructions
No manual mod installation or other configuration is required to play Pinball FX with Archipelago. The client included with the APWorld does all the work by attaching to the game process and monitoring the game state in real-time.

**Notes**
- Since Pinball FX is a competitive game with leaderboards, the implementation doesn't alter gameplay in any way and doesn't give the player any sort of advantage. The scoring-related useful items apply to the calculations made by the client; nothing is changed in-game.
- Game updates are expected to break the implementation. Updates should follow shortly after to maintain support.

## Joining a Multiworld Game
- Launch Pinball FX and proceed until you are in the main menu
- Open the Archipelago Launcher. Find and click _Pinball FX Client_
- Using the _Pinball FX Client_:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and click Connect
  - Input your player name at the bottom when prompted and press Enter
  - You should now be connected to the Archipelago room
  - After a few seconds, you should see a message in the client that says `Pinball FX process found!`
  - You are now ready to play Pinball FX with Archipelago. Make sure to check out the `Pinball FX` tab in the client

## Continuing a Multiworld Game
- Perform the same steps as above

## Extra Notes
- Zen Studios doesn't provide baseline scores for their tables in Pinball FX. The methodology used to generate target scores considers the #100 scores on each table + game mode leaderboard as the base score for calculations. After further calculations are performed at generation time, the experience will roughly translate to this:
  - At 100% score percentage, more casual players should be able to comfortably complete Low / Mid / High target scores. Very High targets will be challenging but shouldn't be impossible.
  - At 400% score percentage, beating a Very High target score should make you crack the Top 100 for that table + game mode
