"""Audita un PDF de CV para verificar compatibilidad ATS, 1 pagina y privacidad.

Uso:
  python .agents/skills/ats-resume-engineer/scripts/audit_ats_pdf.py assets/cv-jesus-velasquez.pdf
"""

from __future__ import annotations

import argparse
import unicodedata
from pathlib import Path
import pypdf

REQUIRED_HEADINGS_ES = [
    "PERFIL PROFESIONAL",
    "EDUCACION",
    "PROYECTOS",
    "EXPERIENCIA Y LIDERAZGO",
    "HABILIDADES TECNICAS",
    "CERTIFICACIONES",
]
REQUIRED_HEADINGS_EN = [
    "PROFESSIONAL SUMMARY", "EDUCATION", "PROJECTS", "EXPERIENCE AND LEADERSHIP",
    "TECHNICAL SKILLS", "CERTIFICATIONS",
]

FORBIDDEN_TERMS = [
    "730E7489",
    "xertify",
    "foto_950kb",
]


def strip_accents(value: str) -> str:
    return "".join(
        ch for ch in unicodedata.normalize("NFD", value) if unicodedata.category(ch) != "Mn"
    )


def audit(pdf_path: Path, language: str = "es") -> int:
    if not pdf_path.exists():
        print(f"ERROR: No existe {pdf_path}")
        return 1

    reader = pypdf.PdfReader(str(pdf_path))
    num_pages = len(reader.pages)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    normalized_upper = strip_accents(text).upper()

    errors: list[str] = []
    if num_pages != 1:
        errors.append(f"Se esperaba 1 pagina, pero el PDF tiene {num_pages} paginas.")

    if len(text.strip()) < 400:
        errors.append(f"Texto extraido insuficiente ({len(text.strip())} chars); posible fallo ATS.")

    headings = REQUIRED_HEADINGS_EN if language == "en" else REQUIRED_HEADINGS_ES
    heading_positions = []
    lines = [line.strip() for line in normalized_upper.splitlines()]
    for heading in headings:
        if heading not in normalized_upper:
            errors.append(f"Falta encabezado esperado: {heading}")
        positions = [index for index, line in enumerate(lines) if line == heading]
        if not positions:
            errors.append(f"El encabezado no aparece en una linea propia: {heading}")
        else:
            heading_positions.append(positions[0])
    if heading_positions != sorted(heading_positions):
        errors.append("Los encabezados no se extraen en orden de lectura.")

    if language == "en":
        if not str(reader.trailer['/Root'].get('/Lang', '')).startswith('en'):
            errors.append("El idioma del PDF no esta declarado como ingles.")
        links = {annotation.get_object().get('/A', {}).get('/URI')
                 for page in reader.pages for annotation in page.get('/Annots', [])}
        for expected in ['mailto:jvelasquez.dev@gmail.com', 'https://github.com/Jesus-engineer',
                         'https://www.linkedin.com/in/jesus-david-velasquez-mercado-dev']:
            if expected not in links:
                errors.append(f"Falta enlace de contacto clicable: {expected}")

    for term in FORBIDDEN_TERMS:
        if term.lower() in text.lower():
            errors.append(f"Termino sensible detectado en PDF publico: {term}")

    print(f"Archivo: {pdf_path}")
    print(f"Paginas: {num_pages} | Caracteres extraibles: {len(text.strip())} | Tamano: {pdf_path.stat().st_size} bytes")

    if errors:
        for err in errors:
            print(f"FAIL: {err}")
        return 1

    print("PASS: PDF cumple 1 pagina, texto lineal extraible, secciones estandar y privacidad.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', nargs='?', type=Path)
    parser.add_argument('--lang', choices=['es', 'en'], default='es')
    args = parser.parse_args()
    target = args.pdf or Path('assets/cv-jesus-velasquez' + ('-en' if args.lang == 'en' else '') + '.pdf')
    raise SystemExit(audit(target, args.lang))
