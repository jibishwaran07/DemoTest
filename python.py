# ----------------------------------------
# LIBRARY MANAGEMENT SYSTEM (No user input)
# ----------------------------------------

# Book class to store book info
class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        return False

    def return_book(self):
        self.copies += 1

    def details(self):
        return f"{self.book_id}: {self.title} by {self.author} (Available: {self.copies})"


# Library class to manage all books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, book_id):
        for b in self.books:
            if b.book_id == book_id:
                return b
        return None

    def show_all_books(self):
        print("\n--- Library Books ---")
        for b in self.books:
            print(b.details())
        print("----------------------\n")


# Student class
class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def borrow_book(self, library, book_id):
        book = library.find_book(book_id)
        if book and book.borrow():
            self.borrowed.append(book)
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Book {book_id} is not available.")

    def return_book(self, library, book_id):
        for b in self.borrowed:
            if b.book_id == book_id:
                b.return_book()
                self.borrowed.remove(b)
                print(f"{self.name} returned '{b.title}'.")
                return
        print(f"{self.name} does not have that book.")

    def show_borrowed(self):
        print(f"\nBooks borrowed by {self.name}:")
        for b in self.borrowed:
            print(f"- {b.title}")
        print("----------------------")


# --------------------------
# Program Execution
# --------------------------

library = Library()

# Add books to library
library.add_book(Book(101, "Python Basics", "John Doe", 3))
library.add_book(Book(102, "AI Revolution", "Elon Keys", 2))
library.add_book(Book(103, "Data Science 101", "Sarah Lee", 1))

# Show library initially
library.show_all_books()

# Create students
s1 = Student("Aarav")
s2 = Student("Meera")

# Borrowing books
s1.borrow_book(library, 101)
s2.borrow_book(library, 101)
s2.borrow_book(library, 103)

# Show updates
library.show_all_books()
s1.show_borrowed()
s2.show_borrowed()

# Returning books
s2.return_book(library, 103)
library.show_all_books()
