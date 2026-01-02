import streamlit as st
from styles import apply_bmt_style
from ads_center import ads_manager
from owner_manager import manage_owner_access, owner_dashboard
from studio_engine import video_rendering_logic, chat_interface

# ၁။ Page Setup
st.set_page_config(page_title="BMT AI EMPIRE", layout="wide", initial_sidebar_state="collapsed")

# ၂။ Session State များ သတ်မှတ်ခြင်း
if 'page_state' not in st.session_state: st.session_state.page_state = 'home'
if 'video_history' not in st.session_state: st.session_state.video_history = []

# ၃။ UI နှင့် Access စစ်ဆေးခြင်း
apply_bmt_style()
manage_owner_access()

# ၄။ Page Logic
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
    st.markdown("<h2 style='text-align:center;'>SELECT YOUR TIER</h2>", unsafe_allow_html=True)
    # Tier ခလုတ်များ ကုဒ်များကို ဤနေရာတွင် ဆက်ရေးပါ...
    if st.button("BACK TO HOME"):
        st.session_state.page_state = 'home'; st.rerun()

# ၅။ ကြော်ငြာနှင့် Dashboard
ads_manager()
owner_dashboard()
