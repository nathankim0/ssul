# Changelog

## v1.3.0 (2026-11-06)

Covers the gaps found when auditing ssul against all 16 source repositories.

### Added
- Modes: reply (replies and quote posts), analyze (pasted viral posts), repurpose (blog, video, README into posts), thread (multi-post threads), plan (a week of ideas tied to real material), profile (bio and pinned post), video (Reels, Shorts, TikTok script, on-screen text, caption).
- Sponsorship and AI disclosure by Korean FTC rules: placement in the first part, approved and banned wording, hashtags, photos, video, AI-generated people (`references/disclosure.md`).
- Meaning-safe polishing (negation, conditions, limits, numbers) and a proofreading pass that keeps intentional casual style (`references/polish.md`).
- Voice profile and story bank saved to `~/.ssul/` with the user's consent (`references/voice-bank.md`).
- First-comment links and posting guidance without unverified posting-time claims (`references/threads.md`).
- Step 0 (load voice and story bank) and passes 8 and 9 (disclosure; meaning and spelling).
- Conflicts 17 to 22.

### Changed
- README credits now list the skills studied and what ssul actually took from each.

## v1.2.0 (2026-11-06)

### Added
- Image mode: "이미지 만들어줘" generates a 4:5 hook image for the post with GPT image generation through the Codex CLI (OpenAI Images API as fallback). The post's first line becomes the headline; every Korean character is checked before the image is shown; numbers must not claim more than the post.
- `references/images.md`: spec, prompt template, checks, and output notes (AI label reminder).

## v1.1.0 (2026-11-06)

### Added
- Three shapes: One-liner, Finding, Hot take. Shape is picked by what the material has: an event, usable facts, or an attitude.
- Value test: a stranger must get a usable fact, a recognizable feeling, or a real laugh.
- Register by niche: 반말 혼잣말 for AI, dev, startup, investing, and hot takes; 해요체 for daily life and brands. Pasted feed samples override the niche default.
- Conflicts 15 and 16: no manufactured humor; no posts about the writing session itself.

### Changed
- Register selection order: the user's own posts, then pasted feed samples, then the niche default (was: always 해요체).
- README example and the Scene example no longer use a story about the writing session itself (now a Finding post, and a placeholder-marked scene).

## v1.0.0 (2026-11-06)

First release.

- `ssul` skill with four modes: draft, polish, audit, hooks
- Real material first: interview questions, conversation mining, `[bracket]` placeholders for anything invented
- 14 conflicts between source writing skills, with rulings (`references/conflicts.md`)
- Korean first-line triggers and killers, 구어체 endings, Korean AI tells graded S1 to S3
- Five shapes: scene, confession, reversal, list, question
- Final checklist and audit output format
- Claude Code plugin and marketplace manifests
