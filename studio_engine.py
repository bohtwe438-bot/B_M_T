import streamlit as st
import time

def run_video_studio(curr):
    # --- UI အလှဆင်ရန် Custom CSS ---
    st.markdown(f"""
        <style>
        /* Sidebar ကို Glassmorphism စတိုင်ပြောင်းခြင်း */
        [data-testid="stSidebar"] {{
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(10px);
            border-right: 1px solid {curr['c']}33;
        }}
        
        /* ခလုတ်များကို Neon Glow ထည့်ခြင်း */
        .stButton>button {{
            background: transparent;
            color: {curr['c']};
            border: 1px solid {curr['c']};
            border-radius: 12px;
            transition: 0.3s;
            text-transform: uppercase;
            font-weight: bold;
        }}
        .stButton>button:hover {{
            background: {curr['c']};
            color: #000;
            box-shadow: 0 0 20px {curr['c']};
        }}
        
        /* Card ပုံစံ စာရိုက်သည့်နေရာ */
        .stTextArea textarea {{
            background: rgba(255,255,255,0.03) !important;
            border: 1px solid {curr['c']}33 !important;
            color: #fff !important;
            border-radius: 15px;
        }}
        </style>
    """, unsafe_allow_html=True)

    # Studio Title with Neon Glow
    st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 25px {curr['c']}; text-align:center; font-size: 50px;'>BMT STUDIO PRO</h1>", unsafe_allow_html=True)
    
    # --- ဘယ်ဘက် Sidebar မှာ Settings ကို Icon လေးတွေနဲ့ ပြောင်းမယ် ---
    with st.sidebar:
        st.markdown(f"<h2 style='color:{curr['c']}'>🎥 CONTROL PANEL</h2>", unsafe_allow_html=True)
        st.divider()
        duration = st.select_slider("⏱ VIDEO LENGTH", options=curr.get('d_list', ["5s", "8s"]))
        resolution = st.selectbox("📺 QUALITY", curr.get('res', ["480p", "720p", "1080p", "2k", "4k"]))
        v_style = st.radio("🎨 ART STYLE", ["Cinematic", "Anime", "3D Render", "Cyberpunk"], horizontal=False)
        st.divider()
        st.markdown(f"<p style='color:{curr['c']}'>📐 ASPECT RATIO</p>", unsafe_allow_html=True)
        aspect_ratio = st.radio("", ["16:9", "9:16", "1:1"], horizontal=True)

    # --- Main Canvas ---
    if st.session_state.get('view') == 'gallery_page':
        display_gallery(curr)
    elif st.session_state.get('generating'):
        show_rendering_animation(curr, duration)
    elif st.session_state.get('video_done'):
        show_video_preview(curr)
    else:
        # Top Bar
        c1, c2 = st.columns([0.8, 0.2])
        with c1: st.markdown(f"<h4 style='color:#888;'>Ready to create your {v_style} masterpiece?</h4>", unsafe_allow_html=True)
        with c2: 
            if st.button("🎞 GALLERY"):
                st.session_state.view = 'gallery_page'
                st.rerun()

        # Prompt Input
        prompt = st.text_area("DESCRIBE YOUR VISION...", height=250, placeholder="Example: A futuristic soldier walking in a neon city...")
        
        # Action Button
        if st.button(f"🔥 START {curr['n']} RENDERING", use_container_width=True):
            st.session_state.generating = True
            st.rerun()

    # Back Button at Bottom
    if st.button("⬅️ EXIT STUDIO", use_container_width=True):
        st.session_state.page_state = 'tier_selection'
        st.rerun()

# --- Functions အဟောင်းများကို ဤနေရာတွင် ဆက်ထားပါ ---
def show_rendering_animation(curr, duration):
    wait_time = 8 if curr['n'] == 'FREE' else 30
    prog_text = st.empty()
    prog_bar = st.progress(0)
    for percent in range(101):
        time.sleep(wait_time / 100)
        prog_text.markdown(f"<h2 style='color:{curr['c']}; text-align:center;'>{percent}%</h2><p style='text-align:center;'>AI IS PAINTING YOUR VISION...</p>", unsafe_allow_html=True)
        prog_bar.progress(percent)
    st.session_state.generating = False
    st.session_state.video_done = True
    st.rerun()

def show_video_preview(curr):
    st.markdown(f"<h3 style='color:{curr['c']}; text-align:center;'>✨ CREATION COMPLETE ✨</h3>", unsafe_allow_html=True)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    c1, c2 = st.columns(2)
    with c1: st.button("📥 SAVE TO DEVICE", use_container_width=True)
    with c2: 
        if st.button("🔄 CREATE NEW", use_container_width=True):
            del st.session_state.video_done
            st.rerun()

def display_gallery(curr):
    st.markdown(f"<h2 style='color:{curr['c']}; text-align:center;'>🎞 YOUR COLLECTION</h2>", unsafe_allow_html=True)
    if st.button("⬅️ BACK TO WORKSPACE", use_container_width=True):
        st.session_state.view = 'studio'
        st.rerun()
