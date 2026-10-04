import enum


class DrMarioColors(enum.Enum):
    BLUE = "Blue"
    RED = "Red"
    YELLOW = "Yellow"


class DrMarioFillerTypes(enum.Enum):
    GARBAGE_CLEANUP = "Garbage Cleanup"
    PLACEBO = "Placebo"
    VIRUS_BUSTER = "Virus Buster"


class DrMarioFinalLevelSpeedOptions(enum.Enum):
    HIGH = 2
    LOW = 0
    MEDIUM = 1


class DrMarioGoalOptions(enum.Enum):
    ANTIVIRAL_SERUM_FINAL_LEVEL = 0
    ANTIVIRAL_SERUM_HUNT = 1


class DrMarioInputEffects(enum.Enum):
    CLOCKWISE_ROTATION_DISABLED = "Clockwise Rotation Disabled"
    COUNTERCLOCKWISE_ROTATION_DISABLED = "Counterclockwise Rotation Disabled"
    REVERSED_CONTROLS = "Reversed Controls"


class DrMarioLevels(enum.Enum):
    LEVEL_0 = "Level 0"
    LEVEL_1 = "Level 1"
    LEVEL_2 = "Level 2"
    LEVEL_3 = "Level 3"
    LEVEL_4 = "Level 4"
    LEVEL_5 = "Level 5"
    LEVEL_6 = "Level 6"
    LEVEL_7 = "Level 7"
    LEVEL_8 = "Level 8"
    LEVEL_9 = "Level 9"
    LEVEL_10 = "Level 10"
    LEVEL_11 = "Level 11"
    LEVEL_12 = "Level 12"
    LEVEL_13 = "Level 13"
    LEVEL_14 = "Level 14"
    LEVEL_15 = "Level 15"
    LEVEL_16 = "Level 16"
    LEVEL_17 = "Level 17"
    LEVEL_18 = "Level 18"
    LEVEL_19 = "Level 19"
    LEVEL_20 = "Level 20"


class DrMarioModes(enum.Enum):
    GAME_OVER = "Game Over"
    LEVEL_SETUP = "Level Setup"
    OPTIONS = "Options"
    PLAYER_SETUP = "Player Setup"
    PLAYING = "Playing"
    ROUND_END = "Round End"
    TITLE = "Title"
    VIRUS_PLACEMENT = "Virus Placement"


class DrMarioMusicTracks(enum.Enum):
    CHILL = "Chill"
    CHILL_LEVEL_CLEAR = "Chill Level Clear"
    CUTSCENE = "Cutscene"
    FEVER = "Fever"
    GAME_OVER = "Game Over"
    LEVEL_CLEAR = "Level Clear"
    LEVEL_TWENTY_LOW_CLEAR = "Level 20 Low Clear"
    OPTIONS = "Options"
    SILENCE = "Silence"
    TITLE = "Title"
    TWO_PLAYER_VICTORY = "Two Player Victory"


class DrMarioMusicTypes(enum.Enum):
    CHILL = "Chill"
    FEVER = "Fever"
    OFF = "Off"


class DrMarioNesColors(enum.Enum):
    BLACK = 0x0F
    BLUE = 0x11
    CYAN = 0x1C
    DARK_BLUE = 0x01
    DARK_CYAN = 0x0C
    DARK_GRAY = 0x2D
    DARK_GREEN = 0x0A
    DARK_INDIGO = 0x02
    DARK_LIME = 0x09
    DARK_MAGENTA = 0x05
    DARK_ORANGE = 0x07
    DARK_PURPLE = 0x04
    DARK_RED = 0x06
    DARK_SPRING_GREEN = 0x0B
    DARK_VIOLET = 0x03
    DARK_YELLOW = 0x08
    GRAY = 0x00
    GREEN = 0x1A
    INDIGO = 0x12
    LIGHT_BLUE = 0x21
    LIGHT_CYAN = 0x2C
    LIGHT_GRAY = 0x10
    LIGHT_GREEN = 0x2A
    LIGHT_INDIGO = 0x22
    LIGHT_LIME = 0x29
    LIGHT_MAGENTA = 0x25
    LIGHT_ORANGE = 0x27
    LIGHT_PURPLE = 0x24
    LIGHT_RED = 0x26
    LIGHT_SPRING_GREEN = 0x2B
    LIGHT_VIOLET = 0x23
    LIGHT_YELLOW = 0x28
    LIME = 0x19
    MAGENTA = 0x15
    ORANGE = 0x17
    PALE_BLUE = 0x31
    PALE_CYAN = 0x3C
    PALE_GRAY = 0x3D
    PALE_GREEN = 0x3A
    PALE_INDIGO = 0x32
    PALE_LIME = 0x39
    PALE_MAGENTA = 0x35
    PALE_ORANGE = 0x37
    PALE_PURPLE = 0x34
    PALE_RED = 0x36
    PALE_SPRING_GREEN = 0x3B
    PALE_VIOLET = 0x33
    PALE_YELLOW = 0x38
    PURPLE = 0x14
    RED = 0x16
    SPRING_GREEN = 0x1B
    VIOLET = 0x13
    WHITE = 0x30
    YELLOW = 0x18


