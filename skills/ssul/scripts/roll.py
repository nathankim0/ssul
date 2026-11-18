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

# Settings passed to roughen.py. Only rough pools have them.
ROUGH_DIMENSIONS = {
    "spacing": {"loose": 65, "standard": 35},
    "spelling": {"habitual": 45, "standard": 55},
    "periods": {"all": 40, "some": 35, "none": 25},
    "lines": {"per_sentence": 40, "block": 30, "gappy": 30},
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
    # measured from 10 popular board posts
    "farm": {
        "shape": {"ask": 35, "log": 20, "caption": 15, "show": 15, "essay": 8, "notice": 7},
        "register": {"hapnida": 55, "hapnida_haeyo": 35, "haeyo_plain": 10},
        "laugh": {"none": 80, "ㅎㅎ": 15, "^^": 5},
        "ellipsis": {"none": 75, "...": 15, "..": 10},
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
SEASON_BY_MONTH = {
    1: ["winter"], 2: ["winter", "spring"], 3: ["spring"], 4: ["spring"], 5: ["spring", "summer"],
    6: ["summer"], 7: ["summer"], 8: ["summer", "autumn"], 9: ["autumn"], 10: ["autumn"],
    11: ["autumn", "winter"], 12: ["winter"],
}


def pick(rng, weights):
    keys = list(weights)
    return rng.choices(keys, weights=[weights[k] for k in keys], k=1)[0]


def roll_one(rng, pool):
    roll = {name: pick(rng, weights) for name, weights in pool.items()}
    shape = roll.get("shape")
    if shape == "caption":
        roll["length"] = "oneline"
    elif shape == "essay":
        roll["length"] = "essay"
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
        for roll, topic in zip(rolls, rng.sample(topics, k=min(n, len(topics)))):
            roll["topic_seed"] = topic

    # In a batch of 3 or more, at least one post has no laugh at all.
    if len(rolls) >= 3 and all(r["laugh"] != "none" for r in rolls):
        rng.choice(rolls)["laugh"] = "none"
    for roll in rolls:
        print(json.dumps(roll, ensure_ascii=False))


if __name__ == "__main__":
    main()
