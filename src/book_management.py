from src.utils import read_csv, write_csv, generate_id

BOOK_FILE = "books.csv"
BOOK_FIELDS = ["book_id", "title", "author", "available"]

def add_book(title, author):
    books = read_csv(BOOK_FILE)
    new_book = {
        "book_id": generate_id("BK"),
        "title": title,
        "author": author,
        "available": "yes"
    }
    books.append(new_book)
    write_csv(BOOK_FILE, books, BOOK_FIELDS)
    print(f"Book '{title}' added successfully.")

def search_books(keyword):
    books = read_csv(BOOK_FILE)
    results = [b for b in books if keyword.lower() in b["title"].lower() or keyword.lower() in b["author"].lower()]
    if results:
        for b in results:
            print(f"{b['book_id']}: {b['title']} by {b['author']} ({'Available' if b['available']=='yes' else 'Borrowed'})")
    else:
        print("No books found.")

def update_book(book_id, new_title=None, new_author=None):
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
