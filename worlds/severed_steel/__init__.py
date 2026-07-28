import worlds.LauncherComponents as LauncherComponents

from .world import SeveredSteelWorld


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="SeveredSteelClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Severed Steel Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="severed_steel",
    )
)

LauncherComponents.icon_paths["severed_steel"] = f"ap:{__name__}/icon.png"
