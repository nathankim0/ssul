<p align="center">
  <img src="assets/banner.png" alt="ssul 배너" width="100%">
</p>

<p align="center">
  <a href="README.md">English</a> · <b>한국어</b>
</p>

# ssul

**AI가 쓴 티 안 나는 한국어 SNS 글.**

*ssul*은 친구한테 털어놓는 진짜 이야기, 그 "썰"입니다. Claude Code와 Codex에서 쓰는 에이전트 스킬로, 스레드·X·인스타 캡션·커뮤니티에 올릴 짧은 한국어 글을 쓰고, 다듬고, 검사합니다.

오픈소스 글쓰기 스킬 네 갈래를 하나로 합쳤고, 서로 부딪히는 규칙은 정리했습니다.

- **훅**: 첫 줄 공식과 첫 줄이 죽는 네 가지 이유
- **스토리텔링**: 마지막 줄부터 쓰고, 장면은 "근데"와 "그래서"로 잇기
- **한국어 AI 티 제거**: 교훈형 마무리, 알맹이 없는 뒤집기, 명사화, 번역투, 습관적 3개 나열
- **구어체**: 실제로 말할 때 쓰는 어미, 보고서 단어 금지

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

모든 글은 이 점검을 거칩니다.

1. **사실**: 숫자, 이름, 대사, 사건은 진짜이거나 `[이렇게]` 자리표시로 표시
2. **처음 보는 사람 테스트**: 맥락 없이 읽어도 모든 줄이 이해되는지
3. **무게 테스트**: 서론, 가짜 목록, 교훈이 없는지
4. **한국어 AI 티**: S1~S3 심각도로 분류
5. **구어체**: 같은 어미 4번 연속 금지, 보고서 단어 금지
6. **플랫폼**: 500자 이내, 해시태그 0~1개, 질문은 최대 하나

## 예시

입력: *"오늘 있었던 일로 글 써줘. 클로드한테 스레드 글 부탁했다가 스킬 저장소를 16개 깔았어."*

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

여기 나온 일은 전부 실제로 있었던 일입니다. 그게 핵심입니다.

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
```

진짜 재료가 부족하면 짧은 질문을 3개까지 먼저 합니다. 예전에 쓴 글을 2~3개 붙여주면 그 말투에 맞춥니다.

## 구성

```text
skills/ssul/SKILL.md              스킬 본문
skills/ssul/references/
  conflicts.md                    원본 스킬끼리 부딪히는 14가지와 정리 기준
  hooks.md                        첫 줄 유형과 실패 패턴 (한국어로 새로 작성)
  korean-voice.md                 구어체 어미와 한국어 AI 티 (S1~S3)
  interview.md                    진짜 재료를 받는 질문
  formats.md                      장면, 고백, 뒤집기, 목록, 질문
  checklist.md                    최종 점검과 검사 출력 형식
.claude-plugin/                   Claude Code 플러그인·마켓플레이스 매니페스트
```

## 참고한 프로젝트

아래 프로젝트를 읽고 만들었습니다. 문장은 가져오지 않았습니다. 자세한 내용은 [ATTRIBUTIONS.md](ATTRIBUTIONS.md)에 있습니다.

Burntgogi/ai-slop-thresher · svy04/rutter · sergebulaev/threads-skills · sergebulaev/x-skills · vyralcontent/content-skills · artemnovitckii/content-skills · rediumvex/viral-hooks-skill · coreyhaines31/marketingskills · ScrapeCreators/social-media-research-skills · amondnet/yoonmoon · epoko77-ai/im-not-ai · hjongc/humanizer-kr · leeandev/stop-slop-ko · NomaDamas/k-skill · SorenKK/writing-signature · crazyrookie777/gueoche-guard

## 라이선스

[MIT](LICENSE)
