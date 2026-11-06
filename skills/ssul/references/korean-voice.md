# Korean voice rules

## Register by niche

Use this only when the user gave no samples of their own posts and no feed samples.

| Niche | Default register | Endings | Feel |
|---|---|---|---|
| AI, dev, startup, investing, tech news, hot takes | **반말 혼잣말** | `~다`, `~함`, `~임`, `~네`, `~냐`, `~듯`, bare nouns | talking to yourself in public; attitude shows |
| daily life, parenting, food, travel, pets | **해요체 구어** | `~거든요`, `~더라고요`, `~잖아요`, `~죠`, `~네요` | telling a friend |
| brand or business accounts | **해요체 구어**, lighter on ㅋㅋ | same | friendly, not cute |

반말 혼잣말 example (two lines is a full post):

> 별 5천 개짜리 클로드 스킬 깔았더니 유료 API 키 내놓으래
> 스킬계에도 강의팔이 왔냐

## Spoken register (구어체)

Write it the way the user would actually say it, in the register chosen above.

Useful endings, mixed naturally:

| Ending | Job | Example |
|---|---|---|
| ~거든요 | reason, background | 바이럴 스킬을 깔았거든요 |
| ~더라고요 | what I saw or heard | 이러더라고요 |
| ~잖아요 | shared knowledge | 다들 알잖아요 |
| ~(라는) 거예요 | the surprise | 영하 2도라는 거예요 |
| ~죠 | light agreement, a beat | 헤드랜턴 켜고 나갔죠 |
| ~네요 | realization | 그게 제일 어렵네요 |
| noun stop | punch | 오늘 아침 1도. |

Spoken connectors: 근데, 그래서, 그러니까, 아니, 결국, 막상. Report connectors are banned in posts: 따라서, 그러나, 또한, 나아가, 종합하면, 결론적으로.

Report words to replace: 부각 -> 눈에 띄다, 안착 -> 자리 잡다, 소진 -> 다 떨어지다, 분기점 -> 갈림길, 괴리 -> 차이, 촉발 -> 시작되다, 진행하다 -> just the verb, 공유드리다 -> 보내다 / 말하다.

Do not stack the same ending 4 times in a row. Do not vary endings just to vary them.

## Korean AI tells

Fix every hit. Severity: **S1** always fix, **S2** fix unless it is the user's own voice, **S3** check.

| Sev | Tell | Example | Fix |
|---|---|---|---|
| S1 | Invented specifics | a number, quote, or scene nobody gave you | real material or `[brackets]` |
| S1 | Lesson ending | "결국 중요한 건 ~라는 걸 깨달았다" | end on the scene or the quote |
| S1 | Aphorism ending | "농사는 하늘이 짓고 걱정은 사람이 짓는다" | cut it, or replace with what someone actually said |
| S1 | Hollow reversal | "이건 단순한 툴이 아닙니다. 방식의 변화입니다" | state the concrete change |
| S1 | Chatbot residue | "좋은 질문입니다", "도움이 되셨길 바랍니다" | delete |
| S2 | Rule of three | 무 뽑고 / 배추 묶고 / 고추 따고, three by reflex | keep the real count; often one vivid action is enough |
| S2 | 명사화 | 검토를 진행한 후 공유드리겠습니다 | 검토하고 보낼게요 |
| S2 | 번역투 | 당신, ~하는 것은 중요합니다, ~에 있어서 | rewrite as speech |
| S2 | Stacked adjectives | 빠르고 신속하며 효율적인 | one fact instead |
| S2 | Significance words | 핵심적인, 혁신적인, 게임체인저 | delete or replace with the fact |
| S2 | Middle dot `·` between words | 기획·개발·운영, 중·하순 | a comma, 와/랑, or spell it out (중순에서 하순) |
| S2 | Circled numbers | ①②③ | `1.` `2.` `3.` or no numbering |
| S2 | Unicode arrows | → ⇒ ➡ | `->`, or words (그래서, 다음에) |
| S2 | Emoji | ✅ 🔥 👉 📌 | none |
| S3 | Em dash, en dash | — | period or comma |
| S3 | Curly quotes or single quotes for emphasis | '진짜' | remove the quotes |
| S3 | Bold, headers, bullets in a casual post | | plain lines |
| S3 | 음슴체 in a 해요체 post | ~함, ~됨 | match the post's register |

No single word proves AI authorship. These are edit points, not a detector score.

## Slang

Use trending slang only if the user's own posts use it, only in draft mode, and only if it is current. When unsure, plain speech wins.
