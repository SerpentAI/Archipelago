import worlds.LauncherComponents as LauncherComponents

from .world import RivenWorld


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="RivenClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Riven Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="riven",
    )
)

LauncherComponents.icon_paths["riven"] = f"ap:{__name__}/icon.png"
