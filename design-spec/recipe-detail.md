# Recipe Detail Page — Design Framework (2026-10-02 확정)

구운 보쌈 레시피 상세 화면의 전체 레이아웃·기능 정리. Figma(cta4gGnJ1511CoeJ91bg31) + 사용자와의 조정 내용이 모두 반영됨.

## Design Tokens
- 페이지 배경: #FFFFFF (순백)
- 칩/카드 배경: #F9F9F9, 칩 글자: #9E9E9E
- Primary: #F48B00 (주황)
- 하트: #E22D57
- 별 채움: #FFD800, 별 빈칸: #E1E1E1
- 폰트: Inter (본문) + Playfair Display 700 (제목) — base64 내장, 오프라인 표시
- 페이지 폭: 375px 고정, 가운데 정렬 (데스크탑 레이아웃은 나중에)

## Section Order (위에서 아래로)
1. Hero 이미지 (favorite 하트 오버레이, 뒤로가기)
2. Title 카드 (히어로와 94px 겹침, 좌우 24px 들여짐, 그림자 0 4px 15px rgba(0,0,0,.04), r12)
3. About ("About this dish")
4. Difficulty (별점)
5. Time (Prep/Cook/Rest)
6. Ingredients
7. Directions
8. Nutrition Facts
9. Start cooking 버튼 (하단 고정 CTA)

## Section Specs

### About
- 미리보기 + "More"/"Close" 서랍
- 서랍 인터랙션: 페이드 없음, 텍스트 위치 고정. 컨테이너만 미닫이식으로 열리며 아래 콘텐츠를 밀어냄 (덜커덕거림 금지)
- 본문: 18px

### Difficulty (2026-10-02 신규)
- About 바로 다음, 279px 흰색 컨테이너, r12, 그림자 없음
- 라벨 "Difficulty": Inter 500, 12px, #9E9E9E, 중앙정렬
- 별 5개: 각 18×18px, 간격 6px (Figma 원본 SVG)
- 구운 보쌈: 3/5점 (#FFD800 ×3 + #E1E1E1 ×2)
- 값은 recipes/*.json의 "difficulty" 필드에서 읽음

### Time
- #F9F9F9 카드, r12
- 라벨 (Prep Time 등): 15px, #9E9E9E
- 값: 18px, 검정, 볼드
- 표기 형식: 15m, 1h10m, 10m (m/h 약어, 띄어쓰기 없음)

### Ingredients
- 헤더: "Ingredients" + Servings 스테퍼 (− 6 +)
- 인분 숫자: 16px
- 재료 행: 일러스트 + 정량(16px) + 재료명(18px, 600)
- 재료명 행간: 1.45 (두 줄이 되어도 하나의 내용으로 보이게)
- 재료 행 간격: 20px (다른 재료와 구분되게)
- 행 높이: min-height 48px (두 줄 이름이 잘리지 않게)
- "Show all ingredients" 서랍: 5개만 표시 후 펼치기
- 서랍 인터랙션: 행이 아래로 슬라이드(translateY -16px→0, 40ms stagger) + 투명도 페이드, 500ms

### Directions
- 스텝 라벨 ("Step 1"): 14px, 600
- 스텝 본문: 18px

### Nutrition Facts
- 라벨: 11px, 600

## Cooking Mode (dialog)
- 스텝 영상: 720×480, 4초, 음소거 루프, 자동재생, 페이드인
- 스텝 설명문: 18px
- 타이머 (Figma 51-782): 3열 카드 (리셋 - 카운트다운 - 시작), #F9F9F9, r8, 높이 98px
  - 원형 버튼 40px #F48B00, 흰색 아이콘
  - 카운트다운: 36px, Inter 500, #232323
  - 버튼 라벨: 12px, #707070
  - 기능: 시작/일시정지/재개/리셋, 종료 비프음, 화면 꺼짐 방지
  - 스텝 6 (40분), 스텝 7 (10분) 공용
- 하단 네비: Previous (16px) / Next (주황 버튼)
  - 스텝 1에서는 Previous 없음 → Next가 전폭 차지

## Future (나중에)
- Favorite 하트: 현재 프론트엔드 껍데기만. 나중에 북마크 기능 추가 (리스팅 화면 + 요리 페이지)
- 데스크탑 반응형 레이아웃: 사용자가 Figma에 직접 디자인한 뒤 구현

## Change Log
- 2026-10-02: Difficulty 섹션 추가, 타이머 UI 재디자인, 폰트 크기 조정 (본문 18px 등), 시간 표기 1h10m 형식, 재료 행간/간격 조정, 스텝1 Next 전폭
