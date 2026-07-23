def get_players():

    players = []

    for boat in range(1, 7):

        players.append({

            "boat": boat,

            # 基本情報

            "number": 0,

            "name": "",

            "rank": "",

            "age": 0,

            "term": 0,

            "branch": "",

            # 成績

            "national_win_rate": 0.0,

            "national_second_rate": 0.0,

            "national_third_rate": 0.0,

            "local_win_rate": 0.0,

            "local_second_rate": 0.0,

            "local_third_rate": 0.0,

            # スタート

            "average_st": 0.00,

            "st_rank": 0,

            # モーター

            "motor_number": 0,

            "motor_second_rate": 0.0,

            "motor_third_rate": 0.0,

            # 展示

            "exhibition_time": 0.00,

            "average_exhibition_time": 0.00

        })

    return players
