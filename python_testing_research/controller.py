class SelfConsumptionController:
    def get_battery_control(self, load_kwh: float, pv_generation_kwh: float) -> float:
        return load_kwh - pv_generation_kwh
