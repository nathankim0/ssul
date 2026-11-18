# Variation

Real accounts do not sound identical every time. Some posts have ㅋㅋ, some do not; some are 반말 talk, some are 해요체; some end on a question, some just stop. A model picking "randomly" in its head drifts to the same choices, so ssul rolls with a real random number generator.

## Roll

Run once per request, with `--n` equal to the number of posts:

```bash
python3 -I "<skill base directory>/scripts/roll.py" --n <posts> --pool <sns|warm|plain>
```

- `sns`: AI, dev, startup, investing, hot takes, and when the voice source is a pasted SNS feed
- `warm`: 2030 daily life, parenting, food
- `plain`: the `farmer` and `midlife` personas (`personas.md`): farmers and readers in their 40s and up

Each line is one post's settings, for example:

```json
{"register": "banmal_talk", "laugh": "ㅋㅋ", "ellipsis": "..", "length": "short", "opener": "reaction", "ending": "question", "flow": "turn", "endings": "mixed"}
```

## What each value means

| Setting | Values |
|---|---|
| register | `banmal_monologue` (~함, ~임, ~네, ~듯), `banmal_talk` (~야, ~어??, ~더라, ~대), `haeyo` (~요, ~거든요, ~더라고요); `plain` pool: `haeyo_plain` (~했어요, ~네요, ~같아요, few 거든요 or 더라고요), `haeyo_hapnida` (해요체 lines with 합니다 or 습니다 lines in the same post), `diary` (~했다, ~했음, a log to yourself) |
| laugh | `none` (about half of all rolls), `ㅋ`, `ㅋㅋ`, `ㅋㅋㅋ`, `ㅎㅎ`, `^^` (`plain` only): use it 0 to 2 times in the post, where something is actually funny, awkward, or friendly |
| ellipsis | `none`, `..`, `...`, `~~` (`plain` only): trailing-off marks, 0 to 3 times |
| length | `short` (2 to 4 lines), `medium` (5 to 8), `long` (9 to 12, still under 500 characters) |
| opener | `straight` (start with the content), `reaction` (아니, 하.., 와, 진짜; `plain`: 아이고, 휴..), `weather` (`plain` only: the weather or the day, as farmers start), `address` (follower or board address, only if the address option is on; otherwise treat as `straight`) |
| ending | `question` (a real one), `reaction` (아니 이게 맞냐고, 흑흑; ㅋㅋㅋ only when laugh is not `none`), `stop` (the last fact, no wrap-up), `wish` (`plain` only: 비 좀 왔으면 좋겠네요), `greeting` (`plain` only: 다들 수고하셨어요, 감기 조심하세요) |
| flow | `turn` (hook, beats joined by 근데 or 그래서, a last line worth quoting), `log` (things in the order they happened, no turn, stops where it stops); the `plain` pool always rolls `log` |
| endings | `repeat` (a few endings, the same one may run 3 or more times in a row), `mixed` (endings vary where speech varies; never spread so each is used once) |

## What overrides the roll

In this order, a higher item wins over the roll for that setting only:

1. What the user asked for in this request ("해요체로", "ㅋㅋ 없이", "짧게").
2. The user's own voice profile (`~/.ssul/voice.md`): roll only within what the user actually does. If they never use ㅋㅋ, laugh is always `none`.
3. Tone fit: a serious post (scam, loss, health, apology, legal disclosure) drops `laugh` to `none`, and says so in the notes.
4. The address option (SKILL.md Step 2).

Pasted samples (SKILL.md Step 2) narrow the range the same way as a voice profile: if none of the samples uses ㅋㅋ, laugh is `none` or what they do use.

Everything else in ssul still applies: register rules per persona, the bans (no emoji unless the voice source uses them, no `·`, ①, →), real material only.

## Several posts at once

With `--n 5`, each post gets its own roll, so a batch never reads like one template. If two rolls come out identical, re-roll the second. In a batch of 3 or more, the script makes sure at least one post has no laugh at all.

When the roll says `laugh: none`, the post has no ㅋ, ㅋㅋ, ㅎㅎ, or 흑흑-style laugh at all, even where one would feel natural. Carry the tone with words instead.

## Notes line

Add the roll to the notes in one short line, e.g. `이번 롤: 반말 대화, ㅋㅋ, 짧게, 질문으로 끝, 순서대로, 어미 반복`. The user can say "다시 굴려" to re-roll the voice for the same content.
