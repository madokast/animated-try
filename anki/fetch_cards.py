import os
import json
import urllib.request
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

URL = os.getenv("ANKI_CONNECT_URL", "http://127.0.0.1:8765")
KEY = os.getenv("ANKI_CONNECT_KEY", "")


def anki(action, **params):
    body = {"action": action, "version": 6}
    if KEY:
        body["key"] = KEY
    if params:
        body["params"] = params
    data = json.dumps(body).encode("utf-8")
    resp = json.load(urllib.request.urlopen(urllib.request.Request(URL, data)))
    if resp.get("error"):
        raise Exception(resp["error"])
    return resp["result"]


N = 3
for q, label in [("is:new", "New"), ("is:due", "Due")]:
    card_ids = anki("findCards", query=q)[:N]
    print(f"=== {label} (前{len(card_ids)}张) ===")
    if not card_ids:
        print("  (无)")
        continue
    cards = anki("cardsInfo", cards=card_ids)
    for c in cards:
        print(f"  cardId={c['cardId']} deck={c['deckName']} model={c['modelName']}")
        for name, f in c["fields"].items():
            val = f["value"][:60].replace("\n", " ")
            print(f"    {name}: {val}")
    print()
