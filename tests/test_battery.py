from python_testing_research.battery import Battery


def test_charge():
    battery = Battery(capacity_kwh=10, initial_state_of_charge_kwh=5)
    energy_used = battery.control(-3)
    assert energy_used == -3
    assert battery.state_of_charge_kwh == 8