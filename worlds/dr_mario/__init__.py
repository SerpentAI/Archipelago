import worlds.LauncherComponents as LauncherComponents

from .world import DrMarioWorld


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="DrMarioClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Dr. Mario Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="dr_mario",
    )
)

LauncherComponents.icon_paths["dr_mario"] = f"ap:{__name__}/icon.png"
