# kondo 프로젝트: 이미지 프롬프트 작업 규칙

이 레포에서 일러스트/이미지 프롬프트를 쓸 때는 **반드시 아래 순서를 지킨다.**

## 0. 작업 전 필수 확인 (캐릭터 외형을 추측하지 않는다)

1. `ugoira_pixel_art/CHARACTERS.md`의 **외형 사전**을 읽는다. 5명(콘도상, 애슐리, 레이, 코하이군, **모브쨩**)의 외형 단어가 정리돼 있다.
2. Notion 도구가 있으면 정본을 직접 확인한다.
   - 「プロンプトフル展開！！Girls The Masterpiece 基本設定」: 캐릭터 프로필과 외견 프롬프트 (모브쨩 포함)
   - 「🖌 イラストプロンプト生成ルール」: 외형 사전, 구도 규칙, 6절 MG 화풍 규칙 (캐릭터별 주의점)
3. 사전에 없는 캐릭터가 나오면 **임의로 만들지 말고** Notion을 검색하고, 그래도 없으면 사용자에게 묻는다.
4. 이 레포의 `CHARACTERS.md`는 노션의 요약본이다. 노션과 다르면 노션이 우선이다.

## 1. 모브쨩 (자주 틀리는 캐릭터)

기본 프롬프트(정본, 변경 금지):
```
the character's outfits : heavy freckles, black hair, short ponytail, grey eyes, white scrunchie, pink bowtie, white shirt, navy pleated skirt, medium breasts, white socks, loafers.
```
- 어떤 구도에서도 `heavy freckles, black hair, short ponytail, grey eyes, white scrunchie`는 항상 넣는다. 정체성 앵커다.
- 단발, 검은 눈, 검은 양말 등으로 바꾸지 않는다. 문장 쪽에도 한 번 "heavy freckles, grey eyes, black hair in a short ponytail tied with a white scrunchie"를 적는다.
- 개별 LoRA/트리거 없음. 외형 단어가 정체성을 전부 담당한다.
- 설정: 자신 없는 모브. 코하이군을 짝사랑하지만 존재를 인식받지 못한다. 마스터피스들 앞에 나서지 못한다.

## 2. 구도별 외형 단어 규칙

- 순서: 얼굴·머리 → 상반신 → 하반신 → 발. 구도에 안 나오는 부위의 단어는 **반드시 뺀다** (안 빼면 모델이 전신으로 끌어당긴다).
- close-up: 얼굴·머리만 / bust shot: + 상반신 / medium shot: + 하반신 / cowboy shot: + 허벅지를 덮는 것(pantyhose 등), 신발·발목 양말은 뺀다 / full body: 전부.
- `petite`(레이)는 cowboy shot 이상에서만. 바스트·클로즈업에서는 뺀다.
- 애슐리의 `large breasts`는 항상 포함 (사용자 지시). 모브쨩의 `medium breasts`는 상반신이 보일 때 포함.

## 3. 사용자 지시 사항 (누적)

- **`slight vignette`는 쓰지 않는다.**
- 셀 쉐이딩의 매끈한 질감은 유지한다. 형식은 [화풍 → 상황 → 포즈/동작/감정 → 배경 → 외형]이고 외형은 `the character's outfits :` 또는 마지막 태그줄에 단어형으로 모은다.
- 콘도상: 노랑 카디건은 전용. 오타쿠에게 상냥하지 않다. 선배 행세/걱정 장면 금지. 금속배트(「ギンタロウ」)는 지시가 있을 때만 등장시킨다.
- 코하이군: 삭발(머리) 강조는 하지 않는다. 밝은 장면에서 피부색이 어둡게 나오지 않도록 `fair skin`을 쓴다. 눈에 별(sparkling) 표현은 지시가 있을 때만.
- **두 캐릭터가 함께 나오는 컷은 기본적으로 접촉 금지**를 문장(`standing about an arm's length apart, never touching`)과 네거티브 프롬프트(`holding hands, linked arms, hugging, touching, shoulder to shoulder, romantic`)로 막는다. 때리는 슬랩스틱 등 접촉이 지시된 장면만 예외 (이 경우 `blood, gore, weapon` 등을 네거티브로).
- 모션그래픽 컷은 `flat color motion graphic illustration, graphic poster layout, crisp cel shading, ... white sticker-style outline around the character` 문법을 쓰고 읽을 수 있는 글자는 `abstract typography-like bars`로 대체한다.
- 콘도상 vs 레이의 최강 논쟁은 확정하지 않는다.

## 4. 산출물 관리

- 모든 프롬프트의 정리본은 `illustration_prompts.md`에 캐릭터·시리즈별로 추가한다 (사용자가 요청할 때).
- 개발 브랜치: `claude/gifted-archimedes-zpozn1`.
