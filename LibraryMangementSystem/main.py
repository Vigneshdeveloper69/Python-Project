import json
import os

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued_to = None

    def issue_book(self, user_id):
        if self.issued_to is None:
            self.issued_to = user_id
            return f"Book '{self.title}' issued to User ID: {user_id}"
        return "Book is already issued!"

    def return_book(self):
        if self.issued_to is not None:
            self.issued_to = None
            return "Book returned successfully!"
        return "Book was not issued."

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self, db_file="library.json"):
        self.db_file = db_file
        self.books, self.users = self.load_data()

    def load_data(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as file:
                data = json.load(file)
                return data.get("books", {}), data.get("users", {})
        return {}, {}

    def save_data(self):
        with open(self.db_file, "w") as file:
            json.dump({"books": self.books, "users": self.users}, file, indent=4)

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            return "Book already exists!"
        self.books[book_id] = {"title": title, "author": author, "issued_to": None}
        self.save_data()
        return f"Book '{title}' added successfully!"

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            self.save_data()
            return "Book removed successfully!"
        return "Book not found!"

    def register_user(self, user_id, name):
        if user_id in self.users:
            return "User already exists!"
        self.users[user_id] = {"name": name, "borrowed_books": []}
        self.save_data()
        return f"User '{name}' registered successfully!"

    def issue_book(self, book_id, user_id):
        if book_id in self.books and user_id in self.users:
            if self.books[book_id]["issued_to"] is None:
                self.books[book_id]["issued_to"] = user_id
                self.users[user_id]["borrowed_books"].append(book_id)
                self.save_data()
                return f"Book '{self.books[book_id]['title']}' issued to User '{self.users[user_id]['name']}'"
            return "Book is already issued!"
        return "Invalid Book ID or User ID!"

    def return_book(self, book_id, user_id):
        if book_id in self.books and user_id in self.users:
            if self.books[book_id]["issued_to"] == user_id:
                self.books[book_id]["issued_to"] = None
                self.users[user_id]["borrowed_books"].remove(book_id)
                self.save_data()
                return "Book returned successfully!"
            return "This book was not issued to this user!"
        return "Invalid Book ID or User ID!"

    def view_books(self):
        if not self.books:
            return "No books available!"
        return "\n".join([f"ID: {b} | Title: {self.books[b]['title']} | Author: {self.books[b]['author']} | Issued To: {self.books[b]['issued_to']}" for b in self.books])

    def view_users(self):
        if not self.users:
            return "No users registered!"
        return "\n".join([f"ID: {u} | Name: {self.users[u]['name']} | Borrowed Books: {self.users[u]['borrowed_books']}" for u in self.users])

def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Register User")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. View Books")
        print("7. View Users")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")
            print(library.add_book(book_id, title, author))

        elif choice == "2":
            book_id = input("Enter Book ID to remove: ")
            print(library.remove_book(book_id))

        elif choice == "3":
            user_id = input("Enter User ID: ")
            name = input("Enter User Name: ")
            print(library.register_user(user_id, name))

        elif choice == "4":
            book_id = input("Enter Book ID: ")
            user_id = input("Enter User ID: ")
            print(library.issue_book(book_id, user_id))

        elif choice == "5":
            book_id = input("Enter Book ID: ")
            user_id = input("Enter User ID: ")
            print(library.return_book(book_id, user_id))

        elif choice == "6":
            print("\n--- Available Books ---")
            print(library.view_books())

        elif choice == "7":
            print("\n--- Registered Users ---")
            print(library.view_users())

        elif choice == "8":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()