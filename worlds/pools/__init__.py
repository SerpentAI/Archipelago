import worlds.LauncherComponents as LauncherComponents

from .world import PoolsWorld


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="PoolsClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "POOLS Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="pools",
    )
)

LauncherComponents.icon_paths["pools"] = f"ap:{__name__}/icon.png"
