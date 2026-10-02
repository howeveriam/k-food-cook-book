# Recipe Details — Figma 원본 디자인 스펙

- 출처: Figma 파일 `cta4gGnJ1511CoeJ91bg31`, 프레임 **"Recipe Details - 1"** (노드 `38:52`)
- 추출일: 2026-10-02, Figma MCP `get_design_context` + `get_metadata` + `get_screenshot`
- 프레임 크기: **375 × 3679 px** (iPhone 375pt 기준, 1x)
- 이 문서의 모든 수치는 **px(1x)**. 좌표는 특별히 적지 않으면 **프레임 좌상단 기준 절대 좌표**.

## 0. 파일

| 파일 | 내용 |
|---|---|
| `figma-full.png` | 프레임 전체 375×3679 |
| `figma-hero-card.png` | y 0–655: 상태바·헤더·히어로·타이틀 카드 |
| `figma-times-ingredients.png` | y 650–1180: 시간 컨테이너 + 재료 섹션 |
| `figma-nutrition-directions.png` | y 1180–2050: Nutrition Facts + Directions Step 1~3 |
| `icons/*.svg` | Figma에서 내려받은 원본 아이콘 SVG (그대로 쓸 것, 크기 속성 변경 금지) |

`icons/` 목록: `arrow-left.svg`(24) · `dots.svg`(24) · `heart-filled.svg`(24, #E22D57) · `circle-minus.svg`(24, #F48B00) · `circle-plus.svg`(24, #F48B00) · `plus.svg`(18 — **이름은 plus지만 실제 모양은 아래 화살표 chevron-down**, #F48B00) · `divider-h.svg`(197×0.5, #D9D9D9) · `divider-v.svg`(0.5×42, #D9D9D9)

---

## 1. 디자인 토큰

### 색상 (Figma 스타일 이름 그대로)

| 토큰 | HEX | 용도 |
|---|---|---|
| Other/Black | `#232323` | 모든 제목·본문 강조·값 텍스트, 아이콘 선 |
| Secondary/700 | `#707070` | About 본문, Step 본문, "Servings" 라벨 |
| Secondary/500 | `#9E9E9E` | 칩 텍스트, 시간 라벨, 영양 라벨 |
| Other/Light Grey | `#F9F9F9` | 칩 배경, 시간 컨테이너 배경 |
| Other/Stroke | `#D9D9D9` | 구분선(0.5px), Show all 버튼 테두리(1px) |
| Other/White | `#FFFFFF` | 페이지 배경, 타이틀 카드, 하트 버튼, 하단 바 |
| Primary (스타일명 없음) | `#F48B00` | More 링크, 서빙 ± 아이콘, Show all 텍스트·chevron, Start cooking 버튼 |
| Error/500 | `#E22D57` | 하트(채워진 상태) |
| Neutral/Black | `#0E1218` | 네이티브 상태바 시계(웹 구현 불필요) |

**페이지 배경은 순백 `#FFFFFF`**. 그라데이션·베이지 톤 없음.

### 폰트

- 본문: **Inter** (400 Regular / 500 Medium / 600 SemiBold / 700 Bold)
- 제목: **Playfair Display** 700 Bold
- Figma 자간 `-1` / `-3`은 **퍼센트**다 → CSS로 `-0.01em` / `-0.03em`.

| 스타일 | 패밀리·굵기 | 크기 | line-height | letter-spacing |
|---|---|---|---|---|
| Heading/H4 | Playfair Display 700 | 24 | 1.1 | -0.72px (-3%) |
| Heading/H6 | Playfair Display 700 | 18 | 1.05 | -0.54px (-3%) |
| Body/large/semibold | Inter 600 | 16 | 1.65 | -0.16px |
| Body/large/bold | Inter 700 | 16 | 1.65 | -0.16px |
| Body/medium/semibold | Inter 600 | 14 | 1.7 | -0.14px |
| Body/small/regular | Inter 400 | 12 | 1.7 | -0.12px |
| Body/small/medium | Inter 500 | 12 | 1.7 | -0.12px |
| Body/small/semibold | Inter 600 | 12 | 1.7 | -0.12px |
| Body/small/bold (More 링크) | Inter 700 | 12 | 1.7 | -0.12px |
| Body/xsmall/medium | Inter **600** | 10 | 1.6 | -0.1px |

### 반경 · 그림자

| 요소 | radius |
|---|---|
| 히어로 이미지 | 16 |
| 타이틀 카드 | 12 |
| 칩 | 8 |
| 시간 컨테이너 | 12 |
| Show all 버튼 | 10 |
| Step 이미지 | 12 |
| Start cooking 버튼 | 12 |
| 하트 버튼 | 60 (= 완전한 원) |
| 재료 썸네일 | 원형(ellipse) |

그림자는 **타이틀 카드 하나뿐**: `drop-shadow(0 4px 15px rgba(0,0,0,0.04))` — 색 검정 4% / blur 15 / x 0 / y 4 / spread 0. 다른 요소(히어로, 하트 버튼, Step 이미지, 버튼)에는 그림자 없음.

---

## 2. 전체 프레임 구조

```
Recipe Details - 1 (375×3679, bg #FFFFFF)
├─ Native/Status Bar        y 0–44     (웹 구현 불필요)
├─ content                  y 44~, padding-top 24, 좌우 padding 24, 세로 gap 24, 콘텐츠 폭 327
│  ├─ header                y 68–94   (327×26)
│  └─ container             y 118~, 세로 gap 24
│     ├─ [그룹 A] 히어로 그룹  y 118–639 (327×521)   ← 히어로 카드 + 타이틀 카드 + 하트 버튼
│     └─ how-to             y 663~, 세로 gap 24
│        ├─ [카드 B] time 컨테이너   y 663–737 (327×74)
│        ├─ ingredients 섹션        y 761–1169 (327×408)
│        ├─ nutrition-facts 섹션    y 1193–1302 (327×109)
│        └─ directions 섹션         y 1326–3563 (327×2237)
└─ button (하단 고정 바)     y 3563–3679 (375×116)
```

**분리된 카드 그룹** (중요):
1. **히어로 카드** — 327×327 이미지, r16. 독립 요소.
2. **타이틀 카드** — 흰 카드, r12, 그림자. 히어로 카드와 **별개의 카드**이며 히어로 아래쪽 위에 떠서 **94px 겹친다** (히어로에 붙어 이어지는 시트 형태가 아님. 좌우로 24px씩 들여져 있어 양옆으로 히어로 이미지가 보인다).
3. **시간 컨테이너** — 타이틀 카드 하단에서 **24px 아래**에 떨어진 독립 회색 카드 (#F9F9F9, r12).
4. 이후 Ingredients / Nutrition Facts / Directions는 카드 배경 없이 흰 페이지 위에 놓인 섹션이며 섹션 간 간격 **24px**.

수직 간격 요약 (위→아래):

| 구간 | 간격 |
|---|---|
| 상태바 아래 → 헤더 | 24 |
| 헤더 → 히어로 | 24 |
| 히어로 상단 → 타이틀 카드 상단 | 233 (히어로 327 중 94px 겹침) |
| 타이틀 카드 하단 → 시간 컨테이너 | 24 |
| 시간 → Ingredients 제목 | 24 |
| Ingredients 블록 → Nutrition Facts 제목 | 24 |
| Nutrition 블록 → Directions 제목 | 24 |
| 섹션 제목 → 섹션 내용 | 16 |
| Directions 마지막 스텝 → 하단 바 | 0 (스크롤 영역이 바 높이 116만큼 확보되어 있음) |

---

## 3. 헤더 (y 68–94, 327×26)

- 가로 flex, `align-items:center`.
- 좌: `arrow-left.svg` 24×24 (선 #232323, stroke 2).
- 중: "Recipe Details" — Inter 600, 16px, lh 1.65, ls -0.16px, `#232323`, **가운데 정렬**, 폭 279(= 327 − 24 − 24).
- 우: `dots.svg` 24×24.
- sticky 아님(정적 배치). 배경 없음.

---

## 4. 그룹 A — 히어로 + 타이틀 카드 (y 118–639)

그룹 박스 327×521, 좌상단 (24, 118). 세 레이어가 같은 그리드 셀에 겹쳐 있다:

### 4-1. 히어로 이미지 카드
- 크기 **327×327 (정사각형, 1:1)**, 위치 그룹 내 (0,0) → 화면 좌우 가장자리에서 **각 24px** 여백.
- `border-radius:16px`, `object-fit:cover`. 테두리·그림자 없음.
- 이미지: 구운 보쌈 일러스트 (데이터의 hero 이미지).

### 4-2. 하트(Save) 버튼
- 그룹 내 위치 (267, 16) → 히어로 카드 **오른쪽 위에서 top 16 / right 16**. 크기 **44×44**.
- 배경 `#FFFFFF`, `border-radius:60px`(원), `padding:10px`, 그림자 없음, 테두리 없음.
- 아이콘: `heart-filled.svg` 24×24, 채움 `#E22D57`. (Figma에는 채워진 = 저장된 상태만 있음.)
- 레이어 순서: 히어로 이미지 위.

### 4-3. 타이틀 카드 (`cards`, 노드 38:64)
- 그룹 내 위치 (24, 233), 크기 **279×288** → 히어로 좌우 안쪽으로 **24px씩** 들여짐, 히어로 상단에서 233px 지점에서 시작 = **히어로 하단과 94px 겹침**. 히어로보다 위 레이어.
- 배경 `#FFFFFF`, `border-radius:12px`, 그림자 `0 4px 15px rgba(0,0,0,0.04)`.
- 레이아웃: 세로 flex, `align-items:center`, `gap:16px`, `padding:16px 0` (좌우 패딩 0 — 자식별로 따로 들여씀).
- 자식 (카드 내부 y):
  1. **제목** y16–42 — "Grilled Bossam", Playfair Display 700, **24px**, lh 1.1, ls -0.72px, `#232323`, 가운데 정렬, 카드 전체 폭.
  2. **칩 영역** y58–130 — 아래 4-4.
  3. **구분선** y146 — 폭 **197px**, 두께 0.5px, `#D9D9D9`, 가운데 (카드 좌우에서 41px).
  4. **About 블록** y162–272 — 폭 **247px** (카드 좌우에서 16px), 아래 4-5.

### 4-4. 칩 4개
- 컨테이너: `display:flex; flex-wrap:wrap; gap:6px; justify-content:flex-start; padding:0 12px; width:100%` (= 내부 폭 255).
- 칩: 배경 `#F9F9F9`, `border-radius:8px`, `padding:0 10px`, 높이 20 (텍스트 lh로 결정, 상하 패딩 0), 테두리 없음.
- 칩 텍스트: Inter 500, 12px, lh 1.7, ls -0.12px, `#9E9E9E`, nowrap.
- 문구·실제 배치 (375 폭에서 3줄, 줄 간격 6):

| 줄 | 칩 (카드 내부 x, 폭) |
|---|---|
| 1 | "Caramelized & crisp-edged" (x12, w174) · "sweet" (x192, w55) |
| 2 | "Melt-in-your-mouth tender" (x12, w172) |
| 3 | "Korea's gathering dish" (x12, w146) |

칩은 **왼쪽 정렬** (가운데 정렬 아님).

### 4-5. "About this dish"
- 세로 flex, `gap:2px`, 폭 247.
- 제목 "About this dish": Inter 600, 16px, lh 1.65, ls -0.16px, `#232323`, **가운데 정렬**.
- 본문: Inter 500, 12px, lh 1.7, ls -0.12px, `#707070`, **왼쪽 정렬**, 3줄.
  문구: "In Korea, bossam is gathering food. Thick slices of tender pork belly, boiled until soft and wrapped in crisp lettuce..."
- "More": Inter **700**, 12px, lh 1.7, ls -0.12px, `#F48B00`, **오른쪽 정렬**, 밑줄 없음, 본문 바로 아래 줄.

---

## 5. 카드 B — 시간 컨테이너 (y 663–737, 327×74)

- 배경 `#F9F9F9`, `border-radius:12px`, `padding:16px 24px`, 테두리·그림자 없음.
- 가로 flex, 3개 셀 **균등 폭**(`flex:1`, 각 93px). **셀 사이 구분선 없음**, 셀별 배경 없음 — 하나의 회색 카드 안에 텍스트만.
- 셀: 세로 flex, `gap:2px`, **왼쪽 정렬**.
  - 라벨: Inter 500, 12px, lh 1.7, ls -0.12px, `#9E9E9E` — 대소문자 그대로 "Prep Time" / "Cook Time" / "Rest Time" (대문자 변환 X)
  - 값: Inter 600, 12px, lh 1.7, ls -0.12px, `#232323` — "15 min" / "1 hr 10 mins" / "10 mins"

---

## 6. Ingredients 섹션 (y 761–1169)

세로 flex, `gap:16px`.

### 6-1. 헤더 행 (327×24, `justify-content:space-between; align-items:center`)
- 좌: "Ingredients" — Playfair Display 700, 18px, lh 1.05, ls -0.54px, `#232323`.
- 우: 가로 flex `gap:10px`
  - "Servings" — Inter 500, 12px, `#707070`.
  - 스테퍼: 가로 flex `gap:9px` — `circle-minus.svg` 24 · 숫자 "6" (Inter 600, 12px, `#232323`) · `circle-plus.svg` 24. 아이콘 선 `#F48B00` stroke 2, 원 안 비움(채움 없음).

### 6-2. 재료 리스트
- 세로 flex, **행 간격 16px**, **행 구분선 없음**, 행 배경 없음.
- 행: 327×48, 가로 flex, `gap:16px`, `align-items:center`.
  - 썸네일: **48×48 원형**(ellipse에 이미지 채움). 테두리·배경색 없음 — 흰 배경 수채화 일러스트.
  - 수량: 폭 **64px** 고정, Inter **400**, 12px, lh 1.7, ls -0.12px, `#232323`. 예 "3½ lb".
  - 이름: `flex:1`(183px), Inter 600, **14px**, lh 1.7, ls -0.14px, `#232323`. 길면 2줄로 줄바꿈 (행 높이 48 유지).
  - **노트 전용 스타일 없음** — Figma는 노트를 이름 문자열 안에 괄호로 넣어 같은 스타일로 표기 (예: "Garlic (about 10 cloves)", "Green onion roots (optional)").
- 기본 표시 5행 (Figma 문구):

| 수량 | 이름 |
|---|---|
| 3½ lb | Skinless pork belly, in 4 chunks |
| 17 cups | Water |
| 1 | Sweet onion, peeled and halved |
| 4 | Green onion roots (optional) |
| 1¾ oz | Garlic (about 10 cloves) |

- 숨김 6행 (Figma에 hidden 레이어로 존재): ½ piece Fresh ginger, thickly sliced / 4 Bay leaves / 2½ cups Sugar / 6½ tbsp Doenjang (Korean soybean paste) / 1¼ cups Soy sauce / 1 cup Corn syrup (mulyeot)

### 6-3. "Show all ingredients" 버튼 (리스트의 마지막 항목, 위 행과 16px 간격)
- 327×**48**, 배경 `#FFFFFF`, 테두리 **1px solid `#D9D9D9`**, `border-radius:10px`, `padding:12px`.
- 내용 가운데 정렬, 가로 `gap:8px`: 텍스트 "Show all ingredients" (Inter 600, 14px, lh 1.7, `#F48B00`) + `plus.svg`(실제로는 chevron-down) 18×18, `#F48B00`.

---

## 7. Nutrition Facts (y 1193–1302)

세로 flex `gap:16px`.
- 제목 "Nutrition Facts" — Playfair Display 700, 18px, lh 1.05, ls -0.54px, `#232323`.
- 영양 행: 327×74, `padding:16px`, 가로 flex, **배경 없음 / 테두리 없음**.
  - 4개 셀 균등 폭(각 73.75), 세로 flex, **가운데 정렬**, 셀 내부 gap 0.
    - **위: 라벨** — Inter 600, 10px, lh 1.6, ls -0.1px, `#9E9E9E`, 대문자 문구 "CALORIES" / "FAT" / "CARBS" / "PROTEIN"
    - **아래: 값** — Inter 700, 16px, lh 1.65, ls -0.16px, `#232323`: "350" / "28g" / "15g" / "23g"
  - 셀 사이 **세로 구분선 3개**: 0.5px, `#D9D9D9`, 높이 42 (셀 높이 전체 = 패딩 안쪽 전체).

---

## 8. Directions (y 1326–3563)

세로 flex `gap:16px`.
- 제목 "Directions" — Playfair Display 700, 18px, lh 1.05, ls -0.54px, `#232323`.
- 스텝 리스트: 세로 flex, **스텝 간격 12px**.
- 스텝 블록: 세로 flex, **gap 4px**:
  1. 라벨 "Step N" — Inter 600, **14px**, lh 1.7, ls -0.14px, `#232323` (번호 원·배지 없음, 텍스트만).
  2. 이미지 — **327×218** (가로:세로 = 3:2), `border-radius:12px`, `object-fit:cover`, 그림자 없음.
  3. 본문 — Inter **400**, 12px, lh 1.7, ls -0.12px, `#707070`, 왼쪽 정렬.
- 스텝 문구 (7개):
  1. Make the braising liquid: pour the water into a large pot and add everything else — onion, green onion roots, garlic, ginger, bay leaves, sugar, doenjang, soy sauce, and corn syrup. Stir well until the doenjang, sugar, and syrup are fully dissolved.
  2. Set the pot over high heat and bring the liquid to a boil.
  3. While it heats, rinse the pork chunks and pat them completely dry with paper towels. Dry surface, good sear — this matters.
  4. Heat a heavy pan over medium heat. Lay the pork in, fatty side down first. The fat will slowly render out into lard; once it does, turn the chunks and brown every side evenly, nice and golden.
  5. When the braising liquid is boiling, lower the seared pork in so it's fully submerged.
  6. Boil over high heat for 40 minutes, until the pork is cooked through and tender.
  7. Turn off the heat and let the pork rest in the liquid for 10 minutes. Then lift it out, slice it thick, and serve.

---

## 9. Start cooking 하단 바 (y 3563–3679, 375×116)

- **화면 하단 고정** (`position:fixed; left:0; right:0; bottom:0`), 배경 **단색 `#FFFFFF`** (그라데이션·블러·상단 그림자·구분선 없음).
- 바 패딩: 상 24 / 좌우 24 / 하 0 + 아래 34px 홈 인디케이터 영역 (웹에서는 `max(34px, env(safe-area-inset-bottom))` 정도로 대체).
- 버튼: 폭 327 (바 폭 − 48), 높이 **58** (`padding:16px` + 텍스트 lh 26.4), 배경 `#F48B00`, `border-radius:12px`, 그림자 없음, 테두리 없음.
- 텍스트 "Start cooking" — Inter 600, 16px, lh 1.65, ls -0.16px, `#FFFFFF`, 가운데.
- 스크롤 콘텐츠는 바 높이(116px)만큼 하단 여백을 둬서 마지막 스텝이 가려지지 않게.

---

## 10. 텍스트·색상 전체 목록

| 위치 | 문구 | 색 |
|---|---|---|
| 헤더 | Recipe Details | #232323 |
| 타이틀 | Grilled Bossam | #232323 |
| 칩 ×4 | Caramelized & crisp-edged / sweet / Melt-in-your-mouth tender / Korea's gathering dish | 글자 #9E9E9E · 배경 #F9F9F9 |
| About 제목 | About this dish | #232323 |
| About 본문 | In Korea, bossam is gathering food. Thick slices of tender pork belly, boiled until soft and wrapped in crisp lettuce... | #707070 |
| About 링크 | More | #F48B00 |
| 시간 라벨 | Prep Time / Cook Time / Rest Time | #9E9E9E |
| 시간 값 | 15 min / 1 hr 10 mins / 10 mins | #232323 |
| 섹션 제목 | Ingredients / Nutrition Facts / Directions | #232323 |
| 서빙 | Servings (#707070) · 6 (#232323) · ± 아이콘 (#F48B00) | |
| 재료 수량·이름 | (6-2 표) | #232323 |
| 펼치기 버튼 | Show all ingredients | #F48B00 · 테두리 #D9D9D9 |
| 영양 라벨 | CALORIES / FAT / CARBS / PROTEIN | #9E9E9E |
| 영양 값 | 350 / 28g / 15g / 23g | #232323 |
| 스텝 라벨 | Step 1 … Step 7 | #232323 |
| 스텝 본문 | (8장 목록) | #707070 |
| CTA | Start cooking | #FFFFFF on #F48B00 |
| 하트 | (아이콘) | #E22D57 on #FFFFFF |

## 11. Figma에 없는 상태 (구현자가 정해야 하는 것)

Figma 프레임은 정적 1장이다. 다음 상태는 원본에 없다: 하트 비저장(빈 하트) 상태, About 펼친 상태("Close"), 재료 펼친 상태("Show fewer"), 재료 체크 상태, 서빙 최소/최대 비활성, 조리 모드 화면. 구현 시 위 토큰(색·폰트·반경)만으로 만들 것.
