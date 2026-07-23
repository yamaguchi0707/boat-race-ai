from venue import get_venue_score

def get_race_data():

    venue = "大村"

    race = {

        "venue": venue,

        "race_number": 1,

        "venue_data": get_venue_score(

            venue

        ),

        "weather": {

            "wind": 2,

            "direction": "向かい風",

            "temperature": 25

        },

        "players": [

            {

                "boat": 1,

                "name": "テスト選手A",

                "rank": "A1",

                "win_rate": 65,

                "second_rate": 48,

                "third_rate": 70,

                "st": 0.12,

                "motor_rate": 45,

                "exhibition_time": 6.70,

                "average_exhibition_time": 6.80

            },

            {

                "boat": 2,

                "name": "テスト選手B",

                "rank": "A2",

                "win_rate": 55,

                "second_rate": 40,

                "third_rate": 60,

                "st": 0.14,

                "motor_rate": 40,

                "exhibition_time": 6.78,

                "average_exhibition_time": 6.80

            },

            {

                "boat": 3,

                "name": "テスト選手C",

                "rank": "B1",

                "win_rate": 35,

                "second_rate": 25,

                "third_rate": 45,

                "st": 0.16,

                "motor_rate": 35,

                "exhibition_time": 6.82,

                "average_exhibition_time": 6.80

            },

            {

                "boat": 4,

                "name": "テスト選手D",

                "rank": "A2",

                "win_rate": 50,

                "second_rate": 38,

                "third_rate": 55,

                "st": 0.13,

                "motor_rate": 48,

                "exhibition_time": 6.72,

                "average_exhibition_time": 6.80

            },

            {

                "boat": 5,

                "name": "テスト選手E",

                "rank": "B1",

                "win_rate": 30,

                "second_rate": 20,

                "third_rate": 35,

                "st": 0.19,

                "motor_rate": 30,

                "exhibition_time": 6.88,

                "average_exhibition_time": 6.80

            },

            {

                "boat": 6,

                "name": "テスト選手F",

                "rank": "B1",

                "win_rate": 25,

                "second_rate": 18,

                "third_rate": 30,

                "st": 0.20,

                "motor_rate": 28,

                "exhibition_time": 6.90,

                "average_exhibition_time": 6.80

            }

        ]

    }

    return race
