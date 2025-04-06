class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)
    
    def __str__(self):
        return f"Vector({self._x}, {self._y})"