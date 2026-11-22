"""Capture the portfolio's current dark design without changing its content.

Requires Python 3, playwright (with Chromium installed), and Pillow.
From the repository root: python scripts/audit_ui.py
English route: python scripts/audit_ui.py --lang en --output artifacts/ui/actual-en
Generated screenshots and the HTML gallery stay in artifacts/ui/ (gitignored).
"""

import argparse
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from functools import partial
from html import escape
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from importlib.metadata import version
from io import BytesIO
import json
import math
from pathlib import Path
import re
import subprocess
import sys
from threading import Thread

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright


ROOT = Path(__file__).resolve().parents[1]
VIEWPORTS = [
    (1024, 768), (1280, 720), (1440, 900), (1920, 1080),
    (320, 568), (360, 800), (390, 844), (430, 932),
]
SECTIONS = ["inicio", "proyectos", "sobre-mi", "certificaciones", "contacto"]
CONTRAST_METHOD = ('Nine background samples per text bounding box with only the measured text elements visibility:hidden; '
    'computed sRGB foreground, rendered DPR 1 background; layout preserved. '
    'This is targeted sampling, not a complete contrast audit.')

MEASURE_HERO_TITLE = r"""() => {
  const profile = document.querySelector('.hero__perfil').getBoundingClientRect();
  const text = document.querySelector('.hero__texto');
  const column = (getComputedStyle(text).display === 'contents'
    ? document.querySelector('.hero__titulo') : text).getBoundingClientRect();
  return [...document.querySelectorAll('.hero__titulo span')].map(e => {
    const range = document.createRange();
    range.selectNodeContents(e);
    const r = range.getBoundingClientRect();
    return {text:e.innerText, left:r.left, right:r.right, top:r.top, bottom:r.bottom,
      columnRight:column.right, profileLeft:profile.left,
      exceedsColumn:r.right > column.right + 1,
      overlapsProfile:r.right > profile.left && r.left < profile.right &&
        r.top < profile.bottom && r.bottom > profile.top};
  });
}"""

MEASURE = r"""() => {
  const round = value => Math.round(value * 100) / 100;
  const visible = e => e && e.getClientRects().length > 0 &&
    getComputedStyle(e).visibility !== 'hidden' && !e.closest('[hidden]');
  const box = e => {
    if (!e) return null;
    const r = e.getBoundingClientRect();
    const style = getComputedStyle(e);
    return {
      x: round(r.x + scrollX), y: round(r.y + scrollY),
      width: round(r.width), height: round(r.height),
      fontSize: parseFloat(style.fontSize),
      paddingTop: style.paddingTop, paddingBottom: style.paddingBottom,
    };
  };
  const label = e => (e.getAttribute('aria-label') || e.innerText || '')
    .replace(/\s+/g, ' ').trim();
  const boxes = selector => [...document.querySelectorAll(selector)]
    .filter(visible).map(e => ({label: label(e), ...box(e)}));
  const sections = Object.fromEntries([...document.querySelectorAll('main > section')]
    .map(e => [e.id, box(e)]));
  const text = [...document.querySelectorAll('body *')].filter(e =>
    visible(e) && !e.closest('svg, script, style, .sr-only, .simbolos') &&
    [...e.childNodes].some(n => n.nodeType === Node.TEXT_NODE && n.textContent.trim())
  ).map(e => ({
    selector: e.className ? '.' + String(e.className).trim().replace(/\s+/g, '.') : e.tagName.toLowerCase(),
    text: label(e).slice(0, 110), fontSize: parseFloat(getComputedStyle(e).fontSize),
    decorative: Boolean(e.closest('[aria-hidden="true"]')),
  }));
  const interactive = [...document.querySelectorAll('a[href], button')]
    .filter(e => visible(e) && !e.closest('.sr-only'))
    .map(e => ({selector: e.className, label: label(e), ...box(e)}));
  const contentSelectors = [
    '.hero__contenido', '.hero__herramientas', '.hero__pie',
    '.proyecto-destacado', '.proyectos__grid', '.sobre-mi__cuerpo',
    '.entornos__grid', '.finder', '.certificaciones', '.contacto__grid', '.pie__interno',
  ];
  const hero = document.querySelector('#inicio').getBoundingClientRect();
  const heroFooter = document.querySelector('.hero__pie').getBoundingClientRect();
  return {
    viewport: {width: innerWidth, height: innerHeight, dpr: devicePixelRatio},
    document: {width: document.documentElement.scrollWidth, height: document.documentElement.scrollHeight,
      horizontalOverflow: document.documentElement.scrollWidth > innerWidth},
    theme: document.documentElement.dataset.theme || 'dark',
    header: box(document.querySelector('.cabecera')),
    heroFitsFirstScreen: hero.bottom <= innerHeight + 1,
    heroFooterFitsFirstScreen: heroFooter.bottom <= innerHeight + 1,
    sections,
    footer: box(document.querySelector('.pie')),
    content: Object.fromEntries(contentSelectors.map(selector => [selector, box(document.querySelector(selector))])),
    projectCards: boxes('.proyectos__grid > .proyecto'),
    certificateCards: boxes('.certificacion'),
    filters: boxes('[data-filtro]'),
    interactive,
    targetsBelow44: interactive.filter(e => e.width < 44 || e.height < 44),
    minimumFontSize: Math.min(...text.map(e => e.fontSize)),
    minimumContentFontSize: Math.min(...text.filter(e => !e.decorative).map(e => e.fontSize)),
    textBelow12: text.filter(e => e.fontSize < 12),
    aboutArtBeforeText: getComputedStyle(document.querySelector('.sobre-mi__arte')).order === '-1',
    aboutArt: box(document.querySelector('.sobre-mi__arte')),
    images: [...document.images].filter(visible).map(e => ({
      src: e.getAttribute('src'), width: e.naturalWidth, height: e.naturalHeight, complete: e.complete,
    })),
  };
}"""


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_args):
        pass


