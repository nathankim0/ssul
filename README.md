<p align="center">
  <img src="assets/banner.png" alt="ssul banner" width="100%">
</p>

<p align="center">
  <b>English</b> · <a href="README.ko.md">한국어</a>
</p>

# ssul

**Korean social posts that read like a real person, not like AI.**

*ssul* (썰) is Korean slang for a casual true story you tell your friends. This is an agent skill for Claude Code and Codex that writes, polishes, and audits short Korean posts for Threads, X, Instagram captions, and community boards.

It merges four kinds of open-source writing skills into one pass and settles the places where they contradict each other:

- **Hooks**: first-line formulas and the four ways a first line dies
- **Storytelling**: write the last line first, join beats with "but" and "so"
- **Korean anti-AI editing**: lesson endings, hollow reversals, 명사화, 번역투, rule-of-three lists
- **Spoken register (구어체)**: endings people actually say, no report words

## Why it exists

Running a dozen popular writing skills together on real Korean Threads posts kept producing the same failure: perfect hooks and smooth Korean that still read as AI. The cause was not style. The scene, the numbers, and the quotes were invented. No style pass can fix that.

So ssul does one thing first: it gets **real material** from you or from the conversation, and it refuses to pass off invented details as true. Then it runs the style passes.

## What it does

| Mode | You say | You get |
|---|---|---|
| Draft | a topic or rough notes | one post, plus at most 3 short notes |
| Polish | a draft + "AI 같아", "너무 무거워" | the fixed post and what changed |
| Audit | "검사해줘" | findings only, with the exact words |
| Hooks | "첫 줄만" | 3 first lines from different triggers, and a pick |

Every post goes through these checks:

1. **Truth**: every number, name, quote, and event is real, or marked `[like this]` as a placeholder
2. **Stranger test**: someone with zero context understands every line
3. **Weight test**: no setup, no fake lists, no morals
4. **Korean AI tells**, graded S1 to S3
5. **Spoken register**: no 4 identical endings in a row, no report words
6. **Platform**: under 500 characters, 0 or 1 hashtag, at most one question

## Example

Input: *"Write a post about today: I asked Claude for a Threads post and ended up installing 16 skill repos."*

```text
클로드한테 스레드 글 좀 써달라 했는데
계속 AI가 쓴 티가 나는 거예요

그래서 글 잘 쓰게 해주는 스킬을 16개나 깔아줬어요
그래도 티가 나길래
"스킬 쓴 거 맞아?" 물어보니까
"아니요, 그냥 썼습니다" ㅋㅋㅋ

다시 시켰더니 이번엔 이러더라고요
"말투는 고쳤는데, 진짜 있었던 일을 하나 알려주셔야 해요"

...그럼 그냥 내가 쓰는 거잖아
```

Every detail in it happened. That is the point.

## Install

### Claude Code (plugin)

```text
/plugin marketplace add nathankim0/ssul
/plugin install ssul@ssul
```

### Claude Code or Codex (manual)

```bash
git clone https://github.com/nathankim0/ssul.git
cp -R ssul/skills/ssul ~/.claude/skills/ssul     # Claude Code
cp -R ssul/skills/ssul ~/.codex/skills/ssul      # Codex
```

### Any agent that supports Agent Skills

```bash
npx skills add nathankim0/ssul
```

## Usage

```text
/ssul 오늘 회의에서 있었던 일로 스레드 글 하나 써줘
/ssul 이 글 AI 같은데 다듬어줘: <draft>
/ssul 검사만 해줘: <draft>
/ssul 첫 줄만 3개
```

If you have not given enough real material, ssul asks up to three short questions first. Paste two or three of your past posts and it matches your voice.

## Repository layout

```text
skills/ssul/SKILL.md              the skill
skills/ssul/references/
  conflicts.md                    14 contradictions between source skills, and the rulings
  hooks.md                        first-line triggers and killers, written in Korean
  korean-voice.md                 구어체 endings and Korean AI tells (S1 to S3)
  interview.md                    questions for getting real material
  formats.md                      scene, confession, reversal, list, question
  checklist.md                    final pass and audit format
.claude-plugin/                   Claude Code plugin and marketplace manifests
```

## Credits

ssul was built by studying these projects. No text was copied; see [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Burntgogi/ai-slop-thresher · svy04/rutter · sergebulaev/threads-skills · sergebulaev/x-skills · vyralcontent/content-skills · artemnovitckii/content-skills · rediumvex/viral-hooks-skill · coreyhaines31/marketingskills · ScrapeCreators/social-media-research-skills · amondnet/yoonmoon · epoko77-ai/im-not-ai · hjongc/humanizer-kr · leeandev/stop-slop-ko · NomaDamas/k-skill · SorenKK/writing-signature · crazyrookie777/gueoche-guard

## License

[MIT](LICENSE)
