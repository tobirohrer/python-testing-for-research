from math import pi, sin

import pandas as pd

from python_testing_research.battery import Battery
from python_testing_research.controller import SelfConsumptionController


def _generate_data_profile(
    start: str = "2026-06-01",
    hours: int = 24,
    constant_load_kwh: float = 1,
    peak_pv_kwh: float = 3,
    sunrise_hour: int = 6,
    sunset_hour: int = 18,
) -> pd.DataFrame:
    """
    Used to generate sample data for the simulation. Load is constant, 
    while PV generation follows a sine wave pattern between sunrise and sunset
    """
    index = pd.date_range(start=start, periods=hours, freq="h")
    pv_generation = []

    for timestamp in index:
        hour = timestamp.hour
        if sunrise_hour < hour < sunset_hour:
            daylight_progress = (hour - sunrise_hour) / (sunset_hour - sunrise_hour)
            pv_generation.append(peak_pv_kwh * sin(pi * daylight_progress))
        else:
            pv_generation.append(0)

    return pd.DataFrame(
        {
            "load_kwh": constant_load_kwh,
            "pv_generation_kwh": pv_generation,
        },
        index=index,
    )


def run_simulation(
    profile: pd.DataFrame,
    battery: Battery,
    controller: SelfConsumptionController,
) -> pd.DataFrame:
    result = profile.copy()
    battery_controls = []
    battery_state_of_charge_kwh = []
    grid_imports = []

    for _, row in profile.iterrows():
        requested_battery_control_kwh = controller.get_battery_control(
            load_kwh=row["load_kwh"],
            pv_generation_kwh=row["pv_generation_kwh"],
        )
        battery_contribution_kwh = battery.control(requested_battery_control_kwh)
        grid_import_kwh = (
            row["load_kwh"]
            - row["pv_generation_kwh"]
            - battery_contribution_kwh
        )

        battery_state_of_charge_kwh.append(battery.state_of_charge_kwh)
        battery_controls.append(battery_contribution_kwh)
        grid_imports.append(grid_import_kwh)

    result["battery_state_of_charge_kwh"] = battery_state_of_charge_kwh
    result["battery_contribution_kwh"] = battery_controls
    result["grid_import_kwh"] = grid_imports
    return result


if __name__ == "__main__":
    data = _generate_data_profile()
    battery = Battery(capacity_kwh=20, initial_state_of_charge_kwh=10)
    controller = SelfConsumptionController()
    result = run_simulation(
        data,
        battery,
        controller,
    )

    print(result.round(2).to_string())
