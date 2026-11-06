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
- **랜덤 변주**: ㅋㅋ, 말투, 길이, 시작, 끝맺음을 매번 실제 난수로 뽑음 (`scripts/roll.py`). 글마다 말투가 같지 않게
- **사람 냄새**: 팔로워한테 말 걸기, 일어난 순서대로 말하기, `..`와 `??` 남기기. 너무 정돈된 글은 AI처럼 읽힘
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

모두 ssul v1.6으로 만들었습니다. 사실은 예시마다 적은 출처에서 가져왔고, 지어낸 내용은 없습니다.

### 1. 같은 사실, 세 가지 랜덤 말투

입력: *"마늘 언제 덮는지 글, 세 버전으로."* ssul이 `roll.py --n 3 --pool warm`을 돌려 글마다 다른 설정을 뽑았습니다. 세 개 중 두 개가 `laugh: none`이 나와서 ㅋ가 아예 없습니다.

롤: `banmal_talk, none, .., long, address, question`

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

롤: `banmal_talk, ㅋㅋ, none, long, address, stop`

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

롤: `banmal_talk, none, none, short, straight, question`

```text
마늘 너무 일찍 덮으면 오히려 얼 수 있대
싹이 겨울 오기 전에 웃자라서 그렇다고
11월 중순에서 하순쯤 덮는 게 좋대
다들 언제 덮어?
```

사실: 너무 일찍 덮으면 겨울 전에 싹이 웃자라 언 피해, 11월 중순에서 하순 피복, 덮기 전 뿌리 확인과 물 주기 (이천시농업기술센터). 너무 일찍 심으면 쪽이 갈라지고 늦으면 뿌리내림이 나쁨, 깊이는 마늘쪽 길이의 2~3배 (농촌진흥청).

### 2. 스레드, 호칭 켜기

입력: *"오늘 오픈소스 스킬 3개 만들었는데 별이 다 0개야. 스레드 글."* 롤: `banmal_talk, ㅋㅋ, .., short, address, reaction`

```text
스친이들 나 오늘 스레드 글 하나 쓰려다가 오픈소스를 3개 만들어버렸어..
깃허브 올려놓고 보니까 별이 셋 다 0개 ㅋㅋ
이게 맞냐고
```

별 개수는 글을 쓴 2026-11-06에 GitHub에서 확인한 값(세 개 모두 0개)입니다. ssul은 그날 오후 첫 별을 받았습니다.

### 3. 커뮤니티, 호칭 끄기, 후킹 이미지

입력: *"커뮤니티에 올릴 병맛 농사 글."* 롤: `banmal_talk, ㅋㅋㅋ, ..., short, address, stop`. 커뮤니티는 호칭을 끄므로 시작이 `straight`로 바뀌었습니다.

```text
배추도 패딩 입히는 타이밍이 있대 ㅋㅋㅋ
겉잎 끈으로 묶어주는 게 배추 패딩인데 너무 일찍 입히면 답답해서 덜 큰대...
그래서 영하 예보 뜰 때 입히는 거래
무는 0도만 돼도 얼어서 그 전에 캐야 된대
```

사실: 겉잎은 영하 예보가 나올 때 묶고, 너무 일찍 묶으면 덜 자람. 무는 0도 안팎에서 얼 수 있어 먼저 캠 (서울시 농업기술센터).

이어서 *"이미지 만들어줘"* (이미지 모드). 첫 줄을 제목으로 쓰고, 한글을 한 글자씩 확인했습니다.

<p align="center">
  <img src="assets/examples/cabbage-hook.jpg" alt="일러스트: 겉잎을 패딩처럼 묶은 배추와 떨고 있는 무, 제목 배추도 패딩 입히는 타이밍이 있대" width="360">
</p>

<p align="center"><sub>AI로 생성한 이미지입니다 (Codex CLI의 GPT 이미지 생성). 올릴 때는 플랫폼의 AI 표시를 켜세요.</sub></p>

### 4. 광고 표시가 필요한 글 다듬기

입력: 테스트용으로 만든 가상 초안이며 실제 게시글이 아닙니다.

```text
이번에 OO브랜드에서 보내주셨어요! 써보니까 진짜 좋아서 할께요 추천. 7일 이내에만 무료 반품 가능하대요 ㅋㅋ 체험단으로 받은거에요 #OO브랜드
```

결과:

```text
[광고] OO브랜드에서 제품을 무료로 제공받았어요

써보니까 진짜 좋아서 추천할게요
7일 이내에만 무료 반품 가능하대요 ㅋㅋ
```

- "보내주셨어요", "체험단", 브랜드명 해시태그는 공정위 기준 광고 표시로 인정되지 않아, 첫 줄에 분명한 표시를 넣었습니다.
- "7일 이내에**만**"은 반품 기한을 제한하는 말이라 그대로 뒀습니다.
- "할께요"는 "할게요"로 고치고, ㅋㅋ는 남겼습니다.

## 필요한 것

- 말투 변주용 Python 3 (`scripts/roll.py`, 표준 라이브러리만 사용). 없으면 ssul이 직접 고릅니다.
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
/ssul 스친 빼고 다시 써줘
/ssul 커뮤니티용으로 써줘
/ssul 다시 굴려
```

진짜 재료가 부족하면 짧은 질문을 3개까지 먼저 합니다. 스친이들, 인친님들, 트친들 같은 호칭은 플랫폼에 맞춰 넣고 "스친 빼고"처럼 켜고 끌 수 있습니다. 예전에 쓴 글을 2~3개 붙여주면 그 말투에 맞추고, 동의하면 말투와 썰을 `~/.ssul/`에 저장해 다음부터 다시 묻지 않습니다.

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
  variation.md                    랜덤 말투 설정과 우선순위
skills/ssul/scripts/roll.py       말투 설정을 뽑는 스크립트 (표준 라이브러리만 사용)
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
