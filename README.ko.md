<p align="center">
  <img src="assets/banner.png" alt="ssul 배너" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a> · <b>한국어</b>
</p>

# ssul

**AI가 쓴 티 안 나는 한국어 SNS 글.**

*ssul*은 친구한테 털어놓는 진짜 이야기, 그 "썰"입니다. Claude Code와 Codex에서 쓰는 에이전트 스킬로, 스레드, X, 인스타 캡션, 커뮤니티에 올릴 짧은 한국어 글을 쓰고, 다듬고, 검사합니다.

오픈소스 글쓰기 스킬 네 갈래를 하나로 합쳤고, 서로 부딪히는 규칙은 정리했습니다.

- **훅**: 첫 줄 공식과 첫 줄이 죽는 네 가지 이유
- **스토리텔링**: 마지막 줄부터 쓰고, 장면은 "근데"와 "그래서"로 잇기
- **한국어 AI 티 제거**: 교훈형 마무리, 알맹이 없는 뒤집기, 명사화, 번역투, 습관적 3개 나열
- **구어체**: 실제로 말할 때 쓰는 어미를 분야별로 (AI, 개발 피드는 반말 혼잣말, 일상은 해요체), 보고서 단어 금지

## 왜 만들었나

인기 있는 글쓰기 스킬 열댓 개를 함께 돌려 스레드 글을 써봤습니다. 첫 줄은 그럴듯하고 문장도 매끄러운데 계속 AI가 쓴 글처럼 읽혔습니다. 문체 문제가 아니었습니다. 장면, 숫자, 대사가 지어낸 것이었습니다. 이건 문체를 아무리 다듬어도 못 고칩니다.

그래서 ssul은 **진짜 재료**부터 받습니다. 사용자에게 묻거나 대화에서 찾습니다. 지어낸 디테일을 사실처럼 내놓지 않습니다. 문체 점검은 그다음입니다.

## 하는 일

| 모드 | 이렇게 말하면 | 이걸 받습니다 |
|---|---|---|
| 초안 | 주제나 메모 | 글 하나 + 짧은 메모 3줄 이내 |
| 다듬기 | 초안 + "AI 같아", "너무 무거워" | 고친 글과 바뀐 점 |
| 검사 | "검사해줘" | 문제 구간과 정확한 문구만 |
| 훅 | "첫 줄만" | 서로 다른 유형의 첫 줄 3개 + 추천 |
| 이미지 | "이미지 만들어줘" | 글에 맞는 4:5 후킹 이미지, 한글 문구 한 글자씩 확인 |
| 답글 | 글 + "답글" | 저마다 구체적인 한 가지를 더하는 답글 2~3개, 또는 인용 글 |
| 분석 | 터진 글 붙여넣기 | 글마다 숨은 패턴, 요약, 내 재료로 쓸 아이디어 |
| 바꾸기 | 블로그, 영상, README + "스레드로" | 가장 강한 포인트로 글 1~3개 |
| 스레드 | "길게 / 연재" | 게시물별 글자 수를 표시한 여러 개짜리 스레드 |
| 계획 | "뭐 올리지" | 내가 가진 실제 재료와 연결된 일주일 아이디어 |
| 프로필 | "프로필" | 바이오 2안과 고정 게시물 추천 |
| 영상 | "릴스 대본 / 캡션" | 화면 자막이 붙은 대본과 캡션 |

모든 글은 이 점검을 거칩니다.

1. **사실**: 숫자, 이름, 대사, 사건은 진짜이거나 `[이렇게]` 자리표시로 표시
2. **처음 보는 사람 테스트**: 맥락 없이 읽어도 모든 줄이 이해되는지
3. **무게 테스트**: 서론, 가짜 목록, 교훈이 없는지
4. **가치 테스트**: 처음 보는 사람이 쓸 만한 정보, 공감할 감정, 진짜 웃음 중 하나를 얻는지. 억지 개그 금지
5. **한국어 AI 티**: S1~S3 심각도로 분류. 이모지, 중간점(`·`), 동그라미 숫자(①), 유니코드 화살표(→)도 포함
6. **구어체**: 같은 어미 4번 연속 금지, 보고서 단어 금지
7. **플랫폼**: 500자 이내, 해시태그 0~1개, 질문은 최대 하나
8. **광고 표시**: 대가를 받았으면 공정위 기준대로 글 첫 부분에 한국어로 밝히기 (광고, 협찬)
9. **의미와 맞춤법**: 다듬을 때 부정, 조건, 숫자는 그대로, 명백한 맞춤법만 고치고 일부러 쓴 구어는 유지

