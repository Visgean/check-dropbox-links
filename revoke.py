import json
import os
import requests
from datetime import datetime

token = os.environ.get("DROPBOX_TOKEN")

if not token:
    raise TypeError("give token")

URL = "https://api.dropboxapi.com/2/sharing/revoke_shared_link"

year = str(datetime.now().year)

with open("links.json") as f:
    links = json.loads(f.read())

for link in links:
    if year not in link["path_lower"]:
        name = link["name"]
        print(f"revoking {name}")
        r = requests.post(
            URL,
            json={"url": link["url"]},
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
        )
        r.raise_for_status()


count = len(links)
print(f"Checked {count} links")
