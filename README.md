# Mid-Mod Memory Handbook 🧠🎨
### Cognitive-Science-Driven Mid-Century Modern A4 Memory Handbook Generator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Antigravity Skill](https://img.shields.io/badge/Google%20Antigravity-Compatible%20Skill-blue.svg)](#)
[![Format](https://img.shields.io/badge/Format-A4%20Portrait%20%7C%20HTML%20%26%20PDF-success.svg)](#)
[![Typography](https://img.shields.io/badge/Typography-Outfit%20%2B%20Plus%20Jakarta%20Sans-purple.svg)](#)

**Mid-Mod Memory Handbook** is an autonomous AI skill and generation engine engineered for deep study, behavioral interview mastery (STAR method), speech delivery, and conceptual internalization.

It bridges the three most empirically validated cognitive learning techniques—**Active Recall**, **Cognitive Chunking**, and **Spaced Repetition (Ebbinghaus)**—with the timeless graphic aesthetic of **Mid-Century Modern (Bauhaus / Swiss Modernism)** design. 

With one prompt or CLI command, it transforms raw study notes, personal case studies, or complex technical concepts into stunning, editable, and print-ready **A4 portrait memory handbooks (HTML & Vector PDF)**.

---

## ✨ Key Features

### 1. 🧠 Cognitive Architecture for Verbal Retrieval
* **First-Principles Core Hook**: Distills the underlying causal mechanism into a memorable, punchy thesis sentence.
* **Progressive 3–5 Chunk Hierarchy**: Deconstructs complex material into 3 to 5 digestible units (*Foundation → Core Dynamics → Governance & Boundaries*), respecting working memory constraints.
* **High-Contrast Active Recall Banners**: Sharp, bold cue banners force the brain into active cognitive retrieval rather than passive re-reading.
* **Dual Coding & Tangible Analogies**: Pairs concise verbal formulas with vivid real-world analogies to stimulate dual-channel memory encoding.
* **5mm Dot-Grid Handwriting Blank**: Dedicated canvas on every chunk page for pen/pencil handwriting, diagram sketching, or oral rehearsal notes after printing.
* **Mastery Audit & Blind Retrieval**: Final page features a cross-dimensional comparison matrix and a 4-point closed-book checklist.

### 2. ⚡ Strict Original Language Fidelity
* **Zero Unwanted Translation**: Preserves the user's input language with 100% fidelity. If notes are in English, the core points, key collocations, and active recall cues stay in **authentic original English**.
* **Engineered for Verbatim Fluency**: Ensures learners memorize exact idiomatic phrasing, action verbs, and terminology needed for job interviews, English presentations, and academic defenses.

### 3. 🎨 Authentic Mid-Mod Aesthetic & Rounded Typography
* **Retro Bauhaus Palette**: Mustard Gold (`#D8AA28`), Vintage Olive (`#989D34`), Sky Blue (`#86CBE6`), Coral Rose (`#F5A8B8`), Terracotta (`#A43926`), and Warm Cream Paper (`#FAF7F0`).
* **Rounded, High-Legibility Typography**: Powered by Google Fonts **`Outfit`** and **`Plus Jakarta Sans`**—circular geometric curves, natural letter casing, open counters, and zero clipping or artificial stretching.
* **Geometric Visual Motifs**: Precision semicircle cutouts, corner triangles, bold oversized numerals (`1`, `2`, `3`), and 3-band panorama overviews.

### 4. 🖨️ Multi-Device Responsive & 1-Click Vector A4 Print
* **Zero-Dependency Clean HTML5**: Lightweight, lightning-fast, and natively responsive across smartphones, tablets, and desktop displays.
* **WYSIWYG In-Browser Editing**: Every heading and paragraph supports native `contenteditable`—click any text in your browser to tweak your notes instantly.
* **Precision Vector PDF Printing**: Calibrated with exact `@page { size: A4 portrait; margin: 0; }` styles. Simply hit **"🖨️ Print / Export PDF"** (or `Cmd + P` / `Ctrl + P`) in any browser to get a seamless, beautifully paginated A4 PDF.

---

## 📂 Project Structure

```text
midmod-memory-handbook/
├── SKILL.md                     # Antigravity Skill definition & prompt engine
├── templates/
│   └── handbook-template.html   # Standalone Mid-Mod A4 HTML template
├── scripts/
│   ├── render_handbook.py       # Python compiler: JSON/Markdown -> A4 HTML
│   └── export_pdf.py            # Headless browser PDF export utility
├── examples/
│   ├── eti-residency-handbook.html  # Case study 1: Artist Residency Coordination (English)
│   ├── eti-residency-data.json      # Dataset 1
│   ├── tcp-handbook.html            # Case study 2: Computer Networking TCP State Machine
│   └── sample-data.json             # Dataset 2
├── LICENSE                      # MIT Open Source License
└── README.md                    # English project documentation
```

---

## 🚀 Quick Start

### Option 1: Install as a Google Antigravity Global Skill
Clone or link this repository into your Antigravity global configuration directory:

```bash
mkdir -p ~/.gemini/config/skills/
git clone https://github.com/Jialanyq/midmod-memory-handbook.git ~/.gemini/config/skills/midmod-memory-handbook
```

Once installed, simply invoke the skill in any Antigravity conversation:
> *"/midmod-memory-handbook Help me organize this interview story into a printable A4 memory handbook:"*  
> *"[Paste your notes or text here]"*

The agent will automatically apply cognitive chunking, preserve your original language, and generate the complete interactive handbook.

---

### Option 2: Standalone CLI Generator
Prepare a structured `data.json` and compile it via Python:

```bash
python3 scripts/render_handbook.py examples/eti-residency-data.json output.html
```

Open the resulting HTML handbook in your default browser:

```bash
open output.html
```

---

## 📖 Data Contract Example (`data.json`)

```json
{
  "title": "ETI ART RESIDENCY 2025",
  "subtitle": "Louhang Art Hill Project · Artist Residency Coordination",
  "topic_badge": "STAR CASE STUDY · BEHAVIORAL INTERVIEW",
  "archive_id": "RESIDENCY-ETI-2025",
  "core_hook": "“Connect the artist's ideas and needs with local resources and people; anchor multi-stakeholder chaos with shared spreadsheet clarity.”",
  "chunks": [
    {
      "part_tag": "Part one · Foundation & Local Connection",
      "name": "Pre-arrival Prep & Local Material Immersion",
      "cue_label": "ACTIVE RECALL CUE",
      "overview_summary": "Pre-arrival logistics, neighborhood visits, and discovering key material at a local veneer factory.",
      "recall_prompt": "What specific preparations did you make before Eti arrived, and how did you connect her artistic vision with local community materials?",
      "points": [
        ["Pre-arrival Logistics: ", "Communicated needs in advance, prepared materials and tools, booked accommodation, arranged airport transport."],
        ["Neighborhood Visits & Veneer Factory: ", "Accompanied visits around the neighborhood, found the main material at a local veneer factory."]
      ],
      "formula": "“Prep Needs & Tools, Scout Veneer, Invite Residents”",
      "analogy": "Like grafting a plant: prepare fertile soil (logistics) and let roots latch onto native earth (veneer factory).",
      "keywords": ["#LouhangArtHill", "#LocalVeneerFactory", "#BridgeArtistNeeds"],
      "practice_prompt": "Verbal Recall Challenge: Without looking above, write down the 4 pre-arrival logistical steps in original English:"
    }
  ],
  "matrix": [
    {
      "dimension": "Part 1: Pre-arrival & Local",
      "purpose": "Bridge artist vision with local community",
      "mechanism": "Pre-arrival logistics + veneer factory visit",
      "anchor": "Prep Ahead & Local Roots"
    }
  ],
  "blind_checklist": [
    {
      "cue": "1. Key Facts Retrieval: ",
      "question": "Can you immediately recite in English: Year (2025), Project (Louhang Art Hill), Artist (Eti), Material (Veneer)?"
    }
  ],
  "pitfall": "Interview Tip: Highlight agency and system resilience over routine logistics: 'My role was really to connect the artist's ideas with local resources, and I used a shared spreadsheet system to keep a complicated project organized.'"
}
```

---

## 🖨️ How to Export to PDF

1. Open any generated `.html` file in **Google Chrome**, **Safari**, or **Microsoft Edge**.
2. Click the floating **"🖨️ Print / Export PDF (A4)"** button in the top toolbar (or press `Cmd + P` / `Ctrl + P`).
3. Set **Destination** to **"Save as PDF"**.
4. Set **Paper Size** to **A4**, **Margins** to **None** or **Default**, and ensure **"Background graphics"** is enabled.
5. Click **Save** to generate a pixel-perfect, vector-sharp A4 PDF document!

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Free for personal, academic, and commercial use.
