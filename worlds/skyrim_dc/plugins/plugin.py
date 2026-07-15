from typing import Any

from .plugin_parser import PluginParser


class Plugin:
    def __init__(self):
        pass

    @classmethod
    def initialize_base_alchemy_ingredients(cls) -> "Plugin":
        return cls.initialize_from_plugin_name("Skyrim Dungeon Crawl - Alchemy Ingredients")

    @classmethod
    def initialize_from_plugin_name(cls, plugin_name: str) -> "Plugin":
        plugin_parser = PluginParser()

        plugin_data: Any = plugin_parser.parse_plugin(plugin_name)

        return plugin_data  # For now...
