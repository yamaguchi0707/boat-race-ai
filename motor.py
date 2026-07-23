def motor_score(motor_rate):

    score = 0

    # モーター2連率評価

    if motor_rate >= 45:

        score += 15

    elif motor_rate >= 40:

        score += 10

    elif motor_rate >= 35:

        score += 5

    else:

        score -= 5

    return score

def motor_comment(motor_rate):

    if motor_rate >= 45:

        return "強力モーター"

    elif motor_rate >= 40:

        return "好調モーター"

    elif motor_rate >= 35:

        return "普通"

    else:

        return "低調"
