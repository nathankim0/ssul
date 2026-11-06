---
name: ssul
description: Write, polish, or audit Korean social content (Threads and X posts and threads, replies, Instagram captions, Reels/Shorts scripts, bios, hook images) so it reads like a real person telling a true story, not like AI. Use when the user asks for a Threads post, 스레드 글, 바이럴 글, 후킹 글, 일상 글, SNS 글, 썰, 답글, 캡션, 릴스 대본, 프로필, 콘텐츠 계획, wants hooks or an image for a post, pastes viral posts to analyze, wants a blog or video turned into a post, says a draft "AI 같다", "너무 무겁다", "뭔 소린지 모르겠다", or needs sponsorship (광고, 협찬) disclosure. Real material first; hooks, storytelling, Korean anti-AI editing, spoken register, meaning-safe polishing, proofreading, and Korean disclosure rules in one pass.
argument-hint: "[topic, rough notes, or a draft to fix]"
---

# ssul

A post works when a stranger reads the first line, keeps going, understands every line without context, and believes a real person wrote it. This skill gets there in one pass. It merges hook formulas, storytelling, anti-AI editing, and Korean spoken-register rules, and settles the places where those sources disagree (see `references/conflicts.md`).

The core lesson behind this skill: style passes cannot rescue invented content. A post with a perfect hook and natural 구어체 still reads as AI if the scene, the numbers, and the quote were made up. Real material comes first.

## Modes

Pick the mode from the request. Do not ask which one.

| Request | Mode | Output |
|---|---|---|
| "써줘", topic or notes | **draft** | one post + a 3-line note |
| a draft + "다듬어줘 / AI 같아 / 무거워 / 맞춤법" | **polish** | the fixed post + changed points (`references/polish.md`) |
| "검사해줘 / 뭐가 문제야" | **audit** | findings only, no rewrite |
| "훅만 / 첫 줄만" | **hooks** | 3 first lines from different triggers + a pick |
| "이미지 / 썸네일 / 카드 만들어줘" | **image** | one generated image for the post (`references/images.md`) |
| a post + "답글 / 인용" | **reply** | 2 or 3 replies or a quote post (`references/reply.md`) |
| pasted posts + "이거 봐 / 왜 터졌어 / 이런 식으로" | **analyze** | pattern per post, a summary, ideas from the user's material (`references/analyze.md`) |
| a blog, video, README, notes + "스레드로" | **repurpose** | 1 to 3 posts from the strongest points (`references/repurpose.md`) |
| "스레드로 길게 / 연재" | **thread** | a multi-post thread with per-post counts (`references/threads.md`) |
| "뭐 올리지 / 이번 주 계획" | **plan** | a week of ideas tied to real material (`references/plan.md`) |
| "프로필 / 바이오" | **profile** | 2 bio options + pinned-post pick (`references/profile.md`) |
| "릴스 / 쇼츠 / 틱톡 대본 / 캡션" | **video** | script with on-screen text, and caption (`references/short-video.md`) |

In image mode, use the current post (draft one first if none exists). Follow `references/images.md`: 4:5 portrait, the first line as the headline, the real subject as the scene, GPT image generation through the Codex CLI, then check every Korean character before showing it.

Every mode uses the same core: real material (Step 1), voice (Step 2), and the passes (Step 6). Out of scope: paid ads, SEO, landing pages, email, and other non-social marketing.

## Step 0. Load what is already known

If `~/.ssul/voice.md` or `~/.ssul/story-bank.md` exist, read them first (`references/voice-bank.md`). They are the voice source and real material. When the user gives new real material or corrects the voice, offer once to save it there.

## Step 1. Get real material (draft mode)

Before writing, you need at least three of these, from the user or from facts already in the conversation:

- **who** is in the scene (me, my dad, a coworker, my cat)
- **where / when** (a field at 9pm, the subway at 8:10, a Monday standup)
- **one concrete detail** you can see or count (영하 2도, 16 repos, a headlamp)
- **one line someone actually said**, or one thing that actually happened
- **why the user wants to post it** (laugh, vent, show, ask)

Facts in the current conversation count as real material: what the user built, installed, said, or asked. Use them. They are often the best source available.

If you do not have enough, ask at most 3 short questions from `references/interview.md` in one message. If the user wants a draft anyway, write it with `[brackets]` around every invented detail and say plainly that those parts are placeholders. Never present invented biography, numbers, quotes, or events as true.

## Step 2. Fix the voice

Pick the register in this order. The first source that exists wins.

