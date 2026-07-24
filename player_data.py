import csv

def get_players():

    players = []

    with open("players.csv", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            players.append({

                "boat": int(row["boat"]),

                "number": int(row["number"]),

                "name": row["name"],

                "rank": row["rank"],

                "age": int(row["age"]),

                "term": int(row["term"]),

                "branch": row["branch"],

                "national_win_rate": float(row["national_win_rate"]),

                "national_second_rate": float(row["national_second_rate"]),

                "national_third_rate": float(row["national_third_rate"]),

                "local_win_rate": float(row["local_win_rate"]),

                "local_second_rate": float(row["local_second_rate"]),

                "local_third_rate": float(row["local_third_rate"]),

                "average_st": float(row["average_st"]),

                "st_rank": int(row["st_rank"]),

                "motor_number": int(row["motor_number"]),

                "motor_second_rate": float(row["motor_second_rate"]),

                "motor_third_rate": float(row["motor_third_rate"]),

                "exhibition_time": float(row["exhibition_time"]),

                "average_exhibition_time": float(row["average_exhibition_time"])

            })

    return players