@contextmanager
def local_site():
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(QuietHandler, directory=str(ROOT)))
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/"
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def screenshot(page, destination):
    page.screenshot(path=str(destination), animations="disabled")


def ready(page):
    page.evaluate("document.fonts.ready")
    page.wait_for_function("[...document.images].filter(e => e.loading !== 'lazy').every(e => e.complete)")


def contact_contrast(page):
    """Sample the rendered background with text hidden, preserving layout."""
    page.evaluate('window.scrollTo(0, 0)')
    content = page.locator('.contacto__texto .seccion__titulo, .contacto__intro, .contacto__etiqueta span')
    text = content.evaluate_all(r'''nodes => nodes.map(e => {
      const range = document.createRange();
      range.selectNodeContents(e);
      const r = range.getBoundingClientRect(), style = getComputedStyle(e);
      return {text:e.innerText, color:style.color, fontSize:parseFloat(style.fontSize),
        fontWeight:parseFloat(style.fontWeight), x:r.x, y:r.y + scrollY, width:r.width, height:r.height};
    })''')
    previous = content.evaluate_all("nodes => nodes.map(e => {const previous=e.style.visibility; e.style.visibility='hidden'; return previous})")
    try:
        background = Image.open(BytesIO(page.screenshot(full_page=True, animations='disabled'))).convert('RGB')
    finally:
        content.evaluate_all('(nodes, previous) => nodes.forEach((e, index) => e.style.visibility=previous[index])', previous)

    def luminance(rgb):
        linear = [value / 255 / 12.92 if value / 255 <= 0.04045
                  else ((value / 255 + 0.055) / 1.055) ** 2.4 for value in rgb]
        return sum(value * weight for value, weight in zip(linear, [0.2126, 0.7152, 0.0722]))

    results = []
    for item in text:
        rgba = [float(value) for value in re.findall(r'[\d.]+', item['color'])]
        alpha = rgba[3] if len(rgba) > 3 else 1
        samples = []
        for horizontal in [0.1, 0.5, 0.9]:
            for vertical in [0.1, 0.5, 0.9]:
                x = min(background.width - 1, max(0, round(item['x'] + item['width'] * horizontal)))
                y = min(background.height - 1, max(0, round(item['y'] + item['height'] * vertical)))
                rgb = background.getpixel((x, y))
                foreground = [color * alpha + base * (1 - alpha) for color, base in zip(rgba[:3], rgb)]
                light, dark = sorted([luminance(foreground), luminance(rgb)], reverse=True)
                samples.append({'x': x, 'y': y, 'background': list(rgb), 'ratio': round((light + 0.05) / (dark + 0.05), 2)})
        item['samples'] = samples
        item['ratioMinimum'] = min(sample['ratio'] for sample in samples)
        item['ratioMaximum'] = max(sample['ratio'] for sample in samples)
        item['threshold'] = 3 if item['fontSize'] >= 24 or item['fontSize'] >= 18.6667 and item['fontWeight'] >= 700 else 4.5
        results.append(item)
    return results


