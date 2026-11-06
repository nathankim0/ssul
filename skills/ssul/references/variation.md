# Variation

Real accounts do not sound identical every time. Some posts have ㅋㅋ, some do not; some are 반말 talk, some are 해요체; some end on a question, some just stop. A model picking "randomly" in its head drifts to the same choices, so ssul rolls with a real random number generator.

## Roll

Run once per request, with `--n` equal to the number of posts:

```bash
python3 -I "<skill base directory>/scripts/roll.py" --n <posts> --pool <sns|warm>
```

- `sns`: AI, dev, startup, investing, hot takes, and when the voice source is a pasted SNS feed
- `warm`: daily life, farming, parenting, food

Each line is one post's settings, for example:

```json
{"register": "banmal_talk", "laugh": "ㅋㅋ", "ellipsis": "..", "length": "short", "opener": "reaction", "ending": "question"}
```

## What each value means

| Setting | Values |
|---|---|
| register | `banmal_monologue` (~함, ~임, ~네, ~듯), `banmal_talk` (~야, ~어??, ~더라, ~대), `haeyo` (~요, ~거든요, ~더라고요) |
| laugh | `none`, `ㅋ`, `ㅋㅋ`, `ㅋㅋㅋ`, `ㅎㅎ`: use it 0 to 2 times in the post, where something is actually funny or awkward |
| ellipsis | `none`, `..`, `...`: trailing-off marks, 0 to 3 times |
| length | `short` (2 to 4 lines), `medium` (5 to 8), `long` (9 to 12, still under 500 characters) |
| opener | `straight` (start with the content), `reaction` (아니, 하.., 와, 진짜), `address` (follower address, only if the address option is on; otherwise treat as `straight`) |
| ending | `question` (a real one), `reaction` (ㅋㅋㅋ, 아니 이게 맞냐고, 흑흑), `stop` (the last fact, no wrap-up) |

## What overrides the roll

In this order, a higher item wins over the roll for that setting only:

1. What the user asked for in this request ("해요체로", "ㅋㅋ 없이", "짧게").
2. The user's own voice profile (`~/.ssul/voice.md`): roll only within what the user actually does. If they never use ㅋㅋ, laugh is always `none`.
3. Tone fit: a serious post (scam, loss, health, apology, legal disclosure) drops `laugh` to `none`, and says so in the notes.
4. The address option (SKILL.md Step 2).

Everything else in ssul still applies: one register per post, the bans (no emoji, `·`, ①, →), real material only.

## Several posts at once

With `--n 5`, each post gets its own roll, so a batch never reads like one template. If two rolls come out identical, re-roll the second.

## Notes line

Add the roll to the notes in one short line, e.g. `이번 롤: 반말 대화, ㅋㅋ, 짧게, 질문으로 끝`. The user can say "다시 굴려" to re-roll the voice for the same content.
