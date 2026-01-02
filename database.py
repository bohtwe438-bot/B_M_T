import json
import os

# ဒေတာသိမ်းမည့် JSON ဖိုင်အမည်
DB_FILE = "user_database.json"

def load_db():
    """ဖိုင်ထဲမှ ဒေတာများကို ဖတ်ယူသည်"""
    if not os.path.exists(DB_FILE):
        return {}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_user_tier(username, tier):
    """User ၏ Tier ကို Database ထဲတွင် အသေသိမ်းသည်"""
    db = load_db()
    db[username] = tier
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

def get_user_tier(username):
    """User ၏ Tier ကို Database ထဲမှ ပြန်ထုတ်သည်"""
    db = load_db()
    # အကယ်၍ အမည်မရှိပါက FREE ဟု သတ်မှတ်မည်
    return db.get(username, "FREE")
