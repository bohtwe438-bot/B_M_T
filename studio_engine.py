import streamlit as st
import time
from datetime import datetime, timedelta
import streamlit.components.v1 as components

# --- Button တုန်ခါမှုနှင့် အသံအတွက် JavaScript ---
def add_button_feedback():
    components.html("""
        <script>
        const playFeedback = () => {
            // Vibration (Mobile အတွက်)
            if (window.navigator.vibrate) window.navigator.vibrate(50);
            // Click Sound (Audio Context သုံးပြီး ထုတ်ခြင်း)
            const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            const oscillator = audioCtx.createOscillator();
            const gainNode = audioCtx.createGain();
            oscillator.connect(gainNode);
            gainNode.connect(audioCtx.destination);
            oscillator.type = 'sine';
            oscillator.frequency.setValueAtTime(400, audioCtx.currentTime);
            gainNode.gain.setValueAtTime(0.1, audioCtx.currentTime);
            oscillator.start();
            oscillator.stop(audioCtx.currentTime + 0.05);
        };
        // Button အားလုံးကို နားထောင်ပြီး Feedback ပေးခြင်း
        parent.document.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', playFeedback);
        });
        </script>
    """, height=0)

def run_video_studio(curr):
    add_button_feedback() # အသံနှင့် တုန်ခါမှုစတင်ခြင်း

    if 'studio_view' not in st.session_state:
        st.session_state.studio_view = 'input_page'
    if 'video_gallery' not in st.session_state:
        st.session_state.video_gallery = []

    # --- 48hr Auto-Delete Logic ---
    now = datetime.now()
    st.session_state.video_gallery = [
        vid for vid in st.session_state.video_gallery 
        if now - vid.get('timestamp', now) < timedelta(hours=48)
    ]

    view = st.session_state.studio_view
    if view == 'input_page':
        show_input_page(curr)
    elif view == 'rendering_page':
        show_rendering_page(curr)
    elif view == 'gallery_page':
        display_gallery(curr)

def show_input_page(curr):
    st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']}; text-align:center;'>BMT STUDIO PRO</h1>", unsafe_allow_html=True)
    
    col_space, col_gal = st.columns([0.8, 0.2])
    with col_gal:
        # Tier အလိုက် Glow ဖြစ်နေမည့် Button
        if st.markdown(f'<style>div.stButton > button {{ border: 2px solid {curr["c"]} !important; box-shadow: 0 0 10px {curr["c"]}; }}</style>', unsafe_allow_html=True): pass
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

def show_rendering_page(curr):
    st.empty() 
    st.markdown("""
        <div style="background: rgba(255,255,255,0.05); border: 2px dashed #3b82f6; padding: 60px; border-radius: 20px; text-align: center; margin-bottom: 40px;">
            <h2 style="color: #3b82f6; margin: 0;">ADVERTISING SPACE</h2>
            <p style="color: #666;">Google Ads Script Loading...</p>
        </div>
    """, unsafe_allow_html=True)

    duration_val = st.session_state.get('selected_duration', "5s")
    wait_time = 60 if any(x in duration_val for x in ["60s", "90s", "120s"]) else 30

    prog_container = st.container()
    with prog_container:
        prog_text = st.empty()
        prog_bar = st.progress(0)
        for percent in range(101):
            time.sleep(wait_time / 100)
            prog_text.markdown(f"<h1 style='color:{curr['c']}; text-align:center; font-size:70px; text-shadow: 0 0 15px {curr['c']};'>{percent}%</h1>", unsafe_allow_html=True)
            prog_bar.progress(percent)

    # ဗီဒီယိုဒေတာသိမ်းချိန်တွင် Timestamp ပါ တစ်ခါတည်းထည့်မည်
    new_video = {
        "id": len(st.session_state.video_gallery)+1, 
        "prompt": st.session_state.current_prompt,
        "timestamp": datetime.now()
    }
    st.session_state.video_gallery.insert(0, new_video)
    st.session_state.studio_view = 'gallery_page'
    st.rerun()

def display_gallery(curr):
    st.markdown(f"<h1 style='color:{curr['c']}; text-align:center;'>🎞 YOUR COLLECTION</h1>", unsafe_allow_html=True)
    
    # ၄၈ နာရီ အသိပေးချက်
    st.markdown(f"""
        <div style="background: rgba(255,0,0,0.1); border: 1px solid red; padding: 10px; border-radius: 10px; text-align: center; color: #ff4b4b; margin-bottom: 20px;">
            ⚠️ Videos are automatically deleted after 48 hours.
        </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.video_gallery:
        st.info("No videos found.")
    else:
        for idx, vid in enumerate(st.session_state.video_gallery):
            with st.container():
                v_col, m_col = st.columns([0.85, 0.15])
                with v_col:
                    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
                    st.caption(f"Prompt: {vid['prompt'][:50]}...")
                
                with m_col:
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

def chat_interface():
    st.markdown("<h1 style='text-align:center;'>BMT AI CHAT</h1>", unsafe_allow_html=True)
    if st.button("⬅️ BACK TO HOME"):
        st.session_state.page_state = 'home'
        st.rerun()
    st.chat_input("မေးမြန်းလိုသည်များကို ရိုက်ထည့်ပါ...")
