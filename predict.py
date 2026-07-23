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

def calculate_score(player):

    score = 50

    # 級別評価

    if player["rank"] == "A1":

        score += 25

    elif player["rank"] == "A2":

        score += 15

    elif player["rank"] == "B1":

        score += 5

    # 成績評価

    score += player.get("win_rate", 0) * 0.3

    score += player.get("second_rate", 0) * 0.15

    score += player.get("third_rate", 0) * 0.1

    # ST評価

    st = player.get("st", 0)

    if 0 < st <= 0.15:

        score += 10

    elif st <= 0.18:

        score += 5

    # モーター評価

    score += player.get("motor_rate", 0) * 0.2

    # コース補正追加

    score += course_bonus(player["boat"])

    return score

def make_prediction():

    race = get_race_data()

    results = []

    for player in race["players"]:

        score = calculate_score(player)

        results.append({

            "boat": player["boat"],

            "name": player["name"],

            "score": round(score,1)

        })

    results.sort(

        key=lambda x:x["score"],

        reverse=True

    )

    return {

        "venue": race["venue"],

        "順位評価": results,

        "本命":

        f"{results[0]['boat']}-{results[1]['boat']}-{results[2]['boat']}",

        "中穴":

        f"{results[0]['boat']}-{results[2]['boat']}-{results[1]['boat']}",

        "穴":

        f"{results[3]['boat']}-{results[0]['boat']}-{results[1]['boat']}"

    }
