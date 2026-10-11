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

### IL04 — 육교 위에서 내려다보는 애슐리 · 컷 09 「わたしは知っていますよ」

> 수정: 카메라를 **육교 아래 도로**에 두고 올려다보게 해서 높이 차이를 확실히. 표정은 웃음 → **안타까운 미소**(힘들어하는 사람을 지켜보는 마음).

```
A wide shot from far below at street level, extreme low angle, looking straight up at a pedestrian overpass that spans the upper part of the frame against the dusk sky. The concrete underside and steel girders of the overpass cut across the top of the frame, and a lone gentle anime girl leans over its railing with her arms folded on the rail, looking down at the viewer far below. Her expression is a sad, worried smile with her eyebrows drawn together, as if she is watching someone who keeps pushing themselves too hard. The solid side panel of the overpass hides her below the chest. Car headlights stream beneath the overpass, and the sky behind her fades from orange to deep navy. An evening wind blows across the overpass, and her blonde hair spills over the railing toward the street below. Leave empty space on the left side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, wistful twilight atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, sad smile, worried, looking down, looking at viewer, white shirt, pink bowtie, large breasts.
```

### IL04b (추가) — 애슐리의 시점: 육교 위에서 본 「あなた」 · 컷 08 「頑張りやさんですね」

> 애슐리의 등 너머로, 아래 횡단보도에 혼자 선 「あなた」(IL03과 같은 옷)를 내려다보는 컷. 컷 08 = IL04b(누구를 보고 있는지) → 컷 09 = IL04(애슐리의 얼굴) 순서.

```
A shot from above over the shoulder, from behind a gentle anime girl leaning on the railing of a pedestrian overpass at dusk, looking down at the street far below. Far below, at the pedestrian crossing, a small lone person in a gray hoodie and dark coat stands waiting at the red light with slumped shoulders, their long shadow stretching across the white stripes. Her hand rests on the railing, fingers curled slightly, as if she wants to reach out but cannot. Car headlights streak along the road beneath the overpass, and the first streetlights flicker on. An evening wind blows across the overpass and lifts strands of her blonde hair into the foreground of the frame. Leave empty space on the right side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, wistful twilight atmosphere. the character's outfits : from behind, over the shoulder, blonde hair, medium hair, blue butterfly hairpin, white shirt.
```

### IL05 — 어두운 방, 무릎을 안은 실루엣 · 컷 10–11 (IL10의 미러 원본)

```
A wide shot at eye level of a small dark bedroom at night, where a lone person sits on the floor against the side of the bed, hugging their knees with their face buried in their arms. The only light is a desk lamp on a cluttered desk, and its warm circle of light stops just short of the person, leaving them at the edge of the shadow. Through the window, distant city lights blur in the night, and a single softly glowing blue butterfly rests on the outside of the glass. A thin gap in the window lets the curtain sway gently, and its shadow ripples across the floor. Leave empty space on the right side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, silent lonely night atmosphere. the character's outfits : 1other, faceless, face buried in knees, androgynous, short dark hair, gray hoodie, sweatpants, barefoot.
```

## Pre-Chorus 1 / Chorus 1

### IL06 — 풀린 신발 끈 / 쭈그려 앉은 애슐리 → **2장으로 분리** · 컷 12–15

> 수정 이유: 한 장에 「애슐리 + 다른 사람의 신발」을 같이 넣으면 모델이 신발을 애슐리에게 신기거나 구도가 무너짐.
> → **애슐리가 나오는 그림에는 발을 아예 안 넣고**, **신발 그림에는 애슐리를 손만** 넣는 식으로 나눔. 각 그림의 요소가 단순해져서 안정적으로 나와요.
>
> | 컷 | 가사 | 사용 |
> |---|---|---|
> | 12–13 | 急がなくていいですよ / 今日は休んでいいですよ | IL06b (애슐리 얼굴) |
> | 14–15 | ほどけた靴のひもを / 結びなおすみたいに | IL06a (풀린 끈 + 애슐리의 손) |

#### IL06a — 풀린 끈과 다가오는 애슐리의 손 (신발 1켤레만)

