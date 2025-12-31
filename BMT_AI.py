Bo Htwe, [12/31/2025 8:33 AM]
import streamlit as st
from groq import Groq

# ၁။ Page Setup
st.set_page_config(page_title="BMT", page_icon="", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'video_history' not in st.session_state:
    st.session_state.video_history = []

# ၂။ Custom CSS (Billion Level Design)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .bmt-title { font-size: 80px; font-weight: 900; text-align: center; color: #3b82f6; letter-spacing: 15px; margin-bottom: 20px; }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px; border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    div.stButton > button {
        border-radius: 12px; font-weight: bold; height: 50px; background-color: #3b82f6; color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Navigation
def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- ပင်မစာမျက်နှာ ---
if st.session_state.page == 'home':
    st.markdown('<h1 class="bmt-title">BMT</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>Myanmar's First Professional AI Engine</p>", unsafe_allow_html=True)
    st.write("---")
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.header(" FREE CHAT")
        st.write("BMT AI နှင့် အကန့်အသတ်မရှိ အခမဲ့ စကားပြောပါ။")
        if st.button("OPEN CHAT", use_container_width=True, key="h_chat"): switch_page('chat')
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.header(" VIDEO STUDIO")
        st.write("Professional AI Video များ ဖန်တီးပါ။ (F/S/G/D)")
        if st.button("OPEN STUDIO", use_container_width=True, key="h_video"): switch_page('video')
        st.markdown('</div>', unsafe_allow_html=True)

# --- Phase 1: AI Chat (BMT Personality) ---
elif st.session_state.page == 'chat':
    if st.button(" BACK TO HOME"): switch_page('home')
    st.title(" BMT FREE CHAT")
    st.write("---")

    if "GROQ_API_KEY" in st.secrets:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])

        if prompt := st.chat_input("BMT AI ကို တစ်ခုခု မေးမြန်းပါ..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)

            system_setup = """
            You are 'BMT AI Chat'. 
            Always identify yourself as 'ကျွန်တော်က BMT AI Chat ပါ' when asked who you are.
            Speak friendly and professional Myanmar language.
            Your mission is to help Myanmar people for free with chat and video scripts.
            """
            chat_completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "system", "content": system_setup}] + st.session_state.messages
            )
            response = chat_completion.choices[0].message.content
            with st.chat_message("assistant"): st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.info(" Founder ရေ... Key ထည့်ပြီးတာနဲ့ ဒီ Chat က အသက်ဝင်ပါပြီ။")

# --- Phase 2: Video Studio (Tiers ခွဲခြားခြင်း) ---
elif st.session_state.page == 'video':
    if st.button(" BACK TO HOME"): switch_page('home')
    st.title(" BMT VIDEO STUDIO")
    st.write("---")
    
    tab1, tab2 = st.tabs([" Create Video", " Gallery"])

Bo Htwe, [12/31/2025 8:33 AM]
with tab1:
        col_l, col_r = st.columns([2, 1])
        with col_l:
            st.markdown("###  Video Script")
            script = st.text_area("ဗီဒီယိုအကြောင်းအရာ ရေးသားပါ", height=250, placeholder="Chat မှ ရလာသော Script ကို ဤနေရာတွင် ထည့်ပါ...")
            if st.button(" AI MAGIC (Enhance Script)"):
                st.write(" Gold/Diamond Plan အတွက် Script ကို အချောကိုင်ပေးနေသည်...")
        
        with col_r:
            st.markdown("###  Configurations")
            tier = st.selectbox("Select Plan", ["F (Free)", "S (Silver)", "G (Gold)", "D (Diamond)"])
            
            # Tier အလိုက် Resolution ကန့်သတ်ချက်
            res_options = ["720p"]
            if tier == "S (Silver)": res_options = ["1080p (Full HD)"]
            elif tier == "G (Gold)": res_options = ["1080p", "2K"]
            elif tier == "D (Diamond)": res_options = ["1080p", "2K", "4K (Ultra HD)"]
            
            res = st.selectbox("Resolution", res_options)
            ratio = st.radio("Aspect Ratio", ["9:16 (Portrait)", "16:9 (Landscape)", "1:1 (Square)"])
            
            if st.button(" GENERATE VIDEO", use_container_width=True):
                if script:
                    st.success(f" {tier} Plan ဖြင့် {res} Video ထုတ်လုပ်နေပါပြီ!")
                    st.session_state.video_history.append({"tier": tier, "res": res, "ratio": ratio})
                else:
                    st.error("Script အရင်ရေးပေးပါ Founder!")

    with tab2:
        st.subheader("Your AI Creations")
        if not st.session_state.video_history:
            st.write("ထုတ်လုပ်ထားသော ဗီဒီယို မရှိသေးပါ။")
        else:
            for vid in st.session_state.video_history:
                st.markdown(f"""
                <div class="glass-card">
                     Plan: {vid['tier']} |  Res: {vid['res']} |  Ratio: {vid['ratio']} <br>
                    <button style="margin-top:10px; padding:5px 15px; border-radius:8px;">Download Video</button>
                </div>
                """, unsafe_allow_html=True)
