## URL Unshorten

```sh
# setup env
sudo apt install python3-venv
python3 -m venv .venv
.venv/bin/pip install requests
.venv/bin/pip install beautifulsoup4

# run the script
.venv/bin/python unshorten_url_linkedin.py -h
.venv/bin/python unshorten_url_linkedin.py -i ./interviews/0-preparation-materials/0.md
.venv/bin/python unshorten_url_linkedin.py -i ./interviews/0-preparation-materials/0.md --replace
.venv/bin/python unshorten_url_linkedin.py -i ./interviews/0-preparation-materials/0.md -o ./interviews/0-preparation-materials/0.md
```
