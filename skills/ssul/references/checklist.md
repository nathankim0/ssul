# Final checklist

Run before returning any post. In audit mode, print each failed item with the exact offending words.

- [ ] **Truth.** Every number, name, quote, and event is real or listed in the notes as invented. No brackets in the post.
- [ ] **First line.** Passes late, confusing, not mine, flat.
- [ ] **Stranger test.** No line needs the conversation or insider jargon to make sense.
- [ ] **Weight test.** No setup, no fake list, no explained joke, no moral.
- [ ] **Value test.** A stranger gets a usable fact, a feeling they recognize, or a real laugh. No forced jokes, no posts about writing the post.
- [ ] **Last line.** `sns` with `flow: turn`: quotable on its own, a scene, a quote, or a punchline. Otherwise it stops where the samples stop (the work, a wish, an ask, a greeting). Never a lesson or an aphorism.
- [ ] **Variation.** Voice settings come from `scripts/roll.py`, with user asks, voice profile, and tone fit applied on top. In a batch, no two posts share the same roll.
- [ ] **Texture.** Not over-crafted: events in order, plain feelings, real asks allowed; no fake typos, no fake feelings.
- [ ] **Persona.** Picked by the user's words, then the voice source, then platform and topic (`personas.md`). Named in the notes.
- [ ] **Flow.** `turn`: beats joined by 근데 or 그래서, never "그리고 나서" filler. `log` (and `farmer`, `midlife`): in order, no added turn, no quotable closing line.
- [ ] **Register.** Chosen from user posts, then pasted samples (including topic-only samples), then the persona default. `sns`: one register. Endings follow the voice source; repetition allowed; not spread evenly.
- [ ] **Korean AI tells.** No S1 hits. S2 only if it is the user's own voice.
- [ ] **Too clean.** Not smoother, more precise, or more connected than the voice source (`korean-voice.md#too-clean`, `personas.md`).
- [ ] **Disclosure.** Anything received for the post is stated in the first part, in Korean, with approved wording (`disclosure.md`). AI people and realistic AI images are labeled.
- [ ] **Meaning and spelling.** Negation, conditions, limits, numbers, and claims unchanged (polish); clear spelling and spacing errors fixed; intentional casual style kept.
- [ ] **Platform.** Threads: under 500 characters; boards: length as the samples. Then 0 or 1 hashtag, no link in post 1, at most one question. No emoji (unless the voice source uses them, or a `farm` post's `deco`), middle dots between words (`·`), circled numbers (①), or Unicode arrows (→; use `->`).
- [ ] **Output.** Post first as paste-ready text, then at most 3 short notes, one of them listing every invented detail. Nothing published.
- [ ] **No copying examples.** No topic, wording, number, or line order taken from an example in `references/`.

Audit output:

```
SSUL AUDIT
  Truth:      FLAG "영하 2도", "아빠" not given by the user
  First line: pass
  Stranger:   FLAG "윤문 스킬" is insider jargon
  Weight:     pass
  Value:      FLAG the ending is an inside joke about the writing session
  Last line:  FLAG "농사는 하늘이 짓고 걱정은 사람이 짓는다" is an aphorism
  Persona:    farmer (asked for "농민 말투")
  Register:   FLAG ~거든요, ~더라고요, ~잖아요 in a farmer post; the samples use ~했어요, ~네요
  Too clean:  FLAG "근데 해가 짧아진 게 이제 확실해요" is a realization turn the samples never make
  AI tells:   S2 rule of three "무 뽑고 / 배추 묶고 / 고추 따고"
  Platform:   pass
```
