"""Genera un CV PDF ATS-friendly de 1 pagina en formato una sola columna.

Uso:
  python .agents/skills/ats-resume-engineer/scripts/build_ats_cv.py
  python .agents/skills/ats-resume-engineer/scripts/build_ats_cv.py --lang en
"""

from __future__ import annotations

import argparse
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_OUT = ROOT / "assets" / "cv-jesus-velasquez.pdf"
DEFAULT_OUT_EN = ROOT / "assets" / "cv-jesus-velasquez-en.pdf"

# Datos publicos sincronizados con content.md, index.html y repositorios verificados.
CV_HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
  body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 8.9pt;
    line-height: 1.26;
    color: #111827;
    margin: 0;
    padding: 0;
  }
  .header {
    text-align: center;
    margin-bottom: 6pt;
  }
  h1 {
    font-size: 16pt;
    font-weight: bold;
    letter-spacing: 0.2pt;
    margin: 0 0 1.5pt 0;
    color: #0b1220;
  }
  .subtitle {
    font-size: 9.3pt;
    font-weight: bold;
    color: #1d4ed8;
    margin: 0 0 2.5pt 0;
  }
  .contact {
    font-size: 8.1pt;
    color: #374151;
    margin: 0;
    line-height: 1.32;
  }
  .contact a {
    color: #1d4ed8;
    text-decoration: none;
  }
  h2 {
    font-size: 9.6pt;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.5pt;
    color: #0b1220;
    border-bottom: 1pt solid #1f2937;
    padding-bottom: 1pt;
    margin: 6.5pt 0 3.5pt 0;
  }
  p {
    margin: 0 0 2.5pt 0;
  }
  .item {
    margin-bottom: 4.5pt;
  }
  .row-head {
    margin: 0 0 1pt 0;
  }
  .title {
    font-weight: bold;
    color: #0b1220;
  }
  .meta {
    color: #4b5563;
    font-size: 8.5pt;
  }
  .tech {
    font-size: 8.3pt;
    color: #374151;
    font-style: italic;
    margin: 0 0 1.5pt 0;
  }
  ul {
    margin: 1pt 0 2.5pt 13pt;
    padding: 0;
  }
  li {
    margin-bottom: 1.3pt;
  }
  .skills-list {
    list-style: none;
    margin: 0;
    padding: 0;
  }
  .skills-list li {
    margin-bottom: 1.6pt;
  }
  .cert-list {
    margin: 1pt 0 0 13pt;
    padding: 0;
  }
  .cert-list li {
    margin-bottom: 1.3pt;
  }
  a {
    color: #1d4ed8;
    text-decoration: none;
  }
