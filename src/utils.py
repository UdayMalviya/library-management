import os
import uuid
from config.settings import config
import pandas as pd # Adding pandas library


# pip install pandas 
def generate_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:6]}"

def read_csv(filename: str) -> pd.DataFrame:
    """ Read the csv file and return a Dataframe obj. """
    # path = os.path.join(settings.DATA_PATH, filename)
    try:

        path = config.DATA_DIR / str(filename)
        if not os.path.exists(path):
            return pd.DataFrame()
        return pd.read_csv(path, encoding='utf-8')  
    except Exception as e:
        print(f"An error occured while reading file: {e}")

def write_csv(filename: str, data: pd.DataFrame, fieldnames: list[str]):
    """custom function to write or update csv file."""

    # path = os.path.join(settings.DATA_PATH, filename)
    try:
        path = config.DATA_DIR / str(filename)
        if data.empty:
            data = data[fieldnames]
        data.to_csv(path, index=False)
    except Exception as e:
        print(f"An error occured while Saving file {e}")

    # with open(path, mode='w', newline='', encoding='utf-8') as file:
    #     writer = csv.DictWriter(file, fieldnames=fieldnames)
        # writer.writeheader()
        # writer.writerows(data)

# import os
# import uuid
# import pandas as pd
# from config.settings import config


# def generate_id(prefix: str) -> str:
#     """Generate a unique ID with a given prefix."""
#     return f"{prefix}-{uuid.uuid4().hex[:6]}"


# def read_csv(filename: str) -> pd.DataFrame:
#     """
#     Read a CSV file using pandas.
    
#     Args:
#         filename (str): Name of the CSV file located in settings.DATA_PATH.
#     Returns:
#         pd.DataFrame: Loaded DataFrame (empty if file does not exist).
#     """
#     # path = os.path.join(config.DATA_DIR, filename)
#     path = config.DATA_DIR / filename
#     if not os.path.exists(path):
#         # Return an empty DataFrame with no columns
#         return pd.DataFrame() 
    
#     return pd.read_csv(path)


# def write_csv(filename: str, data: pd.DataFrame, fieldnames: list[str]) -> None:
#     """
#     Write a pandas DataFrame to CSV.
    
#     Args:
#         filename (str): Name of the CSV file located in settings.DATA_PATH.
#         data (pd.DataFrame): DataFrame to save.
#         fieldnames (list[str]): Expected column order.
#     """
#     path = os.path.join(config.DATA_DIR, filename)

#     # Ensure only expected columns are written
#     if not data.empty:
#         data = data[fieldnames]  # Keep only expected columns

#     data.to_csv(path, index=False, encoding="utf-8")

