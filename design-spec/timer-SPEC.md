# Timer — Design Spec (Figma `cta4gGnJ1511CoeJ91bg31`, node 51:782)

Only the visuals change. Keep `#timer-display`, `#timer-status`, `#timer-toggle` and `#timer-reset`.
**Figma has only one state: idle** (shows `40:00`, a play icon and "Start timer"). Anything marked *(not in Figma)* is my suggestion, not part of the design.

## 1. Layout
```
┌───────────────────────────────────────┐
│   (⟳)           40:00           (▶)   │
│  Reset                     Start timer │
└───────────────────────────────────────┘
```
**Card:** 329 × 98 px, background `#F9F9F9`, border-radius 8px, no border, no shadow.

Positions (from the card's top-left corner):

| Element | x | y | w×h | center |
|---|---|---|---|---|
| Reset button | 45 | 25 | 40×40 | (65, 45) |
| "Reset" label | 49 | 67 | 32×20 | (65, 77) |
| "40:00" | 118 | 23 | 92×44 | (164, 45) |
| Play button | 243 | 25 | 40×40 | (263, 45) |
| "Start timer" label | 233 | 67 | 60×20 | (263, 77) |

- The two button centers sit **99px left and right** of the card's horizontal center.
- The buttons and the time share one center line at **y = 45**. That isn't the card's middle; the content sits high.
- There's a **2px** gap between each button and its label.
- Padding works out to roughly top 23, bottom 11. Left and right differ only because the labels are different widths, so treat both columns as centered.

## 2. Colors
| Use | Hex | Figma token |
|---|---|---|
| Card background | `#F9F9F9` | — |
| Countdown digits | `#232323` | Other/Black |
| Labels | `#707070` | Secondary/700 |
| Button fill (both) | `#F48B00` | — |
| Icons | `#FFFFFF` | — |

## 3. Typography
- **Countdown:** Roboto Medium (500), 36px, line-height 44px, letter-spacing 0, `#232323`, centered, no wrapping. *(Not in Figma: add `tabular-nums` so the digits don't shift while counting.)*
- **Labels:** Inter Regular (400), 12px, line-height 1.7 (about 20px), letter-spacing −0.12px, `#707070`, centered.

## 4. Buttons
- 40×40 circles (`border-radius: 50%`), fill `#F48B00`, no border or shadow.
- **Reset:** white circular-arrow icon, 20×20, centered. In Figma this layer is misnamed "play".
- **Play:** white play-triangle icon, 15×15, 12.5px padding.
- The icons are outline icons from the Hugeicons set. Get the SVGs with Figma `download_assets` on nodes 51:770 (reset) and 51:766 (play).
- The labels sit **below** the circles, not inside them.
- Hover, active and focus states aren't designed. *(Suggestion: hover `#E07F00`, pressed `scale(0.95)`, focus a 2px `#F48B00` outline.)*

## 5. States
| State | In Figma? | Display | Right button |
|---|---|---|---|
| Idle | ✅ | `40:00` | ▶ "Start timer" |
| Running | ❌ | live countdown | *suggest* ⏸ "Pause" |
| Paused | ❌ | frozen value | *suggest* ▶ "Resume" |
| Done | ❌ | `00:00` | no alert designed |

- **`#timer-status` has no place in the design.** I suggest the right-hand label shows the status text (Start timer / Pause / Resume). Keep `#timer-status` hidden on screen but readable by screen readers (`aria-live`).
- The design has no progress ring or bar, icons beyond the two buttons, or decorative elements.
