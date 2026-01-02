import streamlit as st
import time

def run_video_studio(curr):
    # View State ကို စစ်ဆေးပြီး စာမျက်နှာခွဲခြားခြင်း
    current_view = st.session_state.get('studio_view', 'input_page')

    if current_view == 'input_page':
        show_input_page(curr)
    elif current_view == 'rendering_page':
        show_rendering_page(curr)
    elif current_view == 'gallery_page':
        display_gallery(curr)

# --- (၁) စာရိုက်သည့် စာမျက်နှာ (Settings မပါဘဲ Clean ဖြစ်အောင် လုပ်ထားသည်) ---
def show_input_page(curr):
    st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']}; text-align:center;'>CREATE MASTERPIECE</h1>", unsafe_allow_html=True)
    
    # Gallery Button ကို သီးသန့် အပေါ်မှာ ထားသည်
    col_space, col_gal = st.columns([0.8, 0.2])
    with col_gal:
        if st.button("🎞 MY GALLERY", use_container_width=True):
            st.session_state.studio_view = 'gallery_page'
            st.rerun()

    # Video Settings များကို Input Page မှာပဲ တစ်ခါတည်း ရွေးခိုင်းမည်
    with st.expander("🛠 VIDEO CONFIGURATION", expanded=True):
        c1, c2, c3 = st.columns(3)
        duration = c1.selectbox("⏱ LENGTH", curr.get('d_list', ["5s", "30s", "60s", "120s"]))
        resolution = c2.selectbox("📺 QUALITY", curr.get('res', ["1080p", "4K"]))
        ratio = c3.selectbox("📐 RATIO", ["16:9", "9:16", "1:1"])

    prompt = st.text_area("DESCRIBE YOUR VISION...", height=300, placeholder="Enter your script here...")
    
    if st.button(f"🔥 START {curr['n']} GENERATE", use_container_width=True):
        st.session_state.selected_duration = duration # ကြာချိန်ကို မှတ်ထားရန်
        st.session_state.studio_view = 'rendering_page'
        st.rerun()

    if st.button("⬅️ BACK TO TIERS"):
        st.session_state.page_state = 'tier_selection'
        st.rerun()

# --- (၂) Rendering Page (Google Ads + Progress Bar) ---
def show_rendering_page(curr):
    # Screen ကို နှစ်ပိုင်းခွဲခြင်း
    # အပေါ်ပိုင်း - Google Ads Placeholder
    st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border: 2px dashed #3b82f6; padding: 40px; border-radius: 20px; text-align: center; margin-bottom: 30px;">
            <h2 style="color: #3b82f6; margin: 0;">GOOGLE ADS SPACE</h2>
            <p style="color: #666;">Ad script will be injected here</p>
        </div>
    """, unsafe_allow_html=True)

    # အောက်ပိုင်း - Progress UI
    duration_val = st.session_state.get('selected_duration', "5s")
    
    # ကြာချိန်သတ်မှတ်ချက် (User logic အတိုင်း)
    # 5s to 30s -> Wait 30s | 60s to 120s -> Wait 60s
    if any(x in duration_val for x in ["5s", "8s", "10s", "20s", "30s"]):
        wait_time = 30
    else:
        wait_time = 60

    prog_text = st.empty()
    prog_bar = st.progress(0)

    for percent in range(101):
        time.sleep(wait_time / 100)
        prog_text.markdown(f"""
            <div style="text-align: center;">
                <h1 style="color: {curr['c']}; font-size: 50px; margin: 0;">{percent}%</h1>
                <p style="letter-spacing: 5px; color: {curr['c']}; opacity: 0.7;">AI RENDERING IN PROGRESS</p>
            </div>
        """, unsafe_allow_html=True)
        prog_bar.progress(percent)

    # Rendering ပြီးလျှင် Gallery သို့ တန်းသွားမည်
    st.session_state.studio_view = 'gallery_page'
    st.rerun()

# --- (၃) Gallery စာမျက်နှာ ---
def display_gallery(curr):
    st.markdown(f"<h1 style='color:{curr['c']}; text-align:center;'>🎞 VIDEO GALLERY</h1>", unsafe_allow_html=True)
    
    # ဗီဒီယို ထွက်လာသည့်ပုံစံ (နမူနာ)
    st.success("✅ Your video has been generated and saved!")
    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
    
    col1, col2 = st.columns(2)
    if col1.button("🔄 CREATE ANOTHER"):
        st.session_state.studio_view = 'input_page'
        st.rerun()
    if col2.button("📥 DOWNLOAD VIDEO"):
        st.toast("Downloading...")

    if st.button("⬅️ BACK TO STUDIO"):
        st.session_state.studio_view = 'input_page'
        st.rerun()

def chat_interface():
    st.markdown("<h1 style='text-align:center;'>BMT AI CHAT</h1>", unsafe_allow_html=True)
    if st.button("⬅️ BACK TO EMPIRE"):
        st.session_state.page_state = 'home'
        st.rerun()
    st.chat_input("မေးမြန်းလိုသည်များကို ရိုက်ထည့်ပါ...")
