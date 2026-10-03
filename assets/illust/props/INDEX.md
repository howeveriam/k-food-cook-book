# 요리 도구(소품) 일관성 등록표

같은 도구는 모든 이미지에서 형태·색감·질감이 동일하게 나와야 한다. (2026-10-01 사용자 지시)
재료 라이브러리(`assets/illust/ingredients/INDEX.md`)와 같은 방식: 기준을 등록해 두고 생성 때마다 상기시킨다.

## 규칙

1. 이미지 생성 시, 등장하는 도구는 아래 등록표의 기준 이미지를 참조 이미지로 항상 함께 전달한다.
2. 프롬프트에는 아래 기준 묘사를 그대로 넣는다. 도구 묘사를 매번 새로 지어내지 않는다.
3. 스텝 이미지는 앞 스텝의 상태를 이어받는다: 스텝 N 생성 시 스텝 N-1의 이미지를 참조로 함께 주고, 직전 스텝에 보이던 재료·액체 상태를 유지한 채 다음 동작만 더하라고 지시한다. (예: 스텝 1에서 넣은 재료는 스텝 2의 끓는 물에서도 보여야 한다)
4. 새 도구가 처음 등장하면 이 표에 등록한다 (slug, 기준 묘사, 기준 이미지).

## 등록표

| slug | 기준 묘사 (프롬프트에 그대로 사용) | 기준 이미지 |
|---|---|---|
| braising-pot | a wide pale blue-gray speckled enamel pot with two loop side handles and a thick pale rim | `steps/step-6.png` (2026-10-01 냄비 통일본으로 확정) |
| cast-iron-skillet | a black cast-iron skillet | `steps/step-4.png` |
| metal-tongs | stainless steel kitchen tongs | `steps/step-5.png` |
| wooden-spoon | a light wooden spoon | `steps/step-1.png` |
| cutting-board | a thick wooden cutting board | `steps/step-7.png` |
| chefs-knife | a chef's knife | `steps/step-7.png` |
| round-wok | a large round black seasoned wok with two short loop handles on both sides | `steps/jjukkumi-step-11-v3.png` (2026-10-03 쭈꾸미 스텝 11/12/13 통일 기준으로 확정) |

기준 이미지 경로 접두사: `assets/illust/` (예: `assets/illust/steps/step-6.png`)
