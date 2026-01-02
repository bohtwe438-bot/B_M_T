import streamlit as st
import time

def run_video_studio(curr):
    # Studio အတွက် View State ကို စစ်ဆေးခြင်း
    if 'studio_view' not in st.session_state:
        st.session_state.studio_view = 'input_page'
    if 'video_gallery' not in st.session_state:
        st.session_state.video_gallery = []

    view = st.session_state.studio_view

    if view == 'input_page':
        show_input_page(curr)
    elif view == 'rendering_page':
        show_rendering_page(curr)
    elif view == 'gallery_page':
        display_gallery(curr)

# --- (၁) စာရိုက်သည့် စာမျက်နှာ ---
def show_input_page(curr):
    st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']}; text-align:center;'>BMT STUDIO PRO</h1>", unsafe_allow_html=True)
    
    col_space, col_gal = st.columns([0.8, 0.2])
    with col_gal:
        if st.button("🎞 MY GALLERY", use_container_width=True):
            st.session_state.studio_view = 'gallery_page'
            st.rerun()

    with st.expander("🛠 VIDEO SETTINGS", expanded=True):
        c1, c2, c3 = st.columns(3)
        duration = c1.selectbox("⏱ DURATION", curr.get('d_list', ["5s", "30s", "60s", "120s"]))
        resolution = c2.selectbox("📺 QUALITY", curr.get('res', ["1080p", "4K"]))
        ratio = c3.selectbox("📐 RATIO", ["16:9", "9:16", "1:1"])

    prompt = st.text_area("DESCRIBE YOUR VISION", height=200)
    
    if st.button(f"🚀 START {curr['n']} GENERATE", use_container_width=True):
        st.session_state.selected_duration = duration
        st.session_state.current_prompt = prompt
        st.session_state.studio_view = 'rendering_page'
        st.rerun()

    if st.button("⬅️ BACK TO SELECTION"):
        st.session_state.page_state = 'tier_selection'
        st.rerun()

# --- (၂) Rendering Page (စာမျက်နှာအသစ် - ကြော်ငြာ + % ပြရန်) ---
def show_rendering_page(curr):
    # Screen တစ်ခုလုံးကို ရှင်းထုတ်ပြီး အသစ်ပြခြင်း
    st.empty() 
    
    # အပေါ်ပိုင်း - Google Ads Space
    st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border: 2px dashed #3b82f6; padding: 60px; border-radius: 20px; text-align: center; margin-bottom: 40px;">
            <h2 style="color: #3b82f6; margin: 0;">ADVERTISING SPACE</h2>
            <p style="color: #666;">Google Ads Script Loading...</p>
        </div>
    """, unsafe_allow_html=True)

    # Rendering Time Logic
    duration_val = st.session_state.get('selected_duration', "5s")
    wait_time = 60 if any(x in duration_val for x in ["60s", "90s", "120s"]) else 30

    prog_container = st.container()
    with prog_container:
        prog_text = st.empty()
        prog_bar = st.progress(0)
        for percent in range(101):
            time.sleep(wait_time / 100)
            prog_text.markdown(f"<h1 style='color:{curr['c']}; text-align:center; font-size:70px;'>{percent}%</h1>", unsafe_allow_html=True)
            prog_bar.progress(percent)

    # ဗီဒီယိုဒေတာကို Gallery ထဲထည့်ခြင်း (Simulated)
    new_video = {"id": len(st.session_state.video_gallery)+1, "prompt": st.session_state.current_prompt}
    st.session_state.video_gallery.insert(0, new_video) # Y-axis အတိုင်း အသစ်ကို ထိပ်ဆုံးမှာထားမယ်

    st.session_state.studio_view = 'gallery_page'
    st.rerun()

# --- (၃) Gallery စာမျက်နှာ (Y-axis အတိုင်း စီထားခြင်း + 3-Dot Menu) ---
def display_gallery(curr):
    st.markdown(f"<h1 style='color:{curr['c']}; text-align:center;'>🎞 YOUR COLLECTION</h1>", unsafe_allow_html=True)
    
    if not st.session_state.video_gallery:
        st.info("No videos found.")
    else:
        for idx, vid in enumerate(st.session_state.video_gallery):
            with st.container():
                # ကတ်ပြားပုံစံ ဗီဒီယိုပြကွက်
                v_col, m_col = st.columns([0.85, 0.15])
                with v_col:
                    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
                    st.caption(f"Prompt: {vid['prompt'][:50]}...")
                
                with m_col:
                    # 3-Dot Menu ကို Expander ဖြင့် အလှဆင်ခြင်း
                    with st.expander("⋮"):
                        if st.button("🗑 Delete", key=f"del_{idx}"):
                            st.session_state.video_gallery.pop(idx)
                            st.rerun()
                        st.button("📥 Get", key=f"dl_{idx}")
                        st.button("🔗 Share", key=f"sh_{idx}")
                st.divider()

    if st.button("➕ CREATE NEW VIDEO", use_container_width=True):
        st.session_state.studio_view = 'input_page'
        st.rerun()

# --- (၄) AI Chat Interface (မူရင်းမပျောက်စေရန်) ---
def chat_interface():
    st.markdown("<h1 style='text-align:center;'>BMT AI CHAT</h1>", unsafe_allow_html=True)
    if st.button("⬅️ BACK TO HOME"):
        st.session_state.page_state = 'home'
        st.rerun()
    st.chat_input("မေးမြန်းလိုသည်များကို ရိုက်ထည့်ပါ...")