</style>
</head>
<body>
  <div class="header">
    <h1>JESÚS DAVID VELÁSQUEZ MERCADO</h1>
    <p class="subtitle">Estudiante de Ingeniería de Sistemas | Desarrollo Backend, Python, IA &amp; SQL</p>
    <p class="contact">
      Medellín, Antioquia, Colombia · Disponible para prácticas (remoto, híbrido o presencial)<br>
      <a href="mailto:jvelasquez.dev@gmail.com">jvelasquez.dev@gmail.com</a> ·
      <a href="https://www.linkedin.com/in/jesus-david-velasquez-mercado-dev">linkedin.com/in/jesus-david-velasquez-mercado-dev</a><br>
      <a href="https://github.com/Jesus-engineer">github.com/Jesus-engineer</a> ·
      <a href="https://jesus-engineer.github.io/My-Resume-Web/">jesus-engineer.github.io/My-Resume-Web</a>
    </p>
  </div>

  <h2>Perfil profesional</h2>
  <p>
    Estudiante de Ingeniería de Sistemas (UTB) enfocado en desarrollo backend con Python, APIs REST, SQL e Inteligencia Artificial. Experiencia construyendo motores de inferencia con Small Language Models (SLM) cuantizados en CPU sobre Moodle Docker, aplicaciones integradas con FastAPI/JWT e interfaces en React y Flutter. Busco prácticas o rol junior en desarrollo backend o full stack.
  </p>

  <h2>Educación</h2>
  <div class="item">
    <p class="row-head"><span class="title">Universidad Tecnológica de Bolívar</span> — <span class="meta">Ingeniería de Sistemas y Computación | 2023 – 2027 (prev.)</span></p>
    <p class="meta">Programación, estructuras de datos, bases de datos, ingeniería de software y arquitectura de computadores. Miembro IEEE, IEEE Computer Society e IEEE Computational Intelligence Society.</p>
  </div>

  <h2>Proyectos</h2>
  <div class="item">
    <p class="row-head"><span class="title">Savio AI Recommender — Inferencia psicométrica y recomendación para LMS</span> — <span class="meta">En curso (Entregas 1–2 completadas; Entrega 3 en curso) | UTB</span></p>
    <p class="tech">Stack: Python, SLMs cuantizados (GGUF), Ollama, Qwen 2.5 (1.5B/3B), Gemma 2 (2B), Hugging Face, Docker, Moodle, JSON Schemas</p>
    <ul>
      <li>Desarrollé el motor backend de inferencia en Python con <em>system prompts</em>, <em>guardrails</em>, schemas JSON y benchmarks de memoria sobre CPU sin GPU (<strong>~1,2–2,3 GB de RAM</strong> en modelos GGUF).</li>
      <li>Integré bloques psicopedagógicos en <strong>Moodle Docker</strong> y estructuré la estrategia <strong>LLM Maestro → SLM Especializado</strong> sobre puntajes brutos de <strong>3 instrumentos validados</strong> (CHASIDE, Felder-Silverman ILS y Personalidad) bajo objetivos SMART (<strong>12 sprints completados</strong>).</li>
    </ul>
  </div>

  <div class="item">
    <p class="row-head">
      <span class="title">Intelligent IT Incident Prioritization System (SIPIIT)</span> —
      <span class="meta">feb 2026 – may 2026 | <a href="https://github.com/Oyhs-co/Intelligent-IT-incident-prioritization-system">Repositorio GitHub</a></span>
    </p>
    <p class="tech">Stack: Flutter, Dart, Riverpod, go_router, Material Design 3, API REST (FastAPI/JWT), Git</p>
    <ul>
      <li>Diseñé y desarrollé la app multiplataforma en Flutter en <strong>5 módulos (<code>features/</code>)</strong> para <strong>4 roles</strong> (cliente, analista, técnico y admin), integrada con API REST FastAPI y JWT bajo Clean Code.</li>
      <li>Implementé ruteo por rol con <code>go_router</code>, estado con Riverpod y pruebas unitarias/widgets en Git/GitHub.</li>
    </ul>
  </div>

  <div class="item">
    <p class="row-head"><span class="title">GyR Barber — Plataforma de reservas y gestión de agenda</span> — <span class="meta">En progreso (Fase 1 implementada; Fase 2 FastAPI)</span></p>
    <p class="tech">Stack: React 18, TypeScript, Vite, Tailwind CSS, TanStack Query, Zod, MSW 2 · Fase 2: FastAPI, PostgreSQL 16</p>
    <ul>
      <li>Construí la SPA con <strong>12 historias de usuario (HU-01 a HU-12)</strong> sobre contrato <code>/api/v1</code> simulado con MSW 2 para reservas en &lt; 3 minutos y panel administrativo.</li>
      <li>Definí la transición a backend con <strong>FastAPI, PostgreSQL 16, Pydantic, Docker Compose</strong> y webhooks (Wompi / Nequi / PSE).</li>
    </ul>
  </div>

  <h2>Experiencia y liderazgo</h2>
  <div class="item">
    <p class="row-head"><span class="title">Mentor Estudiantil — Programa TEPAYA</span> — <span class="meta">Universidad Tecnológica de Bolívar | ene 2026 – actualidad · Presencial</span></p>
    <ul>
      <li>Acompaño a <strong>~25 estudiantes asignados de primer semestre</strong> (más apoyo continuo adicional) en su transición universitaria, procesos académicos y administrativos.</li>
      <li>Oriento a estudiantes de nuevo ingreso en el uso de recursos institucionales y herramientas académicas.</li>
    </ul>
  </div>

  <h2>Habilidades técnicas</h2>
  <ul class="skills-list">
    <li><strong>Lenguajes:</strong> Python, SQL, JavaScript, TypeScript, Dart</li>
    <li><strong>Backend, Datos e IA:</strong> APIs REST, PostgreSQL, Supabase, FastAPI (integración y diseño de contratos), SLMs cuantizados (GGUF, Ollama), Hugging Face, JSON Schemas, Análisis y Ciencia de datos</li>
    <li><strong>Frontend:</strong> React 18, Flutter, Tailwind CSS, TanStack Query, Zod, HTML5, CSS3</li>
    <li><strong>Herramientas e Infraestructura:</strong> Git, GitHub, Docker, pruebas automatizadas (unitarias/widgets), Linux (terminal), Windows, macOS</li>
    <li><strong>Idiomas:</strong> Español (nativo), Inglés (B1)</li>
  </ul>

  <h2>Certificaciones</h2>
  <ul class="cert-list">
    <li><strong>GCI World April 2026: Fundamental Theories and Implementations of Data Science</strong> — Matsuo-Iwasawa Lab, Univ. de Tokio (ago 2026)</li>
    <li><strong>Curso de Supabase. Backend as a Service (BaaS) desde cero</strong> — Udemy (jun 2026 · 6 horas)</li>
    <li><strong>AI Literacy</strong> — IBM SkillsBuild (mar 2026)</li>
    <li><strong>Análisis de Datos Nivel Intermedio</strong> (dic 2025 · 159 h) y <strong>Programación Nivel Intermedio</strong> (jun 2025 · 159 h) — Bootcamp MinTIC y UTB</li>
  </ul>
