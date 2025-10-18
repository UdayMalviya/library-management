#BOOK MANAGEMENT

import pandas as pd
from src.utils import read_csv, write_csv, generate_id
from config.settings import config


class BookManager:
    """
    BookManager handles all CRUD operations for books stored in a CSV file.
    """

    def __init__(self):
        """Initialize and ensure DataFrame consistency."""
        try:
            self.file_path = config.BOOK_FILE
            self.fields = config.BOOK_FIELDS
            self.df = read_csv(self.file_path)

            # Initialize DataFrame if file is empty or invalid
            if self.df.empty:
                self.df = pd.DataFrame(columns=self.fields)

        except Exception as e:
            print(f"[INIT ERROR] Failed to initialize BookManager: {e}")

    # Core Operations
    
    def add_book(self, title: str, author: str) -> None:
        """
        Add a new book record to the system.

        Args:
            title (str): Title of the book.
            author (str): Author of the book.
        """
        try:
            new_book = {
                "book_id": generate_id("BK"),
                "title": title.strip(),
                "author": author.strip(),
                "available": "yes"
            }

            self.df = pd.concat([self.df, pd.DataFrame([new_book])], ignore_index=True)
            write_csv(self.file_path, self.df, self.fields)

            print(f" Book '{title}' by {author} added successfully.")
        except Exception as e:
            print(f" Error while adding book: {e}")

    

    def search_books(self, keyword: str) -> None:
        """
        Search for books by keyword in title or author.

        Args:
            keyword (str): Keyword to search for.
        """
        try:
            if self.df.empty:
                print(" No books available in the library.")
                return

            mask = (
                self.df["title"].str.contains(keyword, case=False, na=False) |
                self.df["author"].str.contains(keyword, case=False, na=False)
            )
            results = self.df[mask]

            if results.empty:
                print(" No books found matching your search.")
                return

            print(f"\n Search Results for '{keyword}':\n")
            for _, row in results.iterrows():
                status = "Available" if row["available"].lower() == "yes" else "Borrowed"
                print(f"{row['book_id']}: {row['title']} by {row['author']} ({status})")

        except Exception as e:
            print(f" Error while searching books: {e}")


    def update_book(self, book_id: str, new_title: str | None = None, new_author: str | None = None) -> None:
        """
        Update a book's title or author.

        Args:
            book_id (str): ID of the book to update.
            new_title (str, optional): New title.
            new_author (str, optional): New author.
        """
        try:
            if self.df.empty or book_id not in self.df["book_id"].values:
                print(" Book not found.")
                return

            if new_title:
                self.df.loc[self.df["book_id"] == book_id, "title"] = new_title.strip()
            if new_author:
                self.df.loc[self.df["book_id"] == book_id, "author"] = new_author.strip()

            write_csv(self.file_path, self.df, self.fields)
            print(" Book updated successfully.")
        except Exception as e:
            print(f" Error while updating book: {e}")

    

    def delete_book(self, book_id: str) -> None:
        """
        Delete a book record.

        Args:
            book_id (str): Book ID to delete.
        """
        try:
            if self.df.empty or book_id not in self.df["book_id"].values:
                print(" Book not found.")
                return

            self.df = self.df[self.df["book_id"] != book_id]
            write_csv(self.file_path, self.df, self.fields)
            print(" Book deleted successfully.")
        except Exception as e:
            print(f" Error while deleting book: {e}")

    

    def toggle_availability(self, book_id: str, available: bool) -> None:
        """
        Toggle book availability (borrow or return).

        Args:
            book_id (str): ID of the book.
            available (bool): True = returned, False = borrowed.
        """
        try:
            if self.df.empty or book_id not in self.df["book_id"].values:
                print(" Book not found.")
                return

            self.df.loc[self.df["book_id"] == book_id, "available"] = "yes" if available else "no"
            write_csv(self.file_path, self.df, self.fields)

            status = "returned" if available else "borrowed"
            print(f" Book marked as {status}.")
        except Exception as e:
            print(f" Error while toggling book availability: {e}")

    

    def list_all_books(self) -> None:
        """
        Display all books in the library.
        """
        try:
            if self.df.empty:
                print(" No books available.")
                return

            print("\n All Books in Library:\n")
            for _, row in self.df.iterrows():
                status = "Available" if row["available"].lower() == "yes" else "Borrowed"
                print(f"{row['book_id']}: {row['title']} by {row['author']} ({status})")

        except Exception as e:
            print(f" Error while listing books: {e}")
        