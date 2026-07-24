from score import calculate_score

def course_bonus(boat):

    bonus = {

        1: 20,

        2: 8,

        3: 10,

        4: 12,

        5: 5,

        6: 3

    }

    return bonus.get(

        boat,

        0

    )

def water_bonus(player):

    bonus = 0

    wind = float(

        player.get(

            "wind_speed",

            0

        )

    )

    wave = float(

        player.get(

            "wave_height",

            0

        )

    )

    if wind >= 5:

        if player["boat"] >= 4:

            bonus += 8

    if wave >= 3:

        if player.get("rank") == "A1":

            bonus += 5

    return bonus

def make_prediction(players, venue="大村"):

    ranking = []

    for player in players:

        score = (

            calculate_score(player)

            + course_bonus(

                player["boat"]

            )

            + water_bonus(

                player

            )

        )

        ranking.append(

            {

                "boat": player["boat"],

                "score": round(

                    score,

                    1

                )

            }

        )

    ranking.sort(

        key=lambda x:x["score"],

        reverse=True

    )

    boats = [

        x["boat"]

        for x in ranking

    ]

    # 本命系

    main = [

        f"{boats[0]}-{boats[1]}-{boats[2]}",

        f"{boats[0]}-{boats[2]}-{boats[1]}",

        f"{boats[0]}-{boats[1]}-{boats[3]}",

        f"{boats[0]}-{boats[3]}-{boats[1]}",

        f"{boats[0]}-{boats[2]}-{boats[3]}"

    ]

    # 押さえ系

    middle = [

        f"{boats[1]}-{boats[0]}-{boats[2]}",

        f"{boats[1]}-{boats[2]}-{boats[0]}",

        f"{boats[0]}-{boats[3]}-{boats[2]}",

        f"{boats[2]}-{boats[0]}-{boats[1]}",

        f"{boats[3]}-{boats[0]}-{boats[1]}"

    ]

    # 穴系

    hole = [

        f"{boats[2]}-{boats[0]}-{boats[1]}",

        f"{boats[2]}-{boats[1]}-{boats[0]}",

        f"{boats[3]}-{boats[0]}-{boats[2]}",

        f"{boats[4]}-{boats[0]}-{boats[1]}",

        f"{boats[1]}-{boats[3]}-{boats[0]}"

    ]

    return {

        "venue": venue,

        "順位評価": ranking,

        "本命": main[0],

        "中穴": middle[0],

        "穴": hole[0],

        "買い目15点":

            main + middle + hole

    }
