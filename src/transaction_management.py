import datetime
from src.utils import read_csv, write_csv


TRANSACTION_FILE = "transactions.csv"
TRANSACTION_FIELDS = ["member_id", "book_id", "borrow_date", "return_date"]

def borrow_book(member_id, book_id):
    books = read_csv("books.csv")
    book = next((b for b in books if b["book_id"] == book_id and b["available"] == "yes"), None)
    if not book:
        print("Book not available.")
        return
    
    book["available"] = "no"
    write_csv("books.csv", books, ["book_id", "title", "author", "available"])
    
    transactions = read_csv(TRANSACTION_FILE)
    transactions.append({
        "member_id": member_id,
        "book_id": book_id,
        "borrow_date": str(datetime.date.today()),
        "return_date": ""
    })
    write_csv(TRANSACTION_FILE, transactions, TRANSACTION_FIELDS)
    print("Book borrowed successfully.")

def return_book(member_id, book_id):
    transactions = read_csv(TRANSACTION_FILE)
    for t in transactions:
        if t["member_id"] == member_id and t["book_id"] == book_id and not t["return_date"]:
            t["return_date"] = str(datetime.date.today())
            write_csv(TRANSACTION_FILE, transactions, TRANSACTION_FIELDS)
            
            books = read_csv("books.csv")
            for b in books:
                if b["book_id"] == book_id:
                    b["available"] = "yes"
            write_csv("books.csv", books, ["book_id", "title", "author", "available"])
            print("Book returned successfully.")
            return
    print("Transaction not found.")
