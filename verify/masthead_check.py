import re
with open("README.md", encoding="utf-8") as f:
    md = f.read()
assert "capsule-render.vercel.app/api?type=waving&height=220" in md, "capsule header missing"
assert "readme-typing-svg.demolab.com" in md, "typing SVG missing"
assert "Fira+Code" in md and "Building+Scalable+Cloud+Architectures" in md, "typing lines missing"
assert md.count("img.shields.io/badge/LinkedIn") >= 1
assert "customColorList=6,11,20,29" in md
print("masthead OK")
