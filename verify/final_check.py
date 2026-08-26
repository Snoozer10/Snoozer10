with open("README.md", encoding="utf-8") as f:
    md = f.read()
assert "Proof of Competency" in md or "Proof of Impact" in md
assert "Distributed" in md and "GCP" in md
assert "Next.js" in md and "Tailwind" in md
assert "Connect & Collaborate" in md
assert "capsule-render" in md and "section=footer" in md
assert "© 2026 Hesham Alsoufi" in md
assert md.count("for-the-badge") >= 6
print("final OK")
