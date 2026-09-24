import worlds.LauncherComponents as LauncherComponents

from .world import DayOfTheTentacleWorld


def launch_client(*args) -> None:
    from .client import main
    LauncherComponents.launch(main, name="DayOfTheTentacleClient", args=args)


LauncherComponents.components.append(
    LauncherComponents.Component(
        "Day of the Tentacle Client",
        func=launch_client,
        component_type=LauncherComponents.Type.CLIENT,
        icon="day_of_the_tentacle",
    )
)

LauncherComponents.icon_paths["day_of_the_tentacle"] = f"ap:{__name__}/icon.png"
