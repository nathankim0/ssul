# Personas

A persona is who writes the post and who reads it. It sets the register range, the endings, how the post is built, whether hook formulas apply, laugh marks, the roll pool, length, and extra AI tells. The rest of ssul (real material, truth, disclosure, meaning-safe polish) is the same for every persona.

Real samples always beat these defaults. Once the user gives 3 or more real posts from the target writers, measure them (`analyze.md#voice-card`) and follow the samples wherever they differ from the table below.

## Picking the persona

In this order, the first that applies wins:

1. The user names it: "농민 말투", "농부처럼", "50대 농업인", "중장년 대상", "스레드 2030 감성".
2. The voice source: the user's own posts or pasted samples read like one persona.
3. The platform and topic: a farming community board or farming topic for farmers -> `farmer`; a 밴드, 카페, or 카카오스토리 for 40s and up -> `midlife`; Threads, X, Instagram -> `sns`.
4. Otherwise `sns`.

Say the persona in the notes. The user can switch it ("농민 버전으로도", "2030 말투로 바꿔").

## The personas

| | `sns` | `farmer` | `midlife` | `custom` |
|---|---|---|---|---|
| Who | 2030 on Threads, X, Instagram | farmers, mostly 50s to 70s, posting on a farming community board | 40s and up, daily life, family, health, hobbies | anyone, built from samples |
| Register | one per post: 반말 혼잣말 or 해요체 구어 | **합니다체 first** (~했습니다, ~입니다, ~궁금합니다, ~부탁드립니다), with ~네요 or 해요체 lines mixed in | 합니다체 and plain 해요체 | measured |
| Shapes | Scene, Confession, Hot take, and the rest | Ask, Photo caption, Log, Essay, Notice (`formats.md`) | Log, Photo caption, Essay, greeting | measured |
| First line | hook formulas (`hooks.md`) | 안녕하세요, where and what they farm (region, crop, years), the work done, the weather, or naming the photo (crop name plus 입니다) | a greeting or a plain fact | how the samples start |
| Last line | a quote, a punchline, or a real ask | the question (~될까요?, ~궁금합니다, 고견 부탁드립니다), a feeling about the work (즐겁습니다), a wish or well-wishing (평안한 하루 보내시길 바랍니다!), or just the last fact | a wish or a greeting | how the samples end |
| Laugh | ㅋㅋ, ㅋ, ㅎㅎ, or none | mostly none; ㅎㅎ now and then | ㅎㅎ, `^^`, none | measured |
| Punctuation | `..`, `??` | periods, `!` on greetings and wishes, `?` in the middle of a sentence when musing (a thought ending in `?` right before 했습니다), `...` rarely | periods, `!`, `...` | measured |
| Emoji | none | none unless the samples use them | none unless the samples use them | as the samples |
| Numbers | as given | precise on farming facts (product names, mix ratios, distances, temperature ranges, tree age, counts), hedged with 약, 정도, 여, `~` (약 plus a distance, a temperature range with `~`, a count with 여) | as said | as said |
| Length | under 500 characters | anything from one line of nouns (a photo caption) to a long essay; boards have no 500 limit | short to long | measured |
| Roll pool | `sns` or `warm` | `farm` | `plain` | the closest pool, then the samples override |

`sns` is the persona every earlier version of ssul assumed. Nothing about it changed.

## farmer, in more detail

Measured from 10 popular posts on a farming community board (November 2026). Re-measure when the user gives more.

