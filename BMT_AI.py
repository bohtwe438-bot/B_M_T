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
st.set_page_config(page_title="BMT AI EMPIRE", layout="wide")

# ၃။ Session State များ
if 'logged_in' not in st.session_state: st.session_state.logged_in = False
if 'page_state' not in st.session_state: st.session_state.page_state = 'home'
if 'is_owner' not in st.session_state: st.session_state.is_owner = False
if 'show_secret_gate' not in st.session_state: st.session_state.show_secret_gate = False

# ၄။ UI Design & Style
apply_bmt_style()

# --- ၅။ LOGIN & OWNER ACCESS LOGIC ---
if not st.session_state.logged_in:
    show_login_screen()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("© 2026 BMT AI EMPIRE", help="Owner Access"):
        st.session_state.show_secret_gate = not st.session_state.show_secret_gate
        st.rerun()

    if st.session_state.show_secret_gate:
        with st.form("stable_admin_form", clear_on_submit=True):
            admin_pwd = st.text_input("Master Password", type="password")
            if st.form_submit_button("UNLOCK ADMIN PANEL", use_container_width=True):
                if admin_pwd == "bmt999":
                    st.session_state.logged_in = True
                    st.session_state.is_owner = True
                    st.session_state.page_state = 'admin_dashboard' # တန်းပြီး dashboard ပို့မယ်
                    st.rerun()
                else:
                    st.error("မှားယွင်းနေပါသည်")
else:
    # --- ၆။ ADMIN/OWNER AREA ---
    if st.session_state.is_owner:
        with st.sidebar:
            st.markdown("<h2 style='color:#f1c40f; text-align:center;'>👑 ADMIN ACTIVE</h2>", unsafe_allow_html=True)
            
            # Dashboard နဲ့ Studio ကြား ကူးပြောင်းမည့်ခလုတ်
            if st.session_state.page_state == 'admin_dashboard':
                if st.button("🚀 USE STUDIO AS OWNER", use_container_width=True):
                    st.session_state.page_state = 'tier_selection'; st.rerun()
            else:
                if st.button("⚙️ BACK TO DASHBOARD", use_container_width=True):
                    st.session_state.page_state = 'admin_dashboard'; st.rerun()
            
            st.divider()
            if st.button("🚪 LOGOUT ADMIN", use_container_width=True):
                st.session_state.is_owner = False
                st.session_state.logged_in = False
                st.session_state.page_state = 'home'
                st.rerun()
        
        # Dashboard ပြသမည့် အပိုင်း
        if st.session_state.page_state == 'admin_dashboard':
            owner_dashboard() 
            st.stop() 

    # --- ၇။ NORMAL USER AREA ---
    with st.sidebar:
        user_profile_header() 
        st.divider()
        manage_owner_access()

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
    
    elif st.session_state.page_state == 'chat_page': chat_interface()

    elif st.session_state.page_state == 'tier_selection':
        st.markdown("<h2 style='text-align:center;'>SELECT YOUR TIER</h2>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)

        with col1:
            if st.button("🟢 F (FREE)", use_container_width=True): 
                st.session_state.page_state = 'f_page'; st.rerun()

        def tier_button(tier_id, tier_name, emoji):
            if st.button(f"{emoji} {tier_name}", use_container_width=True):
                if st.session_state.is_owner or st.session_state.get('user_tier') == tier_name:
                    st.session_state.page_state = tier_id; st.rerun()
                else:
                    st.warning(f"⚠️ {tier_name} Tier ကို ဝယ်ယူရန် လိုအပ်ပါသည်။")

        with col1: tier_button('g_page', 'GOLD', '🟡 G')
        with col2:
            tier_button('s_page', 'SILVER', '⚪ S')
            tier_button('d_page', 'DIAMOND', '💎 D')
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # BACK ခလုတ် Logic: Owner ဆိုရင် Dashboard ပြန်သွားမယ်၊ User ဆိုရင် Home သွားမယ်
        back_label = "⚙️ BACK TO DASHBOARD" if st.session_state.is_owner else "⬅️ BACK TO HOME"
        back_target = 'admin_dashboard' if st.session_state.is_owner else 'home'
        if st.button(back_label, use_container_width=True): 
            st.session_state.page_state = back_target; st.rerun()

    elif st.session_state.page_state in configs: 
        run_video_studio(configs[st.session_state.page_state])

    ads_manager()
