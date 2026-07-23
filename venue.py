def get_venue_score(venue):

    venue_data = {

        "桐生": {

            "inside_strength": 10,

            "water_type": "淡水",

            "rough_level": "中"

        },

        "戸田": {

            "inside_strength": 5,

            "water_type": "淡水",

            "rough_level": "高"

        },

        "江戸川": {

            "inside_strength": 3,

            "water_type": "海水",

            "rough_level": "高"

        },

        "平和島": {

            "inside_strength": 8,

            "water_type": "海水",

            "rough_level": "中"

        },

        "多摩川": {

            "inside_strength": 12,

            "water_type": "淡水",

            "rough_level": "低"

        },

        "浜名湖": {

            "inside_strength": 10,

            "water_type": "汽水",

            "rough_level": "中"

        },

        "蒲郡": {

            "inside_strength": 12,

            "water_type": "汽水",

            "rough_level": "低"

        },

        "常滑": {

            "inside_strength": 10,

            "water_type": "海水",

            "rough_level": "中"

        },

        "津": {

            "inside_strength": 11,

            "water_type": "淡水",

            "rough_level": "低"

        },

        "三国": {

            "inside_strength": 10,

            "water_type": "海水",

            "rough_level": "中"

        },

        "びわこ": {

            "inside_strength": 9,

            "water_type": "淡水",

            "rough_level": "中"

        },

        "住之江": {

            "inside_strength": 12,

            "water_type": "淡水",

            "rough_level": "低"

        },

        "尼崎": {

            "inside_strength": 13,

            "water_type": "淡水",

            "rough_level": "低"

        },

        "鳴門": {

            "inside_strength": 5,

            "water_type": "海水",

            "rough_level": "高"

        },

        "丸亀": {

            "inside_strength": 11,

            "water_type": "海水",

            "rough_level": "低"

        },

        "児島": {

            "inside_strength": 10,

            "water_type": "海水",

            "rough_level": "中"

        },

        "宮島": {

            "inside_strength": 10,

            "water_type": "海水",

            "rough_level": "中"

        },

        "徳山": {

            "inside_strength": 14,

            "water_type": "海水",

            "rough_level": "低"

        },

        "下関": {

            "inside_strength": 13,

            "water_type": "海水",

            "rough_level": "低"

        },

        "若松": {

            "inside_strength": 9,

            "water_type": "海水",

            "rough_level": "高"

        },

        "芦屋": {

            "inside_strength": 14,

            "water_type": "淡水",

            "rough_level": "低"

        },

        "福岡": {

            "inside_strength": 6,

            "water_type": "汽水",

            "rough_level": "高"

        },

        "唐津": {

            "inside_strength": 10,

            "water_type": "淡水",

            "rough_level": "中"

        },

        "大村": {

            "inside_strength": 15,

            "water_type": "海水",

            "rough_level": "低"

        }

    }

    return venue_data.get(

        venue,

        {

            "inside_strength": 10,

            "water_type": "不明",

            "rough_level": "中"

        }

    )
