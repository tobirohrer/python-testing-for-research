@pytest.mark.parametrize("capa, exp_energy, exp_soc", 
                         [
                            (10, -3, 8), 
                            (-3, 0, 0) 
                         ])
def test_charge(capa, exp_energy, exp_soc):
    if capa <= 0:
        with pytest.raises(ValueError):
            battery = Battery(capacity_kwh=capa, ...)
            return
    battery = Battery(capacity_kwh=capa, ...)
    energy_used = battery.control(-3)
    assert energy_used == exp_energy
    assert battery.state_of_charge_kwh == exp_soc


def test_charge():
    ...

def test_battery_throws_if_parameters_invalid():
    ...