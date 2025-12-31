import streamlit as st
import time

# ၁။ Page Setup & Theme
st.set_page_config(page_title="BMT", page_icon="🤖", layout="wide")

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'video_history' not in st.session_state:
    st.session_state.video_history = []

# ၂။ Advanced UI Styling
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .bmt-title {
        font-size: 80px; font-weight: 900; text-align: center;
        background: linear-gradient(180deg, #ffffff 0%, #3b82f6 100%);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        letter-spacing: 15px; margin-bottom: 30px;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 30px; border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
    }
    div.stButton > button {
        border-radius: 12px; font-weight: bold; transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

def switch_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- Page 1: Home ---
if st.session_state.page == 'home':
    st.markdown('<h1 class="bmt-title">BMT</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div class="glass-card" style="border-top: 5px solid #00d2ff;">', unsafe_allow_html=True)
        st.header("💬 AI CHAT")
        st.write("Smart Conversation & Assistance")
        if st.button("OPEN CHAT", use_container_width=True): switch_page('chat')
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="glass-card" style="border-top: 5px solid #ec4899;">', unsafe_allow_html=True)
        st.header("🎥 VIDEO GEN")
        st.write("Create Professional AI Videos")
        if st.button("OPEN VIDEO TOOL", use_container_width=True): switch_page('video')
        st.markdown('</div>', unsafe_allow_html=True)

# --- Page 2: Chat ---
elif st.session_state.page == 'chat':
    if st.button("⬅️ HOME"): switch_page('home')
    st.title("💬 BMT AI CHAT")
    st.info("Key ရလျှင် ဤနေရာတွင် AI နှင့် တိုက်ရိုက်စကားပြောနိုင်ပါပြီ။")
    st.chat_input("Ask BMT anything...")

# --- Page 3: Video (Ratio, Voice, Gallery အကုန်ပါဝင်သည်) ---
elif st.session_state.page == 'video':
    if st.button("⬅️ HOME"): switch_page('home')
    st.title("🎥 BMT VIDEO STUDIO")
    
    tab1, tab2 = st.tabs(["🎬 Create Video", "📁 My Gallery"])
    
    with tab1:
        col_left, col_right = st.columns([2, 1])
        with col_left:
            st.markdown("### 📝 Script & Magic")
            script = st.text_area("ဗီဒီယိုအကြောင်းအရာ ရေးပါ", height=200)
            if st.button("🪄 AI Magic (Auto-Enhance Script)"):
                st.write("✨ Script ကို AI က ပိုကောင်းအောင် ပြင်ဆင်ပေးနေသည်...")
        
        with col_right:
            st.markdown("### ⚙️ Settings")
            ratio = st.selectbox("Aspect Ratio (အချိုးအစား)", ["9:16 (Portrait)", "16:9 (Landscape)", "1:1 (Square)"])
            voice = st.selectbox("AI Voice (အသံရွေးချယ်ရန်)", ["မြန်မာသံ (အမျိုးသား)", "မြန်မာသံ (အမျိုးသမီး)", "English (Premium)"])
            style = st.select_slider("Quality Style", options=["Fast", "Balanced", "High-End"])
            
            if st.button("🚀 GENERATE NOW", use_container_width=True):
                if script:
                    progress_text = "Video Generating... Please wait."
                    my_bar = st.progress(0, text=progress_text)
                    for percent_complete in range(100):
                        time.sleep(0.01)
                        my_bar.progress(percent_complete + 1, text=progress_text)
                    st.success(f"✅ Video {ratio} ဖြင့် အောင်မြင်စွာ ထုတ်လုပ်ပြီးပါပြီ!")
                    st.session_state.video_history.append({"date": time.ctime(), "ratio": ratio})
                else:
                    st.error("Script အရင်ရေးပေးပါ Founder!")

with tab2:
        st.markdown("### 📁 Your Generated Videos")
        if not st.session_state.video_history:
            st.write("ထုတ်ထားသော ဗီဒီယို မရှိသေးပါ။")
        else:
            for vid in st.session_state.video_history:
                st.markdown(f"""
                <div class="glass-card" style="margin-bottom: 10px;">
                    📅 {vid['date']} | 📐 Ratio: {vid['ratio']} <br>
                    <button style="margin-top: 10px;">⬇️ Download Video</button>
                </div>
                """, unsafe_allow_html=True)
