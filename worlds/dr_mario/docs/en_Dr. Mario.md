# Dr. Mario

## Randomizer Summary

The Dr. Mario randomizer takes the classic virus-busting puzzle game and layers a progression system on top of it. Every level starts stripped down to a single random two-color pill type, and you will need to unlock levels, speeds, the other pill types and various per-level abilities to progress. Collect enough Antiviral Serum and optionally clear a final level to reach your goal.

**Locations**
- Per Level:
  - Eliminating a Quarter / Half of the Viruses
  - Eliminating 1 / 2 / 3 Viruses of Each Color
  - Eliminating All Viruses of Each Color
  - Destroying 2 / 3 Viruses with One Pill
  - Clearing 2 / 3 Lines with One Pill
  - Clearing 2 Lines of the Same Color with One Pill
  - Triggering a 2-Chain
  - Clearing the Level on Low / Medium / High Speed

**Items**
- Antiviral Serum
- Level Unlocks (Progressive or Individual)
- Progressive Speed Unlocks
- Progressive Match Length Reductions (Optional)
- Per Level:
  - Pill Types (Red-Red, Red-Blue, Red-Yellow, Blue-Blue, Blue-Yellow, Yellow-Yellow)
  - Clockwise / Counterclockwise Rotation (Optional)
  - Next Pill Preview (Optional)
  - Progressive Starting Garbage Reductions (Optional)


## Randomizer Features
- All 21 levels and 3 speeds are supported
- 2 goals to choose from:
  - `Antiviral Serum + Final Level`: Collect enough Antiviral Serum to unlock a Final Level and clear it
  - `Antiviral Serum Hunt`: Collect a set amount of Antiviral Serum spread across the multiworld
- Ability to customize the final level (10-20) and the speed it must be cleared on
- Ability to unlock levels progressively or individually
- Ability to customize the starting match length (3-7)
- Ability to start levels with garbage (0-3 levels)
- Option to restrict each level to a single rotation direction
- Option to lock the next pill preview
- Option to disable pill speed-ups
- 6 unique traps to experience with configurable weights and durations
- Support for death link (with the ability to toggle it off with a command)
- Ability to shuffle the music, lock the music choices and randomize Mario, virus and checkerboard colors
- Scales well for all types of multiworlds: Short / Long Syncs, Asyncs; ~170-470 checks
- Custom client UI that displays important information and updates in real-time
- No manual mod installation required! The Archipelago client hooks into the game at runtime. Nothing else to download, install, or configure.
- Feature-complete and tested


## Differences from the Original Game
- Clearing a level returns to the options screen.
- Pressing Select while paused returns to the options screen.
- The TOP score box shows the current level's loadout under `MGNPAB`: Match length, starting Garbage levels, Next pill preview (Y/N), number of Pill types, and the A (clockwise) and B (counterclockwise) rotations (Y/N).
- From Level 2 on, levels have up to 4 more or fewer viruses than usual.


## Tracking

**Universal Tracker**

The APWorld is fully compatible with Universal Tracker. It is a YAML-free implementation (i.e. you don't need to have the YAML used to generate in your Players directory). If Universal Tracker is installed, the client will automatically embed the Tracker tab and will also enhance some of its views with in / out of logic data.
