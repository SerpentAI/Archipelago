import worlds.LauncherComponents as LauncherComponents

from .world import TonyHawksProSkater12World


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="TonyHawksProSkater12Client", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Tony Hawk's Pro Skater 1 + 2 Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="thps12",
    )
)

LauncherComponents.icon_paths["thps12"] = f"ap:{__name__}/icon.jpg"
