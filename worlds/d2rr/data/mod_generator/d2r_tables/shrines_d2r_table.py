from ..d2r_table import D2RTable


class ShrinesD2RTable(D2RTable):
    file_name = "shrines.txt"

    column_names = (
        "Name",
        "*Shrine Type",
        "*Effect",
        "Code",
        "Arg0",
        "Arg1",
        "Duration in frames",
        "reset time in minutes",
        "rarity",
        "StringName",
        "StringPhrase",
        "effectclass",
        "LevelMin",
    )

    def __init__(self):
        super().__init__(index_column="Name")
        
    def _bootstrap(self):
        self.add_row(['None', 'None', 'None', '0', '', '', '', '2', '1', 'ShrId0', 'ShrMsg0', '0', '0'])
        self.add_row(['Refilling Shrine', 'Recharge', 'Gain full Life and Mana', '1', '', '', '', '2', '1', 'ShrId1', 'ShrMsg1', '4', '1'])
        self.add_row(['Health Shrine', 'Recharge', 'Gain full Life', '2', '', '', '', '5', '2', 'ShrId2', 'ShrMsg2', '2', '1'])
        self.add_row(['Mana Shrine', 'Recharge', 'Gain full Mana', '3', '', '', '', '5', '2', 'ShrId3', 'ShrMsg3', '3', '1'])
        self.add_row(['Health Exchange Shrine', 'Recharge', 'Exchange your current Life to restore Mana (Not Used)', '4', '50', '500', '', '', '3', 'ShrId4', 'ShrMsg4', '2', '2'])
        self.add_row(['Mana Exchange Shrine', 'Recharge', 'Exchange your current Mana to restore Life (Not Used)', '5', '50', '500', '', '', '3', 'ShrId5', 'ShrMsg5', '3', '2'])
        self.add_row(['Armor Shrine', 'Booster', 'Increases Defense', '6', '100', '', '2400', '5', '2', 'ShrId6', 'ShrMsg6', '4', '5'])
        self.add_row(['Combat Shrine', 'Booster', 'Increases Physical Damage and Attack Rating', '7', '200', '200', '2400', '5', '2', 'ShrId7', 'ShrMsg7', '4', '8'])
        self.add_row(['Resist Fire Shrine', 'Booster', 'Increases Fire Resistance', '8', '75', '', '3600', '5', '2', 'ShrId8', 'ShrMsg8', '4', '5'])
        self.add_row(['Resist Cold Shrine', 'Booster', 'Increases Cold Resistance', '9', '75', '', '3600', '5', '2', 'ShrId9', 'ShrMsg9', '4', '26'])
        self.add_row(['Resist Lightning Shrine', 'Booster', 'Increases Lightning Resistance', '10', '75', '', '3600', '5', '2', 'ShrId10', 'ShrMsg10', '4', '32'])
        self.add_row(['Resist Poison Shrine', 'Booster', 'Increases Poison Resistance', '11', '75', '', '3600', '5', '2', 'ShrId11', 'ShrMsg11', '4', '21'])
        self.add_row(['Skill Shrine', 'Booster', 'Increases all Skill levels', '12', '2', '', '2400', '5', '2', 'ShrId12', 'ShrMsg12', '4', '1'])
        self.add_row(['Mana Recharge Shrine', 'Booster', 'Increases Mana Recharge Rate', '13', '400', '', '2400', '5', '2', 'ShrId13', 'ShrMsg13', '4', '1'])
        self.add_row(['Stamina Shrine', 'Booster', 'Gain infinite Stamina', '14', '200', '', '4800', '5', '3', 'ShrId14', 'ShrMsg14', '4', '1'])
        self.add_row(['Experience Shrine', 'Booster', 'Temporarily gain bonus Experience from kills', '15', '50', '', '3600', '', '3', 'ShrId15', 'ShrMsg15', '4', '1'])
        self.add_row(['Enirhs Shrine', 'Magic', "Temporarily reverse your character's Name (Not Used)", '16', '', '', '', '', '3', 'ShrId16', 'ShrMsg16', '1', '1'])
        self.add_row(['Portal Shrine', 'Magic', 'Create a neutral Town Portal back to the current Act Town', '17', '', '', '', '', '2', 'ShrId17', 'ShrMsg17', '1', '3'])
        self.add_row(['Gem Shrine', 'Magic', '"Randomly select a gem in your inventory and upgrade its level (Otherwise, create a random chipped gem)"', '18', '', '', '', '', '3', 'ShrId18', 'ShrMsg18', '1', '4'])
        self.add_row(['Fire Shrine', 'Magic', 'Release a nova of fireballs that cause any player or monster to lose a percentage of Life', '19', '50', '2000', '', '', '2', 'ShrId19', 'ShrMsg19', '1', '1'])
        self.add_row(['Monster Shrine', 'Magic', 'Causes the nearest monster to upgrade a Unique or Champion type', '20', '', '', '', '', '3', 'ShrId20', 'ShrMsg20', '1', '3'])
        self.add_row(['Exploding Shrine', 'Magic', 'Deal Fire damage to nearby monsters and create a random number of Exploding Potions', '21', '5', '10', '', '', '3', 'ShrId21', 'ShrMsg21', '1', '1'])
        self.add_row(['Poison Shrine', 'Magic', 'Create Poison Gas that damages nearby monsters and create a random number of Choking Gas Potions', '22', '5', '10', '', '', '3', 'ShrId22', 'ShrMsg22', '1', '1'])
