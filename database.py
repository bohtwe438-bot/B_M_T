import json
import os

# ဒေတာသိမ်းမည့် JSON ဖိုင်အမည် (owner_manager.py က ဒီဖိုင်ထဲမှာပဲ သိမ်းတာပါ)
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

# --- မူရင်း function ကို owner_manager.py နှင့် ချိတ်ဆက်ရန် ပြင်ဆင်ခြင်း ---
def get_api_key(key_name):
    """Admin Panel မှ 'secret_' ခံ၍ သိမ်းထားသော API Key ကို ပြန်ထုတ်ပေးသည်"""
    
    # owner_manager.py က Key တွေကို user_database.json (DB_FILE) ထဲမှာပဲ သိမ်းထားလို့ အဲဒါကိုပဲ ဖတ်ရပါမယ်
    db = load_db()
    
    # Admin ထဲမှာ သိမ်းတဲ့အခါ 'secret_2. LLM (Chat) API' ဆိုပြီး သိမ်းထားလို့ နာမည်ပြန်ပေါင်းပေးရပါတယ်
    lookup_name = f"secret_{key_name}"
    
    # Database ထဲကနေ Key ကို ရှာယူပါသည်
    api_key = db.get(lookup_name)
    
    # အကယ်၍ Key မရှိခြင်း သို့မဟုတ် Default စာသားဖြစ်နေခြင်းကို စစ်ဆေးသည်
    if not api_key or api_key == "HIDDEN_KEY_XXXXX":
        return None
        
    return api_key
