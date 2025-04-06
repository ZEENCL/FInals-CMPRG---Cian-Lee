class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def drive(self):
        print(f"{self._make} {self._model} is now driving.")

    def stop(self):
        print(f"{self._make} {self._model} has stopped.")

    def get_info(self):
        return f"Vehicle: {self._make} {self._model}"