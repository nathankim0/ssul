# Korean voice rules

## Register by niche

Use this only when the user gave no samples of their own posts and no feed samples. Samples always win. The persona (`personas.md`) decides which rows apply.

| Niche | Default register | Endings | Feel |
|---|---|---|---|
| AI, dev, startup, investing, tech news, hot takes | **반말 혼잣말** | `~다`, `~함`, `~임`, `~네`, `~냐`, `~듯`, bare nouns | talking to yourself in public; attitude shows |
| daily life, parenting, food, travel, pets | **해요체 구어** | `~거든요`, `~더라고요`, `~잖아요`, `~죠`, `~네요` | telling a friend |
| brand or business accounts | **해요체 구어**, lighter on ㅋㅋ | same | friendly, not cute |
| farming, rural life, farming communities (`farmer`) | **합니다체**, ~네요 or 해요체 lines mixed in | `~했습니다`, `~입니다`, `~궁금합니다`, `~부탁드립니다`, `~바랍니다`, `~네요`, repeated | writing to other farmers; practical, asking, often with a photo |
| 40s and up, daily life (`midlife`) | 합니다체 and plain 해요체 | `~했습니다`, `~했어요`, `~네요` | a plain account, greetings allowed |

반말 혼잣말 example (two lines is a full post):

> 별 5천 개짜리 클로드 스킬 깔았더니 유료 API 키 내놓으래
> 스킬계에도 강의팔이 왔냐

## Spoken register (구어체)

Write it the way the user would actually say it, in the register chosen above.

The table below is the `sns` persona's 해요체: smooth, young, conversational. For `farmer` and `midlife`, ~거든요, ~더라고요, ~잖아요 are rare; use the plain endings in the niche table above, or what the samples use.

Useful endings for `sns`, mixed naturally:

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

Endings follow the voice source and the roll's `endings` setting. Real posts repeat endings (했어요 / 했어요 / 했네요); that is not a flaw. Do not vary endings just to vary them: endings spread so that each one appears once is an AI tell. Only the `sns` persona with `endings: mixed` treats 4 or more identical endings in a row as a drone to fix.

## Human texture (사람 냄새)

Posts that feel human in the Korean feed are not tight. Over-crafted structure (a hook, a neat contrast, a punchline, nothing out of place) is itself an AI tell. Leave texture in.

| Texture | Looks like |
|---|---|
| Talk to followers | 스친이들, 다들, 여러분은 어떻게 해? Use it in any shape, jokes included, whenever the voice source does it; it is a speech habit, not only a way to ask |
| Things in the order they happened | 30분 전에 메일이 온 거야 / 근데 들어가 보니까 진짜 안 되더라고?? / 카드정보 넣고 나니까 정신이 차려져서 |
| Thinking out loud | `..`, `??`, 하.., 근데, 아 그리고, 물론 내 생각임. 근데 보통 맞음 |
| Feelings in plain words | 대가리 터질 것 같다, 돈이 살살 녹겠네, 흑흑 |
| Real asks | 이거 어떻게 해야 돼?, 다들 어디에 홍보해?? |
| Uneven shape | run-on lines, a list of 2 or 4, no twist, no punchline, an ending that just stops |

Rules:

- When the voice source addresses followers and the address option is on (see Follower address), keep doing it in every shape: Scene, Hot take, 병맛 jokes, Finding.
- Humor posts (병맛) can end on a real question or a plain reaction (ㅋㅋㅋ, 아니 이게 맞냐고) instead of a crafted punchline.
- Not every post needs a hook formula or a last-line punch. Scene, Confession, and Question posts can simply tell what happened and ask.
- Use texture the user's material supports. Do not fake feelings the user did not express.
- Never inject random typos. Keep the user's own typos and spacing when polishing unless they ask for proofreading. The one exception is the `farm` and `plain` pools: when the roll says so, write with the loose spacing and a few habitual spellings real older writers use (할려고, 오래동안), never in numbers, names, or negation.
- The bans still hold: no emoji (unless the voice source uses them), no `·`, no ①, no →.

## Follower address

| Target | Address | Notes |
|---|---|---|
| Threads | 스친이들, 스친분들, 다들 | 반말 posts: 스친이들; 해요체 posts: 스친분들 |
| Instagram | 인친님들, 다들 | |
| X | 트친들, 다들 | |
| Community boards and cafes | none by default | use the board's own habit only if the user gives it |
| Brand accounts | none, or 여러분 | |

