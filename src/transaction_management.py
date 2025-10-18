

import os
import datetime
import pandas as pd
from src.utils import read_csv, write_csv
from config.settings import config

from src.fine_management import FineManager


class TransactionManager:
    """
    Handles all borrow and return transactions between members and books.
    """

    def __init__(self):
        """Initialize and ensure CSV consistency."""
        try:
            self.fine_manager = FineManager()
            self.file_path = config.TRANSACTION_FILE
            self.fields = config.TRANSACTION_FIELDS

            # Ensure the transaction file exists
            if not os.path.exists(self.file_path):
                self.df = pd.DataFrame(columns=self.fields)
                write_csv(self.file_path, self.df, self.fields)
            else:
                self.df = read_csv(self.file_path)

            # Initialize DataFrame if empty
            if self.df.empty:
                self.df = pd.DataFrame(columns=self.fields)

        except Exception as e:
            print(f"[INIT ERROR] Failed to initialize TransactionManager: {e}")

    

    def borrow_book(self, member_id: str, book_id: str) -> None:
        """
        Record a book borrowing transaction.

        Args:
            member_id (str): ID of the borrowing member.
            book_id (str): ID of the book being borrowed.
        """
        try:
            # Load books and members
            books = read_csv(config.BOOK_FILE)
            members = read_csv(config.MEMBER_FILE)

            # Validate member
            if members.empty or member_id not in members["member_id"].values:
                print(" Invalid member ID.")
                return

            member_status = members.loc[members["member_id"] == member_id, "status"].iloc[0]
            if member_status.lower() != "active":
                print(" Member account is suspended. Cannot borrow books.")
                return

            # Validate book availability
            if books.empty or book_id not in books["book_id"].values:
                print(" Book not found.")
                return

            book_status = books.loc[books["book_id"] == book_id, "available"].iloc[0]
            if book_status.lower() != "yes":
                print(" Book is currently not available.")
                return

            # Update book availability
            books.loc[books["book_id"] == book_id, "available"] = "no"
            write_csv(config.BOOK_FILE, books, config.BOOK_FIELDS)

            # Record the transaction
            new_transaction = {
                "member_id": member_id,
                "book_id": book_id,
                "borrow_date": str(datetime.date.today()),
                "return_date": ""
            }

            self.df = pd.concat([self.df, pd.DataFrame([new_transaction])], ignore_index=True)
            write_csv(self.file_path, self.df, self.fields)

            print(f" Book '{book_id}' borrowed successfully by member '{member_id}'.")
        except Exception as e:
            print(f" Error while borrowing book: {e}")

    

    def return_book(self, member_id: str, book_id: str) -> None:
        """
        Process the return of a borrowed book and calculate fines if applicable.

        Args:
            member_id (str): ID of the member returning the book.
            book_id (str): ID of the book being returned.
        """
        try:
            # Locate the transaction
            active_txn = self.df[
                (self.df["member_id"] == member_id) &
                (self.df["book_id"] == book_id) &
                (self.df["return_date"] == "")
            ]

            if active_txn.empty:
                print(" No active borrowing transaction found.")
                return

            borrow_date = active_txn.iloc[0]["borrow_date"]
            return_date = str(datetime.date.today())

            # Optional fine calculation
            fine_amount = 0.0
            
            fine_amount = self.fine_manager.calculate_fine(borrow_date, return_date)

            # Update transaction record
            self.df.loc[
                (self.df["member_id"] == member_id) &
                (self.df["book_id"] == book_id) &
                (self.df["return_date"] == ""),
                "return_date"
            ] = return_date

            write_csv(self.file_path, self.df, self.fields)

            # Update book availability
            books = read_csv(config.BOOK_FILE)
            books.loc[books["book_id"] == book_id, "available"] = "yes"
            write_csv(config.BOOK_FILE, books, config.BOOK_FIELDS)

            if fine_amount > 0:
                print(f" Book returned successfully. Fine due: ₹{fine_amount}")
            else:
                print(" Book returned successfully. No fine due.")

        except Exception as e:
            print(f"Error while returning book: {e}")

    

    def list_transactions(self, member_id: str | None = None) -> None:
        """
        List all transactions (optionally filtered by member).

        Args:
            member_id (str, optional): Filter by member ID.
        """
        try:
            if self.df.empty:
                print(" No transactions recorded yet.")
                return

            df = self.df
            if member_id:
                df = df[df["member_id"] == member_id]

            if df.empty:
                print(f" No transactions found for member '{member_id}'.")
                return

            print("\n Transaction History:\n")
            for _, row in df.iterrows():
                status = "Returned" if row["return_date"] else "Borrowed"
                print(
                    f"Member: {row['member_id']} | "
                    f"Book: {row['book_id']} | "
                    f"Borrowed: {row['borrow_date']} | "
                    f"Returned: {row['return_date'] or '---'} | "
                    f"Status: {status}"
                )
        except Exception as e:
            print(f" Error while listing transactions: {e}")
