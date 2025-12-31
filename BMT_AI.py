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
    st.markdown('<h1 class="bmt-title">BMT</h1>', unsafe_allow_html=True)
    st.markdown("<p class='bmt-sub'>AI CHAT & VIDEO GENERATOR</p>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs([" AI Chat", " Video Studio", " Gallery"])

    # --- AI CHAT ---
    with tab1:
        if st.session_state.api_keys["groq"]:
            client = Groq(api_key=st.session_state.api_keys["groq"])
            for msg in st.session_state.messages:
                with st.chat_message(msg["role"]): st.markdown(msg["content"])
            if prompt := st.chat_input("Ask BMT AI..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                chat_completion = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[{"role": "system", "content": "You are BMT AI. Speak Myanmar."}] + st.session_state.messages
                )
                response = chat_completion.choices[0].message.content
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.rerun()
        else:
            st.warning("Please enter Groq API Key in Sidebar (Owner Mode).")

    # --- VIDEO STUDIO ---
    with tab2:
        col_l, col_r = st.columns([2, 1])
        with col_l:
            script = st.text_area("Video Script", height=200)
        with col_r:
            tier = st.selectbox("Tier", ["F (Free)", "S (Silver)", "G (Gold)", "D (Diamond)"])
            # FSGD Rule Implementation [cite: 2025-12-31]
            durations = {"F (Free)": "8s", "S (Silver)": "12s", "G (Gold)": "60s", "D (Diamond)": "120s"}
            selected_dur = durations[tier]
            
            if st.button("GENERATE VIDEO"):
                if not st.session_state.is_owner and tier != "F (Free)":
                    st.error("Upgrade required for this tier!")
                else:
                    with st.status(f"BMT Rendering {selected_dur}..."):
                        time.sleep(3) # Logic for Video API goes here
                        st.success("Done!")
                        st.session_state.video_history.append({"tier": tier, "dur": selected_dur})

    # --- GALLERY ---
    with tab3:
        st.subheader("Your Gallery")
        for vid in st.session_state.video_history:
            st.write(f" {vid['tier']} Video - {vid['dur']}")

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
