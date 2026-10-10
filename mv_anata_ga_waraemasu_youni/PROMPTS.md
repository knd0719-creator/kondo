# 「あなたが笑えますように」 MV 일러스트 프롬프트 (PixAI / Tsubaki)

스토리보드: [STORYBOARD.md](./STORYBOARD.md)

## 공통 설정

- 모델: **Tsubaki** (자연어 문장형)
- 비율: **16:9 가로** (예: 1344×768 생성 → 업스케일로 1920×1080 이상). IL06·IL07·IL15는 줌을 크게 쓰므로 **2배 업스케일 권장**
- 구성: `구도·앵글 → 상황 → 동작/감정 → 배경·분위기 → the character's outfits : 외모 단어`
- 마지막 `the character's outfits :` 뒤만 고치면 수정 가능

## MV 전용 규칙

| 규칙 | 이유 |
|---|---|
| 「あなた」는 `1other, faceless, androgynous` + 회색 후드 + 어두운 코트로 고정 | 시청자가 자기를 겹쳐 볼 수 있도록. 모든 컷에서 같은 옷 |
| 미러 쌍(IL02↔IL08, IL03↔IL09, IL05↔IL10)은 **구도 문장을 거의 그대로** 두고 인물·시간대만 교체 | 2절 반전 연출. 가능하면 1절 그림을 레퍼런스(img2img)로 넣고 생성 |
| 문자가 들어갈 자리를 비워 둠 (`Leave empty space ...` 문장) | Verse = 좌우 세로쓰기, Chorus = 중앙~하단 가로 |
| 나비는 키 비주얼(IL07, IL15)과 IL05에만 그림. 나머지는 리졸브에서 소재 합성 | 움직이는 나비를 따로 얹기 위해 |
| 집 안 장면(IL10)은 `loafers` 삭제 | 실내에서 신발을 신지 않게 |

---

## Verse 1 / Intro

### IL01 — 해 질 녘 귀갓길 (인물 없음) · 컷 02–03, 50

```
A wide shot at eye level of an empty residential street on the way home at dusk. A narrow asphalt road stretches toward the horizon between low houses, utility poles and tangled power lines, with a pedestrian crossing in the foreground. The setting sun burns low and dusty orange behind the rooftops, and the sky fades into a cool blue-gray toward the top of the frame. A warm evening breeze carries a few dry leaves across the road, and the first streetlights flicker on one by one. Long shadows of the utility poles stretch across the white crossing stripes and bend over the curb. Leave empty space in the upper sky for title text. Intense cinematic lighting, highly detailed anime art style, quiet nostalgic twilight atmosphere. the character's outfits : no humans, scenery.
```

> 컷 50(Outro 낮 버전)은 리졸브 색보정으로 처리. 따로 그릴 경우 `at dusk` → `on a bright clear afternoon`, `dusty orange` → `soft white`, 마지막을 `gentle peaceful daytime atmosphere`로 교체.

### IL02 — 가방에 한숨을 넣는 손 · 컷 04–05 (IL08의 미러 원본)

```
A close-up from above of a pair of tired hands slowly opening a worn canvas shoulder bag on the way home at dusk, hands focus, face out of frame. A faint breath of white mist drifts down from above and sinks into the open bag, as if a sigh is being put away inside. A crumpled notebook, a phone and tangled earphones are visible in the bag. Dusky orange streetlight leaks in from the side, and a cold evening wind ruffles the loose sleeve. The heavy strap presses a deep crease into the fabric over the shoulder. Leave empty space on the right side of the frame. Intense cinematic lighting, highly detailed anime art style, weary twilight atmosphere. the character's outfits : hands only, gray hoodie sleeve, dark coat sleeve, canvas shoulder bag.
```

### IL03 — 횡단보도 앞 뒷모습 · 컷 06–07 (IL09의 미러 원본)

```
A wide shot from behind of a lone person standing at a pedestrian crossing at dusk, raising one hand to wave goodbye to two small distant friends walking away on the far side of the street. The person's face is not visible, and their shoulders are slightly slumped despite the cheerful wave. The traffic light glows red, and the evening wind pushes the hem of the loose coat. Car headlights streak past and scatter reflections across the asphalt. The person's long shadow stretches back toward the viewer over the white stripes. Leave empty space on the left side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, lonely after-school twilight atmosphere. the character's outfits : 1other, from behind, faceless, androgynous, short dark hair, gray hoodie, dark long coat, canvas shoulder bag, sneakers.
```

### IL04 — 육교 위에서 내려다보는 애슐리 · 컷 08–09 (첫 등장)

