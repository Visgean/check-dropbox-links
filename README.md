# check all dropbox links are view-only

Steps: 

1. [Get token](https://dropbox.tech/developers/generate-an-access-token-for-your-own-account) and set it as env variable  `$DROPBOX_TOKEN`
2. Fetch all links json file: ``python download.py``
3. Verify all links with ``python check.py``

Optionally run revoke script ``python revoke.py`` that revokes all links which folder path does not contain current year. 

