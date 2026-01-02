import streamlit as st
import time

# --- (၁) Video Studio ၏ ပင်မ UI နှင့် Logic ---
def run_video_studio(curr_tier_data):
    curr = curr_tier_data
    st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']};'>VIDEO STUDIO - {curr['n']}</h1>", unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])

    # Settings အပိုင်း (ညာဘက်ခြမ်း)
    with col_side:
        st.markdown(f"<h3 style='color:{curr['c']}'> SETTINGS</h3>", unsafe_allow_html=True)
        duration = st.selectbox(" DURATION", curr['d_list'])
        resolution = st.selectbox(" RESOLUTION", curr['res'])
        aspect_ratio = st.radio(" RATIO", ["16:9", "9:16", "1:1"])

    # Studio & Gallery အပိုင်း (ဘယ်ဘက်ခြမ်း)
    with col_main:
        if st.session_state.get('view') == 'gallery_page':
            display_gallery(curr)
        elif st.session_state.get('generating'):
            show_rendering_animation(curr, duration)
        elif st.session_state.get('video_done'):
            show_video_preview(curr)
        else:
            show_input_studio(curr)

# --- (၂) Video ဖန်တီးနေသည့် Animation ---
def show_rendering_animation(curr, duration):
    # Duration အလိုက် စောင့်ရမည့်အချိန် တွက်ချက်ခြင်း
    wait_time = 60 if ("60s" in str(duration) or "min" in str(duration)) else 30
    
    prog_text = st.empty()
    prog_bar = st.empty()

    for percent in range(101):
        time.sleep(wait_time / 100)
        ad_msg = "UPGRADE FOR 4K QUALITY" if percent < 50 else "ENJOY AD-FREE EXPERIENCE"
        prog_text.markdown(f"""
            <div style="text-align: center;">
                <h1 style="color: {curr['c']}; font-size: 75px; font-weight: 900; margin: 0;">{percent}%</h1>
                <p style="color: #888; letter-spacing: 5px;">RENDERING VIDEO...</p>
                <p style="color: {curr['c']};">{ad_msg}</p>
            </div>
        """, unsafe_allow_html=True)
        prog_bar.progress(percent)

    st.session_state.generating = False
    st.session_state.video_done = True
    st.rerun()

# --- (၃) Video Preview ပြသခြင်း ---
def show_video_preview(curr):
    st.markdown(f"<h3 style='color:{curr['c']}; text-align:center;'> PREVIEW SUCCESS</h3>", unsafe_allow_html=True)
    st.video("https://www.w3schools.com/html/mov_bbb.mp4") # နမူနာဗီဒီယို
    
    col_dl, col_sh = st.columns(2)
    col_dl.button(" DOWNLOAD VIDEO", use_container_width=True)
    col_sh.button(" SHARE VIDEO", use_container_width=True)

    if st.button(" BACK TO CREATE", use_container_width=True):
        if 'video_done' in st.session_state:
            del st.session_state.video_done
        st.rerun()

# --- (၄) Input စာရိုက်သည့် Studio ---
def show_input_studio(curr):
    h_col1, h_col2 = st.columns([0.6, 0.4])
    with h_col1:
        st.markdown(f"<h3 style='color:{curr['c']}'>Write Your Script Below</h3>", unsafe_allow_html=True)
    with h_col2:
        if st.button(" MY GALLERY", use_container_width=True):
            st.session_state.view = 'gallery_page'
            st.rerun()

    prompt = st.text_area("DESCRIBE YOUR VIDEO", height=200, placeholder="Enter your prompt here...")
    
    if st.button(f" START {curr['n']} GENERATE", use_container_width=True):
        st.session_state.generating = True
        st.rerun()

# --- (၅) Gallery ပြသခြင်း ---
def display_gallery(curr):
    st.markdown(f"<h2 style='color:{curr['c']}; text-align:center;'>🎞 VIDEO GALLERY</h2>", unsafe_allow_html=True)
    if not st.session_state.get('video_history'):
        st.info("No videos in gallery yet.")
    
    if st.button(" BACK TO STUDIO", use_container_width=True):
        st.session_state.view = 'studio'
        st.rerun()

# --- (၆) AI Chat Logic ---
def chat_interface():
    st.markdown("<h1 style='text-align:center;'>BMT AI CHAT</h1>", unsafe_allow_html=True)
    if st.button(" BACK TO EMPIRE"):
        st.session_state.page_state = 'home'
        st.rerun()
    st.chat_input("မေးမြန်းလိုသည်များကို ရိုက်ထည့်ပါ...")
