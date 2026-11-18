#!/usr/bin/env python3
"""Roughen a finished post the way real posts on farming and older-reader
boards are rough: loose spacing, habitual spellings, uneven periods and line
breaks. The model tidies text by reflex; this does it with a real random
generator instead.

Usage:
  python3 roughen.py --roll '<one JSON line from roll.py>' < post.txt
  python3 roughen.py --spacing loose --spelling habitual --periods some --lines gappy < post.txt

Reads the post on stdin, prints the roughened post on stdout. Stock phrases
the model overuses are listed on stderr as "stock: ..." so they can be
rewritten. Never changes numbers, names, or negation. Standard library only.
"""
import argparse
import json
import random
import re
import sys

HANGUL_BASE = 0xAC00
JONG_RIEUL = 8

# Phrases the model reaches for in farm posts. Flagged, not changed.
STOCK = [
    r"허리", r"뻐근", r"다행입니다", r"다행이네요", r"다행이에요", r"마음이 (?:좀 )?편",
    r"한 ?해 농사", r"걱정했는데", r"이제야", r"제법", r"하루가 다 갔", r"뿌듯", r"보람",
    r"정성", r"땀방울", r"결실", r"속이 시원", r"감사한 마음",
]

# Common nonstandard spellings in real posts by older writers: (standard, habitual).
HABITUAL = [
    ("오랫동안", "오래동안"), ("간식거리", "간식꺼리"), ("먹을거리", "먹을꺼리"), ("금세", "금새"),
    ("웬만", "왠만"), ("희한", "희안"), ("며칠", "몇일"), ("일부러", "일부로"), ("설거지", "설겆이"),
    ("궁금", "궁굼"), ("돼요", "되요"), ("됐", "됬"), ("깎", "깍"), ("할게요", "할께요"),
    ("볼게요", "볼께요"), ("드릴게요", "드릴께요"), ("하고요", "하구요"), ("있고요", "있구요"),
    ("있습니다", "있읍니다"), ("없습니다", "없읍니다"), ("어떡", "어떻"), ("안 돼", "안되"),
    ("그런지", "그런지?"), ("얼마나", "얼만큼"),
]

NOUN_HADA = "작업|수확|정식|청소|살포|탈곡|준비|설치|주문|판매|시작|마무리|정리|건조|보관|확인|생각|걱정|파종|방제|전정|선별|출하"
UNITS = "m|cm|kg|g|도|평|그루|주|상자|박스|개|포기|접|마지기|동|일|시|년|살|번|말|가마"
AUX = "보|봤|봐|본|볼|주|줬|줘|준|줄|놓|놨|놔|두|둬|뒀|버리|버렸|드리|드렸|드릴"


def jong(ch):
    code = ord(ch) - HANGUL_BASE
    return code % 28 if 0 <= code < 11172 else -1


def add_rieul(ch):
    return chr(ord(ch) + JONG_RIEUL)


def maybe(rng, p):
    return rng.random() < p


def sub_random(rng, pattern, repl, text, p):
    return re.sub(pattern, lambda m: m.expand(repl) if maybe(rng, p) else m.group(0), text)


def loosen_spacing(rng, text):
    # 약 600m -> 약600m, 영하 2도 -> 영하2도
    text = sub_random(rng, r"(약|영하|영상|대략|총) (\d)", r"\1\2", text, 0.85)
    # 콩 농사 -> 콩농사, 하고 있습니다 -> 하고있습니다
    text = sub_random(rng, r"([가-힣]) (농사|농가|작업|수확)(?=[가-힣 ])", r"\1\2", text, 0.6)
    text = sub_random(rng, r"고 있(습니다|어요|는)", r"고있\1", text, 0.3)
    # 600 m -> 600m
    text = sub_random(rng, rf"(\d) ({UNITS})(?![가-힣])", r"\1\2", text, 0.9)
    # 35도 정도 <-> 35도정도, 3도까지 -> 3도 까지
    text = sub_random(rng, rf"(\d(?:{UNITS})) (정도|쯤|가량|씩)", r"\1\2", text, 0.5)
    text = sub_random(rng, rf"(\d(?:{UNITS}))(까지|부터)", r"\1 \2", text, 0.35)
    # 해 보았습니다 -> 해보았습니다
    text = sub_random(rng, rf"([아어해와워여]) ({AUX})", r"\1\2", text, 0.7)
    # 할 수 있 -> 할수 있
    text = re.sub(r"([가-힣]) 수 (있|없)",
                  lambda m: f"{m.group(1)}수 {m.group(2)}" if jong(m.group(1)) == JONG_RIEUL and maybe(rng, 0.45) else m.group(0),
                  text)
    # 것 같 -> 것같
    text = sub_random(rng, r"것 같", "것같", text, 0.25)
    # 농사 중입니다 -> 농사중입니다
    text = sub_random(rng, r"([가-힣]{2}) 중(입니다|이에요|이라|인데|에)", r"\1중\2", text, 0.7)
    # 작업했습니다 -> 작업 했습니다
    text = sub_random(rng, rf"({NOUN_HADA})(했|합니다|하고|해서|하려)", r"\1 \2", text, 0.25)
    # 다 못했는데 -> 다못했는데
    text = sub_random(rng, r"(다|안|못) (못|했|해|됐)", r"\1\2", text, 0.35)
    # one particle split off its noun, as in 저희집 에서
    if maybe(rng, 0.4):
        spots = list(re.finditer(r"([가-힣]{2})(에서|으로|까지)(?= )", text))
        if spots:
            m = rng.choice(spots)
            text = text[:m.start()] + m.group(1) + " " + m.group(2) + text[m.end():]
    return text


