from ..d2r_table import D2RTable


class SuperUniquesD2RTable(D2RTable):
    file_name = "superuniques.txt"

    column_names = (
        "Superunique",
        "Name",
        "Class",
        "hcIdx",
        "MonSound",
        "Mod1",
        "Mod2",
        "Mod3",
        "MinGrp",
        "MaxGrp",
        "AutoPos",
        "Stacks",
        "Replaceable",
        "Utrans",
        "Utrans(N)",
        "Utrans(H)",
        "TC",
        "TC Desecrated",
        "TC(N)",
        "TC(N) Desecrated",
        "TC(H)",
        "TC(H) Desecrated",
        "*eol",
    )

    def __init__(self):
        super().__init__(index_column="Name")
        
    def _bootstrap(self):
        self.add_row(['Bishibosh', 'Bishibosh', 'fallenshaman1', '0', '', '8', '9', '0', '2', '2', '1', '0', '', '11', '11', '11', 'Act 1 Super A', '', 'Act 1 (N) Super A', '', 'Act 1 (H) Super A', 'Act 1 (H) Super A Desecrated', '0'])
        self.add_row(['Bonebreak', 'Bonebreak', 'skeleton1', '1', '', '5', '8', '0', '5', '5', '1', '0', '', '5', '5', '5', 'Act 1 Super A', '', 'Act 1 (N) Super A', '', 'Act 1 (H) Super A', 'Act 1 (H) Super A Desecrated', '0'])
        self.add_row(['Coldcrow', 'Coldcrow', 'cr_archer1', '2', '', '18', '0', '0', '4', '4', '1', '0', '', '18', '18', '18', 'Act 1 Super A', '', 'Act 1 (N) Super A', '', 'Act 1 (H) Super A', 'Act 1 (H) Super A Desecrated', '0'])
        self.add_row(['Rakanishu', 'Rakanishu', 'fallen2', '3', '', '17', '6', '0', '8', '8', '0', '0', '1', '29', '29', '29', 'Act 1 Super B', '', 'Act 1 (N) Super B', '', 'Act 1 (H) Super B', 'Act 1 (H) Super B Desecrated', '0'])
        self.add_row(['Treehead WoodFist', 'Treehead WoodFist', 'brute2', '4', '', '5', '6', '0', '2', '2', '1', '0', '1', '4', '4', '4', 'Act 1 Super B', '', 'Act 1 (N) Super B', '', 'Act 1 (H) Super B', 'Act 1 (H) Super B Desecrated', '0'])
        self.add_row(['Griswold', 'Griswold', 'griswold', '5', '', '7', '0', '0', '0', '0', '1', '0', '1', '17', '17', '17', 'Griswold', 'Griswold Desecrated A', 'Griswold (N)', 'Griswold (N) Desecrated A', 'Griswold (H)', 'Griswold (H) Desecrated A', '0'])
        self.add_row(['The Countess', 'The Countess', 'corruptrogue3', '6', 'countess', '9', '0', '0', '6', '6', '1', '0', '', '16', '16', '16', 'Countess', 'Countess Desecrated A', 'Countess (N)', 'Countess (N) Desecrated A', 'Countess (H)', 'Countess (H) Desecrated A', '0'])
        self.add_row(['Pitspawn Fouldog', 'Pitspawn Fouldog', 'bighead2', '7', '', '7', '18', '0', '4', '4', '1', '0', '', '31', '31', '31', 'Act 1 Super B', '', 'Act 1 (N) Super B', '', 'Act 1 (H) Super B', 'Act 1 (H) Super B Desecrated', '0'])
        self.add_row(['Flamespike the Crawler', 'Flamespike the Crawler', 'quillrat4', '8', '', '9', '7', '0', '6', '6', '1', '0', '', '16', '16', '16', 'Act 1 Unique C', '', 'Act 1 (N) Unique C', '', 'Act 1 (H) Unique C', 'Act 1 (H) Unique C Desecrated', '0'])
        self.add_row(['Boneash', 'Boneash', 'skmage_pois3', '9', '', '8', '5', '18', '0', '0', '1', '0', '', '15', '15', '15', 'Act 1 Super C', '', 'Act 1 (N) Super C', '', 'Act 1 (H) Super C', 'Act 1 (H) Super C Desecrated', '0'])
        self.add_row(['Radament', 'Radament', 'radament', '10', '', '6', '0', '0', '3', '3', '1', '0', '', '30', '30', '30', 'Radament', 'Radament Desecrated A', 'Radament (N)', 'Radament (N) Desecrated A', 'Radament (H)', 'Radament (H) Desecrated A', '0'])
        self.add_row(['Bloodwitch the Wild', 'Bloodwitch the Wild', 'pantherwoman1', '11', '', '5', '7', '0', '5', '5', '1', '0', '', '29', '29', '29', 'Act 2 Super A', '', 'Act 2 (N) Super A', '', 'Act 2 (H) Super A', 'Act 2 (H) Super A Desecrated', '0'])
        self.add_row(['Fangskin', 'Fangskin', 'clawviper3', '12', '', '17', '6', '0', '4', '4', '1', '0', '', '14', '14', '14', 'Act 2 Super B', '', 'Act 2 (N) Super B', '', 'Act 2 (H) Super B', 'Act 2 (H) Super B Desecrated', '0'])
        self.add_row(['Beetleburst', 'Beetleburst', 'scarab2', '13', '', '8', '0', '0', '3', '3', '1', '0', '1', '13', '13', '13', 'Act 2 Super B', '', 'Act 2 (N) Super B', '', 'Act 2 (H) Super B', 'Act 2 (H) Super B Desecrated', '0'])
        self.add_row(['Leatherarm', 'Leatherarm', 'mummy2', '14', '', '5', '18', '0', '5', '5', '1', '0', '', '25', '25', '25', 'Act 2 Super A', '', 'Act 2 (N) Super A', '', 'Act 2 (H) Super A', 'Act 2 (H) Super A Desecrated', '0'])
        self.add_row(['Coldworm the Burrower', 'Coldworm the Burrower', 'maggotqueen1', '15', '', '18', '8', '0', '0', '0', '0', '0', '', '13', '13', '13', 'Act 2 Super B', '', 'Act 2 (N) Super B', '', 'Act 2 (H) Super B', 'Act 2 (H) Super B Desecrated', '0'])
        self.add_row(['Fire Eye', 'Fire Eye', 'sandraider3', '16', '', '9', '6', '0', '3', '3', '1', '0', '', '12', '12', '12', 'Act 2 Super B', '', 'Act 2 (N) Super B', '', 'Act 2 (H) Super B', 'Act 2 (H) Super B Desecrated', '0'])
        self.add_row(['Dark Elder', 'Dark Elder', 'darkelder', '17', '', '6', '8', '0', '4', '4', '1', '0', '1', '27', '27', '27', 'Act 2 Super B', '', 'Act 2 (N) Super B', '', 'Act 2 (H) Super B', 'Act 2 (H) Super B Desecrated', '0'])
        self.add_row(['The Summoner', 'The Summoner', 'summoner', '18', '', '5', '6', '0', '0', '0', '1', '0', '', '26', '26', '26', 'Summoner', 'Summoner Desecrated A', 'Summoner (N)', 'Summoner (N) Desecrated A', 'Summoner (H)', 'Summoner (H) Desecrated A', '0'])
        self.add_row(['Ancient Kaa the Soulless', 'Ancient Kaa the Soulless', 'unraveler3', '19', '', '25', '5', '17', '3', '3', '1', '0', '', '11', '11', '11', 'Act 2 Super C', '', 'Act 2 (N) Super C', '', 'Act 2 (H) Super C', 'Act 2 (H) Super C Desecrated', '0'])
        self.add_row(['The Smith', 'The Smith', 'smith', '20', 'smith', '5', '0', '0', '0', '0', '1', '0', '', '26', '26', '26', 'Smith', 'Smith Desecrated A', 'Smith (N)', 'Smith (N) Desecrated A', 'Smith (H)', 'Smith (H) Desecrated A', '0'])
        self.add_row(['Web Mage the Burning', 'Web Mage the Burning', 'arach4', '21', '', '5', '7', '0', '5', '5', '1', '0', '', '19', '19', '19', 'Act 3 Super A', '', 'Act 3 (N) Super A', '', 'Act 3 (H) Super A', 'Act 3 (H) Super A Desecrated', '0'])
        self.add_row(['Witch Doctor Endugu', 'Witch Doctor Endugu', 'fetishshaman4', '22', '', '8', '9', '0', '6', '6', '1', '0', '', '20', '20', '20', 'Act 3 Super B', '', 'Act 3 (N) Super B', '', 'Act 3 (H) Super B', 'Act 3 (H) Super B Desecrated', '0'])
        self.add_row(['Stormtree', 'Stormtree', 'thornhulk3', '23', '', '6', '17', '0', '4', '4', '1', '0', '1', '35', '35', '35', 'Act 3 Super B', '', 'Act 3 (N) Super B', '', 'Act 3 (H) Super B', 'Act 3 (H) Super B Desecrated', '0'])
        self.add_row(['Sarina the Battlemaid', 'Sarina the Battlemaid', 'corruptrogue5', '24', '', '6', '27', '0', '9', '9', '1', '0', '1', '36', '36', '36', 'Act 3 Super B', '', 'Act 3 (N) Super B', '', 'Act 3 (H) Super B', 'Act 3 (H) Super B Desecrated', '0'])
        self.add_row(['Icehawk Riftwing', 'Icehawk Riftwing', 'batdemon3', '25', '', '18', '26', '0', '7', '7', '1', '0', '', '21', '21', '21', 'Act 3 Super A', '', 'Act 3 (N) Super A', '', 'Act 3 (H) Super A', 'Act 3 (H) Super A Desecrated', '0'])
        self.add_row(['Ismail Vilehand', 'Ismail Vilehand', 'councilmember1', '26', '', '6', '7', '0', '2', '2', '1', '0', '', '36', '36', '36', 'Council', 'Council Desecrated A', 'Council (N)', 'Council (N) Desecrated A', 'Council (H)', 'Council (H) Desecrated A', '0'])
        self.add_row(['Geleb Flamefinger', 'Geleb Flamefinger', 'councilmember2', '27', '', '5', '9', '0', '2', '2', '1', '0', '', '37', '37', '37', 'Council', 'Council Desecrated A', 'Council (N)', 'Council (N) Desecrated A', 'Council (H)', 'Council (H) Desecrated A', '0'])
        self.add_row(['Bremm Sparkfist', 'Bremm Sparkfist', 'councilmember3', '28', '', '30', '17', '0', '2', '2', '1', '0', '', '22', '22', '22', 'Council', 'Council Desecrated A', 'Council (N)', 'Council (N) Desecrated A', 'Council (H)', 'Council (H) Desecrated A', '0'])
        self.add_row(['Toorc Icefist', 'Toorc Icefist', 'councilmember1', '29', '', '18', '28', '0', '0', '0', '1', '0', '', '23', '23', '23', 'Council', 'Council Desecrated A', 'Council (N)', 'Council (N) Desecrated A', 'Council (H)', 'Council (H) Desecrated A', '0'])
        self.add_row(['Wyand Voidfinger', 'Wyand Voidfinger', 'councilmember2', '30', '', '25', '26', '0', '0', '0', '1', '0', '', '38', '38', '38', 'Council', 'Council Desecrated A', 'Council (N)', 'Council (N) Desecrated A', 'Council (H)', 'Council (H) Desecrated A', '0'])
        self.add_row(['Maffer Dragonhand', 'Maffer Dragonhand', 'councilmember3', '31', '', '5', '6', '0', '0', '0', '1', '0', '', '23', '23', '23', 'Council', 'Council Desecrated A', 'Council (N)', 'Council (N) Desecrated A', 'Council (H)', 'Council (H) Desecrated A', '0'])
        self.add_row(['Winged Death', 'Winged Death', 'megademon3', '32', '', '5', '7', '0', '7', '7', '1', '0', '', '24', '24', '24', 'Act 4 Super A', '', 'Act 4 (N) Super A', '', 'Act 4 (H) Super A', 'Act 4 (H) Super A Desecrated', '0'])
        self.add_row(['The Tormentor', 'The Tormentor', 'willowisp3', '33', '', '8', '9', '0', '5', '5', '1', '0', '', '9', '9', '9', 'Act 4 Super A', '', 'Act 4 (N) Super A', '', 'Act 4 (H) Super A', 'Act 4 (H) Super A Desecrated', '0'])
        self.add_row(['Taintbreeder', 'Taintbreeder', 'vilemother2', '34', '', '6', '0', '0', '6', '6', '1', '0', '', '10', '10', '10', 'Act 4 Super A', '', 'Act 4 (N) Super A', '', 'Act 4 (H) Super A', 'Act 4 (H) Super A Desecrated', '0'])
        self.add_row(['Riftwraith the Cannibal', 'Riftwraith the Cannibal', 'regurgitator2', '35', '', '18', '26', '0', '8', '8', '1', '0', '', '25', '25', '25', 'Act 4 Super A', '', 'Act 4 (N) Super A', '', 'Act 4 (H) Super A', 'Act 4 (H) Super A Desecrated', '0'])
        self.add_row(['Infector of Souls', 'Infector of Souls', 'megademon3', '36', '', '6', '27', '0', '9', '9', '1', '0', '', '26', '26', '26', 'Act 4 Super B', '', 'Act 4 (N) Super B', '', 'Act 4 (H) Super B', 'Act 4 (H) Super B Desecrated', '0'])
        self.add_row(['Lord De Seis', 'Lord De Seis', 'doomknight3', '37', '', '5', '30', '24', '5', '5', '1', '0', '', '11', '11', '11', 'Act 4 Super C', '', 'Act 4 (N) Super C', '', 'Act 4 (H) Super C', 'Act 4 (H) Super C Desecrated', '0'])
        self.add_row(['Grand Vizier of Chaos', 'Grand Vizier of Chaos', 'fingermage3', '38', '', '5', '9', '0', '9', '9', '1', '0', '', '26', '26', '26', 'Act 4 Super B', '', 'Act 4 (N) Super B', '', 'Act 4 (H) Super B', 'Act 4 (H) Super B Desecrated', '0'])
        self.add_row(['The Cow King', 'The Cow King', 'cowking', '39', '', '8', '17', '0', '6', '6', '1', '0', '', '27', '27', '27', 'Cow King', 'Cow King Desecrated A', 'Cow King (N)', 'Cow King (N) Desecrated A', 'Cow King (H)', 'Cow King (H) Desecrated A', '0'])
        self.add_row(['Corpsefire', 'Corpsefire', 'zombie1', '40', '', '27', '0', '0', '5', '5', '1', '0', '', '25', '25', '25', 'Act 1 Super A', '', 'Act 1 (N) Super A', '', 'Act 1 (H) Super A', 'Act 1 (H) Super A Desecrated', '0'])
        self.add_row(['The Feature Creep', 'The Feature Creep', 'hephasto', '41', 'smithdemon', '27', '30', '0', '0', '0', '1', '0', '', '20', '20', '20', 'Haphesto', 'Haphesto Desecrated A', 'Haphesto (N)', 'Haphesto (N) Desecrated A', 'Haphesto (H)', 'Haphesto (H) Desecrated A', '0'])
        self.add_row(['Expansion', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '0'])
        self.add_row(['Siege Boss', 'Siege Boss', 'overseer1', '42', '', '5', '0', '0', '0', '0', '0', '1', '', '7', '7', '7', 'Act 5 Super A', '', 'Act 5 (N) Super A', '', 'Act 5 (H) Super A', 'Act 5 (H) Super A Desecrated', '0'])
        self.add_row(['Ancient Barbarian 1', 'Ancient Barbarian 1', 'ancientbarb1', '43', '', '0', '0', '0', '0', '0', '0', '1', '', '25', '25', '25', '', '', '', '', '', '', '0'])
        self.add_row(['Ancient Barbarian 2', 'Ancient Barbarian 2', 'ancientbarb2', '44', '', '0', '0', '0', '0', '0', '0', '1', '', '26', '26', '26', '', '', '', '', '', '', '0'])
        self.add_row(['Ancient Barbarian 3', 'Ancient Barbarian 3', 'ancientbarb3', '45', '', '0', '0', '0', '0', '0', '0', '1', '', '11', '11', '11', '', '', '', '', '', '', '0'])
        self.add_row(['Axe Dweller', 'Axe Dweller', 'bloodlord3', '46', '', '8', '9', '0', '2', '2', '0', '0', '', '20', '20', '20', 'Act 5 Super C', '', 'Act 5 (N) Super C', '', 'Act 5 (H) Super C', 'Act 5 (H) Super C Desecrated', '0'])
        self.add_row(['Bonesaw Breaker', 'Bonesaw Breaker', 'reanimatedhorde2', '47', '', '5', '8', '0', '5', '5', '0', '0', '', '35', '35', '35', 'Act 5 Super A', '', 'Act 5 (N) Super A', '', 'Act 5 (H) Super A', 'Act 5 (H) Super A Desecrated', '0'])
        self.add_row(['Dac Farren', 'Dac Farren', 'imp3', '48', '', '18', '0', '0', '4', '4', '0', '0', '1', '36', '36', '36', 'Act 5 Super B', '', 'Act 5 (N) Super B', '', 'Act 5 (H) Super B', 'Act 5 (H) Super B Desecrated', '0'])
        self.add_row(['Megaflow Rectifier', 'Megaflow Rectifier', 'minion1', '49', '', '1', '6', '0', '8', '8', '0', '0', '1', '21', '21', '21', 'Act 5 Super A', '', 'Act 5 (N) Super A', '', 'Act 5 (H) Super A', 'Act 5 (H) Super A Desecrated', '0'])
        self.add_row(['Eyeback Unleashed', 'Eyeback Unleashed', 'deathmauler1', '50', '', '5', '6', '0', '2', '2', '0', '0', '', '8', '8', '8', 'Act 5 Super A', '', 'Act 5 (N) Super A', '', 'Act 5 (H) Super A', 'Act 5 (H) Super A Desecrated', '0'])
        self.add_row(['Threash Socket', 'Threash Socket', 'siegebeast3', '51', '', '7', '0', '0', '0', '0', '0', '0', '', '37', '37', '37', 'Act 5 Super Cx', '', 'Act 5 (N) Super Cx', '', 'Act 5 (H) Super Cx', 'Act 5 (H) Super Cx Desecrated', '0'])
        self.add_row(['Pindleskin', 'Pindleskin', 'reanimatedhorde5', '52', '', '9', '0', '0', '6', '6', '0', '0', '', '22', '22', '22', 'Act 5 Super Cx', '', 'Act 5 (N) Super Cx', '', 'Act 5 (H) Super Cx', 'Act 5 (H) Super Cx Desecrated', '0'])
        self.add_row(['Snapchip Shatter', 'Snapchip Shatter', 'frozenhorror1', '53', '', '7', '18', '0', '4', '4', '0', '0', '', '23', '23', '23', 'Act 5 Super C', '', 'Act 5 (N) Super C', '', 'Act 5 (H) Super C', 'Act 5 (H) Super C Desecrated', '0'])
        self.add_row(['Anodized Elite', 'Anodized Elite', 'succubus4', '54', '', '9', '7', '0', '6', '6', '0', '0', '', '38', '38', '38', 'Act 5 Super C', '', 'Act 5 (N) Super C', '', 'Act 5 (H) Super C', 'Act 5 (H) Super C Desecrated', '0'])
        self.add_row(['Vinvear Molech', 'Vinvear Molech', 'succubuswitch2', '55', '', '8', '5', '18', '0', '0', '0', '0', '', '23', '23', '23', 'Act 5 Super A', '', 'Act 5 (N) Super A', '', 'Act 5 (H) Super A', 'Act 5 (H) Super A Desecrated', '0'])
        self.add_row(['Sharp Tooth Sayer', 'Sharp Tooth Sayer', 'overseer3', '56', '', '6', '0', '0', '3', '3', '0', '0', '1', '24', '24', '24', 'Act 5 Super B', '', 'Act 5 (N) Super B', '', 'Act 5 (H) Super B', 'Act 5 (H) Super B Desecrated', '0'])
        self.add_row(['Magma Torquer', 'Magma Torquer', 'imp5', '57', '', '5', '7', '0', '5', '5', '0', '0', '', '9', '9', '9', 'Act 5 Super C', '', 'Act 5 (N) Super C', '', 'Act 5 (H) Super C', 'Act 5 (H) Super C Desecrated', '0'])
        self.add_row(['Blaze Ripper', 'Blaze Ripper', 'deathmauler5', '58', '', '17', '6', '0', '4', '4', '0', '0', '', '10', '10', '10', 'Act 5 Super C', '', 'Act 5 (N) Super C', '', 'Act 5 (H) Super C', 'Act 5 (H) Super C Desecrated', '0'])
        self.add_row(['Frozenstein', 'Frozenstein', 'snowyeti4', '59', '', '18', '25', '0', '5', '6', '0', '0', '', '19', '19', '19', 'Act 5 Super C', '', 'Act 5 (N) Super C', '', 'Act 5 (H) Super C', 'Act 5 (H) Super C Desecrated', '0'])
        self.add_row(['Nihlathak Boss', 'Nihlathak', 'nihlathakboss', '60', '', '0', '0', '0', '0', '0', '0', '1', '', '28', '28', '28', 'Nihlathak', 'Nihlathak Desecrated', 'Nihlathak (N)', 'Nihlathak (N) Desecrated', 'Nihlathak (H)', 'Nihlathak (H) Desecrated', '0'])
        self.add_row(['Baal Subject 1', 'Baal Subject 1', 'fallenshaman5', '61', '', '9', '0', '0', '5', '5', '0', '1', '', '29', '29', '29', 'Act 5 Champ C', '', 'Act 5 (N) Champ C', '', 'Act 5 (H) Champ C', 'Act 5 (H) Champ C Desecrated', '0'])
        self.add_row(['Baal Subject 2', 'Baal Subject 2', 'unraveler5', '62', '', '23', '0', '0', '3', '3', '0', '1', '', '21', '21', '21', 'Act 5 Champ C', '', 'Act 5 (N) Champ C', '', 'Act 5 (H) Champ C', 'Act 5 (H) Champ C Desecrated', '0'])
        self.add_row(['Baal Subject 3', 'Baal Subject 3', 'baalhighpriest', '63', '', '17', '0', '0', '5', '5', '0', '1', '', '36', '36', '36', 'Act 5 Champ C', '', 'Act 5 (N) Champ C', '', 'Act 5 (H) Champ C', 'Act 5 (H) Champ C Desecrated', '0'])
        self.add_row(['Baal Subject 4', 'Baal Subject 4', 'venomlord', '64', '', '6', '0', '0', '8', '8', '0', '1', '', '20', '20', '20', 'Act 5 Champ C', '', 'Act 5 (N) Champ C', '', 'Act 5 (H) Champ C', 'Act 5 (H) Champ C Desecrated', '0'])
        self.add_row(['Baal Subject 5', 'Baal Subject 5', 'baalminion1', '65', '', '27', '0', '0', '5', '5', '0', '1', '', '20', '20', '20', 'Act 5 Champ C', '', 'Act 5 (N) Champ C', '', 'Act 5 (H) Champ C', 'Act 5 (H) Champ C Desecrated', '0'])
