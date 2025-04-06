from .author import Author

class Book:
    def __init__(self, title, genre, author: Author):
        self._title = title
        self._genre = genre
        self._author = author

    def get_info(self):
        return f"'{self._title}' [{self._genre}] by {self._author.get_info()}"