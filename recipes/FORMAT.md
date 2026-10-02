# 레시피 데이터 포맷 (v1, 2026-09-30)

레시피 1개 = JSON 파일 1개 (`recipes/<id>.json`).
이 데이터가 웹앱과 킨들 EPUB 양쪽의 공통 원본이다.

## 설계 원칙
- 정량은 숫자와 단위를 분리 저장 → 인분 조절 시 자동 계산, 단위 변환 가능
- 정량이 없는 재료(예: "소금 약간")는 quantity를 null로 두고 note에 표현
- 조리 단계 텍스트에는 재료명을 중심으로 쓰고, 정확한 양은 재료 목록을 참조하게 한다
  (단계 안에 숫자를 박으면 인분 계산이 깨진다)
- 언어별 텍스트는 `text.<lang>` 아래 분리 → 언어 추가는 데이터 추가만으로 가능
  (수량·시간·이미지 같은 언어 중립 데이터는 공유)

## 필드
| 필드 | 설명 |
|---|---|
| id | 영문 슬러그 (예: kimchi-jjigae). 파일명과 일치 |
| category | 카테고리 id (예: soups-stews). 표시명은 앱 설정에서 언어별로 매핑 |
| illustration | 프로젝트 루트 기준 이미지 경로 (예: assets/illust/kimchi-jjigae.webp) |
| base_servings | 기준 인분. 모든 재료 수량은 이 인분 기준 |
| prep_minutes / cook_minutes | 준비/조리 시간 (분) |
| rest_minutes | 휴지 시간 (분, 없으면 0 또는 생략) |
| tags[] | 맛·특징 칩 (2~4개, 영어). 공식: [차별점] + [식감 보상] + [먹는 자리] |
| about_dish | { preview, full } — 요리 설명 노트. preview는 접힌 상태 문구(120자 기준·단어 경계), full은 펼친 전문 |
| ingredients[] | { quantity(숫자|null), unit, name{en,kr}, note{en}, img(재료 라이브러리 slug) } |
| text.en.title / story | 제목, 에피소드 인트로 (2~4문장) |
| text.en.steps[] | { text, timer_minutes(선택), img(스텝 일러스트 경로) } — 타이머는 해당 단계에 연결 |
| text.en.mistakes[] | "처음에 내가 망친 포인트" 팁 2~3개 |

## 단위 표기 (영어판 기준)
- 부피: cups, tbsp, tsp / 무게: oz, lb / 개수: cloves, stalks, pieces 등 자연 단위
- 온도는 단계 텍스트에 °F로 표기 (예: 375°F)

## 재료 이미지 (공유 라이브러리)
- 재료 일러스트는 레시피별이 아니라 재료 단위로 관리한다: `assets/illust/ingredients/INDEX.md` 등록표가 원본
- 새 레시피 작업 시 재료 이미지는 등록표에서 먼저 찾고, 있는 재료는 재사용, 없는 것만 Codex로 생성해 등록표에 추가
- 파일 위치: `assets/illust/ingredients/codex/<slug>.png` (slug는 재료 정체성 기준)

## 샘플
- `recipes/kimchi-jjigae.json` — 김치찌개 (기준 2인분), 일러스트 제작 완료분 반영
