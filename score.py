def calculate_score(player):

    score = 50

    if player["rank"] == "A1":

        score += 25

    elif player["rank"] == "A2":

        score += 15

    elif player["rank"] == "B1":

        score += 5

    score += player.get("win_rate", 0) * 0.3

    score += player.get("second_rate", 0) * 0.15

    score += player.get("third_rate", 0) * 0.1

    st = player.get("st", 0)

    if 0 < st <= 0.15:

        score += 10

    elif st <= 0.18:

        score += 5

    score += player.get("motor_rate", 0) * 0.2

    return score
