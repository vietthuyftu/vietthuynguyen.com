"""
AI Ecom Vietnam — Auto Publish Script
Dùng: python auto-publish.py
"""

import os, sys, json, re, subprocess, datetime, textwrap
from pathlib import Path

# ── CẤU HÌNH ──────────────────────────────────────────────
GITHUB_TOKEN  = os.environ.get("GITHUB_TOKEN", "")
GITHUB_USER   = "vietthuyftu"
GITHUB_REPO   = "vietthuynguyen.com"
SITE_DIR      = Path(__file__).parent / "site"
POSTS_READY   = Path(__file__).parent / "posts" / "ready"
POSTS_PUB     = Path(__file__).parent / "posts" / "published"
# ──────────────────────────────────────────────────────────

def run(cmd, cwd=None):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return r.stdout.strip(), r.stderr.strip()

def check_git():
    out, err = run("git --version")
    if "git version" not in out:
        print("❌ Chưa cài Git. Tải tại: https://git-scm.com/download/win")
        sys.exit(1)

def setup_repo():
    """Clone hoặc pull repo về máy nếu chưa có."""
    repo_dir = Path(__file__).parent / ".git"
    if not repo_dir.exists():
        print("📥 Đang clone repo về máy...")
        url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git"
        out, err = run(f'git clone "{url}" .', cwd=Path(__file__).parent)
        if err and "fatal" in err:
            print(f"❌ Lỗi clone: {err}")
            sys.exit(1)
        print("✅ Clone thành công")
    else:
        print("🔄 Đang pull bản mới nhất...")
        run("git pull", cwd=Path(__file__).parent)

def get_posts_to_publish():
    """Lấy danh sách bài trong posts/ready/ chờ đăng."""
    POSTS_READY.mkdir(parents=True, exist_ok=True)
    posts = list(POSTS_READY.glob("*.md")) + list(POSTS_READY.glob("*.html"))
    return posts

