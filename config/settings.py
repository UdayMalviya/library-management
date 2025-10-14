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
        self.MEMBER_FILE = 'member.csv' # todo add them in print_setting func
        self.BOOK_FIELDS = ["book_id", "title", "author", "available"]


        #===== LOGGING =====
        # LOG_FILE = 'your log file name'
        # LOG_VALUE = INFO


    def print_settings(self):
        """Print the configurations for library management system"""
        print("======== CONFIGURATIONS FOR LIBRARY MANAGEMENT =============")
        print('='*60) # repeat `=` 60 times
        print(f"PROJECT ROOT: {self.PROJECT_ROOT}")
        print(f"DATA DIR: {self.DATA_DIR}")
        print(f"FINE_RATE_PER_DAY: {self.FINE_RATE_PER_DAY}")
        print(f"BORROW_PERIOD_DAYS: {self.BORROW_PERIOD_DAYS}")
        print(f"GRACE_PERIOD_DAYS: {self.GRACE_PERIOD_DAYS}")
        print('='*60)

config = Settings()

if __name__ == "__main__":
    config.print_settings()






# FINE_RATE_PER_DAY = 5.0        # Fine amount per overdue day
# BORROW_PERIOD_DAYS = 14        # Default borrowing period
# GRACE_PERIOD_DAYS = 2          # Days allowed before fine starts
# DATA_PATH = "data/"


