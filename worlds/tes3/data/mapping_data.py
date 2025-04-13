from typing import *

from ..enums import TES3Attributes, TES3Classes, TES3Skills


class_attributes: Dict[TES3Classes, Tuple[TES3Attributes]] = {
    TES3Classes.ACROBAT: (
        TES3Attributes.AGILITY,
        TES3Attributes.ENDURANCE,
    ),
    TES3Classes.AGENT: (
        TES3Attributes.AGILITY,
        TES3Attributes.PERSONALITY,
    ),
    TES3Classes.ARCHER: (
        TES3Attributes.AGILITY,
        TES3Attributes.STRENGTH,
    ),
    TES3Classes.ASSASSIN: (
        TES3Attributes.INTELLIGENCE,
        TES3Attributes.SPEED,
    ),
    TES3Classes.BARBARIAN: (
        TES3Attributes.SPEED,
        TES3Attributes.STRENGTH,
    ),
    TES3Classes.BARD: (
        TES3Attributes.INTELLIGENCE,
        TES3Attributes.PERSONALITY,
    ),
    TES3Classes.BATTLEMAGE: (
        TES3Attributes.INTELLIGENCE,
        TES3Attributes.STRENGTH,
    ),
    TES3Classes.CRUSADER: (
        TES3Attributes.AGILITY,
        TES3Attributes.STRENGTH,
    ),
    TES3Classes.HEALER: (
        TES3Attributes.PERSONALITY,
        TES3Attributes.WILLPOWER,
    ),
    TES3Classes.KNIGHT: (
        TES3Attributes.PERSONALITY,
        TES3Attributes.STRENGTH,
    ),
    TES3Classes.MAGE: (
        TES3Attributes.INTELLIGENCE,
        TES3Attributes.WILLPOWER,
    ),
    TES3Classes.MONK: (
        TES3Attributes.AGILITY,
        TES3Attributes.WILLPOWER,
    ),
    TES3Classes.NIGHTBLADE: (
        TES3Attributes.SPEED,
        TES3Attributes.WILLPOWER,
    ),
    TES3Classes.PILGRIM: (
        TES3Attributes.ENDURANCE,
        TES3Attributes.PERSONALITY,
    ),
    TES3Classes.ROGUE: (
        TES3Attributes.PERSONALITY,
        TES3Attributes.SPEED,
    ),
    TES3Classes.SCOUT: (
        TES3Attributes.ENDURANCE,
        TES3Attributes.SPEED,
    ),
    TES3Classes.SORCERER: (
        TES3Attributes.ENDURANCE,
        TES3Attributes.INTELLIGENCE,
    ),
    TES3Classes.SPELLSWORD: (
        TES3Attributes.ENDURANCE,
        TES3Attributes.WILLPOWER,
    ),
    TES3Classes.THIEF: (
        TES3Attributes.AGILITY,
        TES3Attributes.SPEED,
    ),
    TES3Classes.WARRIOR: (
        TES3Attributes.ENDURANCE,
        TES3Attributes.STRENGTH,
    ),
    TES3Classes.WITCHHUNTER: (
        TES3Attributes.AGILITY,
        TES3Attributes.INTELLIGENCE,
    ),
}


class_skills: Dict[TES3Classes, Tuple[TES3Skills]] = {
    TES3Classes.ACROBAT: (
        TES3Skills.ACROBATICS,
        TES3Skills.ALTERATION,
        TES3Skills.ATHLETICS,
        TES3Skills.HAND_TO_HAND,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.MARKSMAN,
        TES3Skills.SNEAK,
        TES3Skills.SPEAR,
        TES3Skills.SPEECHCRAFT,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.AGENT: (
        TES3Skills.ACROBATICS,
        TES3Skills.BLOCK,
        TES3Skills.CONJURATION,
        TES3Skills.ILLUSION,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.MERCANTILE,
        TES3Skills.SHORT_BLADE,
        TES3Skills.SNEAK,
        TES3Skills.SPEECHCRAFT,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.ARCHER: (
        TES3Skills.ATHLETICS,
        TES3Skills.BLOCK,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.LONG_BLADE,
        TES3Skills.MARKSMAN,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.RESTORATION,
        TES3Skills.SNEAK,
        TES3Skills.SPEAR,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.ASSASSIN: (
        TES3Skills.ACROBATICS,
        TES3Skills.ALCHEMY,
        TES3Skills.ATHLETICS,
        TES3Skills.BLOCK,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.LONG_BLADE,
        TES3Skills.MARKSMAN,
        TES3Skills.SECURITY,
        TES3Skills.SHORT_BLADE,
        TES3Skills.SNEAK,
    ),
    TES3Classes.BARBARIAN: (
        TES3Skills.ACROBATICS,
        TES3Skills.ARMORER,
        TES3Skills.ATHLETICS,
        TES3Skills.AXE,
        TES3Skills.BLOCK,
        TES3Skills.BLUNT_WEAPON,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.MARKSMAN,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.BARD: (
        TES3Skills.ACROBATICS,
        TES3Skills.ALCHEMY,
        TES3Skills.BLOCK,
        TES3Skills.ENCHANT,
        TES3Skills.ILLUSION,
        TES3Skills.LONG_BLADE,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.MERCANTILE,
        TES3Skills.SECURITY,
        TES3Skills.SPEECHCRAFT,
    ),
    TES3Classes.BATTLEMAGE: (
        TES3Skills.ALCHEMY,
        TES3Skills.ALTERATION,
        TES3Skills.AXE,
        TES3Skills.CONJURATION,
        TES3Skills.DESTRUCTION,
        TES3Skills.ENCHANT,
        TES3Skills.HEAVY_ARMOR,
        TES3Skills.LONG_BLADE,
        TES3Skills.MARKSMAN,
        TES3Skills.MYSTICISM,
    ),
    TES3Classes.CRUSADER: (
        TES3Skills.ALCHEMY,
        TES3Skills.ARMORER,
        TES3Skills.BLOCK,
        TES3Skills.BLUNT_WEAPON,
        TES3Skills.DESTRUCTION,
        TES3Skills.HAND_TO_HAND,
        TES3Skills.HEAVY_ARMOR,
        TES3Skills.LONG_BLADE,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.RESTORATION,
    ),
    TES3Classes.HEALER: (
        TES3Skills.ALCHEMY,
        TES3Skills.ALTERATION,
        TES3Skills.BLUNT_WEAPON,
        TES3Skills.HAND_TO_HAND,
        TES3Skills.ILLUSION,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.MYSTICISM,
        TES3Skills.RESTORATION,
        TES3Skills.SPEECHCRAFT,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.KNIGHT: (
        TES3Skills.ARMORER,
        TES3Skills.AXE,
        TES3Skills.BLOCK,
        TES3Skills.ENCHANT,
        TES3Skills.HEAVY_ARMOR,
        TES3Skills.LONG_BLADE,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.MERCANTILE,
        TES3Skills.RESTORATION,
        TES3Skills.SPEECHCRAFT,
    ),
    TES3Classes.MAGE: (
        TES3Skills.ALCHEMY,
        TES3Skills.ALTERATION,
        TES3Skills.CONJURATION,
        TES3Skills.DESTRUCTION,
        TES3Skills.ENCHANT,
        TES3Skills.ILLUSION,
        TES3Skills.MYSTICISM,
        TES3Skills.RESTORATION,
        TES3Skills.SHORT_BLADE,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.MONK: (
        TES3Skills.ACROBATICS,
        TES3Skills.ATHLETICS,
        TES3Skills.BLOCK,
        TES3Skills.BLUNT_WEAPON,
        TES3Skills.HAND_TO_HAND,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.MARKSMAN,
        TES3Skills.RESTORATION,
        TES3Skills.SNEAK,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.NIGHTBLADE: (
        TES3Skills.ALTERATION,
        TES3Skills.DESTRUCTION,
        TES3Skills.ILLUSION,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.MARKSMAN,
        TES3Skills.MYSTICISM,
        TES3Skills.SECURITY,
        TES3Skills.SHORT_BLADE,
        TES3Skills.SNEAK,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.PILGRIM: (
        TES3Skills.ALCHEMY,
        TES3Skills.BLOCK,
        TES3Skills.HAND_TO_HAND,
        TES3Skills.ILLUSION,
        TES3Skills.MARKSMAN,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.MERCANTILE,
        TES3Skills.RESTORATION,
        TES3Skills.SHORT_BLADE,
        TES3Skills.SPEECHCRAFT,
    ),
    TES3Classes.ROGUE: (
        TES3Skills.ATHLETICS,
        TES3Skills.AXE,
        TES3Skills.BLOCK,
        TES3Skills.HAND_TO_HAND,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.LONG_BLADE,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.MERCANTILE,
        TES3Skills.SHORT_BLADE,
        TES3Skills.SPEECHCRAFT,
    ),
    TES3Classes.SCOUT: (
        TES3Skills.ALCHEMY,
        TES3Skills.ALTERATION,
        TES3Skills.ATHLETICS,
        TES3Skills.BLOCK,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.LONG_BLADE,
        TES3Skills.MARKSMAN,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.SNEAK,
        TES3Skills.UNARMORED,
    ),
    TES3Classes.SORCERER: (
        TES3Skills.ALTERATION,
        TES3Skills.CONJURATION,
        TES3Skills.DESTRUCTION,
        TES3Skills.ENCHANT,
        TES3Skills.HEAVY_ARMOR,
        TES3Skills.ILLUSION,
        TES3Skills.MARKSMAN,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.MYSTICISM,
        TES3Skills.SHORT_BLADE,
    ),
    TES3Classes.SPELLSWORD: (
        TES3Skills.ALCHEMY,
        TES3Skills.ALTERATION,
        TES3Skills.AXE,
        TES3Skills.BLOCK,
        TES3Skills.BLUNT_WEAPON,
        TES3Skills.DESTRUCTION,
        TES3Skills.ENCHANT,
        TES3Skills.LONG_BLADE,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.RESTORATION,
    ),
    TES3Classes.THIEF: (
        TES3Skills.ACROBATICS,
        TES3Skills.ATHLETICS,
        TES3Skills.HAND_TO_HAND,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.MARKSMAN,
        TES3Skills.MERCANTILE,
        TES3Skills.SECURITY,
        TES3Skills.SHORT_BLADE,
        TES3Skills.SNEAK,
        TES3Skills.SPEECHCRAFT,
    ),
    TES3Classes.WARRIOR: (
        TES3Skills.ARMORER,
        TES3Skills.ATHLETICS,
        TES3Skills.AXE,
        TES3Skills.BLOCK,
        TES3Skills.BLUNT_WEAPON,
        TES3Skills.HEAVY_ARMOR,
        TES3Skills.LONG_BLADE,
        TES3Skills.MARKSMAN,
        TES3Skills.MEDIUM_ARMOR,
        TES3Skills.SPEAR,
    ),
    TES3Classes.WITCHHUNTER: (
        TES3Skills.ALCHEMY,
        TES3Skills.BLOCK,
        TES3Skills.BLUNT_WEAPON,
        TES3Skills.CONJURATION,
        TES3Skills.ENCHANT,
        TES3Skills.LIGHT_ARMOR,
        TES3Skills.MARKSMAN,
        TES3Skills.MYSTICISM,
        TES3Skills.SNEAK,
        TES3Skills.UNARMORED,
    ),
}