1. **The user's own posts** (3 or more): note endings, how often they use ㅋㅋ and emoji, line length, openers and closers. Match them.
2. **Feed samples the user pasted** (other people's posts they want to sound like): match the register most of those posts use, not the polite average.
3. **The niche default** (`references/korean-voice.md#register-by-niche`): AI, dev, startup, investing, and hot-take posts default to **반말 혼잣말** (`~다`, `~함`, `~임`, `~네`, `~냐`). Daily life, parenting, food, and brand accounts default to **해요체 구어** (`~거든요`, `~더라고요`, `~잖아요`).

One register per post. Quotes inside the post keep the speaker's register.

**Roll the voice.** Sources 1 to 3 set the range, not one fixed voice. Then roll real random settings so posts do not all sound the same (`references/variation.md`):

```bash
python3 -I "<skill base directory>/scripts/roll.py" --n <posts> --pool <sns|warm>
```

The roll picks register within the pool, ㅋㅋ or none, `..` or none, length, opener, and ending. The user's explicit asks, their own voice profile, and tone fit (no ㅋㅋ on serious posts) override the roll. Put the roll in the notes; "다시 굴려" re-rolls.

**Follower address is an option.** Decide it from the request, in this order:

1. The user says so: "스친 넣어서", "스친 빼고", "호칭 없이", "인친님들로".
2. The target platform: Threads -> 스친이들, Instagram -> 인친님들, X -> 트친들. Community boards, cafes, and anything else -> no SNS-friend address; follow the board's own habit if the user gives it, otherwise none.
3. No platform named -> follow the voice source; if it addresses followers, include it and say in the notes that the address line can be dropped for other platforms.

When the address is removed, rewrite the opening so it still reads naturally; do not just delete the word. Details: `references/korean-voice.md#follower-address`.

## Step 3. Pick the shape

| Shape | Use when | Goal |
|---|---|---|
| **Scene** (장면) | one moment with a small turn | likes |
| **Confession** (고백) | something real the user did, including the embarrassing part | replies |
| **Reversal** (뒤집기) | a common belief vs what actually happened, both concrete | reposts |
| **List** (목록) | the content is truly a list (tools, steps) and each item is one line | saves |
| **Question** (질문) | the user genuinely wants answers | replies |
| **One-liner** (한두 줄) | one feeling or one verdict says it all | likes, reposts |
| **Finding** (발견) | the user tried something and learned facts others can use | saves, reposts |
| **Hot take** (한마디) | the user has an attitude about a trend: 짜증, 냉소, 자조 | replies, quotes |

Choose by what the material has:

- a real event with a turn -> Scene or Confession
- facts the reader can use -> Finding or List
- an attitude -> Hot take or One-liner

**Do not manufacture humor.** If nothing in the material is actually funny, do not build a punchline. Write the Finding or the attitude instead. Attitude (annoyance, cynicism, self-mockery) carries a post further than a forced joke. Shorter is usually better: a two-line post is a complete post.

**No navel-gazing.** A story about the writing session itself, the tools used to write it, or the AI that helped is insider material. It passes only if the reader has lived the same thing.

Format details per shape: `references/formats.md`.

## Step 4. Write the first line

Generate 3 candidates from different triggers (specific number, a quoted line, a confession, a reversal, a question). Formulas: `references/hooks.md`. Check each against the four killers:

1. **Late**: the topic is not in the first line.
2. **Confusing**: needs a second read or context the reader does not have.
3. **Not mine**: the reader cannot see themselves in it.
4. **Flat**: no gap between what the reader expects and what happened.

Keep the one that passes all four. A first-person line is fine when the moment is one the reader has lived too. Do not force "여러분".

## Step 5. Draft

1. Write the **last line first**. It should be the line people would quote on its own. A concrete punchline or a real quote beats a lesson.
2. Fill the middle with beats joined by **근데** (but) or **그래서** (so). If "그리고 나서" fits between two beats, one of them is filler.
3. Write the way the user would say it to one friend. Line breaks follow breath.
4. Stay under 500 characters per post (Threads limit). Casual daily posts usually land at 120 to 300.
5. **Leave texture in** (`references/korean-voice.md#human-texture`): talk to followers whenever the voice source does (in every shape, jokes included), tell things in the order they happened, keep `..` and `??` and plain feelings. A post that is too neat reads as AI.

## Step 6. Run the passes

Run all of these, in order, on every draft. Details in `references/korean-voice.md` and `references/checklist.md`.

1. **Truth**: every number, name, quote, and event is real or bracketed.
2. **Stranger test**: someone with zero context understands every line. Replace insider words ("윤문 스킬", project names, inside jokes) with plain words. If you need the conversation to understand the post, it fails.
3. **Weight test**: does it read like a report? Cut setup, lists that are not lists, explanations of the joke, and the moral at the end.
4. **Value test**: what does a stranger get: a fact they can use, a feeling they recognize, or a real laugh? If none, change the shape or the material. Do not polish a post that gives nothing.
5. **Korean AI tells**: lesson endings, `X가 아니라 Y다` with a vague Y, rule-of-three lists, 명사화 (`진행하다`, `공유드리다`), 번역투 (`당신`, `~하는 것은 중요합니다`), stacked adjectives, em dashes, curly quotes for emphasis, bold, middle dots (`·`), circled numbers (①), Unicode arrows (→; write `->`), emoji.
6. **Spoken register**: no report words (따라서, 종합하면, 부각, 안착), no 4 identical sentence endings in a row, at most one self-question.
7. **Platform**: 0 or 1 hashtag, no link in the first post (links go in the first reply, `references/threads.md`), no emoji, ends without engagement bait.
8. **Disclosure**: if the user received anything for the post (money, product, discount, points, commission), the first part of the post says so in Korean, by Korean FTC rules (`references/disclosure.md`). If a product or service is recommended and you do not know, ask. Realistic AI people or images are labeled.
9. **Meaning and spelling** (polish mode, and before any output): negation, conditions, limits (`만`, `까지`, `이내`), numbers, and the author's claims are unchanged; clear spelling and spacing errors are fixed without "correcting" intentional casual style (`references/polish.md`).

## Output

Draft and polish modes return the post first, then at most 3 short lines:

- the shape and why
- what is real and what is a placeholder
- one thing the user should check before posting

Do not attach long reports, tables, or scores unless asked. The user asked for a post.

Never publish, schedule, or send anything. Output text only.
