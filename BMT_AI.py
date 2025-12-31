import streamlit as st

# ၁။ Page Config
st.set_page_config(page_title="BMT", page_icon="", layout="wide")

# စာမျက်နှာ ကူးပြောင်းမှု ထိန်းသိမ်းရန်
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'video_history' not in st.session_state:
    st.session_state.video_history = []

# ၂။ Clean UI Styling
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .bmt-title {
        font-size: 70px; font-weight: 900; text-align: center;
        background: linear-gradient(180deg, #ffffff 0%, #3b82f6 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        letter-spacing: 10px; margin-bottom: 20px;
    }
    .glass-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- ပင်မစာမျက်နှာ ---
if st.session_state.page == 'home':
    st.markdown('<h1 class="bmt-title">BMT</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div class="glass-box" style="border-top: 5px solid #00d2ff;">', unsafe_allow_html=True)
        st.header(" AI CHAT")
        if st.button("OPEN CHAT", use_container_width=True, key="btn_chat"):
            switch_page('chat')
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-box" style="border-top: 5px solid #ec4899;">', unsafe_allow_html=True)
        st.header(" VIDEO GEN")
        if st.button("OPEN VIDEO TOOL", use_container_width=True, key="btn_video"):
            switch_page('video')
        st.markdown('</div>', unsafe_allow_html=True)

# --- AI Chat စာမျက်နှာ ---
elif st.session_state.page == 'chat':
    if st.button(" BACK TO HOME", key="back_h"): switch_page('home')
    st.title(" BMT AI CHAT")
    st.write("---")
    st.info("Key ရလျှင် ဤနေရာတွင် စကားပြောနိုင်ပါပြီ။")
    st.chat_input("Ask BMT anything...")

# --- Video Generator စာမျက်နှာ ---
elif st.session_state.page == 'video':
    if st.button(" BACK TO HOME", key="back_v"): switch_page('home')
    st.title(" BMT VIDEO STUDIO")
    
    # Tab စနစ်ကို Error ကင်းအောင် သေချာပြန်စီစဉ်ထားသည်
    tab1, tab2 = st.tabs([" Create Video", " My Gallery"])
    
    with tab1:
        c1, c2 = st.columns([2, 1])
        with c1:
            script_text = st.text_area("Video Script ရေးသားရန်", height=200, placeholder="ဥပမာ- 9:16 Video အတွက် Script ရေးပါ...")
        with c2:
            ratio = st.radio("Ratio ရွေးချယ်ပါ", ["9:16", "16:9", "1:1"])
            voice = st.selectbox("အသံရွေးချယ်ရန်", ["Male", "Female"])
            if st.button(" GENERATE", use_container_width=True):
                if script_text:
                    st.success("Video ထုတ်လုပ်နေပါပြီ...")
                    st.session_state.video_history.append({"ratio": ratio, "text": script_text[:20]})
                else:
                    st.error("စာအရင်ရေးပါ!")

    with tab2:
        st.subheader("Your Videos")
        if not st.session_state.video_history:
            st.write("ဗီဒီယိုများ မရှိသေးပါ။")
        else:
            for item in st.session_state.video_history:
                st.write(f" Ratio: {item['ratio']} | {item['text']}...")
