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
    # စာမျက်နှာ အခြေအနေကို မှတ်သားရန်
    if 'page_state' not in st.session_state:
        st.session_state.page_state = 'home'

    # --- ၁။ HOME PAGE (SELECT TOOL) ---
    if st.session_state.page_state == 'home':
        st.markdown("<h3 style='text-align:center; color:#94a3b8;'>CHOOSE YOUR POWER</h3>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💬 OPEN AI CHAT", key="chat_btn", use_container_width=True):
                st.session_state.page_state = 'chat_page'
                st.rerun()
        with col2:
            if st.button("📹 VIDEO GENERATOR", key="video_btn", use_container_width=True):
                st.session_state.page_state = 'video_page'
                st.rerun()

    # --- ၂။ AI CHAT PAGE (NEW PAGE) ---
    elif st.session_state.page_state == 'chat_page':
        # Back Home Button
        if st.button("⬅️ BACK TO EMPIRE", use_container_width=False):
            st.session_state.page_state = 'home'
            st.rerun()
            
        st.markdown("<h2 style='color:#10b981;'>💬 BMT Intelligent Chat</h2>", unsafe_allow_html=True)
        st.chat_input("ဗိုလ်ချုပ်... ဘာများ သိလိုပါသလဲ?")

    # --- ၃။ VIDEO GENERATOR PAGE (NEW PAGE) ---
    elif st.session_state.page_state == 'video_page':
        # Back Home Button
        if st.button("⬅️ BACK TO EMPIRE", use_container_width=False):
            st.session_state.page_state = 'home'
            st.rerun()
            
        st.markdown("<h2 style='color:#3b82f6;'>📹 BMT Video Engine</h2>", unsafe_allow_html=True)
        
        # FSGD Matrix (ဗိုလ်ချုပ်၏ Update ပါဝင်သည်) [cite: 2025-12-31]
        plans = {
            "F (Free)": {"res": ["480p", "720p"], "dur": ["5s", "8s"]},
            "S (Silver)": {"res": ["720p", "1080p"], "dur": ["10s", "15s", "20s"]},
            "G (Gold)": {"res": ["1080p", "2k"], "dur": ["20s", "30s", "40s", "60s"]},
            "D (Diamond)": {"res": ["1080p", "2k", "4k"], "dur": ["30s", "60s", "90s", "120s"]}
        }

        script = st.text_area("Create your masterpiece (Script)", height=150, placeholder="ဒီမှာ ဗီဒီယိုအတွက် စာသားရေးပါ...")
        
        st.markdown('<div class="option-box">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            tier = st.selectbox("Select Tier", list(plans.keys()))
        with c2:
            st.selectbox("Aspect Ratio", ["9:16", "16:9", "1:1", "4:3", "21:9"])
        with c3:
            # Diamond မှာ 1080p, 2k, 4k ပါဝင်လာပါပြီ
            st.selectbox("Resolution", plans[tier]["res"])
        with c4:
            st.selectbox("Duration", plans[tier]["dur"])
        st.markdown('</div>', unsafe_allow_html=True)
            
        if st.button("🚀 INITIATE RENDERING", use_container_width=True):
            if script:
                st.toast("Processing BMT High-End Video...")
                time.sleep(2)
                st.success(f"Video queued successfully in {tier} mode!")

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
