class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print("Book:", self.title, "by", self.author)



class EBook(Book):
    def __init__(self, title, author, downloadable):
        super().__init__(title, author)
        self.downloadable = downloadable

    def show_info(self):
        print(f"EBook: {self.title} by {self.author} | Downloadable: {self.downloadable}")

    def download(self):
        if self.downloadable.lower() == "yes":
            print(self.title, "is downloading...")
        else:
            print(self.title, "is NOT downloadable.")



class AudioBook(Book):
    def __init__(self, title, author, has_sample):
        super().__init__(title, author)
        self.has_sample = has_sample

    def show_info(self):
        print(f"AudioBook: {self.title} by {self.author} | Sample Available: {self.has_sample}")

    def play_sample(self):
        if self.has_sample.lower() == "yes":
            print("Playing sample of", self.title)
        else:
            print("No sample available for", self.title)



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
b2 = EBook("Python 101", "John Doe", "yes")
b3 = AudioBook("Lord of the Rings", "J.R.R. Tolkien", "no")

library.add_book(b1)
library.add_book(b2)
library.add_book(b3)

library.show_all_books()

library.remove_book("Harry Potter")

library.show_all_books()