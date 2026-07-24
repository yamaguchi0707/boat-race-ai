import json

import os

from datetime import datetime

DATA_FILE = "official_data.json"

def load_official_data():

    if not os.path.exists(DATA_FILE):

        print("official_data.json がありません")

        return None

    with open(DATA_FILE, "r", encoding="utf-8") as f:

        return json.load(f)

def save_official_data(data):

    with open(DATA_FILE, "w", encoding="utf-8") as f:

        json.dump(

            data,

            f,

            ensure_ascii=False,

            indent=4

        )

if __name__ == "__main__":

    data = load_official_data()

    if data:

        print("official_data.json 読み込み成功")

        print("開催場:", data.get("venue"))

        print("レース数:", len(data.get("races", [])))

    else:

        print("official_data.json がありません")
