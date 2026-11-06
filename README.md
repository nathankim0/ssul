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
- **Spoken register (구어체)**: endings people actually say, chosen by niche (반말 혼잣말 for AI and dev feeds, 해요체 for daily life), no report words

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
| Image | "이미지 만들어줘" | a 4:5 hook image for the post, headline text checked character by character |

Every post goes through these checks:

1. **Truth**: every number, name, quote, and event is real, or marked `[like this]` as a placeholder
2. **Stranger test**: someone with zero context understands every line
3. **Weight test**: no setup, no fake lists, no morals
4. **Value test**: a stranger gets a usable fact, a recognizable feeling, or a real laugh; no forced jokes
5. **Korean AI tells**, graded S1 to S3
6. **Spoken register**: no 4 identical endings in a row, no report words
7. **Platform**: under 500 characters, 0 or 1 hashtag, at most one question

## Example

Input: *"I installed 16 skill repos from GitHub today and checked their hooks and scripts. Write a Threads post for the AI crowd."*

Shape: Finding. Register: 반말 혼잣말 (the AI and dev niche default).

```text
클로드 스킬 GitHub에서 16개 깔아보면서 알게 된 거

1. 어떤 플러그인은 깔면 내가 메시지 보낼 때마다 스크립트가 돎
2. 어떤 스킬은 지침이 파일에 없고 쓸 때마다 인터넷에서 받아옴. 내용이 언제든 바뀔 수 있다는 뜻
3. 라이선스 없는 레포도 있음. 이건 가져다 쓰면 안 됨

그래서 이제 깔기 전에 SKILL.md랑 hooks 폴더는 꼭 열어봄
```

Every item was checked during the install, not remembered. That is the point.

### A farming tip, with a hook image

Input: *"A Threads post for farmers, early November, first below-zero days. No personal story; use checked facts."*

Shape: Finding. Register: 해요체 (the daily-life and farming default). First line picked from 3 candidates (number, question, reversal); the reversal passed all four hook checks.

```text
영하 예보 뜨면 배추보다 무가 먼저예요

무는 0도 근처만 가도 얼어요
배추는 영하 3~4도까진 버티고요

그래서 무는 영하 되기 전에 미리 캐두고
배추는 영하 예보 나올 때 겉잎 묶어주면 돼요
너무 일찍 묶으면 오히려 덜 자라거든요

김장 무 얼리면 진짜 아깝잖아요
```

The numbers come from local agricultural extension sources (Seoul and Chungnam agricultural technology centers, a vegetable-garden manual); where sources disagree, the most conservative value was used.

Then: *"이 글로 이미지 만들어줘"* (image mode). The first line became the headline, and every Korean character was checked before showing it.

<p align="center">
  <img src="assets/examples/farm-hook.jpg" alt="Hook image: frosted field at dawn with a radish in front and tied napa cabbages behind, headline 영하 예보 뜨면 배추보다 무가 먼저" width="360">
</p>

<p align="center"><sub>AI-generated image (GPT image generation through the Codex CLI). Turn on the platform's AI label when posting it.</sub></p>

## Requirements

- Nothing for writing, polishing, and auditing.
- For image mode: [Codex CLI](https://github.com/openai/codex) with image generation enabled, or an `OPENAI_API_KEY`.

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
/ssul 이 글로 이미지 만들어줘
```

If you have not given enough real material, ssul asks up to three short questions first. Paste two or three of your past posts and it matches your voice.

## Repository layout

```text
skills/ssul/SKILL.md              the skill
skills/ssul/references/
  conflicts.md                    16 contradictions between source skills, and the rulings
  hooks.md                        first-line triggers and killers, written in Korean
  korean-voice.md                 구어체 endings and Korean AI tells (S1 to S3)
  interview.md                    questions for getting real material
  formats.md                      scene, confession, reversal, list, question, one-liner, finding, hot take
  checklist.md                    final pass and audit format
  images.md                       hook image spec, generation prompt, and checks
.claude-plugin/                   Claude Code plugin and marketplace manifests
```

## Credits

ssul was built by installing and running the 16 repositories below on real Korean Threads posts. No text was copied; ideas are credited here and in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

### Hooks and short-form content

| Repository | Skills used | What ssul took |
|---|---|---|
| [vyralcontent/content-skills](https://github.com/vyralcontent/content-skills) | `viral-hooks`, `viral-short-form`, `viral-captions-and-ctas`, `viral-short-form-ideas`, `viral-tiktok-content`, `viral-instagram-reels`, `viral-youtube-shorts` | hook batches across archetypes; the promise must match the payoff |
| [artemnovitckii/content-skills](https://github.com/artemnovitckii/content-skills) | `viral-hooks`, `storytelling`, `anti-ai-writing`, `dumbify` | the four hook killers; "but / so" beats; last line first; hollow vs earned contrast |
| [rediumvex/viral-hooks-skill](https://github.com/rediumvex/viral-hooks-skill) | `viral-hooks` (100 formulas) | hook triggers grouped by psychology |

### Threads and X

| Repository | Skills used | What ssul took |
|---|---|---|
| [sergebulaev/threads-skills](https://github.com/sergebulaev/threads-skills) | `threads-post-writer`, `threads-hook-extractor`, `threads-humanizer` and 5 more | post shapes chosen by goal; story bank; never invent figures; 500-character and one-hashtag limits |
| [sergebulaev/x-skills](https://github.com/sergebulaev/x-skills) | `x-post-writer`, `x-hook-extractor` and 7 more | short-text hook shapes |

### Korean editing and spoken register

| Repository | Skills used | What ssul took |
|---|---|---|
| [Burntgogi/ai-slop-thresher](https://github.com/Burntgogi/ai-slop-thresher) | `ai-slop-thresher`, `thresh` | preserve meaning while editing Korean; never invent experience to sound human |
| [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | `humanize-korean` | Korean AI-tell taxonomy; facts and numbers stay fixed |
| [amondnet/yoonmoon](https://github.com/amondnet/yoonmoon) | `humanize`, `restyle`, `proofread`, `detect`, `polish-all`, `translate-polish` | humanize, proofread, and restyle kept separate; short SNS text treated as its own case |
| [hjongc/humanizer-kr](https://github.com/hjongc/humanizer-kr) | `humanizer-kr` | match the writer's own samples |
| [leeandev/stop-slop-ko](https://github.com/leeandev/stop-slop-ko) | `stop-slop-ko`, `jasoseo` | `~함` is normal in documents but not in posts; interview for real experience before drafting |
| [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | `korean-humanizer`, `korean-slang-writing` | severity levels for Korean AI tells; slang freshness guardrails |
| [crazyrookie777/gueoche-guard](https://github.com/crazyrookie777/gueoche-guard) | `gueoche` | the general idea of a 구어체 check (no license stated, so nothing was copied) |

### Voice, research, and marketing

| Repository | Skills used | What ssul took |
|---|---|---|
| [SorenKK/writing-signature](https://github.com/SorenKK/writing-signature) | `writing-signature` | voice measured from the writer's own texts |
| [svy04/rutter](https://github.com/svy04/rutter) | `social-media-kr`, `copy-kr` and 27 more | Korean channel context; the feed is the first line |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `social`, `copywriting`, `marketing-psychology` and 50 more | social copy and marketing psychology background |
| [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | `outlier-post-finder`, `trend-discovery`, `comment-mining` and 10 more | study posts that outperformed before writing |

## License

[MIT](LICENSE)