```
A medium shot from below of a gentle anime girl leaning on the railing of a pedestrian overpass at dusk, looking down at the viewer with a soft, knowing smile, hands clasped on the railing. Behind her, the orange sunset sky melts into blue, and city lights begin to glow along the road below. A soft evening wind blows across the overpass, and the warm light catches the dust in the air like tiny sparks. Her blonde hair streams sideways in the wind and the hem of her skirt sways against the railing. Leave empty space on the left side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, tender twilight atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, looking at viewer, white shirt, pink bowtie, large breasts, navy pleated skirt.
```

### IL05 — 어두운 방, 무릎을 안은 실루엣 · 컷 10–11 (IL10의 미러 원본)

```
A wide shot at eye level of a small dark bedroom at night, where a lone person sits on the floor against the side of the bed, hugging their knees with their face buried in their arms. The only light is a desk lamp on a cluttered desk, and its warm circle of light stops just short of the person, leaving them at the edge of the shadow. Through the window, distant city lights blur in the night, and a single softly glowing blue butterfly rests on the outside of the glass. A thin gap in the window lets the curtain sway gently, and its shadow ripples across the floor. Leave empty space on the right side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, silent lonely night atmosphere. the character's outfits : 1other, faceless, face buried in knees, androgynous, short dark hair, gray hoodie, sweatpants, barefoot.
```

## Pre-Chorus 1 / Chorus 1

### IL06 — 풀린 신발 끈과 손을 뻗는 애슐리 · 컷 12–15 (14.5초 사용, 고해상도)

```
A low-angle ground-level POV shot with foreshortening: in the bottom corner of the frame, the viewer's own foot in a worn gray sneaker steps into view, its shoelace untied and lying loose on the warm asphalt. In front of the viewer, a gentle anime girl crouches down and reaches one hand toward the viewer's untied lace, looking up with a soft smile. She wears her own polished brown loafers with black socks, neatly together under her. The golden sunset fills the background with a hazy glow and lens flare. A light breeze lifts the loose end of the shoelace and rolls a few small petals along the ground. Her blonde hair falls forward over her shoulder as she leans in, and her skirt pools around her crouching knees. Leave empty space along the bottom center of the frame for text. Intense cinematic lighting, highly detailed anime art style, warm gentle sunset atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, looking at viewer, white shirt, pink bowtie, large breasts, navy pleated skirt, black socks, brown loafers, squatting, pov.
```

> 그래도 애슐리 발에 스니커가 나오면 **플랜 B**: 스니커를 프롬프트에서 완전히 빼고, 풀린 끈을 애슐리 자신의 로퍼로 바꾼 버전. 「あなた」의 발은 리졸브에서 IL14의 스니커를 잘라 얹거나 생략.
>
> ```
> A low-angle ground-level shot of a gentle anime girl crouching down on the warm asphalt at sunset, looking up at the viewer with a soft smile while reaching one hand toward the viewer, as if offering to help. Beside her, a long loose ribbon of untied lace trails on the ground in the foreground. The golden sunset fills the background with a hazy glow and lens flare. A light breeze lifts the loose end of the lace and rolls a few small petals along the ground. Her blonde hair falls forward over her shoulder as she leans in, and her skirt pools around her crouching knees. Leave empty space along the bottom center of the frame for text. Intense cinematic lighting, highly detailed anime art style, warm gentle sunset atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, looking at viewer, white shirt, pink bowtie, large breasts, navy pleated skirt, black socks, brown loafers, squatting.
> ```

### IL07 ★ — 노을 역광 키 비주얼 · 컷 16–19 (썸네일 후보)

```
A cowboy shot at eye level of a gentle anime girl standing on a riverside embankment, backlit by a huge setting sun, reaching one hand out toward the viewer with foreshortening, as if offering to hold their hand. She is placed on the right third of the frame, smiling softly with slightly teary eyes. Dozens of glowing blue butterflies flutter up around her into the golden sky, and the warm wind carries sparkling motes of light. The sunlight shines through her blonde hair and makes its edges glow, while her hair and skirt sway toward the left. Leave empty space in the lower center of the frame for large lyric text. Intense cinematic lighting, highly detailed anime art style, warm hopeful sunset atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, teary eyes, looking at viewer, outstretched hand, white shirt, pink bowtie, large breasts, navy pleated skirt.
```

## Verse 2 (미러 — 애슐리의 과거)

### IL08 — 비 오는 밤, 가방을 여는 애슐리의 손 · 컷 20–21 (IL02와 같은 구도)

```
A close-up from above of a pair of slender tired hands slowly opening a school bag on the way home on a rainy night, hands focus, face out of frame. A faint breath of white mist drifts down from above and sinks into the open bag, as if a sigh is being put away inside. Neatly packed textbooks and a thick medical reference book are visible in the bag, and a small blue butterfly keyring hangs from the zipper. Cold blue streetlight leaks in from the side, and raindrops streak down and bead on the bag. Water drips from the wet cuff of the shirt sleeve onto the leather. Leave empty space on the right side of the frame. Intense cinematic lighting, highly detailed anime art style, cold rainy night atmosphere. the character's outfits : hands only, white shirt sleeve, school bag, blue butterfly keyring.
```

