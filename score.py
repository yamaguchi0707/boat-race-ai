from motor import motor_score

from exhibition import exhibition_score

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

    score += motor_score(

        player.get("motor_rate", 0)

    )

    # 展示タイム評価

    score += exhibition_score(

        player.get("exhibition_time", 0),

        player.get("average_exhibition_time", 0)

    )

    return score
