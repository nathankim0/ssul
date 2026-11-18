# Changelog

## v1.8.0 (2026-11-18)

### Changed
- Posts are always ready to paste: no `[brackets]`. Invented details are written in plainly and every one is listed in the notes (`지어낸 부분: ...`).
- `farmer` persona re-measured from 10 popular farming-board posts: 합니다체 is the base (not 해요체); posts open with 안녕하세요 or where and what the writer farms; asking with context is the most common post; most posts carry a photo; length runs from a one-line caption to a long essay; farming facts (products, ratios, distances, temperature ranges) are exact and hedged with 약, 정도, `~`; hedged sayings and well-wishes are allowed as closers.
- Example posts were removed from `personas.md` and the Log shape, and outputs must never reuse an example's topic, wording, numbers, or line order. Posts were coming out as copies of the examples.

### Added
- `farm` roll pool for `farmer` (`plain` stays for `midlife`): `hapnida` and `hapnida_haeyo` registers, `oneline` and `essay` lengths, `greeting` and `intro` openers, `feeling` ending.
- Ask, Photo caption, Essay, and Notice shapes for farming boards.
- Conflicts 32 (banned openers and aphorisms vs farming boards) and 33 (rough voice vs precise farming facts).

## v1.7.0 (2026-11-18)

### Added
- Personas (`references/personas.md`): `sns` (2030 Threads, X, Instagram; every earlier rule unchanged), `farmer` (farmers writing to other farmers), `midlife` (40s and up), and `custom` (built from real posts). The persona sets register, endings, flow, hooks, laugh marks, emoji, and the roll pool. Picked from the user's words ("농민 말투", "중장년 대상"), then the voice source, then platform and topic.
- `plain` roll pool for `farmer` and `midlife`: plain 해요체, 해요체 with 합니다, or a diary voice; `^^` and `~~`; weather openers; wish and greeting endings; always `flow: log`.
- New roll settings in every pool: `flow` (`turn` or `log`) and `endings` (`repeat` or `mixed`).
- Log (일지) shape: the day in order, no hook, no turn, no punchline.
- Too clean pass and AI tells: precision beyond the material, every beat connected, an added realization turn, evenly spread endings, nothing off-topic, spacing cleaner than the samples. The voice source is the measure in both directions.
- Voice card in analyze mode: pasted posts are measured (endings, repeats, laugh, spacing, first and last lines) and used as the voice source.
- Conflicts 27 to 31.

### Changed
- Pasted posts are a voice reference even when given only for topics; their text, numbers, and stories are still never reused.
- Hook formulas and last-line-first storytelling apply to `sns` and `flow: turn` only.
- The "no 4 identical endings in a row" rule is gone except for `sns` with `endings: mixed`. Repeated endings are allowed; evenly spread endings are flagged.
- `farmer` and `midlife` may mix 해요체 and 합니다 in one post. Emoji are allowed only when the voice source's real posts use them.
- Polish keeps loose spacing, `~~`, and `^^` as style for `farmer` and `midlife` voices.

## v1.6.1 (2026-11-06)

### Changed
- Posts with no laugh at all are now about half of all rolls (was about a third).
- In a batch of 3 or more, at least one post has no laugh.
- `laugh: none` means no ㅋ, ㅋㅋ, or ㅎㅎ anywhere in the post.

## v1.6.0 (2026-11-06)

### Added
- Random voice variation with a real random generator (`scripts/roll.py`): register within the pool, ㅋㅋ or none, `..` or none, length, opener, and ending. One roll per post; batches never repeat a roll.
- `references/variation.md`: what each setting means and what overrides it (user asks, voice profile, tone fit, address option).
- "다시 굴려" re-rolls the voice for the same content. Conflict 26 and a Variation checklist item.

## v1.5.0 (2026-11-06)

