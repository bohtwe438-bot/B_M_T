import streamlit as st

# ၁။ အခြားဖိုင်များကို Import လုပ်ခြင်း
try:
    from styles import apply_bmt_style
    from ads_center import ads_manager
    from owner_manager import manage_owner_access, owner_dashboard
    from studio_engine import run_video_studio, chat_interface
    from auth_manager import show_login_screen, user_profile_header
except ImportError as e:
    st.error(f"Error: {e}")
    st.stop()

# ၂။ Page Config
st.set_page_config(page_title="BMT AI EMPIRE", layout="wide", initial_sidebar_state="expanded")

# ၃။ Session State များ
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'page_state' not in st.session_state: st.session_state.page_state = 'home'
if 'is_owner' not in st.session_state: st.session_state.is_owner = False

# ၄။ UI Design & Style
apply_bmt_style()

# Login စစ်ဆေးခြင်း
if not st.session_state.logged_in:
    show_login_screen()
else:
    # --- 🔑 Sidebar: Admin Section ကို အပေါ်ဆုံး တင်လိုက်သည် ---
    with st.sidebar:
        st.markdown("<h2 style='color:#f1c40f; text-align:center;'>🛡️ COMMAND</h2>", unsafe_allow_html=True)
        
        if not st.session_state.is_owner:
            with st.expander("🔑 OWNER LOGIN", expanded=True): # Expander နဲ့ဆိုတော့ ပိုမြင်သာပါတယ်
                with st.form("admin_verify_form"):
                    pwd = st.text_input("Admin Password", type="password")
                    if st.form_submit_button("UNLOCK DASHBOARD", use_container_width=True):
                        if pwd == "bmt999":
                            st.session_state.is_owner = True
                            st.rerun()
                        else:
                            st.error("မှားယွင်းနေပါသည်")
        else:
            st.success("OWNER VERIFIED ✅")
            if st.button("🚪 EXIT ADMIN", use_container_width=True):
                st.session_state.is_owner = False
                st.rerun()
        
        st.divider()
        user_profile_header() 

    # --- ၅။ ADMIN CONTROL (is_owner True ဖြစ်မှသာ ပေါ်မည်) ---
    if st.session_state.is_owner:
        owner_dashboard() # 🔑 API Keys ၁၀ ခု စစ်ရမည့်နေရာ
        st.stop() 

    # --- ၆။ NORMAL USER AREA ---
    configs = {
        'f_page': {'bg': '#021202', 'c': '#00ff00', 'n': 'FREE', 'd_list': ["5s", "8s"], 'res': ["480p", "720p"]},
        's_page': {'bg': '#121212', 'c': '#bdc3c7', 'n': 'SILVER', 'd_list': ["10s", "20s"], 'res': ["720p", "1080p"]},
        'g_page': {'bg': '#141101', 'c': '#f1c40f', 'n': 'GOLD', 'd_list': ["30s", "60s"], 'res': ["1080p", "2k"]},
        'd_page': {'bg': '#0d0114', 'c': '#9b59b6', 'n': 'DIAMOND', 'd_list': ["30s", "60s", "90s", "120s"], 'res': ["1080p", "2k", "4k"]}
    }

    if st.session_state.page_state == 'home':
        st.markdown('<div class="bmt-title">BMT AI EMPIRE</div>', unsafe_allow_html=True)
        col_chat, col_vid = st.columns(2)
        if col_chat.button("AI SMART CHAT", use_container_width=True):
            st.session_state.page_state = 'chat_page'; st.rerun()
        if col_vid.button("VIDEO GENERATOR", use_container_width=True):
            st.session_state.page_state = 'tier_selection'; st.rerun()

    elif st.session_state.page_state == 'chat_page':
        chat_interface()

    elif st.session_state.page_state == 'tier_selection':
        st.markdown("<h2 style='text-align:center;'>SELECT YOUR TIER</h2>", unsafe_allow_html=True)
        t1, t2 = st.columns(2)
        t3, t4 = st.columns(2)
        if t1.button("F (FREE)", use_container_width=True): st.session_state.page_state = 'f_page'; st.rerun()
        if t2.button("S (SILVER)", use_container_width=True): st.session_state.page_state = 's_page'; st.rerun()
        if t3.button("G (GOLD)", use_container_width=True): st.session_state.page_state = 'g_page'; st.rerun()
        if t4.button("D (DIAMOND)", use_container_width=True): st.session_state.page_state = 'd_page'; st.rerun()
        if st.button("⬅️ BACK", use_container_width=True): st.session_state.page_state = 'home'; st.rerun()

    elif st.session_state.page_state in configs:
        run_video_studio(configs[st.session_state.page_state])

    ads_manager()
