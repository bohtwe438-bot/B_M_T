import streamlit as st
from groq import Groq
import time

# ==========================================
# ၁။ FOUNDER BMT - API KEYS
# ==========================================
GROQ_KEY = ""  # <-- INSERT GROQ KEY HERE
VOICE_KEY = "" # <-- INSERT VOICE/ELEVENLABS KEY HERE
VIDEO_KEY = "" # <-- INSERT VIDEO GENERATOR KEY HERE

# ==========================================
# ၂။ PAGE SETUP & SESSION STATE
# ==========================================
st.set_page_config(page_title="BMT", page_icon="", layout="wide")

if 'page' not in st.session_state: st.session_state.page = 'home'
if 'messages' not in st.session_state: st.session_state.messages = []
if 'video_history' not in st.session_state: st.session_state.video_history = []
if 'daily_count' not in st.session_state: st.session_state.daily_count = 0

# ==========================================
# ၃။ CUSTOM CSS (BMT Branding Only)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .bmt-title { 
        font-size: 80px; font-weight: 900; text-align: center; 
        color: #3b82f6; letter-spacing: 15px; margin-bottom: 10px; 
    }
    .bmt-sub { text-align: center; font-size: 18px; color: #60a5fa; margin-bottom: 30px; letter-spacing: 3px; }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px; border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    .marquee { background: #1e293b; color: #fbbf24; padding: 10px; font-weight: bold; text-align: center; border-radius: 5px; margin-bottom: 15px; }
    div.stButton > button {
        border-radius: 12px; font-weight: bold; height: 50px; 
        background-color: #3b82f6; color: white; border: none; transition: 0.3s;
    }
    div.stButton > button:hover { background-color: #2563eb; transform: scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# ==========================================
# ၄။ CORE BMT LOGIC
# ==========================================

def get_bmt_durations(tier):
    if tier == "F (Free)": return ["5s", "8s", "12s (Upgrade to S)"]
    elif tier == "S (Silver)": return ["12s", "15s", "20s"]
    elif tier == "G (Gold)": return ["30s", "1 min"]
    elif tier == "D (Diamond)": return ["30s", "1 min", "1:30 min", "2 min"]
    return ["5s"]

def start_bmt_master_render(selected_tier, selected_duration, script):
    if selected_tier == "F (Free)" and "Upgrade" in selected_duration:
        st.warning("၁၂ စက္ကန့် ဗီဒီယိုအတွက် Silver Tier သို့ Upgrade လုပ်ပေးပါ။")
        return False

    ad_space = st.empty()
    progress_space = st.empty()

    with ad_space.container():
        st.markdown(f"""
            <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 2px solid #3b82f6; text-align: center; margin-bottom: 20px;">
                <h4 style="color: #3b82f6;"> BMT SPONSORED AD (30s)</h4>
                <div style="background: black; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 10px;">
                    <p style="color: #64748b;">[ Video Ad Playing... ]</p>
                </div>
                <p style="font-size: 12px; color: gray; margin-top: 10px;">Rendering {selected_duration} for {selected_tier} User</p>
            </div>
        """, unsafe_allow_html=True)

    bar = progress_space.progress(0)
    status_text = st.empty()
    steps = ["Processing Script...", "Generating AI Voice (MM/EN)...", "Creating Visuals...", "Mixing Background Music..."]
    
    for i in range(100):
        time.sleep(0.3) 
        bar.progress(i + 1)
        step = steps[i // 25] if i // 25 < len(steps) else steps[-1]
        status_text.markdown(f"<p style='text-align: center;'><b>BMT Rendering: {i+1}%</b><br><small>{step}</small></p>", unsafe_allow_html=True)
    
    status_text.success(f" BMT AI Video Generated! ({selected_duration})")
    time.sleep(1)
    ad_space.empty()
    return True

# ==========================================
# ၅။ UI NAVIGATION
# ==========================================
st.markdown('<div class="marquee"> FSGD SYSTEM: F (Standard) | S (Silver) | G (Gold) | D (Diamond) - UPGRADE NOW! </div>', unsafe_allow_html=True)
col_head, col_dot3 = st.columns([12, 1])
with col_dot3:
    if st.button("", key="main_dot3"):
        st.toast("BMT Wallet: 0 | Tier: Standard", icon="")

# ==========================================
# ၆။ PAGES
# ==========================================

if st.session_state.page == 'home':
    st.markdown('<h1 class="bmt-title">BMT</h1>', unsafe_allow_html=True)
    st.markdown("<p class='bmt-sub'>AI CHAT & VIDEO GENERATOR</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown('<div class="glass-card"><h3> FREE CHAT</h3><p>BMT AI နှင့် အကန့်အသတ်မရှိ စကားပြောပါ။</p></div>', unsafe_allow_html=True)
        if st.button("OPEN CHAT", use_container_width=True): switch_page('chat')
    with col2:
        st.markdown('<div class="glass-card"><h3> VIDEO STUDIO</h3><p>Professional AI Video များ ဖန်တီးပါ။</p></div>', unsafe_allow_html=True)
        if st.button("OPEN STUDIO", use_container_width=True): switch_page('video')

elif st.session_state.page == 'chat':
    if st.button(" BACK"): switch_page('home')
    st.title(" BMT FREE CHAT")
    
    if GROQ_KEY:
        client = Groq(api_key=GROQ_KEY)
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): st.markdown(msg["content"])
        if prompt := st.chat_input("BMT AI ကို မေးမြန်းပါ..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): st.markdown(prompt)
            chat_completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "system", "content": "You are BMT AI Chat. Speak Myanmar."}] + st.session_state.messages
            )
            response = chat_completion.choices[0].message.content
            with st.chat_message("assistant"): st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.info(" Please insert Groq API Key.")

elif st.session_state.page == 'video':
    if st.button(" BACK"): switch_page('home')
    st.title(" BMT VIDEO STUDIO")
    
    tab1, tab2 = st.tabs([" Create Video", " Gallery"])
    
    with tab1:
        col_l, col_r = st.columns([2, 1])
        with col_l:
            script = st.text_area("ဗီဒီယိုအကြောင်းအရာ ရေးသားပါ", height=200, placeholder="Script ကို ဤနေရာတွင် ထည့်ပါ...")
            if st.button(" AI MAGIC"): st.info("Enhancing Script...")
        
        with col_r:
            tier = st.selectbox("Select Plan", ["F (Free)", "S (Silver)", "G (Gold)", "D (Diamond)"])
            duration = st.selectbox("Video Duration", get_bmt_durations(tier))
            ratio = st.radio("Aspect Ratio", ["9:16", "16:9", "1:1"])
            
            if st.button(" GENERATE VIDEO", use_container_width=True):
                if tier == "F (Free)" and st.session_state.daily_count >= 3:
                    st.error("တစ်ရက် ၃ ကြိမ် ပြည့်သွားပါပြီ!")
                elif script:
                    if start_bmt_master_render(tier, duration, script):
                        st.session_state.video_history.append({"tier": tier, "duration": duration, "ratio": ratio})
                        if tier == "F (Free)": st.session_state.daily_count += 1
                else: st.error("Script အရင်ရေးပေးပါ။")

    with tab2:
        st.subheader("Your BMT Gallery")
        if not st.session_state.video_history:
            st.write("ဗီဒီယို မရှိသေးပါ။")
        else:
            for idx, vid in enumerate(st.session_state.video_history):
                st.markdown(f"""
                <div class="glass-card">
                    <div style="display: flex; justify-content: space-between;">
                        <b>🎥 Video #{idx+1} ({vid['duration']})</b>
                        <span style="color: #3b82f6; font-weight: bold;">⋮</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                c1, c2, c3 = st.columns(3)
                with c1: 
                    if st.button(f"📥 Download", key=f"dl_{idx}"): st.toast("Saved!")
                with c2: 
                    if st.button(f"🔗 Share", key=f"sh_{idx}"): st.toast("Shared!")
                with c3: 
                    if st.button(f"🗑️ Delete", key=f"del_{idx}"): st.toast("Deleted!")

st.sidebar.warning("⚠️ Videos will be deleted after 48 hours.")