def habitual_spelling(rng, text):
    budget = rng.randint(1, 3)
    # 하려면 -> 할려면, 보려고 -> 볼려고
    def rieul(m):
        nonlocal budget
        ch = m.group(1)
        if budget > 0 and jong(ch) == 0 and maybe(rng, 0.6):
            budget -= 1
            return add_rieul(ch) + "려" + m.group(2)
        return m.group(0)
    text = re.sub(r"([가-힣])려(면|고|구)", rieul, text)
    pairs = HABITUAL[:]
    rng.shuffle(pairs)
    for standard, habitual in pairs:
        if budget <= 0:
            break
        if standard in text and maybe(rng, 0.6):
            text = text.replace(standard, habitual, 1)
            budget -= 1
    return text


def split_sentences(line):
    parts = re.split(r"(?<=[.?!])\s+(?=[가-힣A-Za-z0-9\"'])", line.strip())
    return [p for p in parts if p]


def set_periods(rng, lines, mode):
    out = []
    for line in lines:
        s = line.rstrip()
        if not s:
            out.append(s)
            continue
        single_period = s.endswith(".") and not s.endswith("..")
        if mode == "none" and single_period:
            s = s[:-1]
        elif mode == "some" and single_period and maybe(rng, 0.5):
            s = s[:-1]
        elif mode == "all" and re.search(r"[가-힣]$", s) and re.search(r"(다|요|죠|네|까|오)$", s):
            s += "."
        out.append(s)
    return out


def set_lines(rng, text, mode, periods):
    paragraphs = [l for l in text.splitlines()]
    sentences = []
    for line in paragraphs:
        if not line.strip():
            continue
        sentences.extend(split_sentences(line))
    if mode == "block" and periods != "none":
        joined = []
        for s in sentences:
            if not re.search(r"[.?!~^ㅎ]$", s):
                s += "."
            joined.append(s)
        # Long posts split into 2 or 3 blocks, short ones stay one block.
        if len(joined) > 8:
            cut = sorted(rng.sample(range(2, len(joined) - 1), k=min(2, len(joined) - 3)))
            blocks, last = [], 0
            for c in cut:
                blocks.append(" ".join(joined[last:c]))
                last = c
            blocks.append(" ".join(joined[last:]))
            return "\n\n".join(blocks)
        return " ".join(joined)
    lines = sentences
    if mode == "gappy":
        out = []
        for i, s in enumerate(lines):
            out.append(s)
            if i < len(lines) - 1 and maybe(rng, 0.35):
                out.append("")
                if maybe(rng, 0.25):
                    out.append("")
        return "\n".join(out)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--roll", help="one JSON line from roll.py")
    parser.add_argument("--spacing", choices=["loose", "standard"])
    parser.add_argument("--spelling", choices=["habitual", "standard"])
    parser.add_argument("--periods", choices=["all", "some", "none"])
    parser.add_argument("--lines", choices=["per_sentence", "block", "gappy"])
    parser.add_argument("--seed", type=int)
    args = parser.parse_args()

    roll = json.loads(args.roll) if args.roll else {}
    spacing = args.spacing or roll.get("spacing", "standard")
    spelling = args.spelling or roll.get("spelling", "standard")
    periods = args.periods or roll.get("periods", "all")
    lines_mode = args.lines or roll.get("lines", "per_sentence")
    if lines_mode == "block" and periods == "none":
        lines_mode = "per_sentence"

    rng = random.Random(args.seed)
    text = sys.stdin.read().strip()

    for pattern in STOCK:
        for m in re.finditer(pattern, text):
            print(f"stock: {m.group(0)}", file=sys.stderr)

    if spacing == "loose":
        text = loosen_spacing(rng, text)
    if spelling == "habitual":
        text = habitual_spelling(rng, text)
    text = set_lines(rng, text, lines_mode, periods)
    text = "\n".join(set_periods(rng, text.split("\n"), periods)) if lines_mode != "block" else text
    print(text)


if __name__ == "__main__":
    main()