### IL09 — 우산 든 애슐리 뒷모습 · 컷 22 (IL03과 같은 구도)

```
A wide shot from behind of a lone anime girl standing at a pedestrian crossing on a rainy night, holding a transparent umbrella in one hand and raising the other to wave goodbye to two small distant friends walking away on the far side of the street. Her face is not visible, and her shoulders are slightly slumped despite the cheerful wave. The traffic light glows red, and heavy rain falls through the streetlight in silver lines. Car headlights streak past and shatter into reflections on the flooded asphalt. Raindrops bounce off her umbrella and her long shadow stretches back toward the viewer over the wet white stripes. Leave empty space on the left side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, lonely rainy night atmosphere. the character's outfits : from behind, blonde hair, medium hair, blue butterfly hairpin, white shirt, navy pleated skirt, black socks, loafers, school bag, transparent umbrella.
```

### IL09b — 돌아보는 애슐리 (차분) · 컷 23 「言い聞かせてたのはわたし」

```
A bust shot in three-quarter view of a gentle anime girl under a transparent umbrella on a rainy night, glancing back over her shoulder toward the viewer with a fragile smile that does not quite reach her eyes. Behind her, the red traffic light and city lights blur into soft bokeh. Rain streams down the umbrella and splashes in tiny crowns at its edge. Damp strands of blonde hair cling to her cheek, and drops of water slide down the clear umbrella between her and the viewer. Leave empty space on the left side of the frame. Intense cinematic lighting, highly detailed anime art style, bittersweet rainy night atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, teary eyes, looking back, white shirt, pink bowtie, large breasts, transparent umbrella.
```

### IL10 — 책상에 엎드린 애슐리 · 컷 24–27 (IL05와 같은 구도)

```
A wide shot at eye level of a small neat bedroom at night, where a lone anime girl has fallen asleep at her desk, resting her head on her folded arms beside towering stacks of medical textbooks and practice workbooks. The only light is the desk lamp, and its cold white circle of light falls on scattered notes covered in careful handwriting. Through the window, rain streaks down the glass over the dark city, and there is no butterfly outside. A thin gap in the window lets the curtain sway gently, and the pages of an open textbook flutter in the draft. Her pen has rolled to the edge of the desk, and a loose page has slipped onto the floor. Leave empty space on the right side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, silent exhausted night atmosphere. the character's outfits : blonde hair, medium hair, blue butterfly hairpin, closed eyes, white shirt, pink bowtie, navy pleated skirt, black socks.
```

## Pre-Chorus 2 / Chorus 2

### IL11 — 새벽 직전의 구불구불한 강변길 (선택) · 컷 28–31

```
A wide shot from above of a long winding riverside path just before dawn, curving in loose S-shapes along the water toward a distant bridge, with a small anime girl walking alone along one of the bends. The sky is turning from deep violet to pale pink at the horizon, and the river reflects the first faint light. A cool morning breeze bends the tall grass along the bank in silver waves and drifts thin mist over the water. Her footprints trail behind her on the dewy path. Leave empty space in the lower center of the frame for text. Intense cinematic lighting, highly detailed anime art style, quiet pre-dawn atmosphere. the character's outfits : blonde hair, medium hair, blue butterfly hairpin, white shirt, navy pleated skirt, black socks, loafers, school bag.
```

### IL12 — 새벽 강둑, 돌아보며 미소 · 컷 32–35 (IL07의 짝)

```
A medium shot in three-quarter view of a gentle anime girl standing on a grassy riverbank just before dawn, turning back toward the viewer with a soft, relieved smile and a light blush. She is placed on the right third of the frame. The sky behind her glows in layers of lavender, pale pink and the first thin line of gold over the river. A cool morning wind sweeps across the bank, scattering dew from the grass in glittering drops. Her blonde hair and skirt sway with the turn of her body, and a few strands catch the first light. Leave empty space in the lower center of the frame for large lyric text. Intense cinematic lighting, highly detailed anime art style, fresh gentle dawn atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, blush, looking back, white shirt, pink bowtie, large breasts, navy pleated skirt.
```

## Bridge

### IL13 — 웅덩이에 비친 가로등과 두 사람의 발 (선택) · 컷 36–37

