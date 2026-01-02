import streamlit as st
import time

def run_video_studio(curr):
    # Studio Title with Glow
    st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']}; text-align:center;'>BMT STUDIO PRO</h1>", unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])

    # --- (၁) Sidebar Settings ---
    with col_side:
        st.markdown(f"<h3 style='color:{curr['c']}'>⚙️ SETTINGS</h3>", unsafe_allow_html=True)
        duration = st.selectbox("⏱ DURATION", curr.get('d_list', ["5s", "8s"]))
        res_list = curr.get('res', ["480p", "720p", "1080p", "2k", "4k"])
        resolution = st.selectbox("📺 RESOLUTION", res_list)
        
        # ထပ်တိုး - Video Style ရွေးချယ်မှု
        v_style = st.selectbox("🎨 VIDEO STYLE", ["Cinematic", "Realistic", "Anime", "3D Render", "Cyberpunk"])
        
        st.markdown(f"<p style='color:{curr['c']}; font-weight:bold; margin-top:15px;'>📐 ASPECT RATIO</p>", unsafe_allow_html=True)
        aspect_ratio = st.radio("", ["16:9 (Wide)", "9:16 (TikTok)", "1:1 (Square)"], horizontal=True)

    # --- (၂) Main Workspace ---
    with col_main:
        if st.session_state.get('view') == 'gallery_page':
            display_gallery(curr)
        elif st.session_state.get('generating'):
            show_rendering_animation(curr, duration)
        elif st.session_state.get('video_done'):
            show_video_preview(curr)
        else:
            # Header with Gallery Button
            h_col1, h_col2 = st.columns([0.7, 0.3])
            with h_col1:
                st.markdown(f"<h3 style='color:{curr['c']}'>AI Script Generator</h3>", unsafe_allow_html=True)
            with h_col2:
                if st.button("🎞 MY GALLERY", use_container_width=True):
                    st.session_state.view = 'gallery_page'
                    st.rerun()

            # ထပ်တိုး - Prompt Templates (စာရိုက်ရလွယ်ကူစေရန်)
            template = st.selectbox("💡 USE A TEMPLATE", ["Custom Prompt", "Epic War Scene", "Beautiful Nature Walk", "Futuristic Cityscape", "Cute Character Animation"])
            
            default_prompt = ""
            if template == "Epic War Scene": default_prompt = "A high-octane battle scene with dragons and magic, cinematic lighting, 8k resolution."
            elif template == "Beautiful Nature Walk": default_prompt = "Peaceful forest walk during autumn, golden sunlight filtering through trees."

            prompt = st.text_area("DESCRIBE YOUR VISION", value=default_prompt, height=200, placeholder="Describe your video here...")
            
            if st.button(f"🚀 START {curr['n']} GENERATE", use_container_width=True):
                st.session_state.generating = True
                st.rerun()

    # --- (၃) Back Button ---
    st.write("") 
    if st.button("⬅️ BACK TO SELECTION", use_container_width=True):
        if 'video_done' in st.session_state: del st.session_state.video_done
        st.session_state.view = 'studio'
        st.session_state.page_state = 'tier_selection'
        st.rerun()

# --- (၄) Rendering Animation (သင်မှာထားတဲ့အတိုင်း Free tier ဆိုရင် 8s) ---
def show_rendering_animation(curr, duration):
    # Free tier ကန့်သတ်ချက် (၈ စက္ကန့်)
    wait_time = 8 if curr['n'] == 'FREE' else 30
    prog_text = st.empty()
    prog_bar = st.empty()
    for percent in range(101):
        time.sleep(wait_time / 100)
        prog_text.markdown(f"<h1 style='color:{curr['c']}; text-align:center;'>{percent}%</h1><p style='text-align:center; letter-spacing:3px;'>AI IS CREATING MAGIC...</p>", unsafe_allow_html=True)
        prog_bar.progress(percent)
    st.session_state.generating = False
    st.session_state.video_done = True
    st.rerun()

# --- (၅) Video Preview with Download/Share ---
def show_video_preview(curr):
    st.markdown(f"<h3 style='color:{curr['c']}; text-align:center;'>🎉 PREVIEW READY</h3>", unsafe_allow_html=True)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📥 DOWNLOAD", use_container_width=True)
    with c2: st.button("🔗 SHARE", use_container_width=True)
    with c3:
        if st.button("🔄 RE-GENERATE", use_container_width=True):
            del st.session_state.video_done
            st.rerun()

def display_gallery(curr):
    st.markdown(f"<h2 style='color:{curr['c']}; text-align:center;'>🎞 VIDEO GALLERY</h2>", unsafe_allow_html=True)
    st.info("No videos saved yet. Your masterpieces will appear here!")
    if st.button("⬅️ BACK TO STUDIO", use_container_width=True):
        st.session_state.view = 'studio'
        st.rerun()

def chat_interface():
    st.markdown("<h1 style='text-align:center;'>BMT AI CHAT</h1>", unsafe_allow_html=True)
    if st.button("⬅️ BACK TO EMPIRE"):
        st.session_state.page_state = 'home'
        st.rerun()
    st.chat_input("မေးမြန်းလိုသည်များကို ရိုက်ထည့်ပါ...")
