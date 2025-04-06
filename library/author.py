class Author:
    def __init__(self, name, nationality, bio):
        self._name = name
        self._nationality = nationality
        self._bio = bio

    def get_info(self):
        return f"{self._name} ({self._nationality}) - {self._bio}"