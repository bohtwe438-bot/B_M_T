import streamlit as st
from groq import Groq

# ၁။ Page Setup & Session State (Data သိမ်းဆည်းရန်)
st.set_page_config(page_title="BMT", page_icon="🤖", layout="wide")

# App အတွင်း Data များ ပျောက်မသွားအောင် သိမ်းထားခြင်း
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'video_history' not in st.session_state:
    st.session_state.video_history = []

# ၂။ Custom CSS (Billion Level Design Styling)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .bmt-title { 
        font-size: 80px; font-weight: 900; text-align: center; 
        color: #3b82f6; letter-spacing: 15px; margin-bottom: 20px; 
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px; border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    div.stButton > button {
        border-radius: 12px; font-weight: bold; height: 50px; 
        background-color: #3b82f6; color: white; border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #2563eb; transform: scale(1.02);
    }
    </style>
    """, unsafe_allow_html=True)

# စာမျက်နှာ ကူးပြောင်းသည့် Function
def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- Page 1: Home (ပင်မစာမျက်နှာ) ---
if st.session_state.page == 'home':
    st.markdown('<h1 class="bmt-title">BMT</h1>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px; opacity: 0.8;'>Myanmar's First Professional AI Engine</p>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.header("💬 FREE CHAT")
        st.write("BMT AI နှင့် အကန့်အသတ်မရှိ အခမဲ့ စကားပြောပါ။")
        if st.button("OPEN CHAT", use_container_width=True, key="h_chat"): 
            switch_page('chat')
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.header("🎥 VIDEO STUDIO")
        st.write("Professional AI Video များ ဖန်တီးပါ။ (F/S/G/D)")
        if st.button("OPEN STUDIO", use_container_width=True, key="h_video"): 
            switch_page('video')
        st.markdown('</div>', unsafe_allow_html=True)

# --- Page 2: AI Chat (Phase 1 Identity) ---
elif st.session_state.page == 'chat':
    if st.button("⬅️ BACK TO HOME"): 
        switch_page('home')
    st.title("💬 BMT FREE CHAT")
    st.write("---")

    # API Key ရှိမရှိ စစ်ဆေးခြင်း
    if "GROQ_API_KEY" in st.secrets:
        client = Groq(api_key=st.secrets["GROQ_API_KEY"])
        
        # Chat History ပြသခြင်း
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]): 
                st.markdown(msg["content"])

        # User Input
        if prompt := st.chat_input("BMT AI ကို တစ်ခုခု မေးမြန်းပါ..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"): 
                st.markdown(prompt)

            # BMT Personality & Identity Setup
            system_setup = """
            You are 'BMT AI Chat'. 
            Always identify yourself as 'ကျွန်တော်က BMT AI Chat ပါ' when asked who you are.
            Speak friendly and professional Myanmar language.
            Your mission is to help Myanmar people for free with chat and video scripts.
            """
            
            chat_completion = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[{"role": "system", "content": system_setup}] + st.session_state.messages)
            response = chat_completion.choices[0].message.content
            with st.chat_message("assistant"): 
                st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.info("💡 Founder ရေ... Key ထည့်ပြီးတာနဲ့ ဒီ Chat က အသက်ဝင်ပါပြီ။")

# --- Page 3: Video Studio (Phase 2 Tiers) ---
elif st.session_state.page == 'video':
    if st.button("⬅️ BACK TO HOME"): 
        switch_page('home')
    st.title("🎥 BMT VIDEO STUDIO")
    st.write("---")
    
    tab1, tab2 = st.tabs(["🎬 Create Video", "📁 Gallery"])
    
    with tab1:
        col_l, col_r = st.columns([2, 1])
        with col_l:
            st.markdown("### 📝 Video Script")
            script = st.text_area("ဗီဒီယိုအကြောင်းအရာ ရေးသားပါ", height=250, placeholder="Chat မှ ရလာသော Script ကို ဤနေရာတွင် ထည့်ပါ...")
            if st.button("🪄 AI MAGIC (Enhance Script)"):
                st.info("✨ Gold/Diamond Plan အတွက် Script ကို အချောကိုင်ပေးနေသည်...")
        
        with col_r:
            st.markdown("### ⚙️ Configurations")
            tier = st.selectbox("Select Plan", ["F (Free)", "S (Silver)", "G (Gold)", "D (Diamond)"])
            
            # Plan အလိုက် Resolution ရွေးချယ်မှုများ
            res_options = ["720p"]
            if tier == "S (Silver)": res_options = ["1080p (Full HD)"]
            elif tier == "G (Gold)": res_options = ["1080p", "2K"]
            elif tier == "D (Diamond)": res_options = ["1080p", "2K", "4K (Ultra HD)"]
            
            res = st.selectbox("Resolution", res_options)
            ratio = st.radio("Aspect Ratio", ["9:16 (Portrait)", "16:9 (Landscape)", "1:1 (Square)"])
            
            if st.button("🚀 GENERATE VIDEO", use_container_width=True):
                if script:
                    st.success(f"✅ {tier} Plan ဖြင့် {res} Video ထုတ်လုပ်နေပါပြီ!")
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
                    🌟 Plan: {vid['tier']} | 📺 Res: {vid['res']} | 📐 Ratio: {vid['ratio']} <br>
                    <button style="margin-top:10px; padding:5px 15px; border-radius:8px; background:#1e293b; color:white; border:1px solid #3b82f6;">Download Video</button>
                </div>
                """, unsafe_allow_html=True)
