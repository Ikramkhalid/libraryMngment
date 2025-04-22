class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"'{self.title}' by {self.author} - Copies: {self.copies}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, copies):
        self.books.append(Book(title, author, copies))
        print(f"Book '{title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and book.copies > 0:
                book.copies -= 1
                print(f"You have borrowed '{title}'.")
                return
        print(f"'{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.copies += 1
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' does not belong to this library.")


# Example usage
if __name__ == "__main__":
    library = Library()
    library.add_book("1984", "George Orwell", 3)
    library.add_book("To Kill a Mockingbird", "Harper Lee", 2)

    library.display_books()
    library.borrow_book("1984")
    library.display_books()
    library.return_book("1984")
    library.display_books()