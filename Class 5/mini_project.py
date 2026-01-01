
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print("Book:", self.title, "by", self.author)


class EBook(Book):
    def show_info(self):
        print("EBook:", self.title, "by", self.author)

    def download(self):
        print(self.title, "is downloading...")


class AudioBook(Book):
    def show_info(self):
        print("AudioBook:", self.title, "by", self.author)

    def play_sample(self):
        print("Playing sample of", self.title)


class Library:
    def __init__(self):
        self.catalog = []

    def add_book(self, book):
        self.catalog.append(book)
        print("Book added:", book.title)

    def remove_book(self, title):
        for book in self.catalog:
            if book.title == title:
                self.catalog.remove(book)
                print("Book removed:", title)
                return
        print("Book not found:", title)

    def show_all_books(self):
        print("--- Library Catalog ---")
        for book in self.catalog:
            book.show_info()


library = Library()

b1 = Book("Harry Potter", "J.K. Rowling")
b2 = EBook("Python 101", "John Doe")
b3 = AudioBook("Lord of the Rings", "J.R.R. Tolkien")

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.show_all_books()

library.remove_book("Harry Potter")

library.show_all_books()