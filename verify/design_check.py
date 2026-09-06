import re

CANONICAL = [
    "Overview",
    "Colors",
    "Typography",
    "Layout",
    "Elevation & Depth",
    "Shapes",
    "Components",
    "Do's and Don'ts",
]

with open("DESIGN.md", encoding="utf-8") as f:
    doc = f.read()

assert doc.startswith("---\n"), "front matter opening fence missing"
end = doc.find("\n---\n", 3)
assert end != -1, "front matter closing fence missing"
fm = doc[:end]

assert "name: Executive Cobalt Arcade" in fm, "design name missing"
for anchor in ('"#282A36"', '"#00FF41"', "Fira Code"):
    assert anchor in fm, f"required token {anchor} missing"

positions = [doc.find(f"## {h}\n") for h in CANONICAL]
present = [p for p in positions if p != -1]
assert len(present) >= 6, "too few canonical sections present"
assert present == sorted(present), "canonical sections out of order"

sections = {}
current = None
for line in fm.splitlines():
    top = re.match(r"^([a-z][a-z-]+):\s*$", line)
    if top:
        current = top.group(1)
        sections[current] = set()
        continue
    if current:
        child = re.match(r"^  ([a-z0-9-]+):(?:\s|$)", line)
        if child:
            sections[current].add(child.group(1))

refs = set(re.findall(r"\{([a-z-]+)\.([a-z0-9-]+)\}", fm))
for sec, key in refs:
    assert sec in sections, f"broken ref section {{{sec}}}"
    assert key in sections[sec], f"broken ref {{{sec}.{key}}}"

print("design OK")
