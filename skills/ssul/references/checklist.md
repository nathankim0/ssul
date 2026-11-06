# Final checklist

Run before returning any post. In audit mode, print each failed item with the exact offending words.

- [ ] **Truth.** Every number, name, quote, and event is real or in `[brackets]`.
- [ ] **First line.** Passes late, confusing, not mine, flat.
- [ ] **Stranger test.** No line needs the conversation or insider jargon to make sense.
- [ ] **Weight test.** No setup, no fake list, no explained joke, no moral.
- [ ] **Value test.** A stranger gets a usable fact, a feeling they recognize, or a real laugh. No forced jokes, no posts about writing the post.
- [ ] **Last line.** Quotable on its own. A scene, a quote, or a punchline. Not a lesson, not an aphorism.
- [ ] **Variation.** Voice settings come from `scripts/roll.py`, with user asks, voice profile, and tone fit applied on top. In a batch, no two posts share the same roll.
- [ ] **Texture.** Not over-crafted: events in order, plain feelings, real asks allowed; no fake typos, no fake feelings.
- [ ] **Beats.** Joined by 근데 or 그래서, never "그리고 나서" filler.
- [ ] **Register.** Chosen from user posts, then feed samples, then the niche default. One register. No 4 identical endings in a row.
- [ ] **Korean AI tells.** No S1 hits. S2 only if it is the user's own voice.
- [ ] **Disclosure.** Anything received for the post is stated in the first part, in Korean, with approved wording (`disclosure.md`). AI people and realistic AI images are labeled.
- [ ] **Meaning and spelling.** Negation, conditions, limits, numbers, and claims unchanged (polish); clear spelling and spacing errors fixed; intentional casual style kept.
- [ ] **Platform.** Under 500 characters, 0 or 1 hashtag, no link in post 1, at most one question. No emoji, middle dots (`·`), circled numbers (①), or Unicode arrows (→; use `->`).
- [ ] **Output.** Post first, then at most 3 short notes. Nothing published.

Audit output:

```
SSUL AUDIT
  Truth:      FLAG "영하 2도", "아빠" not given by the user
  First line: pass
  Stranger:   FLAG "윤문 스킬" is insider jargon
  Weight:     pass
  Value:      FLAG the ending is an inside joke about the writing session
  Last line:  FLAG "농사는 하늘이 짓고 걱정은 사람이 짓는다" is an aphorism
  Register:   FLAG 4x ~요 in a row (했어요 / 더라고요 / 왔어요 / 알아요)
  AI tells:   S2 rule of three "무 뽑고 / 배추 묶고 / 고추 따고"
  Platform:   pass
```
