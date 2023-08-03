class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = {}
        self.authors = {}

    def add_book(self, author):
        if author not in self.authors:
            self.authors[author] = []
            print(f"Author '{author}' added to the library.")
        else:
            print(f"Author '{author}' already exists in the library.")

        while len(self.authors[author]) < 5:
            book_title = input(f"Enter book title by '{author}': ")
            if book_title:
                self.authors[author].append(book_title)
                self.books.append(book_title)
                print(f"Book '{book_title}' by {author} added to the library.")
            else:
                break

    def display_books(self):
        print("Available Books:")
        for book in self.books:
            print(f"- {book}")

    def borrow_book(self, book_title, borrower):
        found = False
        for author, books in self.authors.items():
            if book_title in books:
                found = True
                if book_title in self.borrowed_books:
                    print(f"Sorry, '{book_title}' is already borrowed by {self.borrowed_books[book_title]}.")
                else:
                    self.borrowed_books[book_title] = borrower
                    print(f"Book '{book_title}' by {author} borrowed by {borrower}.")
        if not found:
            print(f"Book '{book_title}' is not available in the library.")

    def return_book(self, book_title):
        if book_title in self.borrowed_books:
            borrower = self.borrowed_books[book_title]
            del self.borrowed_books[book_title]
            print(f"Book '{book_title}' returned by {borrower}.")
        else:
            print(f"Book '{book_title}' is not borrowed.")

    def view_authors(self):
        print("Indigenous Nigerian Authors in the library:")
        nigerian_authors = [
            "Chinua Achebe",
            "Wole Soyinka",
            "Chimamanda Ngozi Adichie",
            "Ben Okri",
            "Buchi Emecheta",
            "Flora Nwapa",
            "Helon Habila",
            "Chigozie Obioma",
            "Teju Cole",
            "Sefi Atta"
        ]
        for author in nigerian_authors:
            if author in self.authors:
                books_by_author = ", ".join(self.authors[author])
                print(f"- {author}: {books_by_author}")
            else:
                print(f"- {author}: No books available in the library.")

    def about_library(self):
        print("Welcome to Our Library!")
        print("We have a wide range of books for you to borrow.")


def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book/Author")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Authors")
        print("6. About the Library")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            author = input("Enter author name: ")
            library.add_book(author)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book_title = input("Enter book title to borrow: ")
            borrower = input("Enter your name: ")
            library.borrow_book(book_title, borrower)

        elif choice == "4":
            book_title = input("Enter book title to return: ")
            library.return_book(book_title)

        elif choice == "5":
            library.view_authors()

        elif choice == "6":
            library.about_library()

        elif choice == "0":
            print("Thank you for using the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
