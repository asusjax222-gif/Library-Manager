import json
import os

# -------------------------------
# Made By Jayesh Shrivastava
# Submitted to :- Jyoti Maam
# Date :- 22 June 2024
# -------------------------------
class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }


# -------------------------------
# Inventory Class
# -------------------------------
class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_data()

    def add_book(self, title, author, isbn):
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print("Book added successfully!")

    def display_all(self):
        if not self.books:
            print("No books found.")
            return

        for b in self.books:
            print(f"{b.title} | {b.author} | {b.isbn} | {b.status}")

    def search_by_title(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                return b
        return None

    def save_data(self):
        data = [b.to_dict() for b in self.books]
        with open("catalog.json", "w") as f:
            json.dump(data, f)

    def load_data(self):
        if not os.path.exists("catalog.json"):
            return
        try:
            with open("catalog.json", "r") as f:
                data = json.load(f)
                for item in data:
                    self.books.append(
                        Book(item["title"], item["author"], item["isbn"], item["status"])
                    )
        except:
            print("Error loading file. Starting fresh.")


# -------------------------------
# Menu
# -------------------------------
def menu():
    lib = LibraryInventory()

    while True:
        print("\n=== Library Menu ===")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search by Title")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            lib.add_book(title, author, isbn)

        elif choice == "2":
            title = input("Enter title to issue: ")
            b = lib.search_by_title(title)
            if b and b.issue():
                print("Book issued!")
            else:
                print("Cannot issue book.")

        elif choice == "3":
            title = input("Enter title to return: ")
            b = lib.search_by_title(title)
            if b and b.return_book():
                print("Book returned!")
            else:
                print("Cannot return book.")

        elif choice == "4":
            lib.display_all()

        elif choice == "5":
            title = input("Enter title to search: ")
            b = lib.search_by_title(title)
            if b:
                print(f"{b.title} | {b.author} | {b.isbn} | {b.status}")
            else:
                print("Book not found.")

        elif choice == "6":
            lib.save_data()
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice!")

menu()


