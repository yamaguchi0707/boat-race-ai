def generate_buy(results):

    boats = []

    for item in results:

        boats.append(

            item["boat"]

        )

    tickets = []

    # 本命軸

    first = boats[0]

    for second in boats[1:]:

        for third in boats[1:]:

            if (

                first != second

                and first != third

                and second != third

            ):

                tickets.append(

                    f"{first}-{second}-{third}"

                )

    # 最大15点

    return tickets[:15]

def classify_buy(tickets):

    return {

        "買い目": tickets,

        "点数": len(tickets)

    }
