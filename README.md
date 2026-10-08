# Mid-Mod Memory Handbook 🧠🎨
### 基于认知科学的 Mid-Mod 复古几何风 · A4 纵向记忆手册生成器

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Antigravity Skill](https://img.shields.io/badge/Google%20Antigravity-Compatible%20Skill-blue.svg)](#)
[![Format](https://img.shields.io/badge/Format-A4%20Portrait%20%7C%20HTML%20%26%20PDF-success.svg)](#)

**Mid-Mod Memory Handbook** 是一套专为深度记忆、行为面试（STAR 复盘）、原声演讲与复杂概念学习打造的智能 Agent Skill 与生成引擎。

它将认知科学公认最高效的三大记忆方法——**主动回忆（Active Recall）**、**认知组块（Cognitive Chunking）** 与 **艾宾浩斯间隔复习（Spaced Repetition）**，与 20 世纪经典的 **Mid-Century Modern（中世纪现代复古几何 / 包豪斯）** 排版美学深度结合，将任何复杂的输入笔记一键转化为兼具高视觉冲击力、高可读性与实体书写空间的 **标准 A4 纵向记忆手册（可编辑 HTML + 矢量 PDF）**。

---

## ✨ 核心特色 (Key Features)

### 1. 🧠 认知科学三维闭环 (Cognitive Architecture)
* **第一性原理与一句话本质（Core Hook）**：直击本质，提炼朗朗上口的因果隐喻。
* **渐进式 3～5 组块拆解（Cognitive Chunking）**：按「基础起点 → 核心机制 → 治理边界」递进拆解，符合人类大脑 3~5 个工作记忆单元的最佳负荷。
* **高反差主动回忆线索（Active Recall Prompts）**：黑色醒目横幅提问，迫使大脑主动提取信息而非被动阅读。
* **双重编码与记忆钩子（Dual Coding & Mnemonics）**：提炼精简口诀 + 通俗生活类比，激活左右脑双重编码。
* **5mm 点阵手写留白区（Handwriting & Verbal Blank）**：预留实体书写与自测草图空间，鼓励打印后用笔默写、画拓扑图或进行口头复述。
* **合书盲测清单与对比矩阵（Mastery Audit）**：终页提供多维度横向对比表格与 4 条脱口而出盲测挑战。

### 2. ⚡ 严格遵循原输入语言 (Original Language Fidelity)
* **严禁擅自翻译**：若输入为英文，主体记忆内容、原句搭配、线索提问及自测默写**100% 忠实保留原英文**，确保用户能准确记住所输入的原始语言表达（非常适合英文面试、托福/雅思口语、学术答辩与专业概念）。
* **中英双语协同**：英文为主体记忆内容，中文作为元数据标签与避坑建议的辅助语言。

### 3. 🎨 经典 Mid-Mod 几何排版与圆润字体
* **几何撞色系统**：芥末金黄 (`#D8AA28`)、复古橄榄绿 (`#989D34`)、天青柔蓝 (`#86CBE6`)、珊瑚粉 (`#F5A8B8`)、深砖红 (`#A43926`) 与暖米白底 (`#FAF7F0`)。
* **全新圆润几何字体**：引入 Google Fonts 顶级几何字体 **`Outfit`** 与 **`Plus Jakarta Sans`**，圆润优雅、字形舒展，具备极高可读性与设计感，彻底告别生硬拉伸与文字遮挡。
* **Mid-Mod 视觉母题**：半圆弧形切角、大撞角三角形、超大实心数字 `1` `2` `3` 与三色总览导览条。

### 4. 🖨️ 跨设备自适应与 1 步导出 A4 PDF
* **零依赖轻量 HTML**：纯语义化 HTML5 + CSS，手机、平板、电脑均可直接打开流畅阅读。
* **原生所见即所得编辑**：页面内所有文字均支持 `contenteditable`，点击任意文字即可自由微调修改。
* **精准 A4 矢量打印**：内嵌专属 `@media print` 打印样式，点击顶部悬浮工具栏中的 **「🖨️ 打印 / 导出 PDF (A4)」**（或按 `Cmd + P`），即可一键另存为无缝分页的超清矢量 A4 PDF，或直接连接打印机进行实体纸张双面打印！

---

## 📂 项目结构 (Project Structure)

```text
midmod-memory-handbook/
├── SKILL.md                     # Antigravity Skill 核心规范与提示词引擎
├── templates/
│   └── handbook-template.html   # 标准纯净 Mid-Mod A4 HTML 模板
├── scripts/
│   ├── render_handbook.py       # 自动化 JSON -> HTML 渲染生成器
│   └── export_pdf.py            # PDF 导出辅助脚本
├── examples/
│   ├── eti-residency-handbook.html  # 实战范例 1：英文艺术家驻留统筹面试手册
│   ├── eti-residency-data.json      # 范例 1 数据源
│   ├── tcp-handbook.html            # 实战范例 2：计算机网络 TCP 状态机手册
│   └── sample-data.json             # 范例 2 数据源
├── LICENSE                      # MIT 开源许可证
└── README.md                    # 本文档
```

---

## 🚀 快速开始 (Quick Start)

### 方式 1：安装为 Google Antigravity 全局 Skill
将本仓库克隆或复制至您的 Antigravity 全局配置目录：

```bash
mkdir -p ~/.gemini/config/skills/
git clone https://github.com/Jialanyq/midmod-memory-handbook.git ~/.gemini/config/skills/midmod-memory-handbook
```

安装完成后，在任意 Antigravity 对话中直接输入：
> *“/midmod-memory-handbook [输入您想背诵或记忆的内容]”*  
> *“用 Mid-Mod 记忆手册帮我把这段英文面试经历整理成可打印 A4 卡片”*

Agent 将自动基于认知组块化算法为您输出完整手册！

---

### 方式 2：使用命令行独立运行 (CLI)
只需准备一个包含知识组块的 `data.json`，即可一键渲染 HTML：

```bash
python3 scripts/render_handbook.py examples/eti-residency-data.json output.html
```

在浏览器中打开：
```bash
open output.html
```

---

## 📖 数据契约示例 (`data.json`)

```json
{
  "title": "ETI ART RESIDENCY 2025",
  "subtitle": "Louhang Art Hill Project · Artist Residency Coordination",
  "topic_badge": "STAR CASE STUDY · 行为面试与项目管理",
  "archive_id": "RESIDENCY-ETI-2025",
  "core_hook": "“Connect the artist's ideas and needs with local resources and people; anchor multi-stakeholder chaos with shared spreadsheet clarity.”",
  "chunks": [
    {
      "part_tag": "Part one · Foundation & Local Connection",
      "name": "Pre-arrival Prep & Local Material Immersion",
      "cue_label": "ACTIVE RECALL CUE / 主动回忆",
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
  "pitfall": "面试高频避坑：切忌泛泛报流水账，重点突出在跨文化不确定性中建立信任与系统化交付的能力。"
}
```

---

## 📄 开源许可证 (License)

本项目采用 [MIT License](LICENSE) 开源协议。欢迎自由分发、修改与商用。
