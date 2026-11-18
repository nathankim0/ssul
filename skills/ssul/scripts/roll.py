#!/usr/bin/env python3
"""Roll random voice settings for ssul posts.

Usage:
  python3 roll.py                 # one roll, "sns" pool
  python3 roll.py --n 5           # five rolls, one per post
  python3 roll.py --pool warm     # 2030 daily life, parenting, food
  python3 roll.py --pool farm     # farmers on a farming board (farmer persona)
  python3 roll.py --pool plain    # 40s and up, daily life (midlife persona)
  python3 roll.py --pool farm --month 11   # topic seed for that month
  python3 roll.py --seed 42       # reproducible

Prints one line of JSON per roll. Standard library only.
"""
import argparse
import datetime
import json
import random

SNS_DIMENSIONS = {
    "laugh": {"none": 50, "ㅋ": 10, "ㅋㅋ": 20, "ㅋㅋㅋ": 12, "ㅎㅎ": 8},
    "ellipsis": {"none": 40, "..": 40, "...": 20},
    "length": {"short": 35, "medium": 45, "long": 20},
    "opener": {"straight": 40, "reaction": 25, "address": 35},
    "ending": {"question": 35, "reaction": 30, "stop": 35},
}

# How the post is typed. Only rough pools have them; the model writes them.
ROUGH_DIMENSIONS = {
    "spacing": {"loose": 50, "cramped": 20, "standard": 30},
    "spelling": {"habitual": 50, "standard": 50},
    "periods": {"all": 35, "some": 30, "none": 20, "arae": 10, "glued": 5},
    "lines": {"per_sentence": 30, "block": 20, "gappy": 25, "wrapped": 25},
}

POOLS = {
    # AI, dev, startup, investing, hot takes, pasted SNS feeds
    "sns": {
        "register": {"banmal_monologue": 40, "banmal_talk": 40, "haeyo": 20},
        **SNS_DIMENSIONS,
        "flow": {"turn": 60, "log": 40},
        "endings": {"mixed": 65, "repeat": 35},
    },
    # 2030 daily life, parenting, food
    "warm": {
        "register": {"haeyo": 60, "banmal_talk": 30, "banmal_monologue": 10},
        **SNS_DIMENSIONS,
        "flow": {"turn": 45, "log": 55},
        "endings": {"mixed": 55, "repeat": 45},
    },
    # farmers on a farming community board (farmer persona),
    # measured from 25 popular board posts
    "farm": {
        "shape": {"ask": 26, "log": 10, "memo": 8, "diary": 9, "caption": 7, "show": 10,
                  "share": 14, "warn": 6, "essay": 4, "notice": 6},
        "register": {"hapnida": 40, "haeyo_plain": 30, "hapnida_haeyo": 20, "switch": 10},
        "laugh": {"none": 70, "^^": 15, "ㅎㅎ": 12, "ㅋ": 3},
        "ellipsis": {"none": 55, "...": 10, "......": 10, "~~": 10, "..": 10, "~~~~": 5},
        "length": {"short": 50, "medium": 35, "long": 15},
        "opener": {"straight": 35, "greeting": 30, "intro": 20, "weather": 15},
        "ending": {"question": 35, "stop": 30, "wish": 20, "feeling": 15},
        "flow": {"log": 100},  # no added turn; essays wander on their own
        "endings": {"repeat": 65, "mixed": 35},
        **ROUGH_DIMENSIONS,
    },
    # readers in their 40s and up, daily life (midlife persona)
    "plain": {
        "register": {"haeyo_plain": 45, "haeyo_hapnida": 35, "diary": 20},
        "laugh": {"none": 55, "ㅎㅎ": 20, "^^": 15, "ㅋㅋ": 10},
        "ellipsis": {"none": 25, "..": 30, "...": 30, "~~": 15},
        "length": {"short": 35, "medium": 45, "long": 20},
        "opener": {"straight": 40, "weather": 25, "reaction": 15, "address": 20},
        "ending": {"stop": 35, "wish": 20, "question": 25, "greeting": 20},
        "flow": {"log": 100},
        "endings": {"repeat": 65, "mixed": 35},
        **ROUGH_DIMENSIONS,
    },
}