```
A close-up at ground level of a single worn gray sneaker standing on warm asphalt at sunset, its shoelace untied and trailing loosely on the ground, the hem of long dark pants just above it. From the top right of the frame, a slender hand with a white shirt cuff reaches gently down toward the loose lace, fingertips about to pick it up. The golden sunset behind fills the background with hazy glow and soft lens flare. A light breeze lifts the loose end of the lace and rolls a few small petals across the ground. The long shadow of the reaching hand falls across the sneaker's toe. Leave empty space along the bottom center of the frame for text. Intense cinematic lighting, highly detailed anime art style, warm gentle sunset atmosphere. the character's outfits : hand only, white shirt cuff, sneaker, untied shoelace, long dark pants.
```

#### IL06b — 쭈그려 앉아 올려다보며 손을 내미는 애슐리 (발 없음)

```
A bust shot from above, POV, of a gentle anime girl crouching down on the street at sunset right in front of the viewer, looking up at the viewer with a soft, reassuring smile as she reaches one open hand gently toward the viewer's feet, outside the bottom of the frame. The golden sunset behind her fills the background with a hazy glow and lens flare, and the asphalt around her shines warm orange. A light breeze carries a few small petals past her face. Her blonde hair falls forward over her shoulder as she leans in, and the sunlight makes the edges of her hair glow. Leave empty space along the bottom center of the frame for text. Intense cinematic lighting, highly detailed anime art style, warm gentle sunset atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, looking up, looking at viewer, white shirt, pink bowtie, large breasts.
```

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

### IL10 — 산속 저택, 나무로 된 자기 방 책상에 엎드린 애슐리 · 컷 24 (IL05와 같은 구도, 와이드)

> 수정: 애슐리는 **산속의 저택**에 산다 → 도시 야경·현대적인 방 삭제. 원목 기반의 편안한 방으로 변경.
> 구도(왼쪽 인물·책상 스탠드·오른쪽 창)는 IL05와 맞춰서 미러 연출은 유지. 「편안한 방인데 정작 본인은 지쳐 쓰러져 있다」는 대비가 포인트.
> ※ Tsubaki는 문장 속 「city」 같은 단어를 부정문이어도 그려 버릴 수 있어서, 「없음」이라고 쓰지 않고 창밖을 숲과 산으로만 묘사했어요.

```
A wide shot at eye level of a cozy old wooden bedroom in a mansion deep in the mountains at night, where a lone anime girl has fallen asleep at an antique wooden desk, resting her head on her folded arms beside towering stacks of thick medical textbooks and workbooks. The room is built of warm honey-colored timber, with exposed wooden beams, a wooden bookshelf, a soft knitted blanket draped over an armchair and a small potted plant on the windowsill. The only light is an old brass desk lamp, and its dim warm circle of light falls on scattered notes covered in careful handwriting. Through the tall wooden-framed window, rain streaks down the glass over dark pine forest and misty mountain ridges, with no butterfly outside. A thin gap in the window lets the lace curtain sway gently, and the pages of an open textbook flutter in the draft. Her pen has rolled to the edge of the desk, and a loose page has slipped onto the wooden floor. Leave empty space on the right side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, quiet rainy mountain night atmosphere. the character's outfits : blonde hair, medium hair, blue butterfly hairpin, closed eyes, white shirt, pink bowtie, navy pleated skirt, black socks.
```

> **구도 배분 (컷 24–27)**: 와이드 1장만으로 20초를 버티면 단조로워서, 미러는 첫 컷만 지키고 나머지는 구도를 바꿔요.
>
> | 컷 | 가사 | 사용 | 의도 |
> |---|---|---|---|
> | 24 | がんばれなかった日も | IL10 (와이드) | IL05와 겹쳐 보이는 미러 컷 |
> | 25 | わたしにもあるんですよ | IL10c (얼굴 클로즈업) | 「わたし」의 얼굴. 처음으로 애슐리가 약한 모습을 보임 |
> | 26 | 誰にも言えない夜を | IL10d (창밖에서 본 방) | 고립감. 저택 안에서도 혼자 |
> | 27 | ひとりで越えてきました | IL10e (부감, 책상 위) | 쌓인 공부량 = 넘어온 밤의 무게. 새벽빛이 책상에 닿음 |
>
> c·d·e는 필요에 따라 골라 써도 OK (최소 c 하나만 있어도 변화가 생겨요).

### IL10c — 팔에 얼굴을 묻은 애슐리 클로즈업 · 컷 25

