# Voice profile and story bank

So the user does not have to repeat their voice and their stories every time.

## Files

```text
~/.ssul/voice.md        how the user writes
~/.ssul/story-bank.md   real stories, numbers, and quotes the user has given
```

Read both at the start of draft, reply, repurpose, and plan modes if they exist. Their content is real material for Step 1 and the voice source for Step 2.

Create or update them only after the user agrees once ("말투랑 썰 저장해 둘까요? 다음부터 안 물어봐도 돼요"). Show what will be saved. Never save other people's private details, contact info, or anything the user says is private.

## voice.md

Build from 3 or more of the user's own posts. Measure, do not guess:

```markdown
# Voice
updated: YYYY-MM-DD
samples: N posts

register: 반말 혼잣말 | 해요체 | ...
endings (most used): ~다 40%, ~함 25%, ~네 15%, ...
ㅋㅋ: in about N of 10 posts
emoji: none | rare | often (which ones)
line length: short (under 20 chars) | mixed | long
post length: usually N to M characters
openers: e.g. starts with a number; starts mid-scene
closers: e.g. ends on a verdict; never ends with a question
never: words or habits the user avoids
example lines: 2 or 3 short lines quoted from the samples
```

## story-bank.md

```markdown
# Story bank
- [YYYY-MM-DD] who / where / what happened / one line someone said / numbers / can post? yes|ask|no
```

Add an entry whenever the user gives real material during a session. Mark "can post?" from what the user said; default to "ask".

## Updating

When the user corrects the voice ("이렇게 안 써", "너무 무거워"), update `never` or the relevant line in voice.md, with the date.
