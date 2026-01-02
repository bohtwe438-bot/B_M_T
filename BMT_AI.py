import streamlit as st

# ၁။ အခြားဖိုင်များကို Import လုပ်ခြင်း
try:
    from styles import apply_bmt_style
    from ads_center import ads_manager
    from owner_manager import manage_owner_access, owner_dashboard
    from studio_engine import run_video_studio, chat_interface
    from auth_manager import show_login_screen, user_profile_header
    from database import get_user_tier
except ImportError as e:
    st.error(f"Error: {e}")
    st.stop()

# ၂။ Page Config
st.set_page_config(page_title="BMT AI EMPIRE", layout="wide")

# ၃။ Session State Initialization (Error ကာကွယ်ရန်)
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'is_owner' not in st.session_state: st.session_state.is_owner = False
if 'page_state' not in st.session_state: st.session_state.page_state = 'home'
if 'user_name' not in st.session_state: st.session_state.user_name = "Guest"

# --- [အရေးကြီး] AttributeError မတက်စေရန် user_data ကို အလွတ်တစ်ခု ကြိုဆောက်ထားခြင်း ---
if 'user_data' not in st.session_state or st.session_state.user_data is None:
    st.session_state.user_data = {
        "name": "Guest",
        "email": "",
        "photo": "https://cdn-icons-png.flaticon.com/512/149/149071.png", # Default Icon
        "tier": "FREE"
    }

# Tier ကို Database မှ ဖတ်ယူခြင်း
st.session_state.user_tier = get_user_tier(st.session_state.user_name)

# ၄။ UI Style Apply
apply_bmt_style()

# --- ၅။ LOGIN & ADMIN ACCESS ---
if not st.session_state.logged_in:
    show_login_screen()
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("© 2026 BMT AI EMPIRE", help="Admin Access"):
        st.session_state.show_secret_gate = not st.session_state.get('show_secret_gate', False)
        st.rerun()

    if st.session_state.get('show_secret_gate'):
        with st.form("stable_admin_form"):
            admin_pwd = st.text_input("Master Password", type="password")
            if st.form_submit_button("UNLOCK ADMIN PANEL"):
                if admin_pwd == "bmt999":
                    st.session_state.logged_in = True
                    st.session_state.is_owner = True
                    st.session_state.user_name = "Owner_Admin"
                    # Admin အတွက် လိုအပ်သော data များ အပြည့်အစုံ ဖြည့်ပေးခြင်း
                    st.session_state.user_data = {
                        "name": "BMT OWNER",
                        "email": "admin@bmt.com",
                        "photo": "https://cdn-icons-png.flaticon.com/512/1864/1864509.png", # Admin Icon
                        "tier": "OWNER"
                    }
                    st.session_state.page_state = 'admin_dashboard'
                    st.rerun()
                else: st.error("Access Denied!")
else:
    # --- ၆။ SIDEBAR LOGIC (Use Studio ခလုတ် ပေါ်စေရန်) ---
    with st.sidebar:
        if st.session_state.is_owner:
            st.markdown("<h2 style='color:#f1c40f; text-align:center;'>👑 OWNER MENU</h2>", unsafe_allow_html=True)
            
            # Dashboard မှာ ရှိနေစဉ် USE STUDIO ခလုတ်ပြပါမည်
            if st.session_state.page_state == 'admin_dashboard':
                st.info("Key များပြင်ပြီးလျှင် Studio သို့သွားပါ")
                if st.button("🚀 USE STUDIO AS OWNER", use_container_width=True, type="primary"):
                    st.session_state.page_state = 'tier_selection'
                    st.rerun()
            else:
                if st.button("⚙️ BACK TO DASHBOARD", use_container_width=True):
                    st.session_state.page_state = 'admin_dashboard'
                    st.rerun()
            st.divider()
        
        # User Header (Error မတက်အောင် data ညှိထားပြီးဖြစ်သည်)
        user_profile_header()
        st.divider()
        manage_owner_access()

    # --- ၇။ PAGE ROUTING ---
    # A. Admin Dashboard
    if st.session_state.page_state == 'admin_dashboard':
        owner_dashboard()
        # st.stop() ကို ဖြုတ်ထားရပါမည် (Sidebar ပေါ်စေရန်)

    # B. AI Smart Chat (Messenger UI)
    elif st.session_state.page_state == 'chat_page':
        chat_interface()

    # C. Home Page
    elif st.session_state.page_state == 'home':
        st.markdown('<div class="bmt-title">BMT AI EMPIRE</div>', unsafe_allow_html=True)
        col_chat, col_vid = st.columns(2)
        if col_chat.button("💬 AI SMART CHAT", use_container_width=True): 
            st.session_state.page_state = 'chat_page'; st.rerun()
        if col_vid.button("🎬 VIDEO GENERATOR", use_container_width=True): 
            st.session_state.page_state = 'tier_selection'; st.rerun()

    # D. Tier Selection & Video Studio
    elif st.session_state.page_state == 'tier_selection':
        st.markdown("<h2 style='text-align:center;'>SELECT YOUR TIER</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        def t_btn(t_id, t_name, emi):
            if st.button(f"{emi} {t_name}", use_container_width=True):
                if st.session_state.is_owner or st.session_state.user_tier == t_name:
                    st.session_state.page_state = t_id; st.rerun()
                else: st.warning(f"{t_name} Tier ဝယ်ယူရန် လိုအပ်ပါသည်")
        with col1:
            if st.button("🟢 FREE", use_container_width=True): st.session_state.page_state='f_page'; st.rerun()
            t_btn('g_page', 'GOLD', '🟡 G')
        with col2:
            t_btn('s_page', 'SILVER', '⚪ S')
            t_btn('d_page', 'DIAMOND', '💎 D')
        if st.button("⬅️ BACK", use_container_width=True):
            st.session_state.page_state = 'admin_dashboard' if st.session_state.is_owner else 'home'; st.rerun()

    elif st.session_state.page_state in ['f_page', 's_page', 'g_page', 'd_page']:
        configs = {
            'f_page': {'bg': '#021202', 'c': '#00ff00', 'n': 'FREE', 'd_list': ["5s", "8s"], 'res': ["480p", "720p"]},
            's_page': {'bg': '#121212', 'c': '#bdc3c7', 'n': 'SILVER', 'd_list': ["10s", "20s"], 'res': ["720p", "1080p"]},
            'g_page': {'bg': '#141101', 'c': '#f1c40f', 'n': 'GOLD', 'd_list': ["30s", "60s"], 'res': ["1080p", "2k"]},
            'd_page': {'bg': '#0d0114', 'c': '#9b59b6', 'n': 'DIAMOND', 'd_list': ["30s", "60s", "90s", "120s"], 'res': ["1080p", "2k", "4k"]}
        }
        run_video_studio(configs[st.session_state.page_state])

    ads_manager()
