import json

with open("links.json") as f:
    links = json.loads(f.read())

for link in links:
    if link["link_permissions"].get("link_access_level", {}).get(".tag") == "editor":
        print(link["name"], "editable link")

count = len(links)
print(f"Checked {count} links")
