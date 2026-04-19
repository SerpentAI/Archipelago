import worlds.LauncherComponents as LauncherComponents

from .world import MirrorsEdgeWorld


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="MirrorsEdgeClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Mirror's Edge Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="mirrors_edge",
    )
)

LauncherComponents.icon_paths["mirrors_edge"] = f"ap:{__name__}/icon.jpg"
