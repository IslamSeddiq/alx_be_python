# Base class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class - EBook
class EBook(Book):
    def __init__(self, title, author, file_size_kb):
        super().__init__(title, author)
        self.file_size_kb = file_size_kb  # store in KB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size_kb}KB"


# Derived class - PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Composition - Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Only Book instances can be added.")

    def list_books(self):
        for book in self.books:
            print(book)


# Example usage
if __name__ == "__main__":
    library = Library()

    library.add_book(Book("Pride and Prejudice", "Jane Austen"))
    library.add_book(EBook("Snow Crash", "Neal Stephenson", 500))
    library.add_book(PrintBook("The Catcher in the Rye", "J.D. Salinger", 234))

    library.list_books()
