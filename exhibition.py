def exhibition_score(exhibition_time, average_time):

    score = 0

    # 平均より速いほど評価

    diff = average_time - exhibition_time

    if diff >= 0.10:

        score += 10

    elif diff >= 0.05:

        score += 5

    elif diff <= -0.05:

        score -= 5

    return score

def exhibition_comment(exhibition_time, average_time):

    diff = average_time - exhibition_time

    if diff >= 0.10:

        return "展示気配◎"

    elif diff >= 0.05:

        return "展示上位"

    elif diff <= -0.05:

        return "展示劣勢"

    else:

        return "展示普通"
