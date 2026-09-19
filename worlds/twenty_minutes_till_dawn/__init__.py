import worlds.LauncherComponents as LauncherComponents

from .world import TwentyMinutesWorld


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="TwentyMinutesClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "20 Minutes Till Dawn Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="twenty_minutes_till_dawn",
    )
)

LauncherComponents.icon_paths["twenty_minutes_till_dawn"] = f"ap:{__name__}/icon.jpg"
