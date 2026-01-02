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
    return db.get(username, "FREE")

# --- ဤနေရာတွင် function အသစ် ထပ်ဖြည့်ထားပါသည် (Error ပျောက်စေရန်) ---
def get_api_key(key_name):
    """Admin Panel မှ သိမ်းထားသော API Key ကို ပြန်ထုတ်ပေးသည်"""
    # Key များကို သိမ်းမည့် ဖိုင်အမည် (Admin Panel ကုဒ်နှင့် ကိုက်ညီရပါမည်)
    CONFIG_FILE = "admin_config.json" 
    
    if not os.path.exists(CONFIG_FILE):
        return None
        
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            # Admin Panel ကုဒ်အရ 'api_keys' dictionary ထဲတွင် သိမ်းထားလေ့ရှိသည်
            return config.get("api_keys", {}).get(key_name, None)
    except:
        return None