def md_to_html_post(md_path: Path) -> str:
    """Chuyển file .md thành trang HTML hoàn chỉnh."""
    content = md_path.read_text(encoding="utf-8")

    # Parse frontmatter
    title, meta_desc, keyword = "Bài viết mới", "", ""
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm = parts[1]
            body = parts[2]
            for line in fm.strip().splitlines():
                if line.startswith("title:"):
                    title = line.split("title:", 1)[1].strip().strip('"')
                elif line.startswith("description:") or line.startswith("meta:"):
                    meta_desc = line.split(":", 1)[1].strip().strip('"')
                elif line.startswith("keyword:"):
                    keyword = line.split(":", 1)[1].strip()
        content = body.strip()

    # Simple markdown → HTML
    lines, html_lines = content.splitlines(), []
    in_code = False
    for line in lines:
        if line.startswith("```"):
            if not in_code:
                html_lines.append('<div class="code-block">')
                in_code = True
            else:
                html_lines.append('</div>')
                in_code = False
            continue
        if in_code:
            html_lines.append(line)
            continue
        if line.startswith("## "):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith("### "):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        elif line.startswith("# "):
            pass  # dùng title từ frontmatter
        elif line.startswith("- ") or line.startswith("* "):
            html_lines.append(f'<li>{line[2:]}</li>')
        elif line.startswith("> "):
            html_lines.append(f'<div class="callout"><p>{line[2:]}</p></div>')
        elif line.strip() == "":
            html_lines.append("")
        else:
            # Bold & italic
            line = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
            line = re.sub(r'\*(.+?)\*', r'<em>\1</em>', line)
            html_lines.append(f'<p>{line}</p>')

    body_html = "\n".join(html_lines)
    date_str = datetime.date.today().strftime("%d/%m/%Y")
    slug = md_path.stem

    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | AI Ecom Vietnam</title>
  <meta name="description" content="{meta_desc or title}">
  <style>
    :root {{
      --bg:#0f1117;--bg2:#1a1d27;--bg3:#22263a;--border:#2e3350;
      --text:#e2e8f0;--text-muted:#8892b0;--accent:#7c3aed;--accent2:#a855f7;
      --accent-glow:rgba(124,58,237,0.18);--radius:12px;
      --font:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
    }}
    *{{margin:0;padding:0;box-sizing:border-box}}
    body{{background:var(--bg);color:var(--text);font-family:var(--font);line-height:1.75}}
    a{{color:inherit;text-decoration:none}}
    nav{{position:sticky;top:0;z-index:100;background:rgba(15,17,23,0.85);backdrop-filter:blur(12px);border-bottom:1px solid var(--border);padding:0 24px}}
    .nav-inner{{max-width:1100px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:60px}}
    .logo{{font-size:1.1rem;font-weight:700;background:linear-gradient(135deg,#a855f7,#7c3aed);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
    .nav-back{{color:var(--accent2);font-size:.88rem;font-weight:600}}
    .page{{max-width:780px;margin:0 auto;padding:48px 24px 80px}}
    .breadcrumb{{color:var(--text-muted);font-size:.82rem;margin-bottom:16px}}
    .breadcrumb a{{color:var(--accent2)}}
    .post-tag{{display:inline-block;background:var(--accent-glow);color:var(--accent2);border:1px solid var(--accent);padding:3px 12px;border-radius:99px;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;margin-bottom:16px}}
    h1{{font-size:clamp(1.6rem,4vw,2.2rem);font-weight:800;line-height:1.3;margin-bottom:16px}}
    .post-meta{{display:flex;gap:20px;color:var(--text-muted);font-size:.85rem;margin-bottom:32px;flex-wrap:wrap}}
    .post-hero{{background:linear-gradient(135deg,#1e1040,#2d1b69);border-radius:16px;height:220px;display:flex;align-items:center;justify-content:center;font-size:5rem;margin-bottom:36px}}
    h2{{font-size:1.3rem;font-weight:700;margin:36px 0 14px;padding-top:8px;border-top:1px solid var(--border)}}
    h3{{font-size:1.05rem;font-weight:700;margin:24px 0 10px;color:var(--accent2)}}
    p{{margin-bottom:16px;color:var(--text)}}
    li{{margin-bottom:8px;margin-left:20px;color:var(--text)}}
    .code-block{{background:#0d1117;border:1px solid var(--border);border-radius:10px;padding:18px 20px;margin:18px 0;font-family:'Courier New',monospace;font-size:.87rem;color:#a5f3fc;white-space:pre-wrap;line-height:1.7}}
    .callout{{background:var(--accent-glow);border:1px solid var(--accent);border-left:4px solid var(--accent2);border-radius:10px;padding:16px 18px;margin:20px 0}}
    strong{{color:#fff}}
    footer{{border-top:1px solid var(--border);padding:32px 24px;text-align:center;color:var(--text-muted);font-size:.82rem}}
    @media(max-width:600px){{.page{{padding:32px 16px 60px}}}}
  </style>
</head>
<body>
<nav>
  <div class="nav-inner">
    <a href="index.html" class="logo">⚡ AI Ecom Vietnam</a>
    <a href="how-to.html" class="nav-back">← Quay lại</a>
  </div>
</nav>
<div class="page">
  <div class="breadcrumb"><a href="index.html">Trang chủ</a> / <a href="how-to.html">How-to</a> / Bài này</div>
  <span class="post-tag">How-to</span>
  <h1>{title}</h1>
  <div class="post-meta">
    <span>📅 {date_str}</span>
    <span>✍️ Viet Thuy Nguyen</span>
  </div>
  <div class="post-hero">🤖</div>
  <div class="content">
{body_html}
  </div>
</div>
<footer>© 2026 vietthuynguyen.com</footer>
</body>
</html>'''

def publish_post(post_path: Path):
    """Copy bài vào site/, commit và push lên GitHub."""
    slug = post_path.stem
    date_prefix = datetime.date.today().strftime("%Y-%m-%d")

    if post_path.suffix == ".md":
        html_content = md_to_html_post(post_path)
        out_filename = f"{slug}.html"
        out_path = SITE_DIR / out_filename
        out_path.write_text(html_content, encoding="utf-8")
    else:
        # File HTML — copy thẳng
        out_filename = post_path.name
        out_path = SITE_DIR / out_filename
        out_path.write_bytes(post_path.read_bytes())

    print(f"✅ Đã tạo: site/{out_filename}")

    # Git add, commit, push
    repo_root = Path(__file__).parent
    run("git config user.email 'vietthuyftu@gmail.com'", cwd=repo_root)
    run("git config user.name 'Viet Thuy'", cwd=repo_root)
    run(f'git add site/{out_filename}', cwd=repo_root)
    out, err = run(f'git commit -m "📝 Đăng bài: {slug} [{date_prefix}]"', cwd=repo_root)
    print("Commit:", out or err)

    url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_USER}/{GITHUB_REPO}.git"
    out, err = run(f'git push "{url}" main', cwd=repo_root)
    if "main" in (out + err) or err == "":
        print(f"🚀 Đã live: https://{GITHUB_USER}.github.io/{GITHUB_REPO}/{out_filename}")
    else:
        print(f"Push output: {out}\n{err}")

    # Move bài sang published/
    POSTS_PUB.mkdir(parents=True, exist_ok=True)
    dest = POSTS_PUB / post_path.name
    post_path.rename(dest)
    print(f"📁 Đã move bài sang posts/published/")

def main():
    print("=" * 50)
    print("  AI Ecom Vietnam — Auto Publisher")
    print("=" * 50)

    check_git()

    posts = get_posts_to_publish()

    if not posts:
        print("\n📭 Không có bài nào trong posts/ready/ để đăng.")
        print("👉 Đặt file .md hoặc .html vào thư mục posts/ready/ rồi chạy lại.")
        return

    print(f"\n📋 Tìm thấy {len(posts)} bài chờ đăng:")
    for i, p in enumerate(posts, 1):
        print(f"  {i}. {p.name}")

    print("\nBạn muốn đăng tất cả? (y/n): ", end="")
    ans = input().strip().lower()
    if ans != "y":
        print("Đã hủy.")
        return

    for post in posts:
        print(f"\n⏳ Đang đăng: {post.name}")
        publish_post(post)

    print("\n✅ Xong! Blog đã được cập nhật.")
    print(f"🌐 https://{GITHUB_USER}.github.io/{GITHUB_REPO}/")

if __name__ == "__main__":
    main()