## 예시

입력: *"오늘 GitHub에서 스킬 저장소 16개 깔면서 훅이랑 스크립트 확인했어. AI 쪽 사람들 보라고 스레드 글 써줘."*

형식: 발견. 말투: 반말 혼잣말 (AI, 개발 분야 기본값).

```text
클로드 스킬 GitHub에서 16개 깔아보면서 알게 된 거

1. 어떤 플러그인은 깔면 내가 메시지 보낼 때마다 스크립트가 돎
2. 어떤 스킬은 지침이 파일에 없고 쓸 때마다 인터넷에서 받아옴. 내용이 언제든 바뀔 수 있다는 뜻
3. 라이선스 없는 레포도 있음. 이건 가져다 쓰면 안 됨

그래서 이제 깔기 전에 SKILL.md랑 hooks 폴더는 꼭 열어봄
```

모든 항목은 설치하면서 직접 확인한 사실입니다. 그게 핵심입니다.

### 농사 정보 글과 후킹 이미지

입력: *"농민 대상 스레드 글. 11월 초, 첫 영하 시기. 경험담은 없으니 확인된 사실로."*

형식: 발견. 말투: 해요체 (일상, 농사 분야 기본값). 첫 줄은 후보 3개(숫자형, 질문형, 뒤집기형) 중 첫 줄 점검 네 가지를 모두 통과한 뒤집기형으로 골랐습니다.

```text
영하 예보 뜨면 배추보다 무가 먼저예요

무는 0도 근처만 가도 얼어요
배추는 영하 3~4도까진 버티고요

그래서 무는 영하 되기 전에 미리 캐두고
배추는 영하 예보 나올 때 겉잎 묶어주면 돼요
너무 일찍 묶으면 오히려 덜 자라거든요

김장 무 얼리면 진짜 아깝잖아요
```

숫자는 서울시, 충남 농업기술센터와 텃밭 매뉴얼에서 확인했고, 기관마다 기준이 다른 값은 가장 보수적인 쪽을 썼습니다.

이어서: *"이 글로 이미지 만들어줘"* (이미지 모드). 글의 첫 줄을 제목으로 쓰고, 보여주기 전에 한글을 한 글자씩 확인했습니다.

<p align="center">
  <img src="assets/examples/farm-hook.jpg" alt="후킹 이미지: 서리 내린 새벽 밭, 앞에 무, 뒤에 묶은 배추, 제목 영하 예보 뜨면 배추보다 무가 먼저" width="360">
</p>

<p align="center"><sub>AI로 생성한 이미지입니다 (Codex CLI의 GPT 이미지 생성). 올릴 때는 플랫폼의 AI 표시를 켜세요.</sub></p>

## 필요한 것

