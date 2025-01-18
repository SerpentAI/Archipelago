from __future__ import annotations

from typing import List, Set

from dataclasses import dataclass

from Options import OptionSet, Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DeadByDaylightKeymastersKeepOptions:
    dbd_play_style: DbDPlayStyle


class DeadByDaylightGame(Game):
    name = "Dead By Daylight"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS4,
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.NXN,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = True

    @property
    def play_style(self) -> Set[str]:
        return self.archipelago_options.dbdplaystyle.value
    
    @property
    def playing_killer(self) -> bool:
        return "Killer" in self.play_style

    @property
    def playing_survivor(self) -> bool:
        return "Survivor" in self.play_style

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Escape as the last Survivor or earn Merciless Killer without using any Perks",
                data={},
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Earn 4 Iridescent Emblems",
                data={},
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
        ]
    
        if self.playing_killer:
            objectives.extend([
                GameObjectiveTemplate(
                    label="As BASEKILLER earn Merciless Killer",
                    data={
                        "BASEKILLER": (self.base_killers, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER damage 3 Generators in one match",
                    data={
                        "BASEKILLER": (self.base_killers, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER sacrifice 2 Survivors without any addons",
                    data={
                        "BASEKILLER": (self.base_killers, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER down every Survivor at least once without using your power",
                    data={
                        "BASEKILLER": (self.base_killers, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Grab 2 Survivors either from off a generator or out of a locker",
                    data={},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER hook every Survivor in the basement at least once",
                    data={
                        "BASEKILLER": (self.base_killers, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Sacrifice MED Surivors while having a Hex Totem Perk still active",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Sacrifice MED Survivors while having a Hex Totem Perk still active",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Sacrifice MED Survivors without breaking a single pallet",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER grab MED Survivors who are vaulting",
                    data={
                        "MED": (self.medium_range, 1),
                        "BASEKILLER": (self.base_killers, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER get a total of MEDTOTALHOOKS hook stages without any Survivors dying",
                    data={
                        "MEDTOTALHOOKS": (self.medium_total_hooks_range, 1),
                        "BASEKILLER": (self.base_killers, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Hook every Survivor at least once before the first Generator is completed",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
                
                GameObjectiveTemplate(
                    label="Have MED alive Survivors on hook at any given time",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER Sacrifice all 4 Survivors",
                    data={
                        "BASEKILLEER": (self.base_killers, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Sacrifice MED Survivors during Endgame Collapse",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Down MED Survivors while they're Healing",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Hook a single specific Survivor in the Basement MED times",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Down a Survivor while carrying another Survivor",
                    data={},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Down MED Survivors who didn't vault during the chase",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Kick the same Generator at least MED times",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER kick the same Generator at least MED times",
                    data={
                        "MED": (self.medium_range, 1),
                        "BASEKILLEER": (self.base_killers, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="As BASEKILLER down a Survivor who is Clensing a Totem",
                    data={
                        "BASEKILLEER": (self.base_killers, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Down MED Survivors who are Clensing a Totem",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
            ]

        if self.playing_survivor:
            objectives.extend([
                GameObjectiveTemplate(
                    label="Escape after you have done MED generators without missing a skill check",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Clense MED totems",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Complete a Generator while in the Killer's Terror Radius",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Escape MED chases by hiding in a Locker",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Complete HIGH Great Skill Checks in a row",
                    data={
                        "HIGH": (self.high_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Vault HIGH times in a single chase",
                    data={
                        "HIGH": (self.high_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Perform MED safe unhooks",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Complete MED generators before MEDTOTALHOOKS total hook stages",
                    data={
                        "MED": (self.medium_range, 1),
                        "MEDTOTALHOOKS": (self.medium_total_hooks_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Pallet stun the Killer MED times",
                    data={
                        "PALLETSTUNS": (self.medium_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Heal MED other Survivors using a Med-kit",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Rescue all other survivors from the hook at least once",
                    data={},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Take a protection hit for MED other Survivors and escape",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Open MED chests in a match and escape with one of the items",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Blind the killer MED times",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Work on and complete MED Generators with 1 other Survivor",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Escape through Hatch",
                    data={},
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Work on and complete HIGH Generators",
                    data={
                        "HIGH": (self.high_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Escape without using any items or exhaustion perks",
                    data={},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Successfully wiggle out of the Killer's grasp",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Sabotage HIGH hooks",
                    data={
                        "HIGH": (self.high_range, 1),
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Successfully unhook yourself by any means",
                    data={},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Escape without ever being healed to the Healthy state",
                    data={
                        "MED": (self.medium_range, 1),
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ])

    @staticmethod
    def medium_range() -> range:
        return range(2,3)
    
    @staticmethod
    def medium_total_hooks_range() -> range:
        return range(4,6)
        
    @staticmethod
    def high_range() -> range:
        return range(3,4)

    @staticmethod
    def base_killers() -> List[str]:
        return [
            "Trapper",
            "Wraith",
            "Huntress",
            "Nurse",
            "Hillbilly",
        ]

# Archipelago Options
class DbDPlayStyle(OptionSet):
    """
    Indicates if the player wants to play as Survivor, Killer, or Both.
    """
    valid_keys = [
        "Killer",
        "Survivor"
    ]

    default = valid_keys