```
A close-up at eye level, face focus, of a gentle anime girl resting her cheek on her folded arms on an antique wooden desk at night, her eyes half open and unfocused, staring at nothing with tired, glistening eyes. A thick medical textbook lies open right in front of her face, its pages blurred in the foreground. The dim warm glow of an old brass desk lamp lights one side of her face, and the rest of the wooden room fades into soft darkness. Rain taps on the window behind her, and its faint moving shadows ripple across her cheek. A single strand of blonde hair has fallen across her face and trembles with each slow breath. Leave empty space on the right side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, quiet exhausted night atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, tired, half-closed eyes, teary eyes, head on arms.
```

### IL10d — 비 내리는 창밖에서 들여다본 애슐리의 방 · 컷 26

```
A medium-wide shot from outside, looking in through a tall wooden-framed window of an old mansion deep in the mountains on a rainy night. Inside, in a cozy honey-colored wooden room, a lone anime girl sits slumped at an antique desk under the dim warm light of a brass lamp, small within the window frame. The window is the only warm light in the dark, and wet ivy leaves and pine branches frame the glass. Rain streams down the window pane and blurs the warm interior into soft streaks of light. Raindrops gather on the window ledge and drip steadily from the ivy leaves. Leave empty space on the left side of the frame, in the dark wall beside the window, for vertical text. Intense cinematic lighting, highly detailed anime art style, lonely rainy mountain night atmosphere. the character's outfits : blonde hair, medium hair, blue butterfly hairpin, white shirt, sitting at desk.
```

### IL10e — 책상 위 부감, 쌓인 책과 새벽빛 · 컷 27

