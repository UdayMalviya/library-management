import sys

from src.book_management import BookManager
from src.fine_management import FineManager
from src.member_management import MemberManager
from src.transaction_management import TransactionManager

class LibraryCLI:
    """
    Object-Oriented Library Management Command-Line Interface.
    Combines all management modules into a cohesive interactive shell.
    """

    def __init__(self):
        print(" Library Management System Initialized")
        self.book_manager = BookManager()
        self.fine_manager = FineManager() 
        self.member_manager = MemberManager()
        self.transaction_manager = TransactionManager()

    # === MAIN LOOP ===
    def run(self):
        """Main interactive loop."""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip()

            try:
                self.handle_choice(choice)
            except KeyboardInterrupt:
                print("\n Interrupted by user. Exiting...")
                sys.exit(0)
            except Exception as e:
                print(f" Unexpected error: {e}")

    # === MENU ===
    def display_menu(self):
        """Display the main CLI menu."""
        print("\n===  Library Management CLI ===")
        print("1.  Add Book")
        print("2.  Search Books")
        print("3.  Update Book Details")
        print("4.  Delete Book")
        print("5.  Register Member")
        print("6.  Suspend Member")
        print("7.  Borrow Book")
        print("8.  Return Book")
        print("9.  Calculate Fine (Manual Check)")
        print("0.  Exit")

    # === CHOICE HANDLER ===
    def handle_choice(self, choice: str):
        """Route user input to the correct operation."""
        match choice:
            case "1":
                self.add_book()
            case "2":
                self.search_books()
            case "3":
                self.update_book()
            case "4":
                self.delete_book()
            case "5":
                self.register_member()
            case "6":
                self.suspend_member()
            case "7":
                self.borrow_book()
            case "8":
                self.return_book()
            case "9":
                self.calculate_fine()
            case "0":
                print(" Exiting Library Management System...")
                sys.exit(0)
            case _:
                print(" Invalid choice. Please try again.")

    # === BOOK MANAGEMENT ===
    def add_book(self):
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        if not title or not author:
            print(" Both title and author are required.")
            return
        # book_management.add_book(title, author)
        self.book_manager.add_book(title=title, author=author)

    def search_books(self):
        keyword = input("Enter search keyword: ").strip()
        if not keyword:
            print(" Please enter a keyword.")
            return
        self.book_manager.search_books(keyword)

    def update_book(self):
        book_id = input("Enter book ID to update: ").strip()
        new_title = input("Enter new title (press Enter to skip): ").strip()
        new_author = input("Enter new author (press Enter to skip): ").strip()
        self.book_manager.update_book(book_id, new_title or None, new_author or None)

    def delete_book(self):
        book_id = input("Enter book ID to delete: ").strip()
        if not book_id:
            print(" Book ID required.")
            return
        self.book_manager.delete_book(book_id)

    # === MEMBER MANAGEMENT ===
    def register_member(self):
        name = input("Enter member name: ").strip()
        if not name:
            print(" Member name cannot be empty.")
            return
        self.member_manager.register_member(name)

    def suspend_member(self):
        member_id = input("Enter member ID to suspend: ").strip()
        if not member_id:
            print(" Member ID required.")
            return
        self.member_manager.suspend_member(member_id)

    # === TRANSACTIONS ===
    def borrow_book(self):
        member_id = input("Enter member ID: ").strip()
        book_id = input("Enter book ID: ").strip()
        if not member_id or not book_id:
            print(" Both Member ID and Book ID are required.")
            return
        self.transaction_manager.borrow_book(member_id, book_id)

    def return_book(self):
        member_id = input("Enter member ID: ").strip()
        book_id = input("Enter book ID: ").strip()
        if not member_id or not book_id:
            print(" Both Member ID and Book ID are required.")
            return
        self.transaction_manager.return_book(member_id, book_id)

    # === FINES ===
    def calculate_fine(self):
        borrow_date = input("Enter borrow date (YYYY-MM-DD): ").strip()
        return_date = input("Enter return date (YYYY-MM-DD): ").strip()
        fine = self.fine_manager.calculate_fine(borrow_date, return_date)
        print(f" Fine amount: ₹{fine}")


if __name__ == "__main__":
    app = LibraryCLI()
    app.run()
