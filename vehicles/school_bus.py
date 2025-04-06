from .vehicle import Vehicle

class SchoolBus(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self._capacity = capacity

    def drive(self):
        print(f"School Bus {self._make} {self._model} (Capacity: {self._capacity}) is picking up students.")

    def get_capacity(self):
        return self._capacity