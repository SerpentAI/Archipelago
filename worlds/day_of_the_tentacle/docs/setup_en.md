# Day of the Tentacle Randomizer Setup Guide

## Requirements

- Windows OS (Hard required. Client reads, writes and allocates memory in the ScummVM process and redirects some of its function pointers to code it injects there, through the Win32 API. No remote threads are created)
- The CD version of Day of the Tentacle, in English: `tentacle.000`, `tentacle.001` and `monster.sou`
  - If you own Day of the Tentacle Remastered (on GOG or Steam), the classic game files can be extracted from it. See the [PCGamingWiki](https://www.pcgamingwiki.com/wiki/Day_of_the_Tentacle_Remastered#Run_classic_mode_in_ScummVM) for instructions
- ScummVM 2026.3.0 64-bit ([Direct Download](https://downloads.scummvm.org/frs/scummvm/2026.3.0/scummvm-2026.3.0-win32-x86_64.zip))
- Archipelago 0.6.7+


## Game Setup Instructions

No game modding is required to play Day of the Tentacle with Archipelago. The client included with the APWorld does all the work by attaching to the ScummVM process and reading and manipulating the game state in real-time.

- Unzip the contents of the ScummVM zip file you downloaded earlier to a directory of your choosing.
- Launch ScummVM.
- Click `Add Game` and select the directory containing `tentacle.000`, `tentacle.001` and `monster.sou`.
- Verify that the game launches and plays normally.


## Joining a Multiworld Game

- Launch Day of the Tentacle through ScummVM and start a new game.
- Open the Archipelago Launcher. Find and click `Day of the Tentacle Client`.
- Using the `Day of the Tentacle Client`:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and press `Connect`.
  - Input your player name at the bottom when prompted and press `Enter`.
  - You should now be connected to the Archipelago room.
  - After a few seconds, you should see a message in the client that says `Day of the Tentacle process found!`
  - You are now ready to play Day of the Tentacle with Archipelago. Make sure to check out the `Day of the Tentacle` tab in the client.
- Play through the intro as usual. Once it ends, the client prepares your save: the starting items are taken away and you are switched to your starting character.


## Continuing a Multiworld Game

- Perform the same steps as above, but instead of starting a new game, load your latest save file.
  - Always double-check you are loading the save for the seed you intend to play. Loading the wrong save and connecting to the client can send location checks that you haven't performed.


## Important Notes

- Restarting the client or ScummVM is fine. Stop playing until the client is connected again, then load your latest save if ScummVM was restarted.
- Before the finale, the client automatically saves to slot 9, "AP Before Finale". This is quality-of-life for no release players, as there is no going back from the finale. Do NOT use slot 9 for manual saves!
- A few harmless visual glitches are expected:
  - Daring George Washington skips the tree-chopping cutscene. Washington and the tree simply vanish. This is what lets Laverne start directly in the kennel and not require a long Hoagie chain for her to be playable.
  - Using the flagpole crank on the roof briefly shows Laverne without her disguise, but still in its colors.
  - Red Ted briefly disappears while you take the rope off Dr. Fred in the attic.
