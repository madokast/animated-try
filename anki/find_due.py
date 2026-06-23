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


# 1. 列出所有牌组及统计
print("=== 牌组统计 ===")
decks = anki("deckNames")
stats = anki("getDeckStats", decks=decks)
for sid, s in stats.items():
    print(f"  {s['name']}: 新{s['new_count']} 学习{s['learn_count']} 复习{s['review_count']} 共{s['total_in_deck']}")

# 2. 搜索所有待学习卡片 (due = 新卡 + 学习卡 + 到期复习卡)
print("\n=== 搜索到期卡片 ===")
queries = ["is:due", "is:new", "is:review -is:due"]
for q in queries:
    cards = anki("findCards", query=q)
    print(f"  {q}: {len(cards)} 张")