"다들" works on every SNS and is the safe choice when the user wants a softer address. When dropping the address, keep the sentence natural:

> 스친이들 배추도 패딩 입히는 타이밍이 있대 ㅋㅋ
> -> 배추도 패딩 입히는 타이밍이 있대 ㅋㅋ

> 다들 무 벌써 캤어??
> -> 무 벌써 캔 사람?? (a question to readers without an address)

## Korean AI tells

Fix every hit. Severity: **S1** always fix, **S2** fix unless it is the user's own voice, **S3** check.

| Sev | Tell | Example | Fix |
|---|---|---|---|
| S1 | Invented specifics | a number, quote, or scene nobody gave you | real material, or invented in plain text and listed in the notes |
| S1 | Lesson ending | "결국 중요한 건 ~라는 걸 깨달았다" | end on the scene or the quote |
| S1 | Aphorism ending | "농사는 하늘이 짓고 걱정은 사람이 짓는다" | cut it, or replace with what someone actually said. Exception: `farmer` and `midlife` samples use hedged sayings and well-wishes (~는 말이 딱 맞는 것 같습니다, 좋은 하루 보내시길 바랍니다); allowed when the samples do it and the material leads there |
| S1 | Hollow reversal | "이건 단순한 툴이 아닙니다. 방식의 변화입니다" | state the concrete change |
| S1 | Chatbot residue | "좋은 질문입니다", "도움이 되셨길 바랍니다" | delete |
| S2 | Rule of three | 무 뽑고 / 배추 묶고 / 고추 따고, three by reflex | keep the real count; often one vivid action is enough |
| S2 | 명사화 | 검토를 진행한 후 공유드리겠습니다 | 검토하고 보낼게요 |
| S2 | 번역투 | 당신, ~하는 것은 중요합니다, ~에 있어서 | rewrite as speech |
| S2 | Stacked adjectives | 빠르고 신속하며 효율적인 | one fact instead |
| S2 | Significance words | 핵심적인, 혁신적인, 게임체인저 | delete or replace with the fact |
| S2 | Middle dot `·` between words | 기획·개발·운영, 중·하순 | a comma, 와/랑, or spell it out (중순에서 하순). `ㆍ` (U+318D) as a sentence end in `farm` posts is a phone-keyboard habit, not this tell |
| S2 | Circled numbers | ①②③ | `1.` `2.` `3.` or no numbering |
| S2 | Unicode arrows | → ⇒ ➡ | `->`, or words (그래서, 다음에) |
| S2 | Emoji | ✅ 🔥 👉 📌 | none (`farm` posts may use marks and emoji as the roll's `deco` says) |
| S3 | Em dash, en dash | — | period or comma |
| S3 | Curly quotes or single quotes for emphasis | '진짜' | remove the quotes |
| S3 | Bold, headers, bullets in a casual post | | plain lines |
| S3 | 음슴체 in a 해요체 post | ~함, ~됨 | match the post's register (`farmer` and `midlife` may mix 해요체 and 합니다) |

### Too clean

Every tell above is something to remove. These are the opposite: the post is cleaner than a real person would write. Check them against the voice source; the more the samples are rough, the more these matter. Persona-specific ones are in `personas.md`.

| Sev | Tell | Example | Fix |
|---|---|---|---|
| S2 | Precision beyond the material | 오전 6시 47분, 영하 2.3도 when the user said "새벽", "영하" | the precision the material has, said the way the speaker says it. Farmers are exact about products, ratios, and distances; the tell is precision the material does not have, not precision itself |
| S2 | Every beat connected | 근데 / 그래서 / 결국 between every line | the speaker's own joins, or none |
| S2 | A turn the material lacks | an observation recast as a realization (근데 ~게 이제 확실해요) | tell what happened |
| S2 | Evenly spread endings | each sentence ends differently | let the voice source's endings repeat |
| S2 | Nothing off-topic | every line serves the point | keep the user's asides |
| S3 | Spacing and punctuation cleaner than the samples | perfect spacing and periods when the samples use neither | mirror habits found in at least half the samples; never invent typos |
| S3 | Vocabulary above the speaker | literary or written words in a plain voice | the words the samples use |

No single word proves AI authorship. A post can fail by being too rough for its voice as easily as too clean; the voice source is the measure. These are edit points, not a detector score.

## Slang

Use trending slang only if the user's own posts use it, only in draft mode, and only if it is current. When unsure, plain speech wins.
