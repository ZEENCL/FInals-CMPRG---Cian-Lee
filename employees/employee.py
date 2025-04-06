class Employee:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split('-')
        return cls(name, int(age))
    
    def __str__(self):
        return f"Employee: {self._name}, Age {self._age}"