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

# --- မူရင်း function ထဲတွင် logic ထပ်ဖြည့်ခြင်း (Admin Panel မရရင်တောင် အလုပ်လုပ်စေရန်) ---
def get_api_key(key_name):
    """Admin Panel မှ သိမ်းထားသော API Key ကို ပြန်ထုတ်ပေးသည်"""
    
    # ၁။ ဒီနေရာမှာ Owner ရဲ့ Groq Key အမှန်ကို သေချာစွာ ထည့်ပေးပါ
    # "Invalid API Key" Error ပျောက်ရန် gsk_ နဲ့ စတဲ့ Key အပြည့်အစုံကို ကွင်းစကွင်းပိတ်ကြားထဲ ထည့်ရပါမယ်
    if key_name == "2. LLM (Chat) API":
        # ဥပမာ- return "gsk_yX6..." (ဒီနေရာမှာ Owner ရဲ့ Key အစစ်ကို ထည့်ပါ)
        return "gsk_xxxx..."  
        
    # ၂။ အကယ်၍ အပေါ်က Key မရှိမှ အောက်က မူရင်း Admin Config ကို ဖတ်ပါမယ်
    CONFIG_FILE = "admin_config.json" 
    if not os.path.exists(CONFIG_FILE):
        return None
        
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            return config.get("api_keys", {}).get(key_name, None)
    except:
        return None
