class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_books(self, search_string):
        books_result = []
        for i_book in self.books:
            if search_string in i_book.title or search_string in i_book.author:
                books_result.append(i_book)
        return books_result