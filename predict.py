from score import calculate_score

def course_bonus(boat):

    return {

        1: 20,

        2: 8,

        3: 10,

        4: 12,

        5: 5,

        6: 3

    }.get(boat, 0)

def water_bonus(player):

    bonus = 0

    wind = float(player.get("wind_speed", 0))

    wave = float(player.get("wave_height", 0))

    if wind >= 5 and player["boat"] >= 4:

        bonus += 8

    if wave >= 3 and player.get("rank") == "A1":

        bonus += 5

    return bonus

def make_prediction(players, venue="大村"):

    ranking = []

    for player in players:

        score = (

            calculate_score(player)

            + course_bonus(player["boat"])

            + water_bonus(player)

        )

        ranking.append({

            "boat": player["boat"],

            "score": round(score, 1)

        })

    ranking.sort(key=lambda x: x["score"], reverse=True)

    boats = [x["boat"] for x in ranking]

    candidates = [

        f"{boats[0]}-{boats[1]}-{boats[2]}",

        f"{boats[0]}-{boats[2]}-{boats[1]}",

        f"{boats[0]}-{boats[1]}-{boats[3]}",

        f"{boats[0]}-{boats[3]}-{boats[1]}",

        f"{boats[0]}-{boats[2]}-{boats[3]}",

        f"{boats[1]}-{boats[0]}-{boats[2]}",

        f"{boats[1]}-{boats[2]}-{boats[0]}",

        f"{boats[0]}-{boats[3]}-{boats[2]}",

        f"{boats[2]}-{boats[0]}-{boats[1]}",

        f"{boats[3]}-{boats[0]}-{boats[1]}",

        f"{boats[2]}-{boats[1]}-{boats[0]}",

        f"{boats[3]}-{boats[0]}-{boats[2]}",

        f"{boats[4]}-{boats[0]}-{boats[1]}",

        f"{boats[1]}-{boats[3]}-{boats[0]}",

        f"{boats[5]}-{boats[0]}-{boats[1]}"

    ]

    # 重複削除（順序を維持）

    buy_list = list(dict.fromkeys(candidates))

    # 15点に満たない場合は補完

    while len(buy_list) < 15:

        for a in boats:

            for b in boats:

                for c in boats:

                    if len({a, b, c}) == 3:

                        ticket = f"{a}-{b}-{c}"

                        if ticket not in buy_list:

                            buy_list.append(ticket)

                        if len(buy_list) >= 15:

                            break

                if len(buy_list) >= 15:

                    break

            if len(buy_list) >= 15:

                break

    buy_list = buy_list[:15]

    return {

        "venue": venue,

        "順位評価": ranking,

        "本命": buy_list[0],

        "中穴": buy_list[5],

        "穴": buy_list[10],

        "買い目15点": buy_list

    }
