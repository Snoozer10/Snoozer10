with open("README.md", encoding="utf-8") as f:
    md = f.read()
assert "Technical Taxonomy & Toolchain" in md
assert "Core Languages" in md and "Frontend & UI" in md and "Cloud & DevOps" in md
assert "skillicons.dev/icons?i=py,js,ts,bash" in md
assert "gcp,aws,docker,githubactions" in md
assert 'width="25%"' in md
assert md.count('alt="') >= md.count('<img') - 2
print("taxonomy OK")