import time # အပေါ်ဆုံးမှာ မပါသေးရင် ထည့်ပေးပါ

# ၁။ BMT Branding & Dot 3 Logic (UI အပေါ်ဆုံးမှာ ပေါ်ဖို့အတွက်)
def show_bmt_header():
    # FSGD Marquee စာတန်း
    st.markdown("""
        <div style="background: #1e293b; color: #fbbf24; padding: 10px; text-align: center; font-weight: bold; border-radius: 5px;">
             FSGD SYSTEM: Upgrade to S, G, or D for Ad-free & Longer Videos! 
        </div>
        """, unsafe_allow_html=True)
    
    # Dot 3 Menu (ညာဘက်အပေါ်ထောင့်)
    col_main, col_dot3 = st.columns([12, 1])
    with col_dot3:
        if st.button("", key="bmt_dot3_menu"):
            st.toast("Founder: BMT | Wallet: 0 Coins | Tier: F (Standard)", icon="")

# ၂။ ၃၀ စက္ကန့် Split-Screen Rendering Logic
def start_bmt_render_logic(tier_name):
    # အပေါ်အောက် ခွဲလိုက်ခြင်း
    ad_space = st.empty()
    progress_space = st.empty()

    # အပေါ်ပိုင်း - ၃၀ စက္ကန့် Ad
    with ad_space.container():
        st.markdown(f"""
            <div style="background: #0f172a; padding: 20px; border-radius: 15px; border: 2px solid #3b82f6; text-align: center; margin-bottom: 20px;">
                <h4 style="color: #3b82f6;"> BMT SPONSORED AD (30s)</h4>
                <div style="background: black; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 10px; border: 1px solid #1e293b;">
                    <p style="color: #64748b;">[ Video Ad Playing... Founder Profit Growing! ]</p>
                </div>
                <p style="font-size: 12px; color: gray; margin-top: 10px;">Rendering for {tier_name} User</p>
            </div>
        """, unsafe_allow_html=True)

    # အောက်ပိုင်း - ၁% မှ ၁၀၀% တက်မည့် Progress
    bmt_bar = progress_space.progress(0)
    bmt_status = st.empty()
    
    for i in range(100):
        time.sleep(0.3) # ၃၀ စက္ကန့် အတိအကျ (၀.၃ x ၁၀၀)
        bmt_bar.progress(i + 1)
        bmt_status.markdown(f"<p style='text-align: center; font-weight: bold;'>BMT Rendering: {i+1}%</p>", unsafe_allow_html=True)
    
    bmt_status.success(" Video Generated! (Max 8s for F-Tier)")
    time.sleep(1)
    ad_space.empty() # ပြီးသွားလျှင် Ad ကို ဖျက်မည်

