with open("README.md", encoding="utf-8") as f:
    md = f.read()
assert "specialization: \"Full-Stack Development & Enterprise Cloud Architecture\"" in md
assert "150%" in md, "POD 150% growth missing"
assert "300k" in md or "300,000" in md, "300k visitors missing"
assert "40%" in md or "doubled" in md.lower(), "SEO lift missing"
assert "98% error-free" in md, "YLDF metric missing"
assert "International Business Administration" in md or "Twintech" in md
print("summary OK")
