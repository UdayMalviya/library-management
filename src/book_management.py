from src.utils import read_csv, write_csv, generate_id
from config.settings import config
import pandas as pd

class BOOK:
    def add_book(self, title: str, author: str) -> None:
        """
        Add a new book to the CSV file.

        Args:
            title (str): Title of the book.
            author (str): Author's name.
        """
        try:
            df = read_csv(config.BOOK_FILE)

            # Initialize DataFrame if empty
            if df.empty:
                df = pd.DataFrame(columns=config.BOOK_FIELDS)

            new_book = {
                "book_id": generate_id("BK"),
                "title": title.strip(),
                "author": author.strip(),
                "available": "yes"
            }

            df = pd.concat([df, pd.DataFrame([new_book])], ignore_index=True)
            write_csv(config.BOOK_FILE, df, config.BOOK_FIELDS)

            print(f" Book '{title}' added successfully.")
        except Exception as e:
            print(f" Error while adding book: {e}")

# def add_book(title: str, author: str) -> None : # added type hints
#     """ Add book to file
#     Args:
#     - title : str = title of the book
#     - author : str = name of the author
#     """
#     try: 
#         books = read_csv(config.BOOK_FILE)
#         new_book = {
#             "book_id": generate_id("BK"),
#             "title": title,
#             "author": author,
#             "available": "yes"
#         }
#         books.append(new_book)
#         write_csv(config.BOOK_FILE, books, config.BOOK_FIELDS)
#         print(f"Book '{title}' added successfully.")
#     except Exception as e:
#         print(f"Got an exception while adding book: {e}")

# def search_books(keyword: str):
#     """Search a book if it's available in the file.
#      - Args:
#      keyword: str = a keyword to search the file."""
#     try:
#         books = read_csv(config.BOOK_FILE)

#         results = [b for b in books if keyword.lower() in b["title"].lower() or
#                 keyword.lower() in b["author"].lower()] # list comprehensios
#         if results:
#             for b in results:
#                 print(f"{b['book_id']}: {b['title']} by {b['author']} ({'Available' if b['available']=='yes' else 'Borrowed'})")
#         else:
#             print("No books found.")
#     except Exception as e:
#         print(f" An error occured: {e}")

# def update_book(book_id: str, new_title: str | None =None, new_author: str | None = None):
#     """"""
#     books = read_csv(BOOK_FILE)
#     for book in books:
#         if book["book_id"] == book_id:
#             if new_title:
#                 book["title"] = new_title
#             if new_author:
#                 book["author"] = new_author
#             write_csv(BOOK_FILE, books, BOOK_FIELDS)
#             print("Book updated successfully.")
#             return
#     print("Book not found.")

# def delete_book(book_id):
#     books = read_csv(BOOK_FILE)
#     updated = [b for b in books if b["book_id"] != book_id]
#     write_csv(BOOK_FILE, updated, BOOK_FIELDS)
#     print("Book deleted.")


# import pandas as pd
# from src.utils import read_csv, write_csv, generate_id
# from config.settings import config


# def add_book(title: str, author: str) -> None:
#     """
#     Add a new book to the CSV file.

#     Args:
#         title (str): Title of the book.
#         author (str): Author's name.
#     """
#     try:
#         df = read_csv(config.BOOK_FILE)

#         # Initialize DataFrame if empty
#         if df.empty:
#             df = pd.DataFrame(columns=config.BOOK_FIELDS)

#         new_book = {
#             "book_id": generate_id("BK"),
#             "title": title.strip(),
#             "author": author.strip(),
#             "available": "yes"
#         }

#         df = pd.concat([df, pd.DataFrame([new_book])], ignore_index=True)
#         write_csv(config.BOOK_FILE, df, config.BOOK_FIELDS)

#         print(f" Book '{title}' added successfully.")
#     except Exception as e:
#         print(f" Error while adding book: {e}")


# def search_books(keyword: str) -> None:
#     """
#     Search for books by title or author.

#     Args:
#         keyword (str): Keyword to search in title or author.
#     """
#     try:
#         df = read_csv(config.BOOK_FILE)
#         if df.empty:
#             print(" No books available in the library.")
#             return

#         mask = df["title"].str.contains(keyword, case=False, na=False) | \
#                df["author"].str.contains(keyword, case=False, na=False)
#         results = df[mask]

#         if results.empty:
#             print(" No books found matching your search.")
#         else:
#             for _, row in results.iterrows():
#                 status = "Available" if row["available"].lower() == "yes" else "Borrowed"
#                 print(f"{row['book_id']}: {row['title']} by {row['author']} ({status})")
#     except Exception as e:
#         print(f" Error while searching books: {e}")


# def update_book(book_id: str, new_title: str | None = None, new_author: str | None = None) -> None:
#     """
#     Update the title or author of a book.

#     Args:
#         book_id (str): ID of the book to update.
#         new_title (str, optional): New title for the book.
#         new_author (str, optional): New author for the book.
#     """
#     try:
#         df = read_csv(config.BOOK_FILE)
#         if df.empty or book_id not in df["book_id"].values:
#             print(" Book not found.")
#             return

#         if new_title:
#             df.loc[df["book_id"] == book_id, "title"] = new_title.strip()
#         if new_author:
#             df.loc[df["book_id"] == book_id, "author"] = new_author.strip()

#         write_csv(config.BOOK_FILE, df, config.BOOK_FIELDS)
#         print(" Book updated successfully.")
#     except Exception as e:
#         print(f" Error while updating book: {e}")


# def delete_book(book_id: str) -> None:
#     """
#     Delete a book record from the CSV file.

#     Args:
#         book_id (str): ID of the book to delete.
#     """
#     try:
#         df = read_csv(config.BOOK_FILE)
#         if df.empty or book_id not in df["book_id"].values:
#             print(" Book not found.")
#             return

#         df = df[df["book_id"] != book_id]
#         write_csv(config.BOOK_FILE, df, config.BOOK_FIELDS)
#         print(" Book deleted successfully.")
#     except Exception as e:
#         print(f" Error while deleting book: {e}")


# def toggle_availability(book_id: str, available: bool) -> None:
#     """
#     Mark a book as borrowed or returned.

#     Args:
#         book_id (str): ID of the book.
#         available (bool): True if returned, False if borrowed.
#     """
#     try:
#         df = read_csv(config.BOOK_FILE)
#         if df.empty or book_id not in df["book_id"].values:
#             print(" Book not found.")
#             return

#         df.loc[df["book_id"] == book_id, "available"] = "yes" if available else "no"
#         write_csv(config.BOOK_FILE, df, config.BOOK_FIELDS)

#         status = "returned" if available else "borrowed"
#         print(f" Book marked as {status}.")
#     except Exception as e:
#         print(f" Error while updating book availability: {e}")
