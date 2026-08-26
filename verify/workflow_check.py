import yaml
for path in [".github/workflows/activity-graph.yml", ".github/workflows/arcade.yml"]:
    with open(path) as f:
        y = yaml.safe_load(f)
    assert "concurrency" in y, f"missing concurrency {path}"
    assert "cancel-in-progress" in str(y), "cancel missing"
    assert y["jobs"]["build" if "build" in y["jobs"] else "generate"]["timeout-minutes"] == 10
    assert "permissions" in y["jobs"]["build" if "build" in y["jobs"] else "generate"]
    text = open(path).read()
    assert "actions/checkout@v4.1.7" in text
    assert "crazy-max/ghaction-github-pages@v4.0.0" in text
print("workflows OK")
