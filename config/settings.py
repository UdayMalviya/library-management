# Configuration Settings

import sys
from pathlib import Path

class Settings:
    """Configurations for Library Management System."""
    def __init__(self):
        self.PROJECT_ROOT = Path(__file__).resolve().parents[1]
        self.DATA_DIR = self.PROJECT_ROOT / 'data'
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)

        self.FINE_RATE_PER_DAY = 5.0 
        self.BORROW_PERIOD_DAYS = 14
        self.GRACE_PERIOD_DAYS = 2

        # file names 
        self.BOOK_FILE = 'books.csv'
        self.MEMBER_FILE = 'member.csv' 
        self.BOOK_FIELDS = ["book_id", "title", "author", "available"]
        self.MEMBER_FIELDS = ["member_id", "name", "status"]
        self.TRANSACTION_FILE = "transactions.csv"
        self.TRANSACTION_FIELDS = ["member_id", "book_id", "borrow_date", "return_date"]


        #===== LOGGING =====
        # LOG_FILE = 'your log file name'
        # LOG_VALUE = INFO


    def print_settings(self):
        """Print the configurations for library management system"""
        print("======== CONFIGURATIONS FOR LIBRARY MANAGEMENT =============")
        print('='*60) # repeat `=` 60 times
        print(f"PROJECT ROOT: {self.PROJECT_ROOT}")
        print(f"DATA DIR: {self.DATA_DIR}")
        print(f"BOOK FILE NAME: {self.BOOK_FILE}")
        print(f"BOOK FIELDS: {self.BOOK_FIELDS}")
        print(f"MEMBER FILE NAME: {self.MEMBER_FILE}")
        print(f"MEMBER FIELDS: {self.MEMBER_FIELDS}")
        print(f"TRANSACTION FILE NAME: {self.TRANSACTION_FILE}")
        print(f"TRANSACTION FILE FIELDS: {self.TRANSACTION_FIELDS}")
        print(f"FINE_RATE_PER_DAY: {self.FINE_RATE_PER_DAY}")
        print(f"BORROW_PERIOD_DAYS: {self.BORROW_PERIOD_DAYS}")
        print(f"GRACE_PERIOD_DAYS: {self.GRACE_PERIOD_DAYS}")
        print('='*60)

config = Settings()

if __name__ == "__main__":
    config.print_settings()

