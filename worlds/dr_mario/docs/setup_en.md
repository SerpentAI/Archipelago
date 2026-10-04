# Dr. Mario Randomizer Setup Guide

## Requirements

- Windows OS (Hard required. Client reads, writes and allocates memory in the Mesen process and runs remote threads in it, through the Win32 API)
- Your legally obtained Dr. Mario Rev 1 ROM file, probably named `Dr. Mario (Japan, USA) (En) (Rev 1).nes`
- Mesen 2.2.1 ([Direct Download](https://github.com/nesdev-org/MesenCE/releases/download/2.2.1/Mesen_2.2.1_Windows.zip))
- Archipelago 0.6.7+
- [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases) (Strongly recommended. Enables logic tracking in the client and in-game)

**Hash of expected ROM**
```
Name: Dr. Mario (Japan, USA) (En) (Rev 1).nes
CRC32: 92BED9D7
```


## Game Setup Instructions

No game modding is required to play Dr. Mario with Archipelago. The client included with the APWorld does all the work by attaching to the Mesen process and reading and manipulating the game state in real-time. Your ROM file is never modified.

- Unzip the contents of the Mesen zip file you downloaded earlier to a directory of your choosing.
- Launch Mesen and open your Dr. Mario ROM. Set up your controls as usual.
- Verify that the game launches and plays normally.
- The `Dr. Mario Client` launches Mesen with the ROM whenever Mesen isn't already running. The first time, it asks you to locate `Mesen.exe` and your Dr. Mario ROM. Set `rom_start` to `false` under `dr_mario_options` in `host.yaml` to turn this off.


## Joining a Multiworld Game

- Open the Archipelago Launcher. Find and click `Dr. Mario Client`.
- Using the `Dr. Mario Client`:
  - Enter the room's hostname and port number (e.g. archipelago.gg:54321) in the top box and press `Connect`.
  - Input your player name at the bottom when prompted and press `Enter`.
  - You should now be connected to the Archipelago room.
  - After a few seconds, you should see a message in the client that says `Dr. Mario process found!`
  - You are now ready to play Dr. Mario with Archipelago. Make sure to check out the `Dr. Mario` tab in the client.
- The game returns to the title screen when the client attaches.


## Continuing a Multiworld Game

- Perform the same steps as above.


## Important Notes

- Restarting the client or Mesen is fine.
- If you update the APWorld while Mesen is running, restart Mesen.
- Client commands:
  - `/deathlink`: Toggle death link. Only available when death link is enabled in your options.
