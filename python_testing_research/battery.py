class Battery:
    def __init__(
        self,
        capacity_kwh: float,
        initial_state_of_charge_kwh: float = 0,
    ) -> None:
        if capacity_kwh <= 0:
            raise ValueError("Battery capacity must be greater than zero.")

        self.capacity_kwh = capacity_kwh
        self.state_of_charge_kwh = initial_state_of_charge_kwh

    def control(self, amount_kwh: float) -> float:
        """
        Charge or discharge the battery by the specified amount in kWh.
        Negative values indicate charging, while positive values indicate discharging.
        """
        previous_state_of_charge_kwh = self.state_of_charge_kwh
        self.state_of_charge_kwh = min(
            max(self.state_of_charge_kwh - amount_kwh, 0),
            self.capacity_kwh,
        )
        return previous_state_of_charge_kwh - self.state_of_charge_kwh