```
A shot from directly above of an antique wooden desk near dawn, where a gentle anime girl sleeps with her head on her folded arms among towering stacks of medical textbooks, filled notebooks, sticky notes and a cold cup of tea. The brass desk lamp is still on, but the first pale blue light of dawn from the window is beginning to fall across one corner of the desk. A gentle draft from the window turns the pages of an open notebook. The pale dawn light creeps across the papers and reaches the tips of her blonde hair spread over the desk. Leave empty space on the right side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, quiet dawn-breaking atmosphere. the character's outfits : from above, blonde hair, medium hair, blue butterfly hairpin, sleeping, head on arms, white shirt.
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

> 수정: 「あなた」 쪽에 **발목까지 덮는 긴 바지**를 명시.

```
A close-up from above of a puddle on a wet asphalt street after the rain at night, with two pairs of feet standing side by side at its edge: a pair of worn gray sneakers under the hems of long dark jogger pants that cover the ankles, and a pair of brown loafers with black socks. The puddle mirrors a glowing streetlight and the faint silhouettes of the two people. The last drops fall from the eaves above and spread slow rings across the reflection. The rings distort the reflected streetlight into trembling ribbons of warm light. Leave empty space on the left side of the frame for vertical text. Intense cinematic lighting, highly detailed anime art style, calm after-rain night atmosphere. the character's outfits : feet only, two people, long dark pants, sneakers, black socks, brown loafers.
```

### IL14 — 「あなた」의 신발 끈을 묶어 주는 애슐리 · 컷 38

> 수정: 손 클로즈업이면 「자기 신발을 묶는 그림」으로 보여서, **옆에서 본 구도**로 변경. 왼쪽에 「あなた」의 다리(긴 바지+스니커), 그 앞에 한쪽 무릎을 꿇고 끈을 묶는 애슐리의 옆모습 → 두 사람이 따로 있다는 게 한눈에 보이게.

```
A full body side view at ground level on a wet street at night after the rain. At the left edge of the frame stands a person whose lower legs are the only part visible, wearing long dark jogger pants and worn gray sneakers, one shoelace untied. Kneeling on one knee in front of them, a gentle anime girl in profile carefully ties that person's shoelace into a neat bow with both hands, her eyes lowered and her expression gentle and focused. She wears her own brown loafers with black socks. Warm streetlight reflects on the damp asphalt, and a soft wind carries the last fine mist of the rain through the light. Her blonde hair falls forward past her cheek as she leans toward the shoe, and tiny drops shake loose from the laces onto the ground. Leave empty space in the upper left of the frame for text. Intense cinematic lighting, highly detailed anime art style, tender quiet night atmosphere. the character's outfits : profile view, from side, blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, gentle smile, looking down, white shirt, pink bowtie, large breasts, navy pleated skirt, black socks, brown loafers, kneeling, on one knee.
```

### IL14b — 올려다보는 애슐리 (차분) · 컷 39 「ここにいてくださいね」

```
A bust shot from above of a gentle anime girl crouching on a wet street at night, looking up at the viewer with a soft smile and slightly teary eyes, as if asking them to stay. Warm streetlight falls on her face from above, and the wet asphalt around her shines with reflections. A gentle night breeze drifts the last fine mist of the rain through the light. Her blonde hair falls softly around her upturned face, and a single drop glistens at the corner of her eye. Leave empty space at the top of the frame. Intense cinematic lighting, highly detailed anime art style, tender quiet night atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, soft smile, teary eyes, looking up, looking at viewer, white shirt, pink bowtie, large breasts.
```

## Final Chorus

### IL15 ★ — 아침 강둑, 나비 무리, 최고의 미소 · 컷 43–46 (메인 키 비주얼)

> 수정: 처음 보는 언덕 → **IL07(노을)·IL12(새벽)과 같은 강둑의 아침**. 「같은 장소, 노을 → 새벽 → 아침」으로 시간이 흐른 걸 보여 줌.

```
A medium shot at eye level of a gentle anime girl standing on the same grassy riverside embankment in the early morning, laughing brightly at the viewer with a blush, her hands clasped happily in front of her chest. Behind her, the wide river sparkles under the rising sun, with the familiar low town, utility poles and a distant bridge along the far bank. Hundreds of blue butterflies burst up from the grass along the embankment and spiral into the clear pale-blue sky. The morning sun pours in from behind her and fills the air with drifting golden motes. The rush of wings lifts her blonde hair and skirt and scatters glittering dew from the grass. Leave empty space at the top center of the frame for large lyric text. Intense cinematic lighting, highly detailed anime art style, radiant hopeful morning atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, smile, open mouth, blush, looking at viewer, hands clasped, white shirt, pink bowtie, large breasts, navy pleated skirt.
```

### IL16 — 아침의 육교, 「봐요」 하고 세상을 가리키는 애슐리 · 컷 47–48

> 수정: 나란히 선 뒷모습(연인처럼 보임) → **시청자 시점(POV)**. 「あなた」를 그리지 않고, 몇 걸음 앞에서 돌아보며 하늘을 가리키는 애슐리만.
> 장소는 **IL04의 육교**. 1절에서는 애슐리가 혼자 위에서 내려다봤던 곳에, 마지막엔 「あなた」도 같이 올라와 있다 = 같은 높이에 섰다는 의미.

```
A wide POV shot at eye level from the walkway of a pedestrian overpass in the morning, the viewer standing on the bridge. A few steps ahead, a gentle anime girl leans back against the railing, turns toward the viewer and spreads one arm out toward the wide town and sky behind her, as if saying "look". The sky above the town is unraveling like loosened threads of colored light, pale blue, gold and soft pink strands drifting apart and spreading across the horizon. A gentle morning wind sweeps across the overpass and carries the glowing threads over the rooftops. Her blonde hair and skirt stream sideways in the wind, and the railing gleams in the fresh sunlight. Leave empty space in the upper center of the frame for text. Intense cinematic lighting, highly detailed anime art style, liberating morning atmosphere. the character's outfits : blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin, smile, looking at viewer, outstretched arm, white shirt, pink bowtie, large breasts, navy pleated skirt, black socks, loafers, pov.
```

## Outro

### IL17 — 묶인 신발 두 켤레, 나란히 걷는 발밑 · 컷 49

```
A low-angle ground-level side shot of two pairs of feet walking side by side along a sunny sidewalk on a clear afternoon: a pair of sneakers with neatly tied laces and a pair of loafers with black socks, stepping in matching rhythm. Bright soft sunlight filters through roadside trees and dapples the pavement with moving leaf shadows. A light breeze sends a few fresh green leaves tumbling along the ground beside them. The neat bows of the shoelaces bounce with each step, and small pebbles skip away from their feet. Leave empty space in the upper half of the frame for credits. Intense cinematic lighting, highly detailed anime art style, gentle peaceful daytime atmosphere. the character's outfits : feet only, two people, sneakers, tied shoelaces, black socks, loafers.
```

---

## 생성 체크리스트

- [ ] 「あなた」의 회색 후드·어두운 코트(또는 긴 바지)가 IL02·03·04b·05·13·14·17에서 통일됐는지
- [ ] 미러 쌍(02↔08, 03↔09, 05↔10)의 구도가 겹쳐 보이는지 (리졸브에서 디졸브로 확인)
- [ ] 문자 자리(여백)가 남아 있는지
- [ ] 애슐리의 나비 머리핀이 보이는 컷에서 빠지지 않았는지