# ၃။ Daily Limit & 48h Auto-Delete Warning
def check_bmt_limits():
    if 'daily_video_count' not in st.session_state:
        st.session_state.daily_video_count = 0
    
    # ၄၈ နာရီ ဖျက်မည့် သတိပေးချက်
    st.sidebar.warning(" Note: All generated videos will be auto-deleted after 48 hours to maintain server capacity.")
    
    return st.session_state.daily_video_count
import time

# --- ၁။ BMT Tier & Duration Logic (5s, 8s, 12s -> Upgrade) ---
def get_bmt_durations(tier):
    if tier == "F (Free)":
        return ["5s", "8s", "12s (Upgrade to S)"]
    elif tier == "S (Silver)":
        return ["12s", "15s", "20s"]
    elif tier == "G (Gold)":
        return ["30s", "1 min"]
    elif tier == "D (Diamond)":
        return ["30s", "1 min", "1:30 min", "2 min"]
    return ["5s"]

# --- ၂။ ၃၀ စက္ကန့် Split-Screen Ad & Render Logic ---
def bmt_split_render(selected_tier, selected_duration):
    # F-Tier မှာ 12s ကို နှိပ်ခဲ့ရင် Upgrade Page ခေါ်မည်
    if selected_tier == "F (Free)" and "Upgrade" in selected_duration:
        st.warning(" ၁၂ စက္ကန့် ဗီဒီယိုအတွက် Silver Tier သို့ Upgrade လုပ်ပေးပါ ဗိုလ်ချုပ်!")
        return False

    ad_space = st.empty()
    progress_space = st.empty()

    with ad_space.container():
        st.markdown(f"""
            <div style="background: #1e293b; padding: 20px; border-radius: 15px; border: 2px solid #3b82f6; text-align: center;">
                <h4 style="color: #3b82f6;"> BMT SPONSORED AD (30s)</h4>
                <div style="background: black; height: 180px; display: flex; align-items: center; justify-content: center; border-radius: 10px;">
                    <p style="color: #64748b;">[ Video Ad Playing... ]</p>
                </div>
                <p style="color: #60a5fa; font-size: 14px; margin-top: 10px;">Rendering {selected_duration} Video for {selected_tier}</p>
            </div>
        """, unsafe_allow_html=True)

    bar = progress_space.progress(0)
    status = st.empty()
    for i in range(100):
        time.sleep(0.3) # ၃၀ စက္ကန့် အတိအကျ
        bar.progress(i + 1)
        status.markdown(f"<p style='text-align: center;'>BMT Rendering: {i+1}%</p>", unsafe_allow_html=True)
    
    status.success(f" ဗီဒီယို ထုတ်လုပ်ပြီးပါပြီ! ({selected_duration})")
    time.sleep(1)
    ad_space.empty()
    return True

# --- ၃။ Gallery Dot 3 () Logic (Download, Share, Delete) ---
def bmt_gallery_card(vid_data, index):
    with st.container():
        st.markdown(f"""
            <div style="background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 15px; border: 1px solid #3b82f6; margin-bottom: 10px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <span> Video #{index+1} ({vid_data['duration']})</span>
                    <span style="color: #3b82f6; font-weight: bold;"></span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # Dot 3 Functions
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button(f" Download", key=f"dl_{index}"): st.toast("Downloading to phone...")
        with col2:
            if st.button(f" Share", key=f"sh_{index}"): st.toast("Link copied to clipboard!")
        with col3:
            if st.button(f" Delete", key=f"del_{index}"): st.toast("Video deleted!")

# --- ၄။ ၄၈ နာရီ Auto-Delete Warning ---
st.sidebar.info(" BMT Policy: Server Capacity ထိန်းသိမ်းရန် ဗီဒီယိုများကို ၄၈ နာရီအကြာတွင် အလိုလို ဖျက်သွားပါမည်။")
