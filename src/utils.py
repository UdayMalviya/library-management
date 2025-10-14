import csv
import os
import uuid
from config import settings

def generate_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:6]}"

def read_csv(filename):
    path = os.path.join(settings.DATA_PATH, filename)
    if not os.path.exists(path):
        return []
    with open(path, newline='', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def write_csv(filename, data, fieldnames):
    path = os.path.join(settings.DATA_PATH, filename)
    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

