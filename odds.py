def odds_score(odds):

    score = 0

    # 高配当評価

    if odds >= 100:

        score += 15

    elif odds >= 50:

        score += 10

    elif odds >= 20:

        score += 5

    # 人気過剰

    elif odds < 5:

        score -= 5

    return score

def odds_comment(odds):

    if odds >= 100:

        return "高配当期待"

    elif odds >= 50:

        return "中穴配当"

    elif odds < 5:

        return "人気過剰"

    else:

        return "適正オッズ"
