from .vehicle import Vehicle

class SchoolBus(Vehicle):
    def __init__(self, vehicleType, make, model, capacity):
        super().__init__(vehicleType, make, model)
        self._capacity = capacity

    def drive(self):
        print(f"{self._make} {self._model} (Capacity: {self._capacity}) is picking up students.")

    def stop(self):
        print(f"{self._make} {self._model} (Capacity: {self._capacity - self._capacity}) is dropping off students.")

    def get_info(self):
        return f"Vehicle: {self._make} {self._model}, Type: {self._vehicleType}"

    def get_capacity(self):
        return self._capacity