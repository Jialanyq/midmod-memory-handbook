#!/usr/bin/env python3
"""
Convert Mid-Mod Memory Handbook HTML to A4 PDF using Headless Chrome or Playwright/Weasyprint.
"""
import sys
import os
import subprocess
import shutil

def find_chrome():
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chrome"),
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    return None

def convert_html_to_pdf(html_path, pdf_path):
    abs_html = os.path.abspath(html_path)
    abs_pdf = os.path.abspath(pdf_path)
    chrome_bin = find_chrome()

    if not chrome_bin:
        print("[!] No Google Chrome found. Please open the HTML in any browser and press Cmd+P / Ctrl+P to Save as PDF.")
        return False

    temp_profile = os.path.join(os.path.dirname(abs_pdf), ".chrome_pdf_profile")
    os.makedirs(temp_profile, exist_ok=True)

    cmd = [
        chrome_bin,
        "--headless",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--no-pdf-header-footer",
        "--virtual-time-budget=2000",
        f"--user-data-dir={temp_profile}",
        f"--print-to-pdf={abs_pdf}",
        f"file://{abs_html}"
    ]

    print(f"[*] Exporting A4 PDF: {abs_html} -> {abs_pdf} ...")
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=12)
        if os.path.exists(abs_pdf) and os.path.getsize(abs_pdf) > 1000:
            print(f"[✓] Successfully generated PDF: {abs_pdf} ({os.path.getsize(abs_pdf) // 1024} KB)")
            shutil.rmtree(temp_profile, ignore_errors=True)
            return True
        else:
            print(f"[!] Warning: Chrome headless finished without creating PDF (exit code {res.returncode})")
    except Exception as e:
        print(f"[!] Headless Chrome export encountered an error or timeout: {e}")
    finally:
        shutil.rmtree(temp_profile, ignore_errors=True)

    print("[i] Notice: You can open the HTML file directly in Chrome, Safari, or Edge and click '打印 / 导出 PDF' to generate pixel-perfect A4 PDF.")
    return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 export_pdf.py <input.html> [output.pdf]")
        sys.exit(1)
    
    in_html = sys.argv[1]
    out_pdf = sys.argv[2] if len(sys.argv) > 2 else os.path.splitext(in_html)[0] + ".pdf"
    success = convert_html_to_pdf(in_html, out_pdf)
    sys.exit(0 if success else 1)