</body>
</html>
"""


CV_BODY_EN = """
  <div class="header">
    <h1>JESÚS DAVID VELÁSQUEZ MERCADO</h1>
    <p class="subtitle">Systems Engineering Student | Backend Development, Python, AI &amp; SQL</p>
    <p class="contact">
      Medellín, Antioquia, Colombia - Open to internships (remote, hybrid, or on-site)<br>
      <a href="mailto:jvelasquez.dev@gmail.com">jvelasquez.dev@gmail.com</a> -
      <a href="https://www.linkedin.com/in/jesus-david-velasquez-mercado-dev">linkedin.com/in/jesus-david-velasquez-mercado-dev</a><br>
      <a href="https://github.com/Jesus-engineer">github.com/Jesus-engineer</a> -
      <a href="https://jesus-engineer.github.io/My-Resume-Web/en/">jesus-engineer.github.io/My-Resume-Web/en/</a>
    </p>
  </div>

  <h2>Professional Summary</h2>
  <p>
    Systems Engineering student at UTB focused on backend development with Python, REST APIs, SQL, and artificial intelligence. Experience building CPU-based inference engines with quantized Small Language Models (SLMs) on Docker-based Moodle, applications integrated with FastAPI/JWT, and interfaces with React and Flutter. Seeking a backend or full-stack development internship or junior role.
  </p>

  <h2>Education</h2>
  <div class="item">
    <p class="row-head"><span class="title">Universidad Tecnológica de Bolívar</span> - <span class="meta">Systems and Computer Engineering | 2023 - 2027 (expected)</span></p>
    <p class="meta">Programming, data structures, databases, software engineering, and computer architecture. Member of IEEE, IEEE Computer Society, and IEEE Computational Intelligence Society.</p>
  </div>

  <h2>Projects</h2>
  <div class="item">
    <p class="row-head"><span class="title">Savio AI Recommender - Psychometric Inference and LMS Recommendations</span> - <span class="meta">Ongoing (Deliverables 1-2 completed; Deliverable 3 in progress) | UTB</span></p>
    <p class="tech">Stack: Python, quantized SLMs (GGUF), Ollama, Qwen 2.5 (1.5B/3B), Gemma 2 (2B), Hugging Face, Docker, Moodle, JSON Schemas</p>
    <ul>
      <li>Developed the Python inference backend with system prompts, guardrails, JSON schemas, and CPU-only memory benchmarks without a GPU (<strong>~1.2-2.3 GB RAM</strong> for GGUF models).</li>
      <li>Integrated psychopedagogical blocks into <strong>Docker-based Moodle</strong> and structured the <strong>Master LLM to Specialized SLM</strong> strategy using raw scores from <strong>3 validated instruments</strong> (CHASIDE, Felder-Silverman ILS, and Personality), guided by SMART objectives (<strong>12 sprints completed</strong>).</li>
    </ul>
  </div>

  <div class="item">
    <p class="row-head"><span class="title">Intelligent IT Incident Prioritization System (SIPIIT)</span> - <span class="meta">Feb 2026 - May 2026 | <a href="https://github.com/Oyhs-co/Intelligent-IT-incident-prioritization-system">GitHub repository</a></span></p>
    <p class="tech">Stack: Flutter, Dart, Riverpod, go_router, Material Design 3, REST API (FastAPI/JWT), Git</p>
    <ul>
      <li>Designed and developed the cross-platform Flutter app in <strong>5 modules (<code>features/</code>)</strong> for <strong>4 roles</strong> (client, analyst, technician, and admin), integrated with a FastAPI REST API and JWT, following Clean Code practices.</li>
      <li>Implemented role-based routing with <code>go_router</code>, state management with Riverpod, and unit/widget tests using Git/GitHub.</li>
    </ul>
  </div>

  <div class="item">
    <p class="row-head"><span class="title">GyR Barber - Booking and Schedule Management Platform</span> - <span class="meta">In progress (Phase 1 implemented; Phase 2 with FastAPI)</span></p>
    <p class="tech">Stack: React 18, TypeScript, Vite, Tailwind CSS, TanStack Query, Zod, MSW 2 - Phase 2: FastAPI, PostgreSQL 16</p>
    <ul>
      <li>Built the SPA around <strong>12 user stories (HU-01 to HU-12)</strong> and an <code>/api/v1</code> contract mocked with MSW 2 for bookings in under 3 minutes and an administrative dashboard.</li>
      <li>Defined the backend transition using <strong>FastAPI, PostgreSQL 16, Pydantic, Docker Compose</strong>, and webhooks (Wompi / Nequi / PSE).</li>
    </ul>
  </div>

  <h2>Experience and Leadership</h2>
  <div class="item">
    <p class="row-head"><span class="title">Student Mentor - TEPAYA Program</span> - <span class="meta">Universidad Tecnológica de Bolívar | Jan 2026 - Present - On-site</span></p>
    <ul>
      <li>Support <strong>~25 assigned first-semester students</strong>, plus additional ongoing support, with their transition to university and academic and administrative processes.</li>
      <li>Guide incoming students in using institutional resources and academic tools.</li>
    </ul>
  </div>

  <h2>Technical Skills</h2>
  <ul class="skills-list">
    <li><strong>Programming languages:</strong> Python, SQL, JavaScript, TypeScript, Dart</li>
    <li><strong>Backend, Data, and AI:</strong> REST APIs, PostgreSQL, Supabase, FastAPI (integration and API contract design), quantized SLMs (GGUF, Ollama), Hugging Face, JSON Schemas, data analysis and data science</li>
    <li><strong>Frontend:</strong> React 18, Flutter, Tailwind CSS, TanStack Query, Zod, HTML5, CSS3</li>
    <li><strong>Tools and infrastructure:</strong> Git, GitHub, Docker, automated testing (unit/widget), Linux (terminal), Windows, macOS</li>
    <li><strong>Spoken languages:</strong> Spanish (native), English (B1)</li>
  </ul>

  <h2>Certifications</h2>
  <ul class="cert-list">
    <li><strong>GCI World April 2026: Fundamental Theories and Implementations of Data Science</strong> - Matsuo-Iwasawa Lab, The University of Tokyo (Aug 2026)</li>
    <li><strong>Supabase: Backend as a Service (BaaS) from Scratch</strong> - Udemy (Jun 2026 - 6 hours)</li>
    <li><strong>AI Literacy</strong> - IBM SkillsBuild (Mar 2026)</li>
    <li><strong>Intermediate Data Analysis</strong> (Dec 2025 - 159 h) and <strong>Intermediate Programming</strong> (Jun 2025 - 159 h) - MinTIC and UTB Bootcamp</li>
  </ul>
