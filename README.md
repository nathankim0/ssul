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
- **Variation**: ㅋㅋ, register, length, opener, and ending are rolled with a real random generator each time (`scripts/roll.py`), so posts do not all sound the same
- **Human texture**: talk to followers, tell things in the order they happened, keep `..` and `??`; a post that is too neat reads as AI
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
| Reply | a post + "답글" | 2 or 3 replies that each add one specific thing, or a quote post |
| Analyze | pasted viral posts | the pattern behind each post, a summary, and ideas from your own material |
| Repurpose | a blog, video, README + "스레드로" | 1 to 3 posts from the strongest points |
| Thread | "길게 / 연재" | a multi-post thread with per-post character counts |
| Plan | "뭐 올리지" | a week of ideas, each tied to real material you have |
| Profile | "프로필" | 2 bio options and a pinned-post pick |
| Video | "릴스 대본 / 캡션" | a script with on-screen text, and a caption |

Every post goes through these checks:

1. **Truth**: every number, name, quote, and event is real, or marked `[like this]` as a placeholder
2. **Stranger test**: someone with zero context understands every line
3. **Weight test**: no setup, no fake lists, no morals
4. **Value test**: a stranger gets a usable fact, a recognizable feeling, or a real laugh; no forced jokes
5. **Korean AI tells**, graded S1 to S3, including emoji, middle dots (`·`), circled numbers (①), and Unicode arrows (→)
6. **Spoken register**: no 4 identical endings in a row, no report words
7. **Platform**: under 500 characters, 0 or 1 hashtag, at most one question
8. **Disclosure**: anything received for the post is stated up front, in Korean, by Korean FTC rules (광고, 협찬)
9. **Meaning and spelling**: negation, conditions, and numbers unchanged when polishing; clear spelling errors fixed, casual style kept

## Examples

All examples were made with ssul v1.6. Facts come from the sources named under each one; nothing is invented.

### 1. Same facts, three rolled voices

Input: *"Post about when to cover garlic, three versions."* ssul ran `roll.py --n 3 --pool warm`; each post got its own roll. Two of the three rolled `laugh: none`, so they have no ㅋ at all.

Roll: `banmal_talk, none, .., long, address, question`

```text
스친이들 마늘 덮는 것도 타이밍이 있대..
춥다고 일찍 덮어주면 좋을 것 같잖아
근데 너무 일찍 덮으면 겨울 오기 전에 싹이 웃자란대
그 상태로 추위 오면 오히려 언 피해를 입고..
그래서 기온 떨어지는 11월 중순에서 하순쯤 덮는 게 좋대
덮기 전에 뿌리 잘 내렸는지 한 번 보고
물도 넉넉히 주고
이게 중부 기준이라 남쪽은 또 다를 수 있대
다들 마늘 보통 언제 덮어?
```

Roll: `banmal_talk, ㅋㅋ, none, long, address, stop`

```text
스친이들 마늘이 생각보다 예민하더라
일찍 심으면 쪽이 갈라지고
늦게 심으면 뿌리를 잘 못 내리고
깊이도 마늘쪽 길이 2~3배로 맞춰야 되고
겨우 다 심었다 싶으면 이번엔 덮는 타이밍이 있음 ㅋㅋ
너무 일찍 덮으면 싹이 웃자라서 얼 수 있대
그래서 11월 중순에서 하순쯤 덮는 거래
그 전에 뿌리 내렸는지 보고 물도 넉넉히 주고
```

Roll: `banmal_talk, none, none, short, straight, question`

```text
마늘 너무 일찍 덮으면 오히려 얼 수 있대
싹이 겨울 오기 전에 웃자라서 그렇다고
11월 중순에서 하순쯤 덮는 게 좋대
다들 언제 덮어?
```

Facts: covering too early makes sprouts overgrow before winter and freeze; cover in mid to late November; check roots and water first (Icheon Agricultural Technology Center). Planting too early splits cloves, too late weakens rooting, depth 2 to 3 times the clove length (RDA).

### 2. Threads, follower address on

Input: *"I built 3 open-source skills today and they all have 0 stars. Threads post."* Roll: `banmal_talk, ㅋㅋ, .., short, address, reaction`

```text
스친이들 나 오늘 스레드 글 하나 쓰려다가 오픈소스를 3개 만들어버렸어..
깃허브 올려놓고 보니까 별이 셋 다 0개 ㅋㅋ
이게 맞냐고
```

