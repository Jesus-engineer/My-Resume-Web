"""Audita un PDF de CV para verificar compatibilidad ATS, 1 pagina y privacidad.

Uso:
  python .agents/skills/ats-resume-engineer/scripts/audit_ats_pdf.py assets/cv-jesus-velasquez.pdf
"""

from __future__ import annotations

import sys
import unicodedata
from pathlib import Path
import pypdf

REQUIRED_HEADINGS = [
    "PERFIL PROFESIONAL",
    "EDUCACION",
    "PROYECTOS",
    "EXPERIENCIA",
    "HABILIDADES TECNICAS",
    "CERTIFICACIONES",
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


def audit(pdf_path: Path) -> int:
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

    for heading in REQUIRED_HEADINGS:
        if heading not in normalized_upper:
            errors.append(f"Falta encabezado esperado: {heading}")

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
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("assets/cv-jesus-velasquez.pdf")
    raise SystemExit(audit(target))