- **합니다체 is the base.** Most sentences end in ~습니다, ~입니다, ~합니다, ~궁금합니다, ~부탁드립니다, ~바랍니다. ~네요 shows up for a feeling or a small brag. A post written all in 해요체 (~했어요, ~하려고요) reads like a younger writer.
- **Most posts carry a photo or video.** pointing at the attachment, naming the crop in the photo, or a caption of only nouns. Ask whether a photo goes with the post, and write to it.
- **Asking is the most common reason to post.** Give the context a stranger needs to answer (region, crop, variety, tree age, what was already done, the forecast), then ask plainly. Asking experts or fellow farmers by name of role (전문가님, 선배님) is normal.
- **Precise on farming, loose on spelling.** Chemical and fertilizer names, mix ratios, distances, and temperature ranges are exact; spacing is loose (units stuck to numbers, 조사 spaced off) and some words are misspelled. `roughen.py` applies loose spacing and 1 to 3 habitual spellings by roll; beyond that, mirror habits that most samples share and never invent misspellings.
- **Long posts wander, and that is the point.** An essay post moves from the work, to a memory, to a family member, to how-to tips, to the weather, to wishing students luck on an exam. 근데, 그래서, ~거든요, ~잖아요? all appear in long posts, spoken the way an older writer says them, not stacked in a short one.
- **Sayings and wishes are allowed.** A hedged saying near the end (~한다는 말이 딱 맞는 것 같습니다) and a well-wish to readers (따뜻한 하루 보내시길 바랍니다!) are real habits here. Use them only when they fit the material.
- **Selling your own produce is a normal post.** Your own product is not sponsorship; but if the user received anything from a third party for the post, `disclosure.md` still applies.
- **Address.** 안녕하세요 at the start is common; board words (회원님들, 전문가님, 선배님들) only when the samples or the user show it.

No example posts here on purpose: examples get copied. Build each post from the user's material and the samples.

## midlife, in more detail

Not yet measured from real posts; treat these as guesses and replace them with a voice card as soon as samples exist. Same habits as `farmer` for register, greetings, and wishes. Topics are daily: family, health, walks, food, hobbies, news.

## Extra AI tells for farmer and midlife

These are on top of `korean-voice.md#korean-ai-tells`. All are S1 for these personas; this overrides the S2 and S3 grades in `korean-voice.md#too-clean`.

| Tell | Example | Fix |
|---|---|---|
| Young register | a whole post in ~했어요, ~하려고요, ~거든요 | 합니다체 base, as the samples |
| Young engine in a short post | ~거든요, ~더라고요, ~잖아요 stacked in three lines | plain statements; keep these endings for long posts where they come naturally |
| Crafted turn | a short post built as setup, 근데, realization ("근데 해가 짧아진 게 이제 확실해요") | say what happened, or ask |
| Punchline ending | a neat verdict or joke as the last line | the question, the feeling, a wish, or the last fact |
| Fake precision | 오전 6시 47분, 영하 2.3도 | farming facts exact, the rest hedged with 약, 정도, `~` |
| Vague farming | "약을 쳤어요" when a real post would name the product and the ratio | the real name and ratio from the material, or invented and listed in the notes |
| No context in an ask | a question with no region, crop, or tree age | the context a stranger needs to answer |
| Too clean | perfect spacing everywhere, no mid-sentence `?`, every line one tidy sentence | `roughen.py` with the roll, then the samples' habits |
| Stock phrases | 허리가 뻐근, 다행입니다, 마음이 편합니다, 한 해 농사, 걱정했는데 ~ 다행, 제법, 이제야, 뿌듯 (the model's defaults; `roughen.py` flags them) | what this writer actually said, or a different concrete detail |
| Same post every time | weather opener, the day's work, a sore back, relief | the rolled shape and topic seed; in a batch, different shapes, topics, openers, and closers |
| Borrowed SNS words | 스친이들, 갓생, 킹받네, TMI, ㅋㅋㅋ | the community's own words |

## custom

When the user gives samples that fit none of the personas (a cooking community, a fishing club, a parents' group), build the persona from them: register mix, top endings and how often they repeat, laugh and punctuation, emoji, typical first and last lines, line and post length, spacing habits, and whether posts carry photos. Write the result as a voice card (`analyze.md#voice-card`) and use it like a persona. Offer once to save it to `~/.ssul/voice.md` (`voice-bank.md`).