def capture(page, url, output, width, height, theme):
    folder = output / f"{width}x{height}-{theme}"
    folder.mkdir(parents=True, exist_ok=True)
    page.goto(url, wait_until="networkidle")
    ready(page)
    # Load lazy images through ordinary scrolling, then return to the initial view.
    for section in SECTIONS:
        page.locator(f'#{section}').scroll_into_view_if_needed()
    for image in page.locator('img[loading="lazy"]').all():
        image.scroll_into_view_if_needed()
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_function("window.scrollY === 0")
    page.wait_for_function("[...document.images].filter(e => e.getClientRects().length).every(e => e.complete)")
    page.evaluate("new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))")
    metrics = page.evaluate(MEASURE)
    metrics['heroTitle'] = page.evaluate(MEASURE_HERO_TITLE)
    screenshot(page, folder / "primera-vista.png")
    full = Image.open(BytesIO(page.screenshot(full_page=True, animations="disabled")))
    full.save(folder / "pagina-completa.png")
    for section, bounds in {**metrics["sections"], "pie": metrics["footer"]}.items():
        top = math.floor(bounds["y"])
        bottom = min(full.height, math.ceil(bounds["y"] + bounds["height"]))
        full.crop((0, top, full.width, bottom)).save(folder / f"{section}.png")

    interactions = {}
    page.locator('.skip-link').focus()
    interactions["skipLink"] = page.locator('.skip-link').evaluate(
        "e => ({width:e.getBoundingClientRect().width, height:e.getBoundingClientRect().height, "
        "outline:getComputedStyle(e).outlineStyle})"
    )
    menu = page.locator('.cabecera__menu')
    if menu.is_visible():
        menu.click()
        screenshot(page, folder / "menu-abierto.png")
        interactions["menuExpanded"] = menu.get_attribute('aria-expanded') == 'true'
        interactions["menuFirstLinkFocused"] = page.locator('.cabecera__enlace').first.evaluate(
            'e => document.activeElement === e'
        )
        interactions["menuTargets"] = page.locator('#navegacion a, #navegacion button').evaluate_all(
            "nodes => nodes.map(e => ({label:e.innerText, width:e.getBoundingClientRect().width, "
            "height:e.getBoundingClientRect().height}))"
        )
        page.keyboard.press('Escape')
        interactions["menuEscapeAndFocusReturn"] = menu.get_attribute('aria-expanded') == 'false' and menu.evaluate(
            'e => document.activeElement === e'
        )

    filters = []
    categories = page.locator('[data-filtro]').evaluate_all('nodes => nodes.map(e => e.dataset.filtro)')
    for category in categories:
        button = page.locator(f'[data-filtro="{category}"]')
        button.click()
        filters.append({
            "category": category, "visible": page.locator('.certificacion:visible').count(),
            "status": page.locator('#filtro-estado').inner_text(),
        })
    page.locator('[data-filtro="todos"]').click()
    interactions["filters"] = filters

    origin = page.locator('[data-certificado]').first
    origin.click()
    page.wait_for_function("document.querySelector('.visor-certificado__imagen').naturalWidth > 0")
    dialog = page.locator('#visor-certificado')
    screenshot(page, folder / 'visor-abierto.png')
    interactions["modal"] = dialog.evaluate("e => ({width:e.getBoundingClientRect().width, "
        "height:e.getBoundingClientRect().height, top:e.getBoundingClientRect().top, "
        "imageHeight:e.querySelector('img').getBoundingClientRect().height, "
        "title:e.querySelector('h2').innerText})")
    interactions["modal"]["initialFocus"] = page.locator('.visor-certificado__cerrar').evaluate(
        'e => document.activeElement === e')
    page.keyboard.press('Shift+Tab')
    interactions["modal"]["shiftTabTrap"] = page.locator('.visor-certificado__original').evaluate(
        'e => document.activeElement === e')
    page.keyboard.press('Tab')
    interactions["modal"]["tabTrap"] = page.locator('.visor-certificado__cerrar').evaluate(
        'e => document.activeElement === e')
    first_title = page.locator('#visor-certificado-titulo').inner_text()
    page.keyboard.press('ArrowRight')
    interactions["modal"]["arrowNavigation"] = page.locator('#visor-certificado-titulo').inner_text() != first_title
    page.keyboard.press('Escape')
    interactions["modal"]["escapeAndFocusReturn"] = not dialog.is_visible() and origin.evaluate(
        'e => document.activeElement === e')
    origin.click()
    page.wait_for_function("document.querySelector('.visor-certificado__imagen').naturalWidth > 0")
    page.mouse.click(1, 1)
    interactions["modal"]["backdropCloses"] = not dialog.is_visible()
    metrics["interactions"] = interactions
    metrics['contactContrast'] = contact_contrast(page)
    metrics["screenshots"] = [str(p.relative_to(output)).replace('\\', '/') for p in sorted(folder.glob('*.png'))]
    return metrics


