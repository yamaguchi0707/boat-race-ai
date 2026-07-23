def get_players():

    players = []

    for boat in range(1, 7):

        players.append({

            "boat": boat,

            "number": 0000,

            "name": "選手名",

            "rank": "A1",

            "age": 0,

            "term": 0,

            "area": "",

            "win_rate": 0,

            "second_rate": 0,

            "third_rate": 0,

            "st": 0.00,

            "motor_rate": 0,

            "exhibition_time": 0.00,

            "average_exhibition_time": 0.00

        })

    return players
