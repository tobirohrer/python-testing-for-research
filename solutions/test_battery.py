import pytest

from python_testing_research.battery import Battery, _calculate_state_of_charge

def test_charge():
    battery = Battery(capacity_kwh=10, 
                      initial_state_of_charge_kwh=5)
    energy_used = battery.control(-3)
    assert energy_used == -3
    assert battery.state_of_charge_kwh == 8


@pytest.mark.parametrize("control, expected_energy, expected_soc", 
                         [
                            (-3, -3, 8),
                            (-10, -5, 10),
                            (10, 5, 0)
                         ])
def test_charge_with_edge_cases(control, expected_energy, expected_soc):
    battery = Battery(capacity_kwh=10, 
                      initial_state_of_charge_kwh=5)
    energy_used = battery.control(control)
    assert energy_used == expected_energy
    assert battery.state_of_charge_kwh == expected_soc