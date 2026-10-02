# Difficulty — Design Spec (Figma `cta4gGnJ1511CoeJ91bg31`, frame "Recipe Details - 1" node 38:52)

New section the user added below the About section. Read-only extraction via Figma MCP on 2026-10-02; nothing in Figma was changed.

```
┌───────────────────────────────────────┐
│              Difficulty               │  ← gray label, centered
│                                       │
│         ★  ★  ★  ☆  ☆                │  ← 5 stars, centered (3 yellow / 2 gray)
└───────────────────────────────────────┘
```

## 1. Position & Order

Page section order (top → bottom):

1. Hero card → title card → chips → **About this dish** (inside the white `cards` box, node 38:64)
2. **Difficulty** (node 55:783) ← this section
3. Prep / Cook / Rest Time box (node 38:86, first child of `how-to` node 38:85)

Vertical gaps:

| From | To | Gap |
|---|---|---|
| Bottom of About's "More" link (Group-1 y 505) | Difficulty section top | **26px** |
| Bottom of `cards` box (521) | Difficulty section top (531) | **10px** |
| Difficulty section bottom (585) | Time box top (609) | **24px** (container column gap) |

Horizontal: the section is **279px wide**, inset **24px from each side** of the 327px content column — the same width as the `cards` box (279 + 24 + 24 = 327). Frame is 375 wide; section box in frame coordinates: **x 48, y 649, w 279, h 54**.

## 2. Section Container

- **Background:** `#FFFFFF`, `border-radius: 12px`, **no shadow, no border**. (The title card has a `0 4px 15px rgba(0,0,0,0.04)` shadow; Difficulty has none.)
- The page background is also `#FFFFFF`, so the card edge is effectively invisible — it reads as plain content on the page.
- **Layout:** vertical flex column, items centered, **8px gap** between label and star row.
- **Padding:** top **8px**, bottom **0**, left/right **0**.
- Height check: 8 (top pad) + 20 (label) + 8 (gap) + 18 (stars) = **54px** ✓

## 3. "Difficulty" Label (node 55:817)

- **Text:** `Difficulty` (exact case, no transform)
- **Font:** Inter Medium (500) — Figma text style "Body/small/medium"
- **Size:** 12px, **line-height 1.7** (20.4px; box is 20px tall)
- **Letter-spacing:** −1% = **−0.12px**
- **Color:** `#9E9E9E` (token `Secondary/500` — the same gray as chip text and time labels)
- **Alignment:** center, `white-space: nowrap`
- Bounding box (frame coords): x 162, y 657, w 51, h 20 → centered: (279 − 51) / 2 = **114** from section left ✓

## 4. Stars (node 56:859, "Stars")

- **Count:** 5, each an instance of the Figma component `star-filled` (1:26). All five layers are named `star-filled`; filled vs empty is set by **fill color**, not by a different component.
- **Size:** each star **18 × 18 px**, in a horizontal flex row with **6px gap** (centers 24px apart), top-aligned.
- Star row box (frame coords): **x 130.5, y 685, w 114, h 18** (114 = 5×18 + 4×6). Centered: (279 − 114) / 2 = **82.5** from section left ✓
- Per-star x positions relative to the section (y = 36 for all): **82.5 / 106.5 / 130.5 / 154.5 / 178.5**
- **Rating: 3/5** — stars 1–3 filled, stars 4–5 empty.

| State | Fill (hex) | Figma token | Stars |
|---|---|---|---|
| Filled | `#FFD800` | Warning/500 | 1, 2, 3 |
| Empty | `#E1E1E1` | Secondary/100 | 4, 5 |

- **Rendering:** vector, not raster. Both states share the **identical path** — only the fill differs (confirmed from the downloaded SVG assets).
- Asset files (exported from Figma via `download_assets`, saved for the implementer):
  - `design-spec/icons/star-filled.svg` (`#FFD800`)
  - `design-spec/icons/star-empty.svg` (`#E1E1E1`)

Star SVG (`viewBox="0 0 16.4791 15.7452"`, rendered at 18×18):

```svg
<svg viewBox="0 0 16.4791 15.7452" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path id="Vector" fill="#FFD800" d="M5.42731 4.75348L0.642314 5.44723L0.557564 5.46448C0.429268 5.49854 0.31231 5.56603 0.218633 5.66008C0.124956 5.75412 0.0579163 5.87134 0.0243603 5.99977C-0.0091957 6.1282 -0.00806586 6.26323 0.0276344 6.39108C0.0633346 6.51893 0.132326 6.63501 0.227564 6.72748L3.69406 10.1017L2.87656 14.868L2.86681 14.9505C2.85896 15.0832 2.88651 15.2156 2.94665 15.3341C3.00679 15.4526 3.09735 15.5531 3.20907 15.6251C3.32078 15.6971 3.44963 15.7382 3.58242 15.7441C3.71522 15.7499 3.84719 15.7204 3.96481 15.6585L8.24431 13.4085L12.5141 15.6585L12.5891 15.693C12.7129 15.7417 12.8474 15.7567 12.9789 15.7363C13.1104 15.7159 13.234 15.6609 13.3373 15.5769C13.4405 15.493 13.5195 15.383 13.5662 15.2585C13.6129 15.1339 13.6256 14.9991 13.6031 14.868L12.7848 10.1017L16.2528 6.72673L16.3113 6.66298C16.3949 6.56005 16.4497 6.43682 16.4701 6.30582C16.4905 6.17483 16.4759 6.04076 16.4276 5.91727C16.3794 5.79379 16.2993 5.6853 16.1954 5.60286C16.0916 5.52042 15.9678 5.46698 15.8366 5.44798L11.0516 4.75348L8.91256 0.418477C8.85067 0.292878 8.75485 0.187113 8.63596 0.113155C8.51706 0.0391975 8.37984 0 8.23981 0C8.09979 0 7.96257 0.0391975 7.84367 0.113155C7.72478 0.187113 7.62896 0.292878 7.56706 0.418477L5.42731 4.75348Z"/>
</svg>
```

(The empty variant is the same markup with `fill="#E1E1E1"`.)

## 5. Implementation Notes for Codex

- Section is **static display only** — no hover, tap, or interactive states are designed. (The SVG star is a 5-point rounded star; do not substitute a different star glyph.)
- CSS equivalent:

```css
.difficulty {
  width: 279px;
  margin: 0 auto;            /* 24px gutters inside the 327px column */
  background: #FFFFFF;
  border-radius: 12px;
  padding: 8px 0 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.difficulty-label {
  font-family: Inter, sans-serif;
  font-weight: 500;
  font-size: 12px;
  line-height: 1.7;
  letter-spacing: -0.12px;
  color: #9E9E9E;
  text-align: center;
  white-space: nowrap;
}
.difficulty-stars { display: flex; gap: 6px; }
.difficulty-stars svg { width: 18px; height: 18px; display: block; }
```

- Placement in the page flow: **26px below** the bottom of About's "More" link (10px below the `cards` box bottom edge), **24px above** the time container. Side gutters: 24px within the content column (section itself is full column width, 279px).
- The rating value (3/5) comes from recipe data (`recipes/guun-bossam.json`) — render filled stars for the rating count, empty for the rest.
- Fonts: use the existing base64-embedded Inter (offline rule). No Playfair Display here.
