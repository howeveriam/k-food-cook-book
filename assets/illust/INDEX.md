# Illustration Library — 구운 보쌈 (Grilled Bossam)

정리일: 2026-10-02. 확정본만 바로 쓰고, 나머지는 archive/에 보관.

## 확정본 (빌드에서 참조 중 — 이동 금지)

| 폴더 | 내용 | 규격 |
|---|---|---|
| `guun-bossam-hero-v2.png` (루트) | 레시피 대표 이미지 (`recipes/guun-bossam.json`의 `illustration`) | — |
| `steps/step-1..7.png` | 조리 단계 일러스트 7장 (쿠킹모드 포스터로도 사용) | 1536×1024, 3:2 |
| `ingredients/codex/<slug>.png` | 재료 일러스트 공유 라이브러리 (등록표 `ingredients/INDEX.md`) | — |
| `props/` | 도구 등록표 (`props/INDEX.md`) — 냄비·접시·집게 등 기준 이미지 | — |

## 파생본 (영상 제작용)

| 폴더 | 내용 | 용도 |
|---|---|---|
| `steps_veo/step-N-16x9.png` | 16:9 패딩본 (흰 여백 좌우) | Veo API image-to-video 입력용 |
| `steps_9x16/step-N-9x16.png` | 9:16 패딩본 (흰 여백 상하, 1536×2731) | 구글포토 앱 photo-to-video 입력용 |

## 완성된 스텝 영상

`../video/steps/step-1..7.mp4` — 720×480, 4초, 무음. 쿠킹모드에서 재생 중.

## 보관 (archive/)

- `steps/archive/` — 스텝 일러스트 구버전(old/v2/v3), 비교·컨택시트
- `ingredients/archive/` — 재료 생성 작업파일 (media-generation-*)
- `archive/` (루트) — 히어로 구버전, 킴치찌개 webp, 생성 작업파일

## 다음 레시피 영상 일괄 작업 시

1. 위 확정본 `steps/` + `steps_veo/`를 Veo 3.1 API(Lite, 720p, 4초, 무음)에 투입
2. 결과물은 `../video/steps/`에, 크롭은 기존 파이프라인 참고
3. GCP 결제는 그때 등록 (2026-10-02 결정: 일러스트 완성 후 일괄 진행)