# Topic seeds for the farm pool, used only when the user gave no topic or a
# broad one ("11월 이야기"). Neighbouring seasons overlap on purpose.
FARM_TOPICS = {
    "spring": ["못자리", "고추 모종", "감자 심기", "과수 꽃 솎기", "봄 전정 마무리", "밭 갈기", "멀칭 비닐",
               "냉해", "벌 넣기", "모내기 준비", "봄나물", "육묘장 온도", "새 농기계", "퇴비 내기"],
    "summer": ["장마 배수로", "고추 탄저병", "폭염 하우스 환기", "참깨 베기", "풀베기", "벌초 전 약",
               "복숭아 출하", "옥수수 따기", "멧돼지 피해", "태풍 대비", "열과", "택배 포장", "예초기 수리"],
    "autumn": ["벼 수확", "들깨 털기", "고구마 캐기", "서리태 탈곡", "곶감 깎기", "김장 배추 결구",
               "무 수확", "사과 수확 시기", "마늘 양파 정식", "밤 줍기", "감 따기", "공판장 시세",
               "가을 퇴비", "첫서리", "통발 놓기", "꽃 사진"],
    "winter": ["하우스 비닐 보온", "배관 동파", "자연수 집수정", "과수 전정", "석회보르도액", "저장고 온도",
               "농한기 교육", "내년 비료 계획", "묘목 주문", "눈 피해", "메주 쑤기", "농기계 정비",
               "택배 판매", "겨울 딸기"],
}
# Share (좋은 글) posts are about life, not crops.
SHARE_TOPICS = ["이웃", "오랜 친구", "부부", "나이 듦", "만족", "감사", "기다림", "건강", "손주",
                "고향", "부모님", "말 한마디", "욕심", "가을 들녘", "겨울 준비", "새벽", "밥 한 그릇"]

SEASON_BY_MONTH = {
    1: ["winter"], 2: ["winter", "spring"], 3: ["spring"], 4: ["spring"], 5: ["spring", "summer"],
    6: ["summer"], 7: ["summer"], 8: ["summer", "autumn"], 9: ["autumn"], 10: ["autumn"],
    11: ["autumn", "winter"], 12: ["winter"],
}


def pick(rng, weights):
    keys = list(weights)
    return rng.choices(keys, weights=[weights[k] for k in keys], k=1)[0]


# Some farm shapes come with their own register, length, and marks.
SHAPE_RULES = {
    "caption": {"length": "oneline", "deco": "none"},
    "essay": {"length": "essay"},
    "memo": {"register": "memo", "length": "short", "opener": "straight", "ending": "stop", "laugh": "none",
             "deco": "none"},
    "diary": {"register": "haera_diary", "opener": "straight", "ending": {"stop": 60, "wish": 40}},
    "share": {"register": {"hapnida": 50, "haera_poem": 30, "hage_letter": 20},
              "length": {"long": 50, "essay": 50}, "ending": "wish",
              "deco": {"heavy": 45, "light": 40, "none": 15}},
    "warn": {"ending": "wish"},
}


def roll_one(rng, pool):
    roll = {name: pick(rng, weights) for name, weights in pool.items()}
    for key, value in SHAPE_RULES.get(roll.get("shape"), {}).items():
        roll[key] = pick(rng, value) if isinstance(value, dict) else value
    if "shape" in roll and "deco" not in roll:
        roll["deco"] = pick(rng, {"none": 70, "light": 25, "heavy": 5})
    return roll


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--pool", choices=sorted(POOLS), default="sns")
    parser.add_argument("--month", type=int, choices=range(1, 13))
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    pool = POOLS[args.pool]
    n = max(1, args.n)
    rolls = []
    for _ in range(n):
        roll = roll_one(rng, pool)
        tries = 0
        # No identical rolls. In a farm batch, avoid repeating a shape while
        # unused shapes remain.
        while roll in rolls or (
            "shape" in roll and tries < 50 and len(rolls) < len(pool["shape"])
            and roll["shape"] in {r["shape"] for r in rolls}
        ):
            roll = roll_one(rng, pool)
            tries += 1
        rolls.append(roll)

    if args.pool == "farm":
        month = args.month or datetime.date.today().month
        topics = sorted({t for s in SEASON_BY_MONTH[month] for t in FARM_TOPICS[s]})
        farm_seeds = iter(rng.sample(topics, k=min(n, len(topics))))
        share_seeds = iter(rng.sample(SHARE_TOPICS, k=min(n, len(SHARE_TOPICS))))
        for roll in rolls:
            roll["topic_seed"] = next(share_seeds if roll["shape"] == "share" else farm_seeds, None)

    # In a batch of 3 or more, at least one post has no laugh at all.
    if len(rolls) >= 3 and all(r["laugh"] != "none" for r in rolls):
        rng.choice(rolls)["laugh"] = "none"
    for roll in rolls:
        print(json.dumps(roll, ensure_ascii=False))


if __name__ == "__main__":
    main()
