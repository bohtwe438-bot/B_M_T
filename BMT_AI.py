import streamlit as st

# ၁။ Page Config
st.set_page_config(page_title="BMT", page_icon="🤖", layout="wide")

# Session State ကို သုံးပြီး စာမျက်နှာ ကူးပြောင်းမှုကို ထိန်းချုပ်မယ်
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- CSS Styling ---
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    
    /* Home Page Buttons */
    div.stButton > button.home-btn {
        height: 150px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 20px;
        border: none;
        transition: 0.5s;
    }
    
    /* Back Button Style */
    div.stButton > button.back-btn {
        background-color: transparent;
        color: #94a3b8;
        border: 1px solid #334155;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Functions for Pages ---

def go_home():
    st.session_state.page = 'home'

def go_chat():
    st.session_state.page = 'chat'

def go_video():
    st.session_state.page = 'video'

# --- Page Logic ---

# ၁။ Home Page (ပင်မစာမျက်နှာ)
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center; font-size: 80px; letter-spacing: 10px;'>BMT</h1>", unsafe_allow_html=True)
    st.write("<br><br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%); padding: 40px; border-radius: 30px; text-align: center;">
                <h2>💬 SMART CHAT</h2>
                <p>AI နှင့် စကားပြောရန်</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("OPEN CHAT ROOM", use_container_width=True, key="home_chat"):
            go_chat()
            st.rerun()

    with col2:
        st.markdown("""
            <div style="background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%); padding: 40px; border-radius: 30px; text-align: center;">
                <h2>🎥 VIDEO GEN</h2>
                <p>ဗီဒီယိုများ ဖန်တီးရန်</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("OPEN VIDEO TOOLS", use_container_width=True, key="home_video"):
            go_video()
            st.rerun()

# ၂။ AI Chat Page (စာမျက်နှာအသစ်)
elif st.session_state.page == 'chat':
    if st.button("⬅️ BACK TO HOME", key="back_home"):
        go_home()
        st.rerun()
        
    st.markdown("<h1 style='color: #06b6d4;'>💬 BMT AI CHAT</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Chat UI (ဒီနေရာမှာ အလှတစ်မျိုး ပြင်ဆင်မယ်)
    with st.container():
        st.markdown('<div style="background: rgba(6, 182, 212, 0.1); padding: 20px; border-radius: 15px; border-left: 5px solid #06b6d4;">'
                    'AI: မင်္ဂလာပါ Founder! ဘာကူညီပေးရမလဲ?</div>', unsafe_allow_html=True)
        st.write("<br>", unsafe_allow_html=True)
        st.text_input("မေးခွန်းရိုက်ပါ...", key="chat_input_page")

# ၃။ Video Generator Page (စာမျက်နှာအသစ်)
elif st.session_state.page == 'video':
    if st.button("⬅️ BACK TO HOME", key="back_home_v"):
        go_home()
        st.rerun()
        
    st.markdown("<h1 style='color: #ec4899;'>🎥 BMT VIDEO GENERATOR</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Video UI (ဒီနေရာမှာ နောက်ထပ် အလှတစ်မျိုး ပြင်ဆင်မယ်)
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.text_area("Video Script ရေးသားရန်", height=200, placeholder="ဥပမာ- သဘာဝအလှအပအကြောင်း...")
    with col_b:
        st.selectbox("Video Style ရွေးချယ်ပါ", ["Cinematic", "Anime", "3D Render", "Realism"])
        st.button("GENERATE NOW ✨", use_container_width=True)
