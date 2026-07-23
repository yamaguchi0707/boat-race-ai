from data import get_race_data

def course_bonus(boat):

    bonus = {

        1: 15,

        2: 8,

        3: 6,

        4: 10,

        5: 3,

        6: 0

    }

    return bonus.get(boat, 0)

def venue_bonus(boat, venue_data):

    bonus = 0

    inside_strength = venue_data.get("inside_strength", 0)

    # インが強い場は1号艇を加点

    if boat == 1:

        bonus += inside_strength

    return bonus

def calculate_score(player, venue_data):

    score = 50

    # 級別評価

    if player["rank"] == "A1":

        score += 25

    elif player["rank"] == "A2":

        score += 15

    elif player["rank"] == "B1":

        score += 5

    # 勝率

    score += player.get("win_rate", 0) * 0.3

    # 2連率

    score += player.get("second_rate", 0) * 0.15

    # 3連率

    score += player.get("third_rate", 0) * 0.1

    # ST

    st = player.get("st", 0)

    if 0 < st <= 0.15:

        score += 10

    elif st <= 0.18:

        score += 5

    # モーター

    score += player.get("motor_rate", 0) * 0.2

    # コース補正

    score += course_bonus(player["boat"])

    # 場補正

    score += venue_bonus(player["boat"], venue_data)

    return score

def make_prediction():

    race = get_race_data()

    venue_data = race["venue_data"]

    results = []

    for player in race["players"]:

        score = calculate_score(player, venue_data)

        results.append({

            "boat": player["boat"],

            "name": player["name"],

            "score": round(score, 1)

        })

    results.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return {

        "venue": race["venue"],

        "順位評価": results,

        "本命": f"{results[0]['boat']}-{results[1]['boat']}-{results[2]['boat']}",

        "中穴": f"{results[0]['boat']}-{results[2]['boat']}-{results[1]['boat']}",

        "穴": f"{results[3]['boat']}-{results[0]['boat']}-{results[1]['boat']}"

    }