```
A close-up from above of a puddle on a wet asphalt street after the rain at night, with two pairs of feet standing side by side at its edge: a pair of worn sneakers and a pair of loafers with black socks. The puddle mirrors a glowing streetlight and the faint silhouettes of the two people. The last drops fall from the eaves above and spread slow rings across the reflection. The rings distort the reflected streetlight into trembling ribbons of warm light. Leave empty space on the left side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, calm after-rain night atmosphere. the character's outfits : feet only, two people, sneakers, black socks, loafers.
```

### IL14 — 신발 끈을 묶어 주는 손 · 컷 38

```
A close-up at ground level of a pair of slender hands carefully tying the shoelace of someone's worn sneaker into a neat bow, on a wet street at night after the rain, hands focus. A few strands of blonde hair fall into the top of the frame as she leans in. Warm streetlight reflects on the damp asphalt, and a soft wind carries the last fine mist of the rain through the light. The freshly tied laces pull the sneaker snug, and tiny drops shake loose from them onto the ground. Leave empty space in the upper left of the frame for text. Intense cinematic lighting, highly detailed anime art style, tender quiet night atmosphere. the character's outfits : hands only, blonde hair, white shirt sleeve, sneakers.
```

### IL14b — 올려다보는 애슐리 (차분) · 컷 39 「ここにいてくださいね」

```
A bust shot from above of a gentle anime girl crouching on a wet street at night, looking up at the viewer with a soft smile and slightly teary eyes, as if asking them to stay. Warm streetlight falls on her face from above, and the wet asphalt around her shines with reflections. A gentle night breeze drifts the last fine mist of the rain through the light. Her blonde hair falls softly around her upturned face, and a single drop glistens at the corner of her eye. Leave empty space at the top of the frame. Intense cinematic lighting, highly detailed anime art style, tender quiet night atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, teary eyes, looking up, looking at viewer, white shirt, pink bowtie, large breasts.
```

## Final Chorus

### IL15 ★ — 아침 햇살, 나비 무리, 최고의 미소 · 컷 43–46 (메인 키 비주얼)

```
A medium shot at eye level of a gentle anime girl standing in a field of morning light on a hill, laughing brightly at the viewer with a blush, her hands clasped happily in front of her chest. Hundreds of blue butterflies burst up from the grass around her and spiral into the clear pale-blue sky. The morning sun pours in from behind her and fills the air with drifting golden motes. The rush of wings lifts her blonde hair and skirt and sends flower petals whirling past her. Leave empty space at the top center of the frame for large lyric text. Intense cinematic lighting, highly detailed anime art style, radiant hopeful morning atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, smile, open mouth, blush, looking at viewer, hands clasped, white shirt, pink bowtie, large breasts, navy pleated skirt.
```

### IL16 — 나란히 선 뒷모습, 하늘이 풀려 나감 · 컷 47–48

```
A wide shot from behind of two people standing side by side on a hilltop in the morning, a blonde anime girl and a person in a gray hoodie, looking out over a wide town beneath an endless sky. The sky above them is unraveling like loosened threads of colored light, pale blue, gold and soft pink strands drifting apart and spreading across the horizon. A gentle morning wind sweeps up the hill and carries the glowing threads over the town. The grass bends around their feet and her blonde hair streams toward the hoodie person's shoulder. Leave empty space in the upper center of the frame for text. Intense cinematic lighting, highly detailed anime art style, liberating morning atmosphere. the character's outfits : 2 people, from behind, blonde hair, medium hair, blue butterfly hairpin, white shirt, navy pleated skirt, black socks, loafers, 1other, androgynous, short dark hair, gray hoodie, sneakers.
```

## Outro

### IL17 — 묶인 신발 두 켤레, 나란히 걷는 발밑 · 컷 49

```
A low-angle ground-level side shot of two pairs of feet walking side by side along a sunny sidewalk on a clear afternoon: a pair of sneakers with neatly tied laces and a pair of loafers with black socks, stepping in matching rhythm. Bright soft sunlight filters through roadside trees and dapples the pavement with moving leaf shadows. A light breeze sends a few fresh green leaves tumbling along the ground beside them. The neat bows of the shoelaces bounce with each step, and small pebbles skip away from their feet. Leave empty space in the upper half of the frame for credits. Intense cinematic lighting, highly detailed anime art style, gentle peaceful daytime atmosphere. the character's outfits : feet only, two people, sneakers, tied shoelaces, black socks, loafers.
```

---

## 생성 체크리스트

- [ ] 「あなた」의 회색 후드·어두운 코트·짧은 검은 머리가 IL02·03·05·13·14·16·17에서 통일됐는지
- [ ] 미러 쌍(02↔08, 03↔09, 05↔10)의 구도가 겹쳐 보이는지 (리졸브에서 디졸브로 확인)
- [ ] 문자 자리(여백)가 남아 있는지
- [ ] 애슐리의 나비 머리핀이 보이는 컷에서 빠지지 않았는지
