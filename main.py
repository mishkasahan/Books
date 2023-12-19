class Book:
    def __init__(self,name: str, author: str, jear: int):
        self.name = name
        self.author = author
        self.jear = jear

    def __str__(self):
        return f"Книга {self.name} від автора {self.author}, видана в {self.jear} року"


class Library:
    def __init__(self,name: str):
        self.name = name
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def __str__(self):
        return f"В {self.name} є такі книги: {[book.__str__() for book in self.books]}"



book1 = Book("Мами", "Марія Матіос", 2023)
book2 = Book("Інтернат", "Сергій Жадан", 2022)
biblioteka1 = Library("Biblioteka1")
biblioteka1.add_book(book1)
biblioteka1.add_book(book2)
print(biblioteka1)

