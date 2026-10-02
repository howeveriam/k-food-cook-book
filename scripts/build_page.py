#!/usr/bin/env python3
"""레시피 JSON + 최적화 이미지 → 단독 실행 HTML 페이지 빌드.

사용법: python3 scripts/build_page.py recipes/<id>.json prototype/<id>.html
- 이미지는 빌드 시점에 리사이즈·JPEG 변환 후 data URI로 내장한다.
- 본문(제목·칩·재료·스텝 등)은 빌드 시점에 HTML로 미리 렌더링한다
  (JS가 막힌 뷰어에서도 내용이 보이도록; JS는 인터랙션만 담당).
"""
import base64
import html as htmlmod
import io
import json
import pathlib
import sys

from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parent.parent


def _datauri(img: Image.Image, q: int) -> str:
    buf = io.BytesIO()
    img.convert("RGB").save(buf, "JPEG", quality=q, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def _cover(path: pathlib.Path, tw: int, th: int, q: int) -> str:
    im = Image.open(path).convert("RGB")
    s = max(tw / im.width, th / im.height)
    im = im.resize((int(im.width * s + 0.5), int(im.height * s + 0.5)), Image.LANCZOS)
    x = (im.width - tw) // 2
    y = (im.height - th) // 2
    return _datauri(im.crop((x, y, x + tw, y + th)), q)


def fmt_qty(q):
    if q is None:
        return ""
    quarters = round(q * 4)
    if quarters == 0:
        return "a pinch"
    whole, rem = divmod(quarters, 4)
    fr = ["", "¼", "½", "¾"][rem]
    if whole == 0:
        return fr
    return f"{whole}{fr}" if fr else str(whole)


def fmt_time(m):
    m = int(m)
    if m >= 60:
        h, r = divmod(m, 60)
        return f"{h} hr" + (f" {r} mins" if r else "s")
    return f"{m} min" if m == 1 else f"{m} mins"


def esc(s):
    return htmlmod.escape(s, quote=False)


def build(recipe_path: str, out_path: str) -> None:
    recipe = json.loads(pathlib.Path(recipe_path).read_text(encoding="utf-8"))
    T = recipe["text"]["en"]

    # 이미지 최적화
    hero = _cover(ROOT / recipe["illustration"], 660, 660, 80)
    step_imgs = [
        _cover(ROOT / s["img"], 660, 440, 76) for s in T["steps"]
    ]
    ing_imgs = {}
    for ing in recipe["ingredients"]:
        slug = ing.get("img")
        if not slug:
            continue
        p = ROOT / "assets" / "illust" / "ingredients" / "codex" / f"{slug}.png"
        im = Image.open(p).convert("RGB").resize((160, 160), Image.LANCZOS)
        ing_imgs[slug] = _datauri(im, 70)
    recipe["_images"] = {"steps": step_imgs, "ingredients": ing_imgs}

    # 본문 미리 렌더링
    chips = "".join(
        f'<span class="chip">{esc(t)}</span>' for t in recipe.get("tags", [])
    )
    about_full = "".join(
        f"<p>{esc(p)}</p>"
        for p in recipe["about_dish"]["full"].split("\n\n")
    )
    base = recipe["base_servings"]

    def ing_row(ing):
        qty = fmt_qty(ing["quantity"])
        unit = f' {ing["unit"]}' if ing["unit"] else ""
        # Figma display strings; preserve complete source data in recipe JSON.
        names = {"green-onion-roots": "Green onion roots (optional)",
                 "garlic": "Garlic (about 10 cloves)"}
        name = names.get(ing.get("img"), ing["name"]["en"])
        thumb = ing_imgs.get(ing.get("img"), "")
        img = f'<img src="{thumb}" alt="">' if thumb else ""
        return (
            f'<li class="ing" data-i="{recipe["ingredients"].index(ing)}" role="checkbox" tabindex="0" aria-checked="false"'
            + (' hidden' if recipe["ingredients"].index(ing) >= 5 else '') + '>'
            f"{img}"
            f'<span class="qty">{qty}{unit}</span>'
            f'<span class="nm">{esc(name)}</span>'
            f'<span class="tick">✓</span></li>'
        )

    ings = "".join(ing_row(i) for i in recipe["ingredients"])
    N = recipe["nutrition"]
    nutri = (
        f'<div class="cell"><div class="k">CALORIES</div><div class="v">{N["kcal"]}</div></div>'
        f'<div class="cell"><div class="k">FAT</div><div class="v">{N["fat_g"]}g</div></div>'
        f'<div class="cell"><div class="k">CARBS</div><div class="v">{N["carbs_g"]}g</div></div>'
        f'<div class="cell"><div class="k">PROTEIN</div><div class="v">{N["protein_g"]}g</div></div>'
    )

    def step_block(s, i):
        return (
            f'<div class="step"><div class="s-label">Step {i + 1}</div>'
            f'<img src="{step_imgs[i]}" alt="Step {i + 1}">'
            f"<p>{esc(s['text'])}</p></div>"
        )

    divider = (ROOT / "design-spec/icons/divider-v.svg").read_text()
    nutri = nutri.replace('</div></div><div class="cell">', '</div></div>' + divider + '<div class="cell">')

    steps = "".join(step_block(s, i) for i, s in enumerate(T["steps"]))

    template = (ROOT / "prototype" / "template.html").read_text(encoding="utf-8")
    subs = {
        "__HERO__": hero,
        "__TITLE__": esc(T["title"]),
        "__CHIPS__": chips,
        "__ABOUT_PREVIEW__": esc(recipe["about_dish"]["preview"]),
        "__ABOUT_FULL__": about_full,
        "__PREP__": fmt_time(recipe["prep_minutes"]).replace(" mins", " min"),
        "__COOK__": fmt_time(recipe["cook_minutes"]),
        "__REST__": fmt_time(recipe.get("rest_minutes") or 0),
        "__SERVINGS__": str(base),
        "__INGS__": ings,
        "__NUTRI__": nutri,
        "__STEPS__": steps,
        "__RECIPE_JSON__": json.dumps(recipe, ensure_ascii=False).replace("<", "\\u003c"),
    }
    for icon in (ROOT / "design-spec/icons").glob("*.svg"):
        subs["__ICON_" + icon.stem.upper().replace("-", "_") + "__"] = icon.read_text()
    fonts = []
    for family, filename, weight in [("Inter", "inter-latin.woff2", "400 700"),
                                     ("Playfair Display", "playfair-display-latin.woff2", "700")]:
        data = base64.b64encode((ROOT / "prototype/fonts" / filename).read_bytes()).decode()
        fonts.append(f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};font-display:swap;src:url(data:font/woff2;base64,{data}) format('woff2')}}")
    subs["__FONT_CSS__"] = "\n".join(fonts)
    html = template
    for k, v in subs.items():
        html = html.replace(k, v)
    title = T["title"]
    html = html.replace(
        "<title>K-Food Kitchen</title>",
        f"<title>{esc(title)} · K-Food Kitchen</title>",
    )
    out = pathlib.Path(out_path)
    out.write_text(html, encoding="utf-8")
    print(f"built {out} ({len(html.encode("utf-8")) // 1024} KB)")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