"""


def cv_html(language: str) -> str:
    if language == "es":
        return CV_HTML
    css = CV_HTML.split("<style>", 1)[1].split("</style>", 1)[0]
    return ('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><style>'
            + css + '\nbody { font-size: 9.3pt; } h2 { margin-top: 5.5pt; }'
            + ' .item { margin-bottom: 3.5pt; } li { margin-bottom: 1pt; }'
            + '\n</style></head><body>' + CV_BODY_EN + '</body></html>')


def build_pdf(output_path: Path, language: str = "es") -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    story = pymupdf.Story(html=cv_html(language))
    mediabox = pymupdf.paper_rect("letter")
    margin = 31  # ~0.43 in
    where = mediabox + (margin, margin, -margin, -margin)

    # Preserve the HTML's real mailto/HTTPS links as PDF annotations.
    document = story.write_with_links(lambda _number, _filled: (mediabox, where, None))
    if len(document) != 1:
        raise ValueError(f"El contenido requiere {len(document)} paginas; se esperaba una.")
    document.set_language(language)
    document.set_metadata({
        "title": "Jesús David Velásquez Mercado - " + ("Resume" if language == "en" else "CV"),
        "author": "Jesús David Velásquez Mercado",
        "subject": "Software Engineering Resume" if language == "en" else "Hoja de vida de Ingenieria de Sistemas",
    })
    document.save(str(output_path), garbage=4, deflate=True)
    document.close()
    print(f"PDF generado: {output_path} (1 pagina, {language})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Genera el CV ATS en PDF de 1 pagina.")
    parser.add_argument("--lang", choices=["es", "en"], default="es", help="Idioma del CV (es por defecto).")
    parser.add_argument("--out", type=Path, help="Ruta de salida; por defecto se elige segun el idioma.")
    args = parser.parse_args()
    output = args.out or (DEFAULT_OUT_EN if args.lang == "en" else DEFAULT_OUT)
    build_pdf(output, args.lang)


if __name__ == "__main__":
    main()
