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

# --- မူရင်း function ထဲတွင် Admin Panel မှ Key ကိုသာ ဖတ်ရန် ပြင်ဆင်ခြင်း ---
def get_api_key(key_name):
    """Admin Panel မှ သိမ်းထားသော API Key ကို ပြန်ထုတ်ပေးသည်"""
    
    # Key များကို သိမ်းထားသည့် ဖိုင်အမည်
    CONFIG_FILE = "admin_config.json" 
    
    # ဖိုင်မရှိသေးရင် ဘာမှမလုပ်ဘဲ ပြန်ထွက်မည်
    if not os.path.exists(CONFIG_FILE):
        return None
        
    try:
        with open(CONFIG_FILE, "r") as f:
            config = json.load(f)
            # Admin Panel က 'api_keys' ဆိုတဲ့ Dictionary ထဲမှာ Key တွေကို သိမ်းထားတာပါ
            api_keys_dict = config.get("api_keys", {})
            
            # ခေါ်လိုက်တဲ့ key_name (ဥပမာ- "2. LLM (Chat) API") အတိုင်း Key ကို ပြန်ပေးမည်
            return api_keys_dict.get(key_name, None)
    except:
        # ဖိုင်ဖတ်ရတာ အဆင်မပြေရင် Error မတက်အောင် ကာကွယ်ခြင်း
        return None
