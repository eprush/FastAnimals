import os
from pathlib import Path
import uuid

STATIC_DIR = os.path.join(Path(__file__).resolve().parent.parent.parent, "static")

def get_file_path():
    filename = str(uuid.uuid4()) + ".jpg"
    return os.path.join(STATIC_DIR, filename)

def save_image(data: bytes) -> None:
    filepath = get_file_path()
    with open(filepath, "wb") as file:
        file.write(data)
    return