### Added
- Follower address option: on or off by request ("스친 빼고", "호칭 없이"), otherwise by target platform (Threads 스친이들, Instagram 인친님들, X 트친들, community boards none), otherwise by the voice source with a note that it can be dropped.
- Follower address table and natural rewrites when the address is removed (`korean-voice.md`).

## v1.4.1 (2026-11-06)

### Fixed
- Talking to followers (스친이들, 다들) was limited to questions. It now applies in every shape, jokes included, whenever the voice source does it.
- Humor posts may end on a real question or a plain reaction instead of a crafted punchline.

## v1.4.0 (2026-11-06)

### Added
- Human texture section in `korean-voice.md`: talking to followers, events in the order they happened, thinking out loud (`..`, `??`), plain feelings, real asks, uneven shape. No fake typos or fake feelings.
- Draft step 5: leave texture in.
- Conflicts 24 (crafted structure vs human texture) and 25 (one-question limit vs help posts).

## v1.3.1 (2026-11-06)

### Changed
- Posts never use emoji, middle dots (`·`), circled numbers (①②③), or Unicode arrows (→). Use commas or 와/랑, plain `1.` numbering, and `->` or words. Added to the Korean AI tells table, the passes, the checklist, formats, images, short video, and conflict 23.
- Reference docs and examples no longer use these symbols either.

## v1.3.0 (2026-11-06)

Covers the gaps found when auditing ssul against all 16 source repositories.

### Added
- Modes: reply (replies and quote posts), analyze (pasted viral posts), repurpose (blog, video, README into posts), thread (multi-post threads), plan (a week of ideas tied to real material), profile (bio and pinned post), video (Reels, Shorts, TikTok script, on-screen text, caption).
- Sponsorship and AI disclosure by Korean FTC rules: placement in the first part, approved and banned wording, hashtags, photos, video, AI-generated people (`references/disclosure.md`).
- Meaning-safe polishing (negation, conditions, limits, numbers) and a proofreading pass that keeps intentional casual style (`references/polish.md`).
- Voice profile and story bank saved to `~/.ssul/` with the user's consent (`references/voice-bank.md`).
- First-comment links and posting guidance without unverified posting-time claims (`references/threads.md`).
- Step 0 (load voice and story bank) and passes 8 and 9 (disclosure; meaning and spelling).
- Conflicts 17 to 22.

### Changed
- README credits now list the skills studied and what ssul actually took from each.

## v1.2.0 (2026-11-06)

### Added
- Image mode: "이미지 만들어줘" generates a 4:5 hook image for the post with GPT image generation through the Codex CLI (OpenAI Images API as fallback). The post's first line becomes the headline; every Korean character is checked before the image is shown; numbers must not claim more than the post.
- `references/images.md`: spec, prompt template, checks, and output notes (AI label reminder).

## v1.1.0 (2026-11-06)

### Added
- Three shapes: One-liner, Finding, Hot take. Shape is picked by what the material has: an event, usable facts, or an attitude.
- Value test: a stranger must get a usable fact, a recognizable feeling, or a real laugh.
- Register by niche: 반말 혼잣말 for AI, dev, startup, investing, and hot takes; 해요체 for daily life and brands. Pasted feed samples override the niche default.
- Conflicts 15 and 16: no manufactured humor; no posts about the writing session itself.

### Changed
- Register selection order: the user's own posts, then pasted feed samples, then the niche default (was: always 해요체).
- README example and the Scene example no longer use a story about the writing session itself (now a Finding post, and a placeholder-marked scene).

## v1.0.0 (2026-11-06)

First release.

- `ssul` skill with four modes: draft, polish, audit, hooks
- Real material first: interview questions, conversation mining, `[bracket]` placeholders for anything invented
- 14 conflicts between source writing skills, with rulings (`references/conflicts.md`)
- Korean first-line triggers and killers, 구어체 endings, Korean AI tells graded S1 to S3
- Five shapes: scene, confession, reversal, list, question
- Final checklist and audit output format
- Claude Code plugin and marketplace manifests
