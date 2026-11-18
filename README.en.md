<p align="center">
  <img src="assets/banner.png" alt="ssul banner" width="100%">
</p>

<p align="center">
  <a href="README.md">한국어</a> · <b>English</b>
</p>

# ssul

**Korean social posts that don't read like AI.**

*ssul* (썰) is Korean slang for a true story you tell your friends. ssul is an agent skill for Claude Code and Codex that writes, polishes, and audits Korean posts for Threads, X, Instagram captions, and community boards.

## Why it exists

Running a dozen writing skills together still produced posts that read as AI. The style was not the problem: the scenes, numbers, and quotes were invented. So ssul gets **real material** first, and fixes style second.

## Features

- **Real material first**: never passes invented details off as true. Without material, the post is still ready to paste, and every invented detail is listed in the notes.
- **Personas**: 2030 Threads users (`sns`), farmers on a farming board (`farmer`), readers in their 40s and up (`midlife`), or a voice built from pasted posts (`custom`). Each has its own endings, flow, first lines, and laugh marks.
- **Real posts set the voice**: pasted posts are the voice reference even when given only for topics. Their content is never reused.
- **Random variation**: register, ㅋㅋ, length, opener, and ending come from a real random generator (`roll.py`). Farm posts also roll shape, topic, and typing habits (spacing, spelling, line breaks), and the AI writes the post that way from the start.
- **AI-tell checks**: removes lesson endings, 번역투, 명사화, and emoji, and also catches posts that are cleaner than real ones.
- **Disclosure**: anything received for the post is stated up front, by Korean FTC rules.

## Install

```text
/plugin marketplace add nathankim0/ssul
/plugin install ssul@ssul
```

Manual install or other agents:

```bash
git clone https://github.com/nathankim0/ssul.git
cp -R ssul/skills/ssul ~/.claude/skills/ssul     # Claude Code
cp -R ssul/skills/ssul ~/.codex/skills/ssul      # Codex
npx skills add nathankim0/ssul                    # agents that support Agent Skills
```

Python 3 enables random variation (standard library only). Image mode needs [Codex CLI](https://github.com/openai/codex) image generation or an `OPENAI_API_KEY`.

## Usage

```text
/ssul 오늘 회의에서 있었던 일로 스레드 글 써줘
/ssul 농민 말투로 커뮤니티에 올릴 글 3개 써줘
/ssul 이 인기글들 말투로 써줘: <posts> <notes>
/ssul 이 글 AI 같은데 다듬어줘: <draft>
/ssul 검사만 해줘: <draft>
/ssul 이 글로 이미지 만들어줘
/ssul 다시 굴려
```

It also does first lines only, replies, blog to thread, multi-post threads, weekly plans, bios, and Reels scripts. Paste your past posts and it matches your voice; with your OK it saves it to `~/.ssul/`.

## Examples

Made with ssul v1.10. These were test runs with no real material, so places, numbers, and people are invented; ssul lists invented details in notes outside the post. Posts are shown exactly as output.

| # | Request | Persona, shape | Output |
|---|---|---|---|
| 1 | Threads write-up: things I noticed using AI writing tools | `sns`, hot take, 반말 | 스친이들 AI한테 글 다듬어 달라 하면 내 말버릇이 싹 빠지더라<br>요즘 블로그 초안 넣고 자연스럽게 해달라 하는데<br>돌려받으면 문장은 진짜 매끄러워...<br>근데 내가 맨날 쓰는 "암튼"이 하나도 없어 ㅎㅎ<br>괄호 열고 하던 딴소리도 다 지워져 있고<br>그래서 원본이랑 나란히 놓고 읽어봤거든<br>맞춤법은 AI 쪽이 다 맞아<br>근데 친구한테 보낼 거면 원본 보낼 듯<br>요즘은 맞춤법만 고쳐달라고 해 |
| 2 | Instagram caption: digging sweet potatoes with my kid | `sns` daily life, log, 반말 | 인친님들 주말에 애랑 할머니네 밭에서 고구마 캤어<br>호미 쥐여줬더니 고구마는 안 캐고 지렁이만 찾더라 ㅋㅋ<br>결국 한 바구니는 내가 다 캠..<br>다들 캔 고구마 바로 먹어 아님 며칠 말려?? |
| 3 | Farming community post in a farmer's voice, November (1/3) | `farmer`, show, 합니다체 | ☆★서리태 탈곡 했습니다★☆<br><br>오늘 바람이 없어서 서리태 털었습니다.<br><br>두마지기 밭에서 약3가마 정도 나왔습니다 ^^<br><br>올해는 콩알이 굵은데 다들 작황은 어떠신지요? ♧♧♧ |
| 4 | Same request (2/3) | `farmer`, ask, 합니다체 | 충남 당진에서 꿀고구마 300평 했습니다.<br><br>이번주에 캤는데 껍질에 검은 반점 같은게 올라온게 많습니다...<br><br>밭이물빠짐이안좋아서9월에비많이온게원인인가싶습니다.<br><br>캔지 일주일 정도 됐고 창고에 신문지 깔고 두었습니다.<br><br>무슨 병인지 먹어도 되는지 궁금합니다.<br><br>※판매할 것은 따로 골라놨습니다. |
| 5 | Same request (3/3) | `farmer`, log, 합니다체 | 안녕하세요♡<br><br>오늘 아침 기온이 영하로 떨어져서 대봉감 땄습니다<br><br>사다리 놓고 남편이랑 둘이 약300개 정도 땄읍니다..<br><br>높은데 달린건 장대로 땄는데 몇일 더 두면 홍시 될 것 같습니다.<br><br>꼭대기 몇개는 까치밥으로 남겨 두었습니다<br><br>담주에는 곶감 깎으려고 합니다. 손은 많이 가도 깎는 일은 즐겁습니다. |

## Layout

```text
skills/ssul/SKILL.md          the skill
skills/ssul/references/       voice, personas, shapes, hooks, AI tells, disclosure, loaded on demand
skills/ssul/scripts/          roll.py (random settings)
.claude-plugin/               plugin manifests
```

## Credits

Built by running 16 open-source writing skills on real Korean posts; no text was copied. What came from each project is in [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

## License

[MIT](LICENSE)
