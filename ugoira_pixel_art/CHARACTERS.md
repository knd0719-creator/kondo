# 캐릭터 레퍼런스 (노션 「プロンプトフル展開！！Girls The Masterpiece 基本設定」 기준)

## 콘도상 (近藤 綾香)
- 불량 갸루. 자신감 넘치고 장난기 많은 악동.
- 비주얼: 갈색 머리, 웨이브 헤어, 노란 카디건. 동기화 오브젝트: 금속배트 「ギンタロウ」.
- 말투: 간사이벤(과하지 않게). 일인칭 ウチ. 「~やねん！」「~やで！」「ほんまに？」
- 호칭: 애슐리 「あしゅしゅ」, 레이 「玲たん」, 코하이 「お前」/「コーハイ」.
- 주의: 「오타쿠에게 상냥함」은 구현에 실패한 개그. 상냥하게 걱정하거나 선배 행세 금지.

## 하뉴 애슐리 (羽生 アシュリー)
- 상냥하고 우월한 미모의 우등생. 미-일 하프. 의사의 딸.
- 비주얼: 금발, 파란 나비 머리핀, 글래머. 나비(蝶々さんたち)를 불러옴.
- 말투: 경어 기본. 일인칭 私. 곤란할 때 「はうう～」.
- 주의: 남을 욕하지 않고 폐를 끼치지 않음. 「マジで！」 같은 말투 금지.

## 스즈시로 레이 (鈴代 玲)
- 풍기위원장. 유도 유단자. 콘도상과 맞붙을 수 있는 유일한 인물.
- 비주얼: 보랏빛 흑발, 풍기위원 완장(腕章), 검은 스타킹.
- 말투: 경어 기본, 속어 없음. 일인칭 私. 입버릇 「~なはずです。減点。」. 화나면 「近藤さん」→「近藤！」.
- 주의: 규칙을 어기거나 대충 넘기지 않음.

## 이마다 코하이 (今田 功俳, 코하이군) — 참고
- 자칭 불량계 초신성. 일인칭 俺. 입버릇 「うっす」「押忍」. 모두를 센파이로 부름.
- 비주얼: 삭발, 장신. 남자. 실은 누구도 다치게 한 적 없음.

## 모브쨩 (이름 없는 모브 캐릭터, 설정상 클라우드이지만 준 마스터피스)
- 특별하지 않은 자신에게 자신감이 없으면서도 연애 감정에는 불타는 성격.
- 코하이군을 짝사랑하지만 본인은 그 존재조차 알아주지 않는다. 러브 코메디 에피소드에서 주로 활약.
- 관계: 모브쨩 → 코하이 = 짝사랑 (일방통행, 설렘과 자신 없음).
- 출처: 노션 「基本設定」 3항 「모브쨩」. **외견 프롬프트는 아래 외형 사전의 문자열을 그대로 쓴다.**

---

# 외형 사전 (이미지 프롬프트용 / 노션 「基本設定」「イラストプロンプト生成ルール」 기준)

프롬프트 말미 `the character's outfits :` 뒤에 붙이는 단어열. **구도에 따라 화면에 안 나오는 부위의 열은 뺀다.** 순서는 얼굴·머리 → 상반신 → 하반신 → 발.

| 캐릭터 | 얼굴·머리 (항상) | 상반신 | 하반신 | 발 |
| --- | --- | --- | --- | --- |
| 콘도상 | Kondo_Ayaka, brown hair, long wavy hair, brown eyes | yellow cardigan, white shirt, pink bowtie | navy pleated skirt | white loose socks, loafers |
| 애슐리 | blue eyes, tareme, blonde hair, medium hair, blunt bangs, blue butterfly hairpin | white shirt, pink bowtie, large breasts | navy pleated skirt | black socks, loafers |
| 레이 | dark short hair, purple eyes | navy jacket, white shirt, pink bowtie, red prefect armband | navy pleated skirt, petite | black pantyhose, loafers |
| 코하이군 | Imada_Kohai, sharp eyes, black eyes, shaved head | white shirt, open collar, black tank top undershirt | navy pants | white sneakers |
| **모브쨩** | **heavy freckles, black hair, short ponytail, grey eyes, white scrunchie** | **pink bowtie, white shirt, medium breasts** | **navy pleated skirt** | **white socks, loafers** |

## 모브쨩 기본 프롬프트 (정본, 한 글자도 바꾸지 말 것)
```
the character's outfits : heavy freckles, black hair, short ponytail, grey eyes, white scrunchie, pink bowtie, white shirt, navy pleated skirt, medium breasts, white socks, loafers.
```
- 정체성 앵커: `heavy freckles`, `short ponytail`, `white scrunchie`, `grey eyes`. 어떤 구도에서도 얼굴·머리 열은 전부 넣는다. 특히 클로즈업에서 빠지면 다른 사람이 된다.
- 문장 쪽에도 한 번 "heavy freckles, grey eyes, black hair in a short ponytail tied with a white scrunchie"를 적어 두면 안정적이다.
- 모브쨩은 개별 LoRA와 트리거가 없다. 외형 단어가 캐릭터 정체성을 전부 담당한다.
- 임의로 단발·검은 눈·검은 양말 등으로 바꾸지 않는다. (과거 세션에서 노션을 확인하지 않아 발생한 오류)

## 캐릭터별 주의 (노션 「イラストプロンプト生成ルール」 6-5절, 2026-10-19)
- 콘도상: `light fair skin`. `gyaru`는 쓰지 않는다. 카디건은 콘도상 전용.
- 애슐리: 트리거 `hanyu_ashley`를 맨 앞에. `large breasts`는 상의 태그 뒤에 항상.
- 레이: 트리거 `suzushiro_rei`, `hair between eyes`. 발이 나오는 그림은 `full body` (카우보이샷에서는 발이 잘림). `petite`는 카우보이샷 이상에서만.
- 코하이군: 머리는 밝은 회색의 매끈한 둥근 형태. `shaved head, very short light gray hair, light gray scalp`. `black hair`, `teeth showing`은 쓰지 않는다.

## 최강 논쟁
- 콘도상 vs 레이 중 누가 최강인지는 **확정하지 않음**. 싸우기 직전에 말리거나 흐지부지되게 처리.

## 시즌 복선 메모 (프롤 시즌 기획)
- 주제: 「창작이란 무엇인가」와 「캐릭터에 대한 애정」. 주 3회 연재, 약 300화 목표.
- 악플 = 네거티브 프롬프트 구현체, 선플 = 포지티브 프롬프트. 마스터피스 = 「만든 사람이 사랑한 존재」.
