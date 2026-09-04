def test_soc_calculation():
    soc = _calculate_state_of_charge(
        previous_state_of_charge_kwh=5,
        amount_kwh=-3,
        capacity_kwh=10)
    assert soc == 8

def test_charge():
    battery = Battery(...)
    energy_used = battery.control(-3)
    assert energy_used == -3
    assert battery.state_of_charge_kwh == 8