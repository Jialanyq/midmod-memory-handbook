#!/usr/bin/env python3
"""
Mid-Mod Memory Handbook & Obsidian Markdown Generator
Outputs:
1. Mid-Mod Retro Geometric A4 HTML (Editable in browser, print-calibrated, with 1-click Markdown download button)
2. Standalone 15-Block Obsidian Markdown (.md) note for long-term retention & vault import.
"""
import sys
import os
import json
import html
import re

COLOR_CLASSES = [
    ("geom-blue", "row-blue", "#86CBE6"),
    ("geom-olive", "row-olive", "#989D34"),
    ("geom-pink", "row-pink", "#F5A8B8"),
    ("geom-mustard", "row-mustard", "#D8AA28"),
    ("geom-terracotta", "row-terracotta", "#A43926"),
]

def escape(val):
    if val is None:
        return ""
    return html.escape(str(val))

def build_obsidian_markdown(data):
    """
    Builds the complete 15-Block Obsidian Markdown note following the Knowledge Memory Designer blueprint.
    """
    title = data.get("title", "MEMORY MAP")
    subtitle = data.get("subtitle", "")
    kicker = data.get("topic_badge", "STAR CASE STUDY")
    archive_id = data.get("archive_id", "ARCHIVE #01")
    core_hook = data.get("core_hook", "Connect vision with local ground; anchor chaos with administrative clarity.")
    chunks = data.get("chunks", [])
    
    # 1. Frontmatter
    tags_list = [f'"{kw.lstrip("#")}"' for chunk in chunks for kw in chunk.get("keywords", [])[:2]]
    tags_str = ", ".join(list(dict.fromkeys(tags_list))[:6])
    
    md = []
    md.append("---")
    md.append(f'title: "{title}"')
    md.append(f'subtitle: "{subtitle}"')
    md.append(f'kicker: "{kicker}"')
    md.append("cover:")
    md.append('  theme: "Mid-Mod Retro Geometric"')
    md.append(f'  archive_id: "{archive_id}"')
    md.append(f"  chunks_count: {len(chunks)}")
    md.append(f"tags: [{tags_str}]")
    md.append("created: 2026-10-09")
    md.append("---\n")
    
    # 2. H1 Title
    md.append(f"# 🧠 {title}")
    md.append(f"> **{core_hook}**\n")
    
    # 3. Usage Guide
    md.append("> [!abstract] 这份笔记怎么用（30 秒读完）")
    md.append("> - **倒计时 3 天**：只看 §1 全景图 + §2 口诀组，确保能闭眼画出骨架、口述口诀；")
    md.append("> - **倒计时 1 天**：刷 §5 速记卡，看定位与锚点链，遮住核对区自己复述，再点开 `> [!quote]-` 核对；")
    md.append("> - **进考场 / 面试前 30 分钟**：只看 §4 数字记忆桩 + §6 难点话术，给大脑注入定海神针。\n")
    
    # 4. §1 One-Page Panorama (Mermaid TD)
    md.append("## 1. 🗺️ 一页全景图")
    md.append("> **记忆原理**：人脑对「空间并列结构」的编码速度远快于线性段落。先建地图，再填细节。\n")
    md.append("```mermaid")
    md.append("flowchart TD")
    md.append(f'    ROOT["{title}<br/>{core_hook[:32]}..."]')
    for i, c in enumerate(chunks):
        c_id = chr(ord('A') + i)
        c_name = c.get("name", f"Chunk {i+1}")
        md.append(f'    ROOT --> {c_id}["{i+1}️⃣ {c_name}"]')
        for j, p in enumerate(c.get("points", [])[:3]):
            p_head = p[0] if isinstance(p, (list, tuple)) else f"Point {j+1}"
            p_clean = re.sub(r'[:：\s]+$', '', p_head)
            md.append(f'    {c_id} --> {c_id}{j+1}["{p_clean}"]')
    md.append("```\n")
    
    # 5. §2 Mnemonics
    md.append("## 2. ⚡ 压缩口诀组")
    for i, c in enumerate(chunks):
        formula = c.get("formula", f"口诀 {i+1}")
        c_name = c.get("name", "")
        md.append(f"### 口诀 {i+1} ｜ {c_name}")
        md.append("| 一字诀 | 核心短语 | 还原解释 | 应用场景 |")
        md.append("|:-:|---|---|---|")
        # Split formula into chars
        chars = [ch for ch in re.sub(r'[\W\d_]+', '', formula)[:5]]
        for ch in chars:
            md.append(f"| **{ch}** | {ch}字要素 | 紧扣该阶段核心动作与交付物 | 回答该阶段第一问 |")
        md.append(f"\n> [!tip] 一句话记住\n> **{formula}**\n")
    
    # 6. §3 Alignment & Elevator Pitch
    md.append("## 3. 🎯 匹配度 / 应用速记")
    md.append("| 目标要求 (Requirement) | 我的底牌 (My Card) | 一句话话术 (Punchline) |")
    md.append("|---|---|---|")
    for c in chunks:
        c_name = c.get("name", "")
        c_summary = c.get("overview_summary", "")
        md.append(f"| 复杂统筹 · {c_name} | {c_summary[:36]}... | *“My role was to bridge artist needs with local soil, anchoring chaos with administrative rigor.”* |")
    md.append("\n> [!note] 5 字优势口诀\n> **「通 · 探 · 联 · 表 · 控」**（沟通前置、探访在地、联合多方、表格定序、掌控全局）\n")
    
    # 7. §4 Case Pool & Number Pegs
    md.append("## 4. 🗃️ 案例池 + 复用矩阵")
    md.append("```mermaid")
    md.append("flowchart LR")
    md.append('    M1["素材：单板木皮厂探访"] --> D1["跨文化在地沟通"]')
    md.append('    M2["素材：7天艺博会与6方协同"] --> D2["高压多线程现场统筹"]')
    md.append('    M3["素材：Done/Next/Owner/DDL表格"] --> D3["复杂项目行政系统化"]')
    md.append("```\n")
    md.append("### 复用矩阵表")
    md.append("| 素材 / 钩子 | 主用途 (Primary) | 兼用途 (Secondary) | 调取关键词 |")
    md.append("|---|---|---|---|")
    for i, c in enumerate(chunks):
        c_name = c.get("name", "")
        kws = ", ".join(c.get("keywords", [])[:3])
        md.append(f"| 模块 {i+1}：{c_name} | 考察独立统筹与执行 | 考察突发问题与在地破冰 | {kws} |")
    md.append("\n### 数字记忆桩表")
    md.append("| 数字 | 记忆句 (Memory Anchor) | 对应事实 |")
    md.append("|:-:|---|---|")
    md.append("| **1** | **1 个月驻留**，为以色列艺术家 Eti 全流程定制人行宿物底座 | 驻留周期与主体 |")
    md.append("| **2** | **双轨招募**（社区走访面对面 + 社交媒体网络），攻克共创参与人数 | 共创工作坊破冰 |")
    md.append("| **3** | **3 大物料排期支柱**（materials, staff, schedules），支撑每场活动 | 7 天活动运营 |")
    md.append("| **4** | **4 维共享表格**（Done, Next, Owner, Deadline），终结多方混乱 | 核心管理系统 |")
    md.append("| **6** | **6 方利益相关者**（艺术家/设计/搭建/志愿者/主办方/文旅局）无缝同频 | 协同网络 |\n")
    
    # 8. §5 5-Part Flashcards
    md.append("## 5. 📇 五段式主动回忆速记卡")
    for i, c in enumerate(chunks):
        c_name = c.get("name", "")
        recall_q = c.get("recall_prompt", "")
        points = c.get("points", [])
        formula = c.get("formula", "")
        keywords = " ➔ ".join([kw.lstrip("#") for kw in c.get("keywords", [])[:5]])
        
        md.append(f"### Card {i+1} ｜ {c_name}")
        md.append(f"**定位**：第 {i+1} 核心单元，口述作答建议控制在 90 秒内。\n")
        md.append(f"**锚点链**\n`[{keywords}]`\n")
        md.append("**骨架**\n```text")
        for p in points:
            if isinstance(p, (list, tuple)) and len(p) >= 2:
                head = re.sub(r'[:：\s]+$', '', p[0])
                md.append(f"[{head}] {p[1][:60]}...")
            else:
                md.append(f"[Point] {str(p)[:60]}...")
        md.append("```\n")
        md.append(f"> [!quote]- 展开核对：完整提炼与原述回答\n> **核心提问**：{recall_q}\n>")
        for p in points:
            if isinstance(p, (list, tuple)) and len(p) >= 2:
                md.append(f"> - **{p[0]}** {p[1]}")
            else:
                md.append(f"> - {p}")
        md.append(">\n")
        md.append(f"**记忆抓手**：> [!tip]\n> {formula}\n")
    
    # 9. §6 Difficulties & Mindset
    md.append("## 6. 🛡️ 难点 · 已备话术")
    md.append("> **应对四步心法**：**认同痛点 ➔ 表明原则 ➔ 给出抓手 ➔ 交付结果**。\n")
    md.append("| 难点场景 / 追问 | 核心风险 | 已备应对原则与话术 |")
    md.append("|---|---|---|")
    md.append("| 追问：如果志愿者临时爽约怎么办？ | 现场活动脱节 | 提前在表格设立 Owner 备份制与浮动候补池，现场快速补位。 |")
    md.append("| 追问：外籍艺术家沟通有文化隔阂怎么办？ | 创作意图扭曲 | 倾听第一，陪同在地走访建立人际信任，用实体材料（单板木皮）建立共同事实。 |")
    md.append("| 追问：多方协作中主办方和文旅诉求冲突怎么办？ | 责任推诿 | 依托共享表格作为单一事实源（Single Source of Truth），把模糊口头诉求转化为明确 Deadline。 |\n")
    
    # 10. §7 Multi-Scenario
    md.append("## 7. 🎭 高频素材的多场景用法")
    md.append("| 提问场景 | 调取本篇哪一段素材 | 怎么说（切入角度） |")
    md.append("|---|---|---|")
    md.append("| “请谈谈你最成功的一次项目协调经历” | 完整串联 Part 1~3 | 从前置后勤到在地探厂，重点落在 6 方协同与表格交付。 |")
    md.append("| “你如何处理工作中的巨大压力与多线程任务” | 聚焦 Part 3 (Spreadsheets) | 重点讲 Done/Next/Owner/Deadline 如何给团队和自己建立心理安全感。 |")
    md.append("| “你如何与不同背景的人建立合作关系” | 聚焦 Part 1 (Community) | 讲陪同走访单板厂、邀请居民与社交媒体双轨招募的破冰经验。 |\n")
    
    # 11. §8 Reverse Questions
    md.append("## 8. 🔍 反向提问 / 延伸思考")
    md.append("| # | 面试反向提问 | 考察用意 / 策略 |")
    md.append("|:-:|---|---|")
    md.append("| 1 | 团队在过往驻留项目中，最看重协调人在‘在地链接’还是‘行政流程’上的能力？ | 摸清团队文化偏好 |")
    md.append("| 2 | 针对跨部门（如设计、施工、文旅）的协作，目前团队采用什么协作工具与沟通节奏？ | 展示自己系统化接入的能力 |\n")
    
    # 12. §9 Checklist
    md.append("## 9. ✅ 复习验收 Checklist")
    md.append("- [ ] 闭眼能徒手画出 §1 的 4 枝全景图树状结构")
    md.append("- [ ] 顺畅背诵 3 组口诀，并能向他人解释每个字的含义")
    md.append("- [ ] 盲测 5 个数字记忆桩（1、2、3、4、6），数字与事实完全焊死")
    md.append("- [ ] 随机抽取 1 张速记卡，不看核对区能在 90 秒内顺畅复述")
    md.append("- [ ] 针对 3 个难点追问，能按照四步心法脱口而出应对策略\n")
    
    # 13. §10 Keywords
    md.append("## 10. 🏷️ 关键词速查表")
    md.append("| 维度 | 核心英文专有名词 / 短语 | 中文对照 |")
    md.append("|---|---|---|")
    md.append("| **人物与地点** | Louhang Art Hill, Israeli artist Eti, Local veneer factory | 楼巷艺术山、以色列艺术家Eti、单板木皮厂 |")
    md.append("| **核心机制** | Pre-arrival logistics, Collaborative workshops, Solo exhibition | 前置后勤、共创工作坊、个人展览 |")
    md.append("| **协同对象** | Visual designer, Installation staff, Community volunteers, Culture & Tourism Dept | 视觉设计、搭建布展、志愿者、文旅局 |")
    md.append("| **管理系统** | Shared spreadsheets, Single source of truth, Done/Next/Owner/Deadline | 共享在线表格、单一真实事实源、四大看板列 |\n")
    
    # 14. §11 Timeline
    md.append("## 11. ⏳ 倒计时记忆排期")
    md.append("```text")
    md.append("[Day 1] 空间建模 ➔ 绘制 §1 全景图 + 熟记 §2 口诀组")
    md.append("   │")
    md.append("[Day 2] 深度编码 ➔ 默写 §4 记忆桩 + 过一遍 §5 速记卡（闭目复述）")
    md.append("   │")
    md.append("[Day 3] 极限自测 ➔ 全真模拟面试，快刷 §6 难点话术 + 验收 §9 Checklist")
    md.append("```\n")
    md.append("| 阶段 | 重点看哪一节 | 自测标准 |")
    md.append("|---|---|---|")
    md.append("| **D-3（建模）** | §1 全景图、§2 口诀组 | 白纸上能手绘树状分支 |")
    md.append("| **D-2（自测）** | §4 记忆桩、§5 五段卡 | 遮住核对区口述 90 秒无卡顿 |")
    md.append("| **D-1（冲刺）** | §6 难点、§7 多场景 | 面对突发追问能本能反应 |\n")
    
    # 15. End Links
    md.append(f"**相关笔记**：[[{title}]] · [[STAR 面试法总览]] · [[复杂项目行政管理体系]]")
    
    return "\n".join(md)

def build_handbook_html(data):
    """
    Builds the Mid-Mod styled HTML with Outfit fonts, A4 paging,
    inline collapsible details for active recall, and a 1-click Markdown download button.
    """
    title = escape(data.get("title", "MEMORY HANDBOOK"))
    subtitle = escape(data.get("subtitle", "基于认知科学的主动回忆与信息组块速记手册"))
    topic_badge = escape(data.get("topic_badge", "THEME DECK / 深度记忆"))
    archive_id = escape(data.get("archive_id", "ARCHIVE #01"))
    core_hook = escape(data.get("core_hook", "理解是记忆的捷径，组块是提取的索引，线索是自测的钥匙。"))
    chunks = data.get("chunks", [])

    # Compile the Markdown representation for 1-click download
    obsidian_markdown = build_obsidian_markdown(data)

    # Overview rows on Cover page
    overview_rows_html = []
    for i, chunk in enumerate(chunks):
        c_class, r_class, hex_col = COLOR_CLASSES[i % len(COLOR_CLASSES)]
        part_tag = escape(chunk.get("part_tag", f"Part {i+1}"))
        c_summary = escape(chunk.get("overview_summary", chunk.get("name", "")))
        
        overview_rows_html.append(f"""
        <div class="overview-row {r_class}">
          <div class="overview-content">
            <div class="overview-tag" contenteditable="true">{part_tag}</div>
            <div class="overview-summary" contenteditable="true">{c_summary}</div>
          </div>
          <div class="overview-num">{i+1}</div>
        </div>
        """)

    # Build dedicated chunk pages (Page 2..N)
    chunk_pages_html = []
    for i, chunk in enumerate(chunks):
        c_num = i + 1
        c_class, r_class, hex_col = COLOR_CLASSES[i % len(COLOR_CLASSES)]
        part_tag = escape(chunk.get("part_tag", f"Part {c_num}"))
        chunk_name = escape(chunk.get("name", f"核心组块 {c_num}"))
        cue_label = escape(chunk.get("cue_label", "ACTIVE RECALL CUE / 主动回忆"))
        recall_prompt = escape(chunk.get("recall_prompt", "核心问题：该知识点的第一性原理是什么？"))
        formula = escape(chunk.get("formula", "极简口诀：一词定性，二点定位"))
        analogy = escape(chunk.get("analogy", "生活化类比：类比直观场景建立深刻认知锚点。"))
        practice_prompt = escape(chunk.get("practice_prompt", "自测挑战：不看上方解析，在下方点阵区独立写出核心逻辑："))
        tip_text = escape(chunk.get("tip", "* 提示：遮挡上方文字，先独立用原语言口述该组块的核心要素与句式 / Cover text and recite verbally in original language."))
        placeholder_text = escape(chunk.get("placeholder", "在此手写默写原语言关键词、绘制逻辑草图、或演练口头复述表达 / Write keywords, process diagrams, or verbal recall cues here..."))
        
        # Points
        points_html = []
        for p in chunk.get("points", []):
            if isinstance(p, (list, tuple)) and len(p) >= 2:
                head, body = escape(p[0]), escape(p[1])
                points_html.append(f'<li contenteditable="true"><strong>{head}</strong>{body}</li>')
            else:
                points_html.append(f'<li contenteditable="true">{escape(p)}</li>')

        # Keywords
        kw_html = []
        for kw in chunk.get("keywords", []):
            kw_clean = str(kw) if str(kw).startswith("#") else f"#{kw}"
            kw_html.append(f'<span class="kw-pill" contenteditable="true">{escape(kw_clean)}</span>')

        # Mid-Mod graphic motif & padding protection against collisions
        if i % 2 == 0:
            motif_html = '<div class="graphic-cutout-arc"></div>'
            hook_padding = 'padding-right: 28mm;'
        else:
            motif_html = '<div class="graphic-cutout-triangle"></div>'
            hook_padding = 'padding-left: 18mm;'

        chunk_pages_html.append(f"""
  <!-- =========================================================
       PAGE {c_num + 1}: CHUNK {c_num} DEEP-DIVE
       ========================================================= -->
  <div class="page" id="page-{c_num + 1}">
    <div class="page-header">
      <div class="meta-tag" contenteditable="true">CHUNK 0{c_num} · {chunk_name}</div>
      <div class="meta-sub" contenteditable="true">ACTIVE RECALL MODULE · SHEET 0{c_num + 1}</div>
    </div>

    <div class="page-body">
      <!-- Chunk Header -->
      <div class="chunk-header-block {c_class}">
        <div class="chunk-header-left">
          <div class="chunk-part-title" contenteditable="true">{part_tag}</div>
          <div class="chunk-name" contenteditable="true">{chunk_name}</div>
        </div>
        <div class="chunk-header-num">{c_num}</div>
      </div>

      <!-- Trigger Prompt Bar -->
      <div class="recall-prompt-bar">
        <span class="cue-tag">{cue_label}</span>
        <div class="cue-question" contenteditable="true">{recall_prompt}</div>
      </div>

      <!-- Theory vs Hook Grid -->
      <div class="chunk-main-grid">
        <div class="chunk-theory-col">
          <div>
            <div class="section-eyebrow">认知要点与原句萃取 / COGNITIVE CHUNKS</div>
            <ul class="theory-points">
              {''.join(points_html)}
            </ul>
          </div>
          <div style="font-size: 9.5pt; color: #7A766D; font-style: italic;" contenteditable="true">
            {tip_text}
          </div>
        </div>

        <div class="chunk-hook-col">
          <div class="hook-graphic-box">
            {motif_html}
            <div class="hook-content" style="{hook_padding}">
              <div class="section-eyebrow">记忆钩子与类比 / MNEMONIC & DUAL CODING</div>
              <div class="hook-formula" contenteditable="true">{formula}</div>
              <div class="hook-analogy" contenteditable="true">{analogy}</div>
            </div>
          </div>
          <div class="hook-keyword-pills">
            {''.join(kw_html)}
          </div>
        </div>
      </div>

      <!-- Handwriting & Practice Canvas -->
      <div class="chunk-practice-zone">
        <div class="practice-header">
          <div class="practice-title">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 013 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
            实体手写自测与原语言口述演练区 (VERBAL & HANDWRITING BLANK)
          </div>
          <div style="font-size: 9pt; color: #8F8B80;">建议用笔默写或口头复述</div>
        </div>
        <div class="practice-prompt-text" contenteditable="true">
          {practice_prompt}
        </div>
        <div class="note-grid-canvas" contenteditable="true">
          <div class="note-grid-placeholder">{placeholder_text}</div>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <div>MEMORIZATION HANDBOOK</div>
      <div>SHEET 0{c_num + 1} / CHUNK 0{c_num}</div>
    </div>
  </div>
        """)

    # Build Final Synthesis Page
    matrix_rows = data.get("matrix", [])
    matrix_rows_html = []
    for row in matrix_rows:
        dim = escape(row.get("dimension", ""))
        purpose = escape(row.get("purpose", ""))
        mech = escape(row.get("mechanism", ""))
        anchor = escape(row.get("anchor", ""))
        matrix_rows_html.append(f"""
        <tr>
          <td style="font-weight: 700;" contenteditable="true">{dim}</td>
          <td contenteditable="true">{purpose}</td>
          <td contenteditable="true">{mech}</td>
          <td contenteditable="true">{anchor}</td>
        </tr>
        """)

    blind_items = data.get("blind_checklist", [])
    blind_items_html = []
    for item in blind_items:
        cue = escape(item.get("cue", ""))
        q = escape(item.get("question", ""))
        blind_items_html.append(f"""
        <div class="checklist-row">
          <div class="check-box"></div>
          <div class="check-content">
            <span class="check-cue" contenteditable="true">{cue}</span>
            <span contenteditable="true">{q}</span>
          </div>
        </div>
        """)

    pitfall = escape(data.get("pitfall", "最常见的遗忘点在于将表面步骤与因果关系混为一谈。务必用手写默写验证因果关系。"))

    total_pages = len(chunks) + 2
    final_page_num = total_pages

    final_page_html = f"""
  <!-- =========================================================
       PAGE {final_page_num}: FINAL SYNTHESIS & BLIND RECALL
       ========================================================= -->
  <div class="page" id="page-{final_page_num}">
    <div class="page-header">
      <div class="meta-tag" contenteditable="true">SYNTHESIS & BLIND RECALL</div>
      <div class="meta-sub" contenteditable="true">FINAL MASTERY AUDIT · SHEET 0{final_page_num}</div>
    </div>

    <div class="page-body">
      <!-- Final Header Banner -->
      <div class="final-hero">
        <div>
          <h2 contenteditable="true">闭环自测与总览速查 (MASTERY AUDIT)</h2>
          <p contenteditable="true">合上手册后，能否用原语言脱口而出？完成以下无提示自测检查清单与对比矩阵。</p>
        </div>
        <div style="font-family: var(--font-display); font-size: 32pt; font-weight: 800; opacity: 0.3;">
          ★ 100%
        </div>
      </div>

      <!-- Matrix Comparison Table -->
      <div class="matrix-section">
        <div class="section-eyebrow">认知组块横向对比矩阵 / CHUNK MATRIX</div>
        <table class="matrix-table">
          <thead>
            <tr>
              <th style="width: 22%;">组块维度 / Phase</th>
              <th style="width: 28%;">核心目的 / Purpose</th>
              <th style="width: 28%;">主导机制 / Mechanism</th>
              <th style="width: 22%;">速记锚点 / Anchor</th>
            </tr>
          </thead>
          <tbody>
            {''.join(matrix_rows_html)}
          </tbody>
        </table>
      </div>

      <!-- Blind Recall Checklist -->
      <div class="blind-recall-section">
        <div class="section-eyebrow">合书自测清单 / BLIND RETRIEVAL CHECKLIST</div>
        <div class="checklist-items">
          {''.join(blind_items_html)}
        </div>

        <div class="pitfall-box">
          <strong>⚠️ 表达与避坑警示 (PITFALL ALERT)：</strong>
          <span contenteditable="true">{pitfall}</span>
        </div>
      </div>
    </div>

    <div class="page-footer">
      <div>MEMORIZATION HANDBOOK</div>
      <div>SHEET 0{final_page_num} / FINAL RETRIEVAL</div>
    </div>
  </div>
    """

    # Assemble complete HTML
    full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} · Mid-Mod A4 认知记忆手册</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Newsreader:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
  <style>
    :root {{
      --mm-mustard: #D8AA28;
      --mm-olive: #989D34;
      --mm-blue: #86CBE6;
      --mm-pink: #F5A8B8;
      --mm-terracotta: #A43926;
      --mm-cream: #FAF7F0;
      --mm-dark: #1A1A1A;
      --mm-white: #FFFFFF;
      --mm-card-border: #202020;
      --mm-subtle-gray: #EAE6DC;
      --mm-text-muted: #5A5852;
      
      --font-display: 'Outfit', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif;
      --font-body: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      --font-serif: 'Newsreader', "Songti SC", Georgia, serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      background-color: #E7E3D8;
      font-family: var(--font-body);
      color: var(--mm-dark);
      padding: 24px 0 60px 0;
      line-height: 1.5;
    }}

    .action-bar {{
      position: sticky;
      top: 12px;
      z-index: 9999;
      width: 210mm;
      max-width: 95vw;
      margin: 0 auto 16px auto;
      background: var(--mm-dark);
      color: var(--mm-cream);
      padding: 10px 18px;
      border-radius: 999px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      box-shadow: 0 10px 25px rgba(0,0,0,0.25);
      border: 1px solid rgba(255,255,255,0.15);
      font-size: 13px;
    }}

    .action-bar .tips {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 500;
    }}

    .action-bar .tips span.badge {{
      background: var(--mm-mustard);
      color: var(--mm-dark);
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.5px;
    }}

    .action-bar .btn-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .btn-download-md {{
      background: var(--mm-mustard);
      color: var(--mm-dark);
      border: none;
      padding: 6px 14px;
      border-radius: 999px;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      transition: transform 0.15s ease, background 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-download-md:hover {{
      background: #E5B824;
      transform: translateY(-1px);
    }}

    .btn-print {{
      background: var(--mm-blue);
      color: var(--mm-dark);
      border: none;
      padding: 6px 14px;
      border-radius: 999px;
      font-weight: 700;
      font-size: 13px;
      cursor: pointer;
      transition: transform 0.15s ease, background 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-print:hover {{
      background: #70BDDA;
      transform: translateY(-1px);
    }}

    .page {{
      width: 210mm;
      height: 297mm;
      min-height: 297mm;
      max-height: 297mm;
      margin: 0 auto 28px auto;
      background: var(--mm-cream);
      border: 2px solid var(--mm-card-border);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 12px 30px rgba(0,0,0,0.12);
      page-break-after: always;
      break-after: page;
      page-break-inside: avoid;
    }}

    .page-header {{
      height: 24mm;
      border-bottom: 2px solid var(--mm-card-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16mm;
      background: var(--mm-cream);
      flex-shrink: 0;
    }}

    .meta-tag {{
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--mm-dark);
    }}

    .meta-sub {{
      font-size: 10px;
      color: var(--mm-text-muted);
      font-weight: 600;
      letter-spacing: 0.5px;
    }}

    .page-footer {{
      height: 14mm;
      border-top: 2px solid var(--mm-card-border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 16mm;
      background: var(--mm-cream);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      flex-shrink: 0;
    }}

    .page-body {{
      flex: 1;
      padding: 0;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    [contenteditable="true"] {{
      outline: none;
      transition: background 0.15s ease;
      cursor: text;
    }}
    [contenteditable="true"]:hover {{
      background: rgba(216, 170, 40, 0.15);
      border-radius: 2px;
    }}
    [contenteditable="true"]:focus {{
      background: rgba(134, 203, 230, 0.25);
      border-radius: 2px;
    }}

    .cover-hero {{
      background: var(--mm-mustard);
      border-bottom: 2px solid var(--mm-card-border);
      padding: 16mm 16mm 12mm 16mm;
      position: relative;
    }}

    .cover-hero .badge-topic {{
      display: inline-block;
      background: var(--mm-dark);
      color: var(--mm-cream);
      padding: 4px 12px;
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      margin-bottom: 6mm;
      border-radius: 2px;
    }}

    .cover-title {{
      font-family: var(--font-display);
      font-size: 28pt;
      font-weight: 800;
      line-height: 1.1;
      letter-spacing: -0.02em;
      color: var(--mm-dark);
      margin-bottom: 5mm;
      word-break: break-word;
    }}

    .cover-subtitle {{
      font-family: var(--font-serif);
      font-size: 13pt;
      color: #2E2B20;
      line-height: 1.4;
      max-width: 90%;
    }}

    .tracker-bar {{
      background: var(--mm-cream);
      border-bottom: 2px solid var(--mm-card-border);
      padding: 5mm 16mm;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .tracker-label {{
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }}

    .tracker-pills {{
      display: flex;
      gap: 8px;
    }}

    .tracker-pill {{
      border: 1.5px solid var(--mm-card-border);
      background: var(--mm-white);
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 10px;
      font-weight: 700;
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .tracker-box {{
      width: 11px;
      height: 11px;
      border: 1.5px solid var(--mm-dark);
      display: inline-block;
      background: #fff;
    }}

    .overview-chunks {{
      flex: 1;
      display: flex;
      flex-direction: column;
      border-bottom: 2px solid var(--mm-card-border);
    }}

    .overview-row {{
      flex: 1;
      display: flex;
      border-bottom: 2px solid var(--mm-card-border);
      position: relative;
    }}
    .overview-row:last-child {{
      border-bottom: none;
    }}

    .overview-row.row-blue {{ background: var(--mm-blue); }}
    .overview-row.row-olive {{ background: var(--mm-olive); color: var(--mm-white); }}
    .overview-row.row-pink {{ background: var(--mm-pink); }}
    .overview-row.row-mustard {{ background: var(--mm-mustard); }}
    .overview-row.row-terracotta {{ background: var(--mm-terracotta); color: var(--mm-white); }}

    .overview-content {{
      flex: 1;
      padding: 6mm 16mm;
      display: flex;
      flex-direction: column;
      justify-content: center;
    }}

    .overview-tag {{
      font-family: var(--font-serif);
      font-size: 16pt;
      font-weight: 600;
      margin-bottom: 2mm;
    }}

    .overview-summary {{
      font-size: 10.5pt;
      font-weight: 500;
      line-height: 1.35;
      opacity: 0.95;
    }}

    .overview-num {{
      width: 32mm;
      border-left: 2px solid var(--mm-card-border);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-size: 50pt;
      font-weight: 800;
      line-height: 1;
      background: rgba(255,255,255,0.15);
    }}

    .cover-bottom-essence {{
      padding: 6mm 16mm;
      background: var(--mm-cream);
      display: flex;
      align-items: center;
      gap: 12mm;
    }}
    .essence-title {{
      font-family: var(--font-display);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      white-space: nowrap;
    }}
    .essence-text {{
      font-family: var(--font-serif);
      font-size: 12pt;
      font-style: italic;
      color: var(--mm-dark);
    }}

    .chunk-header-block {{
      height: 44mm;
      border-bottom: 2px solid var(--mm-card-border);
      display: flex;
    }}

    .chunk-header-left {{
      flex: 1;
      padding: 6mm 16mm;
      display: flex;
      flex-direction: column;
      justify-content: center;
      border-right: 2px solid var(--mm-card-border);
    }}

    .chunk-part-title {{
      font-family: var(--font-serif);
      font-size: 16pt;
      font-weight: 600;
      line-height: 1.1;
      margin-bottom: 1.5mm;
      color: rgba(0,0,0,0.75);
    }}

    .chunk-name {{
      font-family: var(--font-display);
      font-size: 17pt;
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.01em;
      color: var(--mm-dark);
    }}

    .chunk-header-num {{
      width: 44mm;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: var(--font-display);
      font-size: 58pt;
      font-weight: 800;
      line-height: 1;
      color: var(--mm-dark);
      position: relative;
    }}

    .geom-blue {{ background: var(--mm-blue); }}
    .geom-olive {{ background: var(--mm-olive); color: var(--mm-white) !important; }}
    .geom-pink {{ background: var(--mm-pink); }}
    .geom-mustard {{ background: var(--mm-mustard); }}
    .geom-terracotta {{ background: var(--mm-terracotta); color: var(--mm-white) !important; }}

    .recall-prompt-bar {{
      background: var(--mm-dark);
      color: var(--mm-cream);
      padding: 6mm 16mm;
      border-bottom: 2px solid var(--mm-card-border);
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }}

    .recall-prompt-bar .cue-tag {{
      background: var(--mm-mustard);
      color: var(--mm-dark);
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.8px;
      padding: 3px 8px;
      text-transform: uppercase;
      flex-shrink: 0;
      margin-top: 2px;
      border-radius: 2px;
    }}

    .recall-prompt-bar .cue-question {{
      font-size: 12pt;
      font-weight: 600;
      line-height: 1.35;
    }}

    .chunk-main-grid {{
      height: 98mm;
      display: flex;
      border-bottom: 2px solid var(--mm-card-border);
    }}

    .chunk-theory-col {{
      flex: 1.25;
      padding: 8mm 16mm;
      border-right: 2px solid var(--mm-card-border);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: var(--mm-white);
    }}

    .section-eyebrow {{
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1px;
      text-transform: uppercase;
      color: var(--mm-text-muted);
      margin-bottom: 3mm;
    }}

    .theory-points {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 3mm;
    }}

    .theory-points li {{
      font-size: 10pt;
      line-height: 1.38;
      position: relative;
      padding-left: 18px;
    }}

    .theory-points li::before {{
      content: "";
      position: absolute;
      left: 0;
      top: 6px;
      width: 7px;
      height: 7px;
      background: var(--mm-dark);
      border-radius: 1px;
    }}

    .theory-points strong {{
      color: var(--mm-dark);
      font-weight: 700;
      background: rgba(216, 170, 40, 0.2);
      padding: 1px 4px;
      border-radius: 2px;
    }}

    .chunk-hook-col {{
      flex: 0.95;
      background: var(--mm-cream);
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }}

    .hook-graphic-box {{
      flex: 1;
      padding: 6mm 10mm;
      display: flex;
      flex-direction: column;
      justify-content: center;
      position: relative;
      border-bottom: 2px solid var(--mm-card-border);
    }}

    .graphic-cutout-arc {{
      position: absolute;
      right: 0;
      top: 50%;
      transform: translateY(-50%);
      width: 28mm;
      height: 28mm;
      border-radius: 50% 0 0 50%;
      background: var(--mm-olive);
      opacity: 0.85;
      border-left: 2px solid var(--mm-card-border);
      border-top: 2px solid var(--mm-card-border);
      border-bottom: 2px solid var(--mm-card-border);
      pointer-events: none;
    }}

    .graphic-cutout-triangle {{
      position: absolute;
      left: 0;
      bottom: 0;
      width: 0;
      height: 0;
      border-bottom: 32mm solid var(--mm-terracotta);
      border-right: 32mm solid transparent;
      opacity: 0.85;
      pointer-events: none;
    }}

    .hook-content {{
      position: relative;
      z-index: 2;
    }}

    .hook-formula {{
      font-family: var(--font-display);
      font-size: 12.5pt;
      font-weight: 700;
      line-height: 1.35;
      letter-spacing: -0.01em;
      color: var(--mm-dark);
      margin-bottom: 2.5mm;
    }}

    .hook-analogy {{
      font-family: var(--font-serif);
      font-size: 10pt;
      line-height: 1.4;
      color: var(--mm-text-muted);
    }}

    .hook-keyword-pills {{
      padding: 4mm 10mm;
      background: var(--mm-white);
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }}

    .kw-pill {{
      border: 1px solid var(--mm-card-border);
      background: var(--mm-cream);
      padding: 2px 8px;
      font-size: 9pt;
      font-weight: 700;
      border-radius: 3px;
    }}

    .chunk-practice-zone {{
      flex: 1;
      padding: 6mm 16mm;
      background: #FDFBF7;
      display: flex;
      flex-direction: column;
    }}

    .practice-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 2.5mm;
    }}

    .practice-title {{
      font-family: var(--font-display);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: var(--mm-dark);
      display: flex;
      align-items: center;
      gap: 6px;
    }}

    .practice-prompt-text {{
      font-size: 10pt;
      font-weight: 600;
      color: #3A3832;
      margin-bottom: 2.5mm;
    }}

    .note-grid-canvas {{
      flex: 1;
      border: 1.5px dashed #B8B3A4;
      border-radius: 4px;
      background-color: #FFFFFF;
      background-image: radial-gradient(#B8B3A4 1.2px, transparent 1.2px);
      background-size: 6mm 6mm;
      padding: 4mm 6mm;
      position: relative;
      font-family: var(--font-serif);
      font-size: 11pt;
      color: #2F3542;
    }}

    .note-grid-placeholder {{
      color: #9C988D;
      font-size: 9.5pt;
      font-style: italic;
      user-select: none;
    }}

    .final-hero {{
      background: var(--mm-terracotta);
      color: var(--mm-white);
      padding: 10mm 16mm;
      border-bottom: 2px solid var(--mm-card-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .final-hero h2 {{
      font-family: var(--font-display);
      font-size: 21pt;
      font-weight: 800;
      letter-spacing: -0.01em;
      text-transform: uppercase;
    }}

    .final-hero p {{
      font-size: 10.5pt;
      opacity: 0.9;
    }}

    .matrix-section {{
      padding: 7mm 16mm;
      border-bottom: 2px solid var(--mm-card-border);
      background: var(--mm-white);
    }}

    .matrix-table {{
      width: 100%;
      border-collapse: collapse;
      border: 2px solid var(--mm-card-border);
      font-size: 9.5pt;
    }}

    .matrix-table th {{
      background: var(--mm-dark);
      color: var(--mm-cream);
      font-family: var(--font-display);
      font-size: 9pt;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      padding: 6px 10px;
      border: 1px solid var(--mm-card-border);
      text-align: left;
    }}

    .matrix-table td {{
      padding: 7px 10px;
      border: 1px solid var(--mm-card-border);
      vertical-align: top;
      line-height: 1.35;
    }}

    .matrix-table tr:nth-child(even) td {{
      background: #FDFCF7;
    }}

    .blind-recall-section {{
      flex: 1;
      padding: 7mm 16mm;
      background: var(--mm-cream);
      display: flex;
      flex-direction: column;
      border-bottom: 2px solid var(--mm-card-border);
    }}

    .checklist-items {{
      display: flex;
      flex-direction: column;
      gap: 3mm;
      margin-top: 3mm;
    }}

    .checklist-row {{
      display: flex;
      align-items: flex-start;
      gap: 10px;
      background: var(--mm-white);
      border: 1.5px solid var(--mm-card-border);
      padding: 6px 12px;
      border-radius: 4px;
    }}

    .check-box {{
      width: 15px;
      height: 15px;
      border: 2px solid var(--mm-dark);
      border-radius: 2px;
      flex-shrink: 0;
      margin-top: 2px;
    }}

    .check-content {{
      font-size: 10pt;
      line-height: 1.35;
    }}

    .check-cue {{
      font-weight: 700;
      color: var(--mm-dark);
    }}

    .pitfall-box {{
      margin-top: 4mm;
      background: #FFE8E5;
      border: 1.5px solid var(--mm-terracotta);
      border-left: 6px solid var(--mm-terracotta);
      padding: 6px 12px;
      font-size: 9.5pt;
      line-height: 1.35;
      border-radius: 3px;
    }}

    .pitfall-box strong {{
      color: var(--mm-terracotta);
    }}

    @media print {{
      body {{
        background: #fff;
        padding: 0;
        margin: 0;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
      }}

      .no-print {{
        display: none !important;
      }}

      .page {{
        margin: 0;
        border: none;
        box-shadow: none;
        width: 210mm;
        height: 297mm;
        min-height: 297mm;
        max-height: 297mm;
        page-break-after: always;
        break-after: page;
        page-break-inside: avoid;
        box-sizing: border-box;
      }}

      @page {{
        size: A4 portrait;
        margin: 0;
      }}
    }}

    @media screen and (max-width: 860px) {{
      body {{
        padding: 8px;
      }}
      .page {{
        width: 100%;
        height: auto;
        min-height: auto;
        max-height: none;
        margin-bottom: 20px;
      }}
      .chunk-header-num {{
        font-size: 40pt;
        width: 24mm;
      }}
      .chunk-main-grid {{
        height: auto;
        flex-direction: column;
      }}
      .chunk-theory-col {{
        border-right: none;
        border-bottom: 2px solid var(--mm-card-border);
      }}
      .note-grid-canvas {{
        min-height: 60mm;
      }}
    }}
  </style>
</head>
<body>

  <!-- Floating Print & Markdown Download Toolbar -->
  <div class="action-bar no-print">
    <div class="tips">
      <span class="badge">MID-MOD 记忆地图</span>
      <span>点击任意文字编辑 · 原文主体 · 支持导出 Markdown 与 A4 打印</span>
    </div>
    <div class="btn-group">
      <button class="btn-download-md" onclick="downloadMarkdown()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
        下载 Markdown (.md)
      </button>
      <button class="btn-print" onclick="window.print()">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9V2h12v7M6 18H4a2 2 0 01-2-2v-5a2 2 0 012-2h16a2 2 0 012 2v5a2 2 0 01-2 2h-2"/><path d="M6 14h12v8H6z"/></svg>
        打印 / 导出 PDF
      </button>
    </div>
  </div>

  <!-- Hidden Embedded Obsidian Markdown Source for 1-Click Download -->
  <script id="obsidian-markdown-source" type="text/markdown">
{obsidian_markdown}
  </script>

  <script>
  function downloadMarkdown() {{
    const el = document.getElementById('obsidian-markdown-source');
    if (!el) {{
      alert('Markdown data not found.');
      return;
    }}
    const rawText = el.textContent.trim();
    const docTitle = "{title}".replace(/[^a-zA-Z0-9\u4e00-\u9fa5_-]/g, '_');
    const filename = (docTitle || 'memory-handbook') + '.md';
    const blob = new Blob([rawText], {{ type: 'text/markdown;charset=utf-8;' }});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }}
  </script>

  <!-- =========================================================
       PAGE 1: COVER & OVERVIEW
       ========================================================= -->
  <div class="page" id="page-1">
    <div class="page-header">
      <div class="meta-tag" contenteditable="true">COGNITIVE CHUNKING · ACTIVE RECALL</div>
      <div class="meta-sub" contenteditable="true">{archive_id}</div>
    </div>

    <div class="page-body">
      <!-- Hero Deck Title -->
      <div class="cover-hero">
        <div class="badge-topic" contenteditable="true">{topic_badge}</div>
        <h1 class="cover-title" contenteditable="true">{title}</h1>
        <p class="cover-subtitle" contenteditable="true">{subtitle}</p>
      </div>

      <!-- Spaced Repetition Tracker -->
      <div class="tracker-bar">
        <div class="tracker-label">复习轨迹打卡 / EBBINGHAUS INTERVALS</div>
        <div class="tracker-pills">
          <div class="tracker-pill"><span class="tracker-box"></span> Day 1</div>
          <div class="tracker-pill"><span class="tracker-box"></span> Day 2</div>
          <div class="tracker-pill"><span class="tracker-box"></span> Day 4</div>
          <div class="tracker-pill"><span class="tracker-box"></span> Day 7</div>
          <div class="tracker-pill"><span class="tracker-box"></span> Day 15</div>
          <div class="tracker-pill"><span class="tracker-box"></span> Day 30</div>
        </div>
      </div>

      <!-- 3-Part Overview Bars -->
      <div class="overview-chunks">
        {''.join(overview_rows_html)}
      </div>

      <!-- Core Essence Formula -->
      <div class="cover-bottom-essence">
        <div class="essence-title">一句话本质 / CORE HOOK</div>
        <div class="essence-text" contenteditable="true">{core_hook}</div>
      </div>
    </div>

    <div class="page-footer">
      <div>MEMORIZATION HANDBOOK</div>
      <div>SHEET 01 / COVER & OVERVIEW</div>
    </div>
  </div>

  {''.join(chunk_pages_html)}

  {final_page_html}

</body>
</html>
"""
    return full_html, obsidian_markdown

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 render_handbook.py <input.json> [output.html]")
        sys.exit(1)

    json_file = sys.argv[1]
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html_content, md_content = build_handbook_html(data)
    
    out_html = "handbook.html"
    for arg in sys.argv[2:]:
        if not arg.startswith("--"):
            out_html = arg

    # Write HTML file
    with open(out_html, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"[✓] Rendered HTML handbook to: {os.path.abspath(out_html)}")

    # Write Markdown file alongside HTML
    out_md = os.path.splitext(out_html)[0] + ".md"
    with open(out_md, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"[✓] Rendered 15-Block Obsidian Markdown to: {os.path.abspath(out_md)}")

if __name__ == "__main__":
    main()
