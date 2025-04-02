import worlds.LauncherComponents as LauncherComponents


from worlds.AutoWorld import World


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="DiscordRichPresenceClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Discord Rich Presence Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT
    )
)


class DiscordRichPresenceWorld(World):
    game = "Discord Rich Presence"
    hidden = True
    item_name_to_id = dict()
    location_name_to_id = dict()