- 글 쓰기, 다듬기, 검사에는 따로 필요한 게 없습니다.
- 이미지 모드: 이미지 생성이 켜진 [Codex CLI](https://github.com/openai/codex) 또는 `OPENAI_API_KEY`.

## 설치

### Claude Code (플러그인)

```text
/plugin marketplace add nathankim0/ssul
/plugin install ssul@ssul
```

### Claude Code 또는 Codex (직접 복사)

```bash
git clone https://github.com/nathankim0/ssul.git
cp -R ssul/skills/ssul ~/.claude/skills/ssul     # Claude Code
cp -R ssul/skills/ssul ~/.codex/skills/ssul      # Codex
```

### Agent Skills를 지원하는 에이전트

```bash
npx skills add nathankim0/ssul
```

## 사용법

```text
/ssul 오늘 회의에서 있었던 일로 스레드 글 하나 써줘
/ssul 이 글 AI 같은데 다듬어줘: <초안>
/ssul 검사만 해줘: <초안>
/ssul 첫 줄만 3개
/ssul 이 글로 이미지 만들어줘
/ssul 이 글에 답글 달아줘: <글>
/ssul 이 블로그 글 스레드로 바꿔줘: <본문>
/ssul 이번 주 뭐 올리지
```

진짜 재료가 부족하면 짧은 질문을 3개까지 먼저 합니다. 예전에 쓴 글을 2~3개 붙여주면 그 말투에 맞추고, 동의하면 말투와 썰을 `~/.ssul/`에 저장해 다음부터 다시 묻지 않습니다.

## 구성

```text
skills/ssul/SKILL.md              스킬 본문
skills/ssul/references/
  conflicts.md                    원본 스킬끼리 부딪히는 22가지와 정리 기준
  hooks.md                        첫 줄 유형과 실패 패턴 (한국어로 새로 작성)
  korean-voice.md                 구어체 어미와 한국어 AI 티 (S1~S3)
  interview.md                    진짜 재료를 받는 질문
  formats.md                      장면, 고백, 뒤집기, 목록, 질문, 한두 줄, 발견, 한마디
  checklist.md                    최종 점검과 검사 출력 형식
  images.md                       후킹 이미지 규격, 생성 프롬프트, 점검
  disclosure.md                   광고, 협찬, AI 표시 규칙 (공정위 기준)
  polish.md                       의미 보존 윤문과 맞춤법
  reply.md                        답글과 인용 글
  analyze.md                      터진 글 분석
  repurpose.md                    다른 콘텐츠를 글로 바꾸기
  threads.md                      여러 개짜리 스레드, 첫 댓글, 게시
  voice-bank.md                   말투 프로필과 스토리 뱅크 저장
  plan.md                         주간 콘텐츠 계획
  profile.md                      바이오와 고정 게시물
  short-video.md                  릴스, 쇼츠, 틱톡 대본과 캡션
.claude-plugin/                   Claude Code 플러그인, 마켓플레이스 매니페스트
```

## 참고한 프로젝트

아래 16개 저장소를 설치하고 실제 한국어 스레드 글에 돌려보면서 만들었습니다. 문장은 가져오지 않았습니다. 저장소마다 살펴본 스킬, ssul이 가져온 것, ssul 안의 위치를 적었습니다. 자세한 내용은 [ATTRIBUTIONS.md](ATTRIBUTIONS.md)에 있습니다.

### 훅과 숏폼 콘텐츠

| 저장소 | 살펴본 스킬 | ssul이 가져온 것 | ssul 안의 위치 |
|---|---|---|---|
| [vyralcontent/content-skills](https://github.com/vyralcontent/content-skills) | `viral-hooks`, `viral-short-form`, `viral-captions-and-ctas`, `viral-tiktok-content`, `viral-instagram-reels`, `viral-youtube-shorts`, `viral-short-form-ideas` | 여러 유형의 훅 뽑기, 약속과 내용 맞추기, 영상 훅 3요소, 화면 자막, 캡션, CTA 규칙, 해시태그의 실제 효과, 콘텐츠 기둥 | hooks.md, short-video.md, plan.md |
| [artemnovitckii/content-skills](https://github.com/artemnovitckii/content-skills) | `viral-hooks`, `storytelling`, `anti-ai-writing`, `dumbify` | 첫 줄이 죽는 네 가지 이유, 근데/그래서 전개, 마지막 줄 먼저, 알맹이 있는 대비 구분, 처음 보는 사람도 읽히는 쉬운 말 | SKILL.md, hooks.md, korean-voice.md |
| [rediumvex/viral-hooks-skill](https://github.com/rediumvex/viral-hooks-skill) | `viral-hooks` | 심리 유형별 훅 | hooks.md |

### 스레드와 X

| 저장소 | 살펴본 스킬 | ssul이 가져온 것 | ssul 안의 위치 |
|---|---|---|---|
| [sergebulaev/threads-skills](https://github.com/sergebulaev/threads-skills) | `threads-post-writer`, `threads-hook-extractor`, `threads-humanizer`, `threads-reply-drafter`, `threads-repurposer`, `threads-content-planner`, `threads-profile-optimizer`, `threads-audience-insights` | 목표별 글 형식, 스토리 뱅크와 말투 프로필, 수치 지어내지 않기, 500자, 해시태그 1개, 답글, 바꾸기, 계획, 프로필, 글 분석 절차 | formats.md, voice-bank.md, reply.md, repurpose.md, plan.md, profile.md, analyze.md |
| [sergebulaev/x-skills](https://github.com/sergebulaev/x-skills) | `x-post-writer`, `x-thread-builder`, `x-hook-extractor`, `x-reply-drafter`, `x-repurposer` | 짧은 글 훅, 스레드 구조 (첫 글의 약속, 앞에 핵심 배치, 각 글 독립) | threads.md, hooks.md |

### 한국어 윤문과 구어체

| 저장소 | 살펴본 스킬 | ssul이 가져온 것 | ssul 안의 위치 |
|---|---|---|---|
| [Burntgogi/ai-slop-thresher](https://github.com/Burntgogi/ai-slop-thresher) | `ai-slop-thresher`, `thresh` | 의미 보존 (부정, 조건, 제한어), 경험 지어내지 않기 | polish.md, SKILL.md |
| [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai) | `humanize-korean`, `humanize-scan` | 한국어 AI 티 분류, 사실과 숫자 고정 | korean-voice.md |
| [amondnet/yoonmoon](https://github.com/amondnet/yoonmoon) | `humanize`, `restyle`, `proofread`, `detect`, `translate-polish` | 윤문, 교정, 문체 변환 분리, 맞춤법 교정표, 짧은 SNS 글 별도 처리 | polish.md, korean-voice.md |
| [hjongc/humanizer-kr](https://github.com/hjongc/humanizer-kr) | `humanizer-kr` | 글쓴이의 실제 글에 말투 맞추기 | voice-bank.md |
| [leeandev/stop-slop-ko](https://github.com/leeandev/stop-slop-ko) | `stop-slop-ko`, `jasoseo` | `~함`은 문서용, 인터뷰로 실제 경험 받기 | korean-voice.md, interview.md |
| [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) | `korean-humanizer`, `korean-slang-writing` | AI 티 심각도, 유행어 신선도 기준 | korean-voice.md, conflicts.md |
| [crazyrookie777/gueoche-guard](https://github.com/crazyrookie777/gueoche-guard) | `gueoche` | 구어체 점검이라는 아이디어 (라이선스가 없어 아무것도 가져오지 않음) | korean-voice.md |

### 말투, 리서치, 규정, 마케팅

| 저장소 | 살펴본 스킬 | ssul이 가져온 것 | ssul 안의 위치 |
|---|---|---|---|
| [SorenKK/writing-signature](https://github.com/SorenKK/writing-signature) | `writing-signature` | 글쓴이 본인의 글로 말투 측정 | voice-bank.md |
| [svy04/rutter](https://github.com/svy04/rutter) | `social-media-kr`, `influencer-kr`, `ad-compliance-kr`, `copy-edit-kr` | 한국 채널 맥락, 공정위 광고, 협찬 표시 규정, 근거 없는 최고, 1위 표현 금지 | disclosure.md, profile.md, threads.md |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | `social`, `copywriting`, `marketing-psychology`, `image` | SNS 카피 배경지식, 마케팅 이미지 기준 | images.md, plan.md |
| [ScrapeCreators/social-media-research-skills](https://github.com/ScrapeCreators/social-media-research-skills) | `outlier-post-finder`, `trend-discovery`, `comment-mining`, `content-repurposing` | 쓰기 전에 튄 글 분석, 원본 하나로 여러 글 만들기 | analyze.md, repurpose.md |

## 라이선스

[MIT](LICENSE)
