from worlds.keymasters_keep.test import KeymastersKeepTestBase


class TestEmptyBacklog(KeymastersKeepTestBase):
    options = {
        "game_selection": ['Custom (META)', 'Game Backlog (META)'],
        "game_backlog_game_selection": [],
    }


class TestEmptyCustom(KeymastersKeepTestBase):
    options = {
        "game_selection": ['Custom (META)', 'Game Backlog (META)'],
        "custom_game_objectives": [],
    }