def contact_sheets(output, runs):
    folder = output / 'resumenes'
    folder.mkdir(exist_ok=True)
    font = ImageFont.load_default(size=16)
    sheets = []
    for mobile in [False, True]:
        for theme in ['dark', 'light']:
            selected = [r for r in runs if (r['viewport']['width'] < 768) == mobile and r['theme'] == theme]
            for name in [*SECTIONS, 'pie', 'visor-abierto', 'menu-abierto']:
                thumbnails = []
                for run in selected:
                    viewport = run['viewport']
                    source = output / f"{viewport['width']}x{viewport['height']}-{theme}" / f'{name}.png'
                    if not source.exists():
                        continue
                    with Image.open(source) as original:
                        thumb = original.convert('RGB')
                        thumb.thumbnail((320, 2600), Image.Resampling.LANCZOS)
                    thumbnails.append((f"{viewport['width']}x{viewport['height']} {theme}", thumb))
                if not thumbnails:
                    continue
                sheet = Image.new('RGB', (332 * len(thumbnails) + 12,
                    max(im.height for _, im in thumbnails) + 48), '#e4e9f1')
                draw = ImageDraw.Draw(sheet)
                for index, (title, thumb) in enumerate(thumbnails):
                    x = 12 + index * 332
                    draw.text((x, 8), title, font=font, fill='#16202d')
                    sheet.paste(thumb, (x, 36))
                path = folder / f"{'movil' if mobile else 'escritorio'}-{theme}-{name}.webp"
                sheet.save(path, quality=82)
                sheets.append(path.relative_to(output).as_posix())
    return sheets


def gallery(output, runs, sheets):
    cards = []
    for run in runs:
        viewport = run['viewport']
        title = f"{viewport['width']} × {viewport['height']} · {run['theme']}"
        figures = ''.join(
            f'<figure><a href="{escape(path)}"><img src="{escape(path)}" loading="lazy" '
            f'alt="{escape(title)}: {escape(Path(path).stem)}"></a>'
            f'<figcaption>{escape(Path(path).stem)}</figcaption></figure>'
            for path in run['screenshots']
        )
        cards.append(f'<details><summary>{escape(title)}</summary><div class="grid">{figures}</div></details>')
    document = '''<!doctype html><html lang="es"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Auditoría visual del sitio</title>
<style>body{margin:2rem;font:16px/1.5 system-ui;background:#f4f5f7;color:#16202d}
h1{font-size:1.7rem}summary{cursor:pointer;padding:1rem;font-weight:650;background:white}
details{margin:1rem 0;border:1px solid #c3cad5}a{color:#1649a0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1rem;padding:1rem}
figure{margin:0}img{width:100%;max-height:600px;object-fit:contain;object-position:top;background:#dfe4ec}
figcaption{padding:.5rem 0}a:focus-visible,summary:focus-visible{outline:3px solid #1649a0}</style>
<h1>Auditoría visual · capturas originales</h1><p>Capturas completas y por sección de la revisión local.
Abre cada imagen para ver su tamaño original. Las alturas corresponden a píxeles CSS, escala 1.</p>'''
    overviews = '<h2>Resumen por sección y tamaño</h2><ul>' + ''.join(
        f'<li><a href="{escape(path)}">{escape(Path(path).stem)}</a></li>' for path in sheets
    ) + '</ul><h2>Capturas originales</h2>'
    (output / 'index.html').write_text(document + overviews + ''.join(cards) + '</html>', encoding='utf-8')


