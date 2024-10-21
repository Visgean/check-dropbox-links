import json
import os
import requests

token = os.environ.get("DROPBOX_TOKEN")

if not token:
    raise TypeError("give token")

URL = "https://api.dropboxapi.com/2/sharing/list_shared_links"

links = []
cursor = None

while True:
    params = {}
    if cursor:
        params["cursor"] = cursor

    r = requests.post(
        URL,
        json=params,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )

    data = r.json()
    links.extend(data["links"])
    cursor = data.get("cursor")

    if not data.get("has_more"):
        break

    print(data)

with open("links.json", "w") as f:
    f.write(json.dumps(links, indent=2))
