import datetime
from config import settings

def calculate_fine(borrow_date_str, return_date_str):
    borrow_date = datetime.datetime.strptime(borrow_date_str, "%Y-%m-%d").date()
    return_date = datetime.datetime.strptime(return_date_str, "%Y-%m-%d").date()
    overdue_days = (return_date - borrow_date).days - (settings.BORROW_PERIOD_DAYS + settings.GRACE_PERIOD_DAYS)
    return max(0, overdue_days * settings.FINE_RATE_PER_DAY)
