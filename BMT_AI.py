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
    # ၁။ စာမျက်နှာ အခြေအနေ မှတ်သားခြင်း [cite: 2026-01-01]
    if 'page_state' not in st.session_state:
        st.session_state.page_state = 'home'

    # --- CSS: Tier အလိုက် မတူညီသော အရောင်နှင့် Scanner Effect များ --- [cite: 2026-01-01]
    st.markdown("""
        <style>
        .stApp { background: #0a0e14; color: white; }
        /* Glassmorphism Buttons [cite: 2026-01-01] */
        div.stButton > button {
            border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.05); backdrop-filter: blur(10px);
            font-weight: bold; transition: 0.3s;
        }
        /* Scanner Animation [cite: 2026-01-01] */
        @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }
        .scanner-box { 
            position: relative; overflow: hidden; height: 60px; 
            border: 1px solid #00f2ff; background: rgba(0,242,255,0.05);
            display: flex; align-items: center; justify-content: center;
        }
        .scanner-line {
            position: absolute; width: 100%; height: 2px;
            background: #00f2ff; box-shadow: 0 0 15px #00f2ff;
            animation: scan 2s linear infinite;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- ၂။ HOME PAGE (SIDE-BY-SIDE RECTANGLE) --- [cite: 2026-01-01]
    if st.session_state.page_state == 'home':
        st.markdown("<div style='text-align:center; padding: 40px 0;'><h1 style='font-size:100px; letter-spacing:20px; margin:0;'>BMT</h1></div>", unsafe_allow_html=True)
        
        col_chat, col_vid = st.columns(2)
        with col_chat:
            if st.button("\n\nAI SMART CHAT", key="home_chat", use_container_width=True):
                st.session_state.page_state = 'chat_page'; st.rerun()
        with col_vid:
            if st.button("\n\nVIDEO GENERATOR", key="home_vid", use_container_width=True):
                st.session_state.page_state = 'tier_selection'; st.rerun()

    # --- ၃။ TIER SELECTION PAGE (F, S, G, D) --- [cite: 2026-01-01]
    elif st.session_state.page_state == 'tier_selection':
        st.markdown("<h2 style='text-align:center; padding: 20px;'>SELECT YOUR TIER</h2>", unsafe_allow_html=True)
        t1, t2, t3, t4 = st.columns(4)
        # ခလုတ်တစ်ခုစီတွင် မတူညီသော အရောင် Glow များ ထည့်သွင်းမည် [cite: 2026-01-01]
        if t1.button("F (FREE)"): st.session_state.page_state = 'f_page'; st.rerun()
        if t2.button("S (SILVER)"): st.session_state.page_state = 's_page'; st.rerun()
        if t3.button("G (GOLD)"): st.session_state.page_state = 'g_page'; st.rerun()
        if t4.button("D (DIAMOND)"): st.session_state.page_state = 'd_page'; st.rerun()
        if st.button(" BACK"): st.session_state.page_state = 'home'; st.rerun()

    # --- ၄။ INDIVIDUAL VIDEO PAGES (F, S, G, D) --- [cite: 2026-01-01]
    elif st.session_state.page_state in ['f_page', 's_page', 'g_page', 'd_page']:
        # Tier အလိုက် Layout နှင့် အလှအပ ခြားနားချက်များ [cite: 2026-01-01]
        configs = {
            'f_page': {'c': '#00ff00', 'n': 'FREE', 'd': '8s', 'res': ["480p", "720p"]},
            's_page': {'c': '#bdc3c7', 'n': 'SILVER', 'd': '20s', 'res': ["720p", "1080p"]},
            'g_page': {'c': '#f1c40f', 'n': 'GOLD', 'd': '60s', 'res': ["1080p", "2k"]},
            'd_page': {'c': '#9b59b6', 'n': 'DIAMOND', 'd': '120s', 'res': ["1080p", "2k", "4k"]}
        }
        curr = configs[st.session_state.page_state]
        
        st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']};'>VIDEO STUDIO - {curr['n']}</h1>", unsafe_allow_html=True)
        
        # Side-to-Side Layout: ဇာတ်ညွှန်း Box က ပိုကြီးရမည် [cite: 2025-12-31]
        col_main, col_side = st.columns([3, 1])
        with col_main:
            prompt = st.text_area("WRITE YOUR SCRIPT (PROMPT)", height=300, placeholder="Enter your imagination...")

# START GENERATE ခလုတ်ကို ဇာတ်ညွှန်းအောက်တွင် အရောင်ထင်ရှားစွာ ထားခြင်း [cite: 2025-12-31]
            if st.button(f" START {curr['n']} GENERATE", use_container_width=True):
                st.markdown(f'<div class="scanner-box"><div class="scanner-line"></div><span style="color:{curr["c"]}">ANALYZING SCRIPT...</span></div>', unsafe_allow_html=True)
                time.sleep(3) # Scanner Animation Effect [cite: 2026-01-01]
                st.success(f"{curr['n']} Video Generation Started!")
        
        with col_side:
            # ဘေးတွင် သေးငယ်သော အကွက်များဖြင့် စီခြင်း [cite: 2025-12-31]
            st.selectbox("Resolution", curr['res'])
            st.info(f"Duration: {curr['d']}")
            if st.button(" BACK"): st.session_state.page_state = 'tier_selection'; st.rerun()

    # --- ၅။ AI CHAT PAGE --- [cite: 2026-01-01]
    elif st.session_state.page_state == 'chat_page':
        st.markdown("<h1>BMT AI CHAT</h1>", unsafe_allow_html=True)
        if st.button(" BACK TO EMPIRE"): st.session_state.page_state = 'home'; st.rerun()
        st.chat_input("မေးမြန်းလိုသည်များကို ရိုက်ထည့်ပါ...")

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
