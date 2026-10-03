# 재료 일러스트 공유 라이브러리

재료 이미지는 요리가 아니라 재료 단위로 관리한다. (2026-10-01 사용자 지시)
한 번 만든 재료 그림은 등록해 두고, 다른 레시피에서 같은 재료가 나오면 새로 그리지 않고 재사용한다.

## 규칙

1. 새 레시피의 재료 이미지가 필요하면, 먼저 아래 등록표에서 slug로 찾는다.
2. 이미 있는 재료는 등록된 파일을 그대로 재사용한다. 다시 생성하지 않는다.
3. 없는 재료만 Codex로 생성하고, 등록표에 한 줄 추가한다 (slug = 파일명).
4. slug는 재료의 정체성 기준이다 (예: `garlic`). 손질 상태가 달라 그림이 달라져야 하면 별도 slug를 만든다 (예: `green-onion-roots` vs 대파 전체).
5. 생성 규칙은 기존과 동일: 수채화 스타일, 흰 배경, 정사각형, 굵고 단순하게 — 작은 원형 썸네일(약 40px)에서도 읽혀야 한다.
6. 정식 라이브러리는 이 폴더의 `codex/` 하위 폴더. 이 폴더 루트에 있는 구 Muse 생성본(`media-generation-*.png`)은 폐기된 것이므로 사용하지 않는다.
7. `codex/water-pitcher-test.png`는 테스트본 — 사용 금지.

## 등록표

경로: `assets/illust/ingredients/codex/<slug>.png`

| slug | EN | KR | 최초 사용 |
|---|---|---|---|
| pork-belly | Pork belly | 삼겹살 | guun-bossam |
| water | Water | 물 | guun-bossam |
| yellow-onion | Sweet onion | 양파 | guun-bossam |
| green-onion-roots | Green onion roots | 대파뿌리 | guun-bossam |
| garlic | Garlic | 마늘 | guun-bossam |
| ginger | Ginger | 생강 | guun-bossam |
| bay-leaves | Bay leaves | 월계수잎 | guun-bossam |
| sugar | Sugar | 설탕 | guun-bossam |
| doenjang | Doenjang (Korean soybean paste) | 된장 | guun-bossam |
| soy-sauce | Soy sauce | 간장 | guun-bossam |
| corn-syrup | Corn syrup (mulyeot) | 물엿 | guun-bossam |
| la-galbi | LA galbi (flanken-cut beef short ribs) | LA 갈비 | yangnyeom-galbi |
| green-onion-chopped | Chopped green onion | 다진 대파 | yangnyeom-galbi |
| garlic-minced | Minced garlic | 간마늘 | yangnyeom-galbi |
| cooking-wine | Cooking wine (mat-sul) | 맛술 | yangnyeom-galbi |
| ginger-minced | Grated ginger | 간생강 | yangnyeom-galbi |
| black-pepper | Black pepper | 후추 | yangnyeom-galbi |
| sesame-oil | Sesame oil | 참기름 | yangnyeom-galbi |
| pear-juice | Pear juice | 배주스 | yangnyeom-galbi |
