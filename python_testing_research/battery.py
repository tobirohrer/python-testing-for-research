class Battery:
    def __init__(
        self,
        capacity_kwh: float,
        initial_state_of_charge_kwh: float = 0,
    ) -> None:
        if capacity_kwh <= 0:
            raise ValueError("Battery capacity must be greater than zero.")
        if initial_state_of_charge_kwh < 0:
            raise ValueError("Initial SOC cannot be negative.")

        self.capacity_kwh = capacity_kwh
        self.state_of_charge_kwh = initial_state_of_charge_kwh

    def control(self, amount_kwh: float) -> float:
        """
        Charge or discharge the battery by the specified amount in kWh.
        Negative values indicate charging, while positive values indicate discharging.

        Returns: 
            The actual amount of energy used or taken from the battery. Negative if used for charging, 
            positive for discharging. Note, that the returned energy does not need to match `amount_kwh` 
            if the operation is not fully possible due to current state of.
        """
        previous_state_of_charge_kwh = self.state_of_charge_kwh
        self.state_of_charge_kwh = _calculate_state_of_charge(self.state_of_charge_kwh, amount_kwh, self.capacity_kwh)
        return previous_state_of_charge_kwh - self.state_of_charge_kwh

def _calculate_state_of_charge(
    previous_state_of_charge_kwh: float,
    amount_kwh: float,
    capacity_kwh: float,
) -> float:
    return min(max(previous_state_of_charge_kwh - amount_kwh, 0), capacity_kwh)
