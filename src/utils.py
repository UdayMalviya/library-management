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
