class SelfConsumptionController:
    def get_battery_control(self, 
                            load_kwh: float, 
                            pv_generation_kwh: float) -> float:
        """
        Controler for balancing load and PV generation with battery storage. 
        If there is excess PV generation, storage is charged. If load is higher then PV, storage is discharged.
        """
        return load_kwh - pv_generation_kwh
