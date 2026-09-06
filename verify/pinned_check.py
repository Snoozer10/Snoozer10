with open("README.md", encoding="utf-8") as f:
    md = f.read()
assert "Featured" in md or "Pinned" in md
assert md.count("img.shields.io/badge") >= 8
assert "github-stats-extended.vercel.app/api/pin" in md or "github-readme-stats.vercel.app/api/pin" in md or "pin/?username=Snoozer10" in md
assert "<table>" in md and (md.count('<td width="50%"') >= 2 or md.count("pin/?username=Snoozer10") >= 2)
# 1x2 real-only: exactly 2 curated pins (public repos verified 200 OK)
assert md.count("pin/?username=Snoozer10") == 2, f"expected 2 pins, got {md.count('pin/?username=Snoozer10')}"
assert "gcp-cloud-architect" not in md, "fabricated pin gcp-cloud-architect must not be in README"
assert "nextjs-tailwind-growth" not in md, "fabricated pin nextjs-tailwind-growth must not be in README"
assert "local-youtube-automation" in md and "Snoozer10" in md
# thematic/lychee invariants (global constraints)
assert "theme=dracula" in md
assert "hide_border=false" in md
assert 'width="50%"' in md
assert 'width="100%"' in md
assert 'alt=' in md
assert "http://" not in md, "https only"
print("pinned OK")
