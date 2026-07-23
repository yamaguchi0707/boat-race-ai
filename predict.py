def calculate_score(player):

    score = 50

    # 級別評価

    if player["rank"] == "A1":

        score += 25

    elif player["rank"] == "A2":

        score += 15

    elif player["rank"] == "B1":

        score += 5

    # 1着率評価

    score += player.get("win_rate", 0) * 0.3

    # ST評価（早いほど加点）

    if player.get("st", 0) <= 0.15:

        score += 10

    return score

def make_prediction():

    players = [

        {"boat":1, "rank":"A1", "win_rate":60, "st":0.12},

        {"boat":2, "rank":"A2", "win_rate":45, "st":0.15},

        {"boat":3, "rank":"B1", "win_rate":35, "st":0.18},

        {"boat":4, "rank":"A2", "win_rate":42, "st":0.14},

        {"boat":5, "rank":"B1", "win_rate":30, "st":0.19},

        {"boat":6, "rank":"B1", "win_rate":25, "st":0.20}

    ]

    results = []

    for player in players:

        score = calculate_score(player)

        results.append({

            "boat": player["boat"],

            "score": score

        })

    results.sort(

        key=lambda x: x["score"],

        reverse=True

    )

    return {

        "順位評価": results,

        "本命": "1-2-3",

        "中穴": "1-4-2",

        "穴": "4-1-5"

    }
