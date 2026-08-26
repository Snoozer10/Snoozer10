with open("README.md", encoding="utf-8") as f:
    md = f.read()
assert "trophy" in md.lower(), "trophy missing"
assert "streak-stats" in md, "streak missing"
assert "top-langs" in md, "top langs missing"
assert ("wakatime" in md.lower() or "waka" in md.lower()) or ("komarev" in md or "ghpvc" in md), "views/waka missing"
assert ("3d" in md.lower() or "profile-3d" in md.lower() or "3d-contrib" in md.lower()) or ("komarev" in md or "ghpvc" in md), "3d contrib missing"
print("impact OK")
