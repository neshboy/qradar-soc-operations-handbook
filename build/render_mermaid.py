import os
import re
import subprocess
import glob

ROOT = r"C:\Users\User\projects\qradar-soc-operations-handbook"
CHAPTER_GLOBS = [
    os.path.join(ROOT, "chapters", "*.md"),
    os.path.join(ROOT, "appendices", "*.md"),
]
DIAGRAM_DIR = os.path.join(ROOT, "assets", "diagrams")
os.makedirs(DIAGRAM_DIR, exist_ok=True)

MERMAID_RE = re.compile(r"```mermaid\r?\n(.*?)```", re.DOTALL)
# Matches the whitespace immediately following a closing mermaid fence, so we can tell
# whether an image tag is already there (already rendered in a prior pass) vs. missing.
POST_FENCE_RE = re.compile(r"\A(\r?\n)*(!\[[^\]]*\]\([^)]*\))")
MMDC_CMD = ["npx", "-y", "@mermaid-js/mermaid-cli"]


def slug_for(path):
    base = os.path.splitext(os.path.basename(path))[0]
    return base


def render_one(mmd_text, out_svg):
    tmp_mmd = out_svg + ".mmd"
    with open(tmp_mmd, "w", encoding="utf-8") as f:
        f.write(mmd_text)
    cmd = MMDC_CMD + ["-i", tmp_mmd, "-o", out_svg, "-b", "white"]
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True, timeout=90)
    ok = os.path.exists(out_svg) and os.path.getsize(out_svg) > 0
    try:
        os.remove(tmp_mmd)
    except OSError:
        pass
    return ok, result.stdout, result.stderr


def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    matches = list(MERMAID_RE.finditer(content))
    if not matches:
        return 0, 0, 0

    slug = slug_for(path)
    rendered = 0
    failed = 0
    skipped = 0
    new_content = content
    offset = 0

    for i, m in enumerate(matches, start=1):
        fig_name = f"{slug}-fig{i:02d}"

        # Idempotency guard: this book already had 9/24 mermaid fences rendered in a
        # prior pass (image tag inserted right after the closing fence). Re-running
        # blindly like DEH's original script would double-insert on those. Check the
        # text immediately following this fence's end (in the ORIGINAL content, not
        # the mutating new_content) for an existing image tag and skip if present.
        tail = content[m.end():m.end() + 300]
        if POST_FENCE_RE.match(tail):
            skipped += 1
            continue

        mmd_text = m.group(1)
        out_svg = os.path.join(DIAGRAM_DIR, fig_name + ".svg")
        rel_path = f"../assets/diagrams/{fig_name}.svg"

        ok, out, err = render_one(mmd_text, out_svg)
        if ok:
            rendered += 1
            img_line = f"\n\n![{fig_name}]({rel_path})\n"
        else:
            failed += 1
            img_line = f"\n\n<!-- RENDER FAILED for {fig_name}: {err.strip()[:300]} -->\n"

        insert_at = m.end() + offset
        new_content = new_content[:insert_at] + img_line + new_content[insert_at:]
        offset += len(img_line)

    if rendered or failed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return rendered, failed, skipped


def main():
    files = []
    for g in CHAPTER_GLOBS:
        files.extend(sorted(glob.glob(g)))

    total_rendered = 0
    total_failed = 0
    total_skipped = 0
    for path in files:
        rendered, failed, skipped = process_file(path)
        if rendered or failed or skipped:
            print(f"{os.path.basename(path)}: rendered={rendered} failed={failed} skipped(existing)={skipped}", flush=True)
        total_rendered += rendered
        total_failed += failed
        total_skipped += skipped

    print(f"\n=== TOTAL: rendered={total_rendered} failed={total_failed} skipped(existing)={total_skipped} ===")


if __name__ == "__main__":
    main()
