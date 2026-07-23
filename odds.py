def odds_score(odds):

    score = 0

    # 高配当は少しだけ評価

    if odds >= 100:

        score += 6

    elif odds >= 50:

        score += 4

    elif odds >= 20:

        score += 2

    # 人気過剰を軽く減点

    elif odds < 5:

        score -= 2

    return score

def odds_comment(odds):

    if odds >= 100:

        return "高配当穴候補"

    elif odds >= 50:

        return "中穴候補"

    elif odds < 5:

        return "人気集中"

    else:

        return "適正オッズ"
