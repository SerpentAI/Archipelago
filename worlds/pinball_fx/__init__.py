import worlds.LauncherComponents as LauncherComponents

from .world import PinballFXWorld


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="PinballFXClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Pinball FX Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="pinball_fx",
    )
)

LauncherComponents.icon_paths["pinball_fx"] = f"ap:{__name__}/icon.png"
