class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_issued = False

    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}")


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}")
        print("Borrowed Books:", self.borrowed_books)


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        book_id = input("Enter Book ID: ")
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        if book_id in self.books:
            print("Book already exists!")
        else:
            self.books[book_id] = Book(book_id, title, author)
            print("Book added successfully!")

    def add_member(self):
        member_id = input("Enter Member ID: ")
        name = input("Enter Name: ")

        if member_id in self.members:
            print("Member already exists!")
        else:
            self.members[member_id] = Member(member_id, name)
            print("Member added successfully!")

    def lend_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        if book_id not in self.books:
            print("Book not found!")
            return

        if member_id not in self.members:
            print("Member not found!")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book.is_issued:
            print("Book already issued!")
        else:
            book.is_issued = True
            member.borrowed_books.append(book.title)
            print("Book issued successfully!")

    def return_book(self):
        book_id = input("Enter Book ID: ")
        member_id = input("Enter Member ID: ")

        if book_id not in self.books or member_id not in self.members:
            print("Invalid ID!")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if book.title in member.borrowed_books:
            book.is_issued = False
            member.borrowed_books.remove(book.title)
            print("Book returned successfully!")
        else:
            print("This member didn't borrow this book!")

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            for book in self.books.values():
                book.display()


# Menu-driven interface
def main():
    lib = Library()

    while True:
        print("\n===== Library Menu =====")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Display Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            lib.add_book()
        elif choice == '2':
            lib.add_member()
        elif choice == '3':
            lib.lend_book()
        elif choice == '4':
            lib.return_book()
        elif choice == '5':
            lib.display_books()
        elif choice == '6':
            print("Exiting system...")
            break
        else:
            print("Invalid choice! Try again.")


# Run program
main()