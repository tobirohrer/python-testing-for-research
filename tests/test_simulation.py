import time
import pytest

from python_testing_research import Battery, SelfConsumptionController
from python_testing_research.simulation import generate_data_profile, run_simulation


def test_one_day_is_self_sufficient_with_a_large_battery():
    # Try Out Session 1
    # Arrange
    data = generate_data_profile(hours=24, peak_pv_kwh=3, constant_load_kwh=1)
    battery = Battery(capacity_kwh=20, initial_state_of_charge_kwh=10)
    controller = SelfConsumptionController()

    # Act
    # ToDo: Implement simulation run (check simulation.py)

    # Assert
    pass


def test_results_did_not_change():
    # Try Out Session 3
    # ToDo
    pass