class DrMarioPaletteRegions(enum.Enum):
    BACKDROP = "Backdrop"
    BORDERS = "Borders"
    BOTTLE = "Bottle"
    CHECKERBOARD_HIGH = "Checkerboard High"
    CHECKERBOARD_LOW = "Checkerboard Low"
    CHECKERBOARD_MEDIUM = "Checkerboard Medium"
    CLIPBOARD = "Clipboard"
    HIGHLIGHTS = "Highlights"
    MAGNIFIER_FRAME = "Magnifier Frame"
    MAGNIFIER_LENS = "Magnifier Lens"
    SPLASH_CHECKERBOARD = "Splash Checkerboard"


class DrMarioSpeeds(enum.Enum):
    HIGH = "High"
    LOW = "Low"
    MEDIUM = "Medium"


class DrMarioSpeedUpBehaviorOptions(enum.Enum):
    DISABLED = 1
    VANILLA = 0


class DrMarioTags(enum.Enum):
    CHAIN_2_LOCATION = "Trigger a 2-Chain Location"
    CHAIN_LOCATION = "Chain Location"
    COLOR_ELIMINATION_BLUE_LOCATION = "Eliminate All Blue Viruses Location"
    COLOR_ELIMINATION_LOCATION = "Color Elimination Location"
    COLOR_ELIMINATION_RED_LOCATION = "Eliminate All Red Viruses Location"
    COLOR_ELIMINATION_YELLOW_LOCATION = "Eliminate All Yellow Viruses Location"
    COLOR_LINE_BLUE_LOCATION = "Clear 2 Blue Lines with One Pill Location"
    COLOR_LINE_LOCATION = "Color Line Location"
    COLOR_LINE_RED_LOCATION = "Clear 2 Red Lines with One Pill Location"
    COLOR_LINE_YELLOW_LOCATION = "Clear 2 Yellow Lines with One Pill Location"
    COLOR_VIRUS_COUNT_1_LOCATION = "Eliminate 1 Color Virus Location"
    COLOR_VIRUS_COUNT_2_LOCATION = "Eliminate 2 Color Viruses Location"
    COLOR_VIRUS_COUNT_3_LOCATION = "Eliminate 3 Color Viruses Location"
    COLOR_VIRUS_COUNT_LOCATION = "Color Virus Count Location"
    FILLER_ITEM = "Filler Item"
    GARBAGE_REDUCTION_ITEM = "Garbage Reduction Item"
    GOAL_ITEM = "Goal Item"
    LEVEL_0_ITEM = "Level 0 Item"
    LEVEL_1_ITEM = "Level 1 Item"
    LEVEL_2_ITEM = "Level 2 Item"
    LEVEL_3_ITEM = "Level 3 Item"
    LEVEL_4_ITEM = "Level 4 Item"
    LEVEL_5_ITEM = "Level 5 Item"
    LEVEL_6_ITEM = "Level 6 Item"
    LEVEL_7_ITEM = "Level 7 Item"
    LEVEL_8_ITEM = "Level 8 Item"
    LEVEL_9_ITEM = "Level 9 Item"
    LEVEL_10_ITEM = "Level 10 Item"
    LEVEL_11_ITEM = "Level 11 Item"
    LEVEL_12_ITEM = "Level 12 Item"
    LEVEL_13_ITEM = "Level 13 Item"
    LEVEL_14_ITEM = "Level 14 Item"
    LEVEL_15_ITEM = "Level 15 Item"
    LEVEL_16_ITEM = "Level 16 Item"
    LEVEL_17_ITEM = "Level 17 Item"
    LEVEL_18_ITEM = "Level 18 Item"
    LEVEL_19_ITEM = "Level 19 Item"
    LEVEL_20_ITEM = "Level 20 Item"
    LEVEL_0_LOCATION = "Level 0 Location"
    LEVEL_1_LOCATION = "Level 1 Location"
    LEVEL_2_LOCATION = "Level 2 Location"
    LEVEL_3_LOCATION = "Level 3 Location"
    LEVEL_4_LOCATION = "Level 4 Location"
    LEVEL_5_LOCATION = "Level 5 Location"
    LEVEL_6_LOCATION = "Level 6 Location"
    LEVEL_7_LOCATION = "Level 7 Location"
    LEVEL_8_LOCATION = "Level 8 Location"
    LEVEL_9_LOCATION = "Level 9 Location"
    LEVEL_10_LOCATION = "Level 10 Location"
    LEVEL_11_LOCATION = "Level 11 Location"
    LEVEL_12_LOCATION = "Level 12 Location"
    LEVEL_13_LOCATION = "Level 13 Location"
    LEVEL_14_LOCATION = "Level 14 Location"
    LEVEL_15_LOCATION = "Level 15 Location"
    LEVEL_16_LOCATION = "Level 16 Location"
    LEVEL_17_LOCATION = "Level 17 Location"
    LEVEL_18_LOCATION = "Level 18 Location"
    LEVEL_19_LOCATION = "Level 19 Location"
    LEVEL_20_LOCATION = "Level 20 Location"
    LEVEL_CLEAR_HIGH_SPEED_LOCATION = "Clear the Level on High Speed Location"
    LEVEL_CLEAR_LOCATION = "Level Clear Location"
    LEVEL_CLEAR_LOW_SPEED_LOCATION = "Clear the Level on Low Speed Location"
    LEVEL_CLEAR_MEDIUM_SPEED_LOCATION = "Clear the Level on Medium Speed Location"
    LEVEL_UNLOCK_ITEM = "Level Unlock Item"
    MATCH_LENGTH_REDUCTION_ITEM = "Match Length Reduction Item"
    MULTI_LINE_2_LOCATION = "Clear 2 Lines with One Pill Location"
    MULTI_LINE_3_LOCATION = "Clear 3 Lines with One Pill Location"
    MULTI_LINE_LOCATION = "Multi-Line Location"
    MULTI_VIRUS_2_LOCATION = "Destroy 2 Viruses with One Pill Location"
    MULTI_VIRUS_3_LOCATION = "Destroy 3 Viruses with One Pill Location"
    MULTI_VIRUS_LOCATION = "Multi-Virus Location"
    MUSIC_UNLOCK_ITEM = "Music Unlock Item"
    NEXT_PILL_PREVIEW_ITEM = "Next Pill Preview Item"
    OOL_ITEM = "OOL Item"
    PILL_ITEM = "Pill Item"
    ROTATION_ITEM = "Rotation Item"
    SPEED_UNLOCK_ITEM = "Speed Unlock Item"
    TRAP_ITEM = "Trap Item"
    VIRUS_ELIMINATION_HALF_LOCATION = "Eliminate Half of the Viruses Location"
    VIRUS_ELIMINATION_LOCATION = "Virus Elimination Location"
    VIRUS_ELIMINATION_QUARTER_LOCATION = "Eliminate a Quarter of the Viruses Location"


class DrMarioTrapTypes(enum.Enum):
    CONTAGION = "Contagion Trap"
    GARBAGE = "Garbage Trap"
    GRAYSCALE = "Grayscale Trap"
    MUTATION = "Mutation Trap"
    REVERSE_CONTROL = "Reverse Control Trap"
    SMILEY = ":) Trap"
