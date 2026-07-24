import json

import os

from datetime import datetime

DATA_FILE = "data/race_data.json"

OUTPUT_FILE = "official_data.json"

def load_race_data():

    if not os.path.exists(DATA_FILE):

        print("race_data.json がありません")

        return None

    with open(

        DATA_FILE,

        "r",

        encoding="utf-8"

    ) as f:

        return json.load(f)

def save_official_data(data):

    with open(

        OUTPUT_FILE,

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            data,

            f,

            ensure_ascii=False,

            indent=4

        )

def convert_data(data):

    result = {

        "venue": data.get(

            "venue",

            "大村"

        ),

        "update_time": str(

            datetime.now()

        ),

        "races": data.get(

            "races",

            []

        )

    }

    return result

if __name__ == "__main__":

    print("=== データ取得開始 ===")

    data = load_race_data()

    if data:

        official = convert_data(data)

        save_official_data(

            official

        )

        print(

            "official_data.json 更新完了"

        )

    else:

        print(

            "データ取得失敗"

        )
