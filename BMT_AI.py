import streamlit as st

# ၁။ အခြားဖိုင်များကို Import လုပ်ခြင်း
try:
    from styles import apply_bmt_style
    from ads_center import ads_manager
    from owner_manager import manage_owner_access, owner_dashboard
    from studio_engine import run_video_studio, chat_interface
except ImportError as e:
    st.error(f"ဖိုင်တစ်ခုခု ပျောက်ဆုံးနေပါတယ် သို့မဟုတ် နာမည်မှားနေပါတယ်: {e}")
    st.stop()

# ၂။ Page Config (အပေါ်ဆုံးမှာ ရှိရပါမယ်)
st.set_page_config(page_title="BMT AI EMPIRE", layout="wide", initial_sidebar_state="collapsed")

# ၃။ Session State များ သတ်မှတ်ခြင်း
if 'page_state' not in st.session_state: st.session_state.page_state = 'home'
if 'video_history' not in st.session_state: st.session_state.video_history = []

# ၄။ UI Design နှင့် Access စစ်ဆေးခြင်း
apply_bmt_style()
manage_owner_access()

# ၅။ Tier Config များ သတ်မှတ်ခြင်း
configs = {
    'f_page': {'bg': '#021202', 'c': '#00ff00', 'n': 'FREE', 'd_list': ["5s", "8s"], 'res': ["480p", "720p"]},
    's_page': {'bg': '#121212', 'c': '#bdc3c7', 'n': 'SILVER', 'd_list': ["10s", "20s"], 'res': ["720p", "1080p"]},
    'g_page': {'bg': '#141101', 'c': '#f1c40f', 'n': 'GOLD', 'd_list': ["30s", "60s"], 'res': ["1080p", "2k"]},
    'd_page': {'bg': '#0d0114', 'c': '#9b59b6', 'n': 'DIAMOND', 'd_list': ["30s", "60s", "90s", "120s"], 'res': ["1080p", "2k", "4k"]}
}

# ၆။ Page Logic Flow
if st.session_state.page_state == 'home':
    st.markdown('<div class="bmt-title">BMT AI EMPIRE</div>', unsafe_allow_html=True)
    st.markdown('<div class="bmt-sub">The Future of AI Video Generation</div>', unsafe_allow_html=True)
    
    col_chat, col_vid = st.columns(2)
    if col_chat.button("AI SMART CHAT", use_container_width=True):
        st.session_state.page_state = 'chat_page'; st.rerun()
    if col_vid.button("VIDEO GENERATOR", use_container_width=True):
        st.session_state.page_state = 'tier_selection'; st.rerun()

elif st.session_state.page_state == 'chat_page':
    chat_interface()

elif st.session_state.page_state == 'tier_selection':
    st.markdown("<h2 style='text-align:center; padding: 20px;'>SELECT YOUR TIER</h2>", unsafe_allow_html=True)
    t1, t2, t3, t4 = st.columns(4)
    if t1.button("F (FREE)"): st.session_state.page_state = 'f_page'; st.rerun()
    if t2.button("S (SILVER)"): st.session_state.page_state = 's_page'; st.rerun()
    if t3.button("G (GOLD)"): st.session_state.page_state = 'g_page'; st.rerun()
    if t4.button("D (DIAMOND)"): st.session_state.page_state = 'd_page'; st.rerun()
    if st.button("BACK"): st.session_state.page_state = 'home'; st.rerun()

elif st.session_state.page_state in configs:
    # Studio Engine ကို Tier အလိုက် ခေါ်သုံးခြင်း
    run_video_studio(configs[st.session_state.page_state])

# ၇။ Ads နှင့် Dashboard (အောက်ဆုံးမှာ အမြဲပြနေစေရန်)
ads_manager()
owner_dashboard()