def source_inventory():
    assets = []
    for name in ['styles.css', 'app.js', 'assets/foto.webp', 'assets/proyectos/sipiit-portada.webp',
                 'assets/fondos/certificaciones.webp', 'assets/fondos/contacto.webp']:
        path = ROOT / name
        asset = {'path': name, 'bytes': path.stat().st_size}
        if path.suffix == '.webp':
            with Image.open(path) as image:
                asset['dimensions'] = list(image.size)
        assets.append(asset)
    css = (ROOT / 'styles.css').read_text(encoding='utf-8')
    return {'assets': assets, 'maxWidthMediaQueries': re.findall(r'@media\s*\(max-width:\s*([^)]+)\)', css)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'artifacts/ui/actual')
    parser.add_argument('--lang', choices=['es', 'en'], default='es')
    args = parser.parse_args()
    output = args.output.resolve()
    if not output.is_relative_to(ROOT):
        parser.error('--output must stay inside the repository')
    output.mkdir(parents=True, exist_ok=True)
    revision = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip()
    report = {
        'date': datetime.now(timezone(timedelta(hours=-5))).isoformat(timespec='seconds'),
        'timezone': 'America/Bogota', 'revision': revision,
        'language': args.lang,
        'method': 'Local HTTP, Chromium, DPR 1, reduced motion, fonts and images loaded; mobile emulation below 768px.',
        'contrastMethod': CONTRAST_METHOD,
        'tooling': {'python': sys.version.split()[0], 'playwright': version('playwright'), 'Pillow': version('Pillow')},
        'sourceInventory': source_inventory(),
        'runs': [],
    }
    with local_site() as url, sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        report['browser'] = f'Chromium {browser.version}'
        for width, height in VIEWPORTS:
            for theme in ['dark']:
                context = browser.new_context(viewport={'width': width, 'height': height},
                    device_scale_factor=1, reduced_motion='reduce', locale='es-CO',
                    is_mobile=width < 768, has_touch=width < 768, color_scheme='dark')
                page = context.new_page()
                errors, failed_requests = [], []
                page.on('pageerror', lambda error: errors.append(str(error)))
                page.on('console', lambda message: errors.append(message.text) if message.type == 'error' else None)
                page.on('response', lambda response: failed_requests.append({'url': response.url.replace(url, '/'),
                    'status': response.status}) if response.status >= 400 else None)
                page.on('requestfailed', lambda request: failed_requests.append({
                    'url': request.url.replace(url, '/'), 'failure': request.failure}))
                run = capture(page, url + ('en/' if args.lang == 'en' else ''), output, width, height, theme)
                run['consoleErrors'], run['failedRequests'] = errors, failed_requests
                report['runs'].append(run)
                context.close()
                print(f"{width}x{height} {theme}: hero={run['sections']['inicio']['height']}, "
                    f"page={run['document']['height']}, overflow={run['document']['horizontalOverflow']}", flush=True)
        browser.close()
    (output / 'metricas.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    gallery(output, report['runs'], contact_sheets(output, report['runs']))
    print(f"Saved {len(report['runs'])} runs and {sum(len(run['screenshots']) for run in report['runs'])} screenshots: {output}")


if __name__ == '__main__':
    main()
