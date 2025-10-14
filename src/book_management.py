from src.utils import read_csv, write_csv, generate_id
from config.settings import config

# BOOK_FILE = "books.csv"


def add_book(title: str, author: str) -> None : # added type hints
    """ Add book to file
    Args:
    - title : str = title of the book
    - author : str = name of the author
    """
    try: 
        books = read_csv(config.BOOK_FILE)
        new_book = {
            "book_id": generate_id("BK"),
            "title": title,
            "author": author,
            "available": "yes"
        }
        books.append(new_book)
        write_csv(config.BOOK_FILE, books, config.BOOK_FIELDS)
        print(f"Book '{title}' added successfully.")
    except Exception as e:
        print(f"Got an exception while adding book: {e}")

def search_books(keyword: str):
    """Search a book if it's available in the file.
     - Args:
     keyword: str = a keyword to search the file."""
    try:
        books = read_csv(config.BOOK_FILE)

        results = [b for b in books if keyword.lower() in b["title"].lower() or
                keyword.lower() in b["author"].lower()] # list comprehensios
        if results:
            for b in results:
                print(f"{b['book_id']}: {b['title']} by {b['author']} ({'Available' if b['available']=='yes' else 'Borrowed'})")
        else:
            print("No books found.")
    except Exception as e:
        print(f" An error occured: {e}")

def update_book(book_id: str, new_title: str | None =None, new_author: str | None = None):
    """"""
    books = read_csv(BOOK_FILE)
    for book in books:
        if book["book_id"] == book_id:
            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author
            write_csv(BOOK_FILE, books, BOOK_FIELDS)
            print("Book updated successfully.")
            return
    print("Book not found.")

def delete_book(book_id):
    books = read_csv(BOOK_FILE)
    updated = [b for b in books if b["book_id"] != book_id]
    write_csv(BOOK_FILE, updated, BOOK_FIELDS)
    print("Book deleted.")
