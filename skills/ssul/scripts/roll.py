#!/usr/bin/env python3
"""Roll random voice settings for ssul posts.

Usage:
  python3 roll.py                 # one roll, "sns" pool
  python3 roll.py --n 5           # five rolls, one per post
  python3 roll.py --pool warm     # 2030 daily life, parenting, food
  python3 roll.py --pool plain    # farmers, 40s and up (farmer, midlife personas)
  python3 roll.py --seed 42       # reproducible

Prints one line of JSON per roll. Standard library only.
"""
import argparse
import json
import random

SNS_DIMENSIONS = {
    "laugh": {"none": 50, "ㅋ": 10, "ㅋㅋ": 20, "ㅋㅋㅋ": 12, "ㅎㅎ": 8},
    "ellipsis": {"none": 40, "..": 40, "...": 20},
    "length": {"short": 35, "medium": 45, "long": 20},
    "opener": {"straight": 40, "reaction": 25, "address": 35},
    "ending": {"question": 35, "reaction": 30, "stop": 35},
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
    # farmers and readers in their 40s and up (farmer, midlife personas)
    "plain": {
        "register": {"haeyo_plain": 45, "haeyo_hapnida": 35, "diary": 20},
        "laugh": {"none": 55, "ㅎㅎ": 20, "^^": 15, "ㅋㅋ": 10},
        "ellipsis": {"none": 25, "..": 30, "...": 30, "~~": 15},
        "length": {"short": 35, "medium": 45, "long": 20},
        "opener": {"straight": 40, "weather": 25, "reaction": 15, "address": 20},
        "ending": {"stop": 35, "wish": 20, "question": 25, "greeting": 20},
        "flow": {"log": 100},  # farmer and midlife posts never add a turn
        "endings": {"repeat": 65, "mixed": 35},
    },
}


def pick(rng, weights):
    keys = list(weights)
    return rng.choices(keys, weights=[weights[k] for k in keys], k=1)[0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1)
    parser.add_argument("--pool", choices=sorted(POOLS), default="sns")
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    pool = POOLS[args.pool]
    rolls = []
    for _ in range(max(1, args.n)):
        roll = {name: pick(rng, weights) for name, weights in pool.items()}
        while roll in rolls:
            roll = {name: pick(rng, weights) for name, weights in pool.items()}
        rolls.append(roll)
    # In a batch of 3 or more, at least one post has no laugh at all.
    if len(rolls) >= 3 and all(r["laugh"] != "none" for r in rolls):
        rng.choice(rolls)["laugh"] = "none"
    for roll in rolls:
        print(json.dumps(roll, ensure_ascii=False))


if __name__ == "__main__":
    main()
