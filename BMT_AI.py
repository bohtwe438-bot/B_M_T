import streamlit as st
from groq import Groq
import time

# ==========================================
# ၁။ အလှအပ (STYLING & THEME)
# ==========================================
def apply_bmt_style():
    st.set_page_config(page_title="BMT AI EMPIRE", layout="wide")
    st.markdown("""
        <style>
        .stApp { background-color: #0f172a; color: white; }
        .bmt-title { font-size: 80px; font-weight: 900; text-align: center; color: #3b82f6; letter-spacing: 15px; }
        .bmt-sub { text-align: center; font-size: 18px; color: #60a5fa; margin-bottom: 30px; letter-spacing: 3px; }
        .glass-card { background: rgba(255, 255, 255, 0.05); padding: 25px; border-radius: 20px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 20px; }
        .owner-tag { color: #facc15; font-weight: bold; border: 1px solid #facc15; padding: 5px; border-radius: 5px; text-align: center; }
        </style>
        """, unsafe_allow_html=True)

# ==========================================
# ၂။ ပိုင်ရှင် KEY များ (OWNER KEYS & API)
# ==========================================
def manage_owner_keys():
    # Initialize Keys in Session State
    if 'api_keys' not in st.session_state:
        st.session_state.api_keys = {"groq": "", "video": "", "voice": ""}
    if 'is_owner' not in st.session_state:
        st.session_state.is_owner = False

    with st.sidebar:
        st.header(" BMT Access")
        pwd = st.text_input("Owner Password", type="password")
        if pwd == "bmt999": # ဗိုလ်ချုပ် စိတ်ကြိုက်ပြောင်းနိုင်သည်
            st.session_state.is_owner = True
            st.markdown('<div class="owner-tag">OWNER VERIFIED </div>', unsafe_allow_html=True)
            st.divider()
            st.subheader(" API Configuration")
            st.session_state.api_keys["groq"] = st.text_input("Groq AI Key", value=st.session_state.api_keys["groq"], type="password")
            st.session_state.api_keys["video"] = st.text_input("Video Engine Key", value=st.session_state.api_keys["video"], type="password")
            st.session_state.api_keys["voice"] = st.text_input("Voice Key", value=st.session_state.api_keys["voice"], type="password")
        else:
            st.session_state.is_owner = False

# ==========================================
# ၃။ AI CHAT & VIDEO GENERATOR (CORE LOGIC)
# ==========================================
def ai_studio_module():
    # ၁။ Navigation Buttons (အနားကွက်အရောင်ပါဝင်သော ခလုတ်များ)
    if 'mode' not in st.session_state: st.session_state.mode = 'chat'
    
    col1, col2 = st.columns(2)
    with col1:
        # Chat ခလုတ် (အစိမ်းရောင်အနားကွက်)
        if st.button(" AI CHAT", key="chat_btn", use_container_width=True):
            st.session_state.mode = 'chat'
    with col2:
        # Video ခလုတ် (အပြာရောင်အနားကွက်)
        if st.button(" VIDEO GENERATOR", key="video_btn", use_container_width=True):
            st.session_state.mode = 'video'

    st.divider()

    # ၂။ လုပ်ဆောင်ချက်အပိုင်းများ
    if st.session_state.mode == 'chat':
        st.subheader("BMT Intelligent Chat")
        st.chat_input("Ask BMT AI...")
        
    else:
        st.subheader("BMT Video Engine")
        # ဗိုလ်ချုပ်ရဲ့ Tier အလိုက် Resolution & Duration Matrix [cite: 2025-12-31]
        plans = {
            "F (Free)": {"res": ["480p", "720p"], "dur": ["5s", "8s"]},
            "S (Silver)": {"res": ["720p", "1080p"], "dur": ["10s", "15s", "20s"]},
            "G (Gold)": {"res": ["1080p", "2k"], "dur": ["20s", "30s", "40s", "60s"]},
            "D (Diamond)": {"res": ["2k", "4k"], "dur": ["30s", "60s", "90s", "120s"]}
        }

        # စာရေးရမည့်နေရာ
        st.text_area("ဗီဒီယိုအတွက် Script ရေးသားပါ", height=150, placeholder="ဒီမှာ စာရေးပါ...")
        
        # Option ရွေးချယ်မှုများ
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            tier = st.selectbox("Tier", list(plans.keys()))
            st.session_state.selected_tier = tier
        with c2:
            st.selectbox("Ratio", ["9:16", "16:9", "1:1", "4:3", "21:9"])
        with c3:
            # Tier အလိုက် Resolution ပြောင်းလဲခြင်း
            st.selectbox("Resolution", plans[tier]["res"])
        with c4:
            # Tier အလိုက် Duration ပြောင်းလဲခြင်း
            st.selectbox("Duration", plans[tier]["dur"])
            
        st.button(" START RENDER", use_container_width=True)

# ==========================================
# ၄။ ကြော်ငြာ (ADVERTISEMENTS)
# ==========================================
def ads_manager():
    if not st.session_state.is_owner:
        st.divider()
        st.markdown("""
            <div style="background: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; text-align: center;">
                <h4 style="color: #3b82f6; margin:0;">BMT SPONSORED AD</h4>
                <p style="font-size: 14px;">Upgrade to Diamond for 120s Videos!</p>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# ၅။ ပိုင်ရှင်ကြည့်ရန် (OWNER DASHBOARD)
# ==========================================
def owner_dashboard():
    if st.session_state.is_owner:
        st.divider()
        st.subheader(" BMT Business Insights")
        c1, c2, c3 = st.columns(3)
        c1.metric("Daily Users", "150", "+5%")
        c2.metric("Revenue", "350,000 MMK", "Peak")
        c3.metric("Video Tasks", len(st.session_state.video_history))

# ==========================================
# ၆။ အစီအစဉ်ကျ RUN ခြင်း (MAIN EXECUTION)
# ==========================================
if 'messages' not in st.session_state: st.session_state.messages = []
if 'video_history' not in st.session_state: st.session_state.video_history = []

apply_bmt_style()       # ၁။ အလှပြင်
manage_owner_keys()     # ၂။ Key စစ်/ထည့်
ai_studio_module()      # ၃။ Chat & Video
ads_manager()           # ၄။ ကြော်ငြာ
owner_dashboard()       # ၅။ ပိုင်ရှင်ကြည့်ရန်