The star counts were 0 when checked on GitHub on 2026-11-06, when the post was written. ssul got its first star later that day.

### 3. Community board, address off, with a hook image

Input: *"병맛 farming post for a community board."* Roll: `banmal_talk, ㅋㅋㅋ, ..., short, address, stop`. The address option is off for community boards, so the opener became `straight`.

```text
배추도 패딩 입히는 타이밍이 있대 ㅋㅋㅋ
겉잎 끈으로 묶어주는 게 배추 패딩인데 너무 일찍 입히면 답답해서 덜 큰대...
그래서 영하 예보 뜰 때 입히는 거래
무는 0도만 돼도 얼어서 그 전에 캐야 된대
```

Facts: tie outer leaves when a below-zero forecast comes, since tying too early slows growth; radishes can freeze near 0°C, so pull them first (Seoul agricultural technology center).

Then *"이미지 만들어줘"* (image mode). The first line became the headline; every Korean character was checked.

<p align="center">
  <img src="assets/examples/cabbage-hook.jpg" alt="Illustration: a napa cabbage with its outer leaves tied like a padded jacket next to a shivering radish, headline 배추도 패딩 입히는 타이밍이 있대" width="360">
</p>

<p align="center"><sub>AI-generated image (GPT image generation through the Codex CLI). Turn on the platform's AI label when posting it.</sub></p>

### 4. Polish with sponsorship disclosure

Input: a sample draft written for testing, not a real post.

```text
이번에 OO브랜드에서 보내주셨어요! 써보니까 진짜 좋아서 할께요 추천. 7일 이내에만 무료 반품 가능하대요 ㅋㅋ 체험단으로 받은거에요 #OO브랜드
```

Output:

```text
[광고] OO브랜드에서 제품을 무료로 제공받았어요

써보니까 진짜 좋아서 추천할게요
7일 이내에만 무료 반품 가능하대요 ㅋㅋ
```

- 보내주셨어요, 체험단, and a brand-name hashtag do not count as disclosure under the Korean FTC guidelines; a clear disclosure went to the first line.
- 7일 이내에**만** kept: it limits returns to 7 days.
- 할께요 fixed to 할게요; ㅋㅋ kept.

## Requirements

- Python 3 for voice variation (`scripts/roll.py`, standard library only). Without it, ssul picks the voice itself.
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
/ssul 이 글에 답글 달아줘: <post>
/ssul 이 블로그 글 스레드로 바꿔줘: <text>
/ssul 이번 주 뭐 올리지
/ssul 스친 빼고 다시 써줘
/ssul 커뮤니티용으로 써줘
/ssul 다시 굴려
```

If you have not given enough real material, ssul asks up to three short questions first. Follower address (스친이들, 인친님들, 트친들) follows the platform and can be turned on or off ("스친 빼고"). Paste two or three of your past posts and it matches your voice; with your OK it saves your voice and stories to `~/.ssul/` so you do not repeat them.

## Repository layout

```text
skills/ssul/SKILL.md              the skill
skills/ssul/references/
  conflicts.md                    22 contradictions between source skills, and the rulings
  hooks.md                        first-line triggers and killers, written in Korean
  korean-voice.md                 구어체 endings and Korean AI tells (S1 to S3)
  interview.md                    questions for getting real material
  formats.md                      scene, confession, reversal, list, question, one-liner, finding, hot take
  checklist.md                    final pass and audit format
  images.md                       hook image spec, generation prompt, and checks
  disclosure.md                   Korean sponsorship and AI disclosure rules
  polish.md                       meaning-safe editing and proofreading
  reply.md                        replies and quote posts
  analyze.md                      breaking down posts that worked
  repurpose.md                    turning other content into posts
  threads.md                      multi-post threads, first comment, posting
  voice-bank.md                   saved voice profile and story bank
  plan.md                         weekly content plan
  profile.md                      bio and pinned post
  short-video.md                  Reels, Shorts, TikTok scripts and captions
  variation.md                    random voice settings and what overrides them
