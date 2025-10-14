import sys
from src import book_management, member_management, transaction_management

def main(): # function
    while True:
        print("\n=== Library Management CLI ===")
        print("1. Add Book")
        print("2. Search Books")
        print("3. Register Member")
        print("4. Borrow Book")
        print("5. Return Book")
        print("0. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            book_management.add_book(title, author)
        elif choice == "2":
            keyword = input("Enter search keyword: ")
            book_management.search_books(keyword)
        elif choice == "3":
            name = input("Enter member name: ")
            member_management.register_member(name)
        elif choice == "4":
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            transaction_management.borrow_book(member_id, book_id)
        elif choice == "5":
            member_id = input("Enter member ID: ")
            book_id = input("Enter book ID: ")
            transaction_management.return_book(member_id, book_id)
        elif choice == "0":
            sys.exit()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
