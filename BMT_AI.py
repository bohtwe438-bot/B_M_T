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
import streamlit as st
import time

def ai_empire_terminal():
    # ၁။ စာမျက်နှာ အခြေအနေ မှတ်သားခြင်း (Navigation State) [cite: 2026-01-01]
    if 'page_state' not in st.session_state:
        st.session_state.page_state = 'home'

    # --- CSS: Tier အလိုက် မတူညီသော အလှအပနှင့် Background များ --- [cite: 2026-01-01]
    st.markdown("""
        <style>
        .stApp { background: #0a0e14; color: white; }
        /* Glassmorphism Buttons */
        div.stButton > button {
            border-radius: 15px; border: 1px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.05); backdrop-filter: blur(10px);
            transition: 0.3s;
        }
        /* Scanner Animation [cite: 2026-01-01] */
        @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }
        .scanner { position: relative; overflow: hidden; }
        .scanner::after {
            content: ""; position: absolute; width: 100%; height: 2px;
            background: #00f2ff; box-shadow: 0 0 15px #00f2ff;
            animation: scan 2s linear infinite;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- ၂။ HOME PAGE (SIDE-BY-SIDE RECTANGLE) --- [cite: 2026-01-01]
    if st.session_state.page_state == 'home':
        st.markdown("<h1 style='text-align:center; font-size:80px; letter-spacing:15px;'>BMT</h1>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            if st.button("\n\nAI CHAT", use_container_width=True):
                st.session_state.page_state = 'chat_page'; st.rerun()
        with col2:
            if st.button("\n\nVIDEO GENERATOR", use_container_width=True):
                st.session_state.page_state = 'tier_selection'; st.rerun()

    # --- ၃။ TIER SELECTION PAGE (F, S, G, D) --- [cite: 2026-01-01]
    elif st.session_state.page_state == 'tier_selection':
        st.markdown("<h2 style='text-align:center;'>SELECT YOUR TIER</h2>", unsafe_allow_html=True)
        t1, t2, t3, t4 = st.columns(4)
        with t1: 
            if st.button("F (FREE)", key="f_btn"): st.session_state.page_state = 'f_page'; st.rerun()
        with t2: 
            if st.button("S (SILVER)", key="s_btn"): st.session_state.page_state = 's_page'; st.rerun()
        with t3: 
            if st.button("G (GOLD)", key="g_btn"): st.session_state.page_state = 'g_page'; st.rerun()
        with t4: 
            if st.button("D (DIAMOND)", key="d_btn"): st.session_state.page_state = 'd_page'; st.rerun()

    # --- ၄။ INDIVIDUAL TIER PAGES (F, S, G, D) --- [cite: 2026-01-01]
    # မှတ်ချက် - Page တစ်ခုချင်းစီတွင် အရောင်နှင့် ပါဝင်ပုံများ မတူညီအောင် ခွဲထားပါသည် [cite: 2026-01-01]
    elif st.session_state.page_state in ['f_page', 's_page', 'g_page', 'd_page']:
        tier_data = {
            'f_page': {'color': '#00ff00', 'name': 'FREE', 'dur': '8s'},
            's_page': {'color': '#bdc3c7', 'name': 'SILVER', 'dur': '20s'},
            'g_page': {'color': '#f1c40f', 'name': 'GOLD', 'dur': '60s'},
            'd_page': {'color': '#9b59b6', 'name': 'DIAMOND', 'dur': '120s'}
        }
        current = tier_data[st.session_state.page_state]
        
        # UI Heading
        st.markdown(f"<h1 style='color:{current['color']}; text-shadow: 0 0 15px {current['color']};'>VIDEO GENERATOR - {current['name']}</h1>", unsafe_allow_html=True)
        
        # Side-to-Side Layout [cite: 2026-01-01]
        c_main, c_side = st.columns([3, 1])
        with c_main:
            prompt = st.text_area("WRITE YOUR SCRIPT", height=250, placeholder="Enter prompt...")
            if st.button(f" START {current['name']} GENERATE", use_container_width=True):
                with st.container():
                    st.markdown('<div class="scanner">Processing...</div>', unsafe_allow_html=True)
                    time.sleep(3) # Scanner Effect Duration
            st.success(f"Video ({current['dur']}) is being generated!")
        with c_side:
            st.selectbox("Resolution", ["720p", "1080p", "4K"])
            st.info(f"Max Duration: {current['dur']}")
            if st.button(" BACK"): 
                st.session_state.page_state = 'home'; st.rerun()

ai_empire_terminal()

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
