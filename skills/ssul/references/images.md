# Images

Run only when the user asks for an image ("이미지 만들어줘", "썸네일", "카드 이미지"). The image carries the post's first line; the post carries the rest.

## Spec

| Item | Rule |
|---|---|
| Size | portrait 4:5 (about 1080x1350) for Threads and Instagram; 1:1 if the user asks |
| Headline | the post's first line, 2 lines max, about 6 to 12 Korean characters per line |
| Emphasis | one phrase in a contrasting color (yellow on dark, or red on light); everything else white or black |
| Label | optional one small label with the key number or contrast from the post; separate items with a space or `/`, never a middle dot `·` |
| Scene | the post's real subject, concrete and in season: the actual object, place, and time of year |
| Style | realistic photo for information and farm or food posts; simple illustration for opinions and hot takes |
| Never | emoji, circled numbers, text not given in the prompt, logos, watermarks, brand names, real people's faces, invented events presented as real |

Every number in the image must match the post and its source. A short label can change meaning ("배추 -3℃" can read as "cabbage freezes at -3℃"); if a number cannot be labeled without that risk, leave it out.

## Generate

Use GPT image generation through the Codex CLI. Check once: `codex features list | grep image_generation` should say `true`.

```bash
OUT=<scratchpad>/ssul-img; mkdir -p "$OUT"
codex exec --skip-git-repo-check --sandbox workspace-write -C "$OUT" \
  "Use your image generation tool to create ONE social media image, portrait 4:5 (about 1080x1350). \
Purpose: <one sentence: what the post tells the reader>. \
Visual: <style>, <the concrete scene: objects, place, season, light>. \
Typography: large bold <white> Korean headline with a subtle shadow at the top, exactly two lines: \
line 1 '<line 1>', line 2 '<line 2>' (make '<emphasis phrase>' <yellow>). \
<optional: At the bottom, a small rounded dark label with exactly this text: '<label>'.> \
Korean text must be spelled exactly as given, no other text, no logos, no watermarks. \
Save the final image as ./hook.png (PNG) and print the absolute path." \
  > "$OUT/log.txt" 2>&1
```

If Codex is not available but `OPENAI_API_KEY` is set, call the OpenAI Images API with the same prompt. If neither exists, say so and give the user the prompt to paste into an image tool.

## Check before showing

Open the image and check:

1. **Korean text**: every character matches the prompt exactly. Image models misspell Korean; one wrong syllable means regenerate.
2. **No extra text**, logos, or watermarks.
3. **Meaning**: the image does not claim more than the post (numbers, causes, before and after).
4. **Readable at phone size**: the headline is legible in a feed thumbnail.

Regenerate up to 2 times on failure. If Korean text keeps failing, generate the scene without text and tell the user to add the headline in an editor.

## Output

Show the image, the file path, and at most 2 notes. Always include: realistic AI images should carry the platform's AI label (Threads and Instagram: "AI 정보"), and a real photo beats a generated one when the user has it.
