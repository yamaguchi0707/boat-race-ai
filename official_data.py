import json

import os

def load_official_data():

    file_path = "official_data.json"

    if not os.path.exists(file_path):

        return None

    with open(file_path, "r", encoding="utf-8") as f:

        return json.load(f)
