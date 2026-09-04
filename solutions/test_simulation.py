import time

import pytest

from python_testing_research import Battery, SelfConsumptionController
from python_testing_research.simulation import generate_data_profile, run_simulation

def test_one_day_is_self_sufficient_with_a_large_battery():
    # Arrange
    data = generate_data_profile(hours=24, peak_pv_kwh=3, constant_load_kwh=1)
    battery = Battery(capacity_kwh=20, initial_state_of_charge_kwh=10)
    controller = SelfConsumptionController()

    # Act
    result = run_simulation(data, battery, controller)
    
    assert result["grid_import_kwh"].tolist() == pytest.approx([0] * 24, abs=1e-6)


def test_results_did_not_change():
    data = generate_data_profile(hours=24 * 7 * 4, peak_pv_kwh=3, constant_load_kwh=1)
    battery = Battery(capacity_kwh=5, initial_state_of_charge_kwh=5)
    controller = SelfConsumptionController()

    start = time.perf_counter()

    results = run_simulation(data, battery, controller)
    elapsed = time.perf_counter() - start

    assert elapsed < 0.1
    assert results["grid_import_kwh"].sum() == pytest.approx(28.96, abs=0.1)
    assert results["battery_state_of_charge_kwh"].iloc[-1] == pytest.approx(0, abs=0.1)