
import datetime
from config.settings import config


class FineManager:
        
    def calculate_fine(self, borrow_date_str: str, return_date_str: str) -> float:
        """
        Calculate the overdue fine for a borrowed book.

        Args:
            borrow_date_str (str): Borrow date in 'YYYY-MM-DD' format.
            return_date_str (str): Return date in 'YYYY-MM-DD' format.

        Returns:
            float: The fine amount (0 if no fine).
        """
        try:
            # Parse input dates
            borrow_date = datetime.datetime.strptime(borrow_date_str, "%Y-%m-%d").date()
            return_date = datetime.datetime.strptime(return_date_str, "%Y-%m-%d").date()

            # Validate date order
            if return_date < borrow_date:
                raise ValueError("Return date cannot be earlier than borrow date.")

            # Compute allowed borrowing period
            allowed_days = config.BORROW_PERIOD_DAYS + config.GRACE_PERIOD_DAYS
            total_days = (return_date - borrow_date).days

            # Compute overdue days and fine
            overdue_days = max(0, total_days - allowed_days)
            fine_amount = overdue_days *  config.FINE_RATE_PER_DAY

            # Optional: Round to 2 decimal places
            return round(fine_amount, 2)

        except Exception as e:
            print(f" Unexpected error while calculating fine: {e}")
            return 0.0
