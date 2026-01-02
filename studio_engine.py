import streamlit as st
import time

def run_video_studio(curr):
    # Studio Title
    st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']};'>VIDEO STUDIO - {curr['n']}</h1>", unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])

    # --- Sidebar Settings ---
    with col_side:
        st.markdown(f"<h3 style='color:{curr['c']}'>⚙️ SETTINGS</h3>", unsafe_allow_html=True)
        
        # Duration Select
        duration = st.selectbox("⏱ DURATION", curr.get('d_list', ["5s", "8s"]))
        
        # Resolution Select (ဒီနေရာမှာ 480p ကနေ 4k အထိ ပေါ်လာပါမယ်)
        res_list = curr.get('res', ["480p", "720p"]) # Config ထဲကအတိုင်း ယူမယ်
        resolution = st.selectbox("📺 RESOLUTION", res_list)
        
        # Ratio အလှဆင်ခြင်း
        st.markdown(f"<p style='color:{curr['c']}; font-weight:bold; margin-top:15px;'>📐 ASPECT RATIO</p>", unsafe_allow_html=True)
        aspect_ratio = st.radio("", ["16:9 (Wide)", "9:16 (TikTok)", "1:1 (Square)"], horizontal=True)

    # --- Main Workspace ---
    with col_main:
        if st.session_state.get('generating'):
            show_rendering_animation(curr, duration)
        elif st.session_state.get('video_done'):
            show_video_preview(curr)
        else:
            st.markdown(f"<h3 style='color:{curr['c']}'>Write Your Script</h3>", unsafe_allow_html=True)
            prompt = st.text_area("DESCRIBE YOUR VIDEO", height=200, placeholder="Enter your prompt here...")
            
            if st.button(f"🚀 START {curr['n']} GENERATE", use_container_width=True):
                st.session_state.generating = True
                st.rerun()

    # Back Button
    st.divider()
    if st.button("⬅️ BACK TO SELECTION", use_container_width=True):
        if 'video_done' in st.session_state: del st.session_state.video_done
        st.session_state.page_state = 'tier_selection'
        st.rerun()

def show_rendering_animation(curr, duration):
    wait_time = 60 if ("60s" in str(duration)) else 30
    prog_text = st.empty()
    prog_bar = st.empty()
    for percent in range(101):
        time.sleep(wait_time / 100)
        prog_text.markdown(f"<h1 style='color:{curr['c']}; text-align:center;'>{percent}%</h1>", unsafe_allow_html=True)
        prog_bar.progress(percent)
    st.session_state.generating = False
    st.session_state.video_done = True
    st.rerun()

def show_video_preview(curr):
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    if st.button("CREATE ANOTHER ONE", use_container_width=True):
        del st.session_state.video_done
        st.rerun()

def chat_interface():
    st.title("BMT AI CHAT")
    if st.button("BACK"): st.session_state.page_state = 'home'; st.rerun()