skills/ssul/scripts/roll.py       rolls the voice settings (standard library only)
.claude-plugin/                   Claude Code plugin and marketplace manifests
```

## Credits

ssul was built by installing and running the 16 repositories below on real Korean Threads posts. No text was copied. Each row lists the skills studied, what ssul took, and where it lives in ssul. More detail in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

### Hooks and short-form content

| Repository | Skills studied | What ssul took | In ssul |
|---|---|---|---|
| [vyralcontent/content-skills](https://github.com/vyralcontent/content-skills) | `viral-hooks`, `viral-short-form`, `viral-captions-and-ctas`, `viral-tiktok-content`, `viral-instagram-reels`, `viral-youtube-shorts`, `viral-short-form-ideas` | hook batches; promise matches payoff; three-layer video hook; on-screen text; caption and CTA rules; hashtag reality; content pillars | hooks.md, short-video.md, plan.md |
| [artemnovitckii/content-skills](https://github.com/artemnovitckii/content-skills) | `viral-hooks`, `storytelling`, `anti-ai-writing`, `dumbify` | four hook killers; but/so beats; last line first; hollow vs earned contrast; plain words for strangers | SKILL.md, hooks.md, korean-voice.md |
| [rediumvex/viral-hooks-skill](https://github.com/rediumvex/viral-hooks-skill) | `viral-hooks` | hook triggers grouped by psychology | hooks.md |

### Threads and X

| Repository | Skills studied | What ssul took | In ssul |
|---|---|---|---|
| [sergebulaev/threads-skills](https://github.com/sergebulaev/threads-skills) | `threads-post-writer`, `threads-hook-extractor`, `threads-humanizer`, `threads-reply-drafter`, `threads-repurposer`, `threads-content-planner`, `threads-profile-optimizer`, `threads-audience-insights` | shapes by goal; story bank and voice profile; no invented figures; 500-character and one-hashtag limits; reply, repurpose, plan, profile, and post-analysis workflows | formats.md, voice-bank.md, reply.md, repurpose.md, plan.md, profile.md, analyze.md |
| [sergebulaev/x-skills](https://github.com/sergebulaev/x-skills) | `x-post-writer`, `x-thread-builder`, `x-hook-extractor`, `x-reply-drafter`, `x-repurposer` | short-text hook shapes; thread structure (post 1 promise, front-loading, standalone posts) | threads.md, hooks.md |

### Korean editing and spoken register

| Repository | Skills studied | What ssul took | In ssul |
|---|---|---|---|
| [Burntgogi/ai-slop-thresher](https://github.com/Burntgogi/ai-slop-thresher) | `ai-slop-thresher`, `thresh` | meaning preservation: negation, conditions, limits; never invent experience | polish.md, SKILL.md |
| [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | `humanize-korean`, `humanize-scan` | Korean AI-tell taxonomy; facts and numbers stay fixed | korean-voice.md |
| [amondnet/yoonmoon](https://github.com/amondnet/yoonmoon) | `humanize`, `restyle`, `proofread`, `detect`, `translate-polish` | separate humanize, proofread, and restyle; proofreading table; short SNS text as its own case | polish.md, korean-voice.md |
| [hjongc/humanizer-kr](https://github.com/hjongc/humanizer-kr) | `humanizer-kr` | match the writer's own samples | voice-bank.md |
| [leeandev/stop-slop-ko](https://github.com/leeandev/stop-slop-ko) | `stop-slop-ko`, `jasoseo` | `~함` belongs to documents, not posts; interview for real experience | korean-voice.md, interview.md |
| [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | `korean-humanizer`, `korean-slang-writing` | severity levels for Korean AI tells; slang freshness guardrails | korean-voice.md, conflicts.md |
| [crazyrookie777/gueoche-guard](https://github.com/crazyrookie777/gueoche-guard) | `gueoche` | the general idea of a 구어체 check (no license stated, so nothing was copied) | korean-voice.md |

### Voice, research, rules, and marketing

| Repository | Skills studied | What ssul took | In ssul |
|---|---|---|---|
| [SorenKK/writing-signature](https://github.com/SorenKK/writing-signature) | `writing-signature` | voice measured from the writer's own texts | voice-bank.md |
| [svy04/rutter](https://github.com/svy04/rutter) | `social-media-kr`, `influencer-kr`, `ad-compliance-kr`, `copy-edit-kr` | Korean channel context; Korean FTC sponsorship disclosure rules; no unverifiable superlatives | disclosure.md, profile.md, threads.md |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `social`, `copywriting`, `marketing-psychology`, `image` | social copy background; marketing image guidance | images.md, plan.md |
| [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | `outlier-post-finder`, `trend-discovery`, `comment-mining`, `content-repurposing` | study what outperformed before writing; turn one source into several posts | analyze.md, repurpose.md |

## License

[MIT](LICENSE)
