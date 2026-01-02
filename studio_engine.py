import streamlit as st
import time
from datetime import datetime, timedelta
import streamlit.components.v1 as components

# --- Button တုန်ခါမှုနှင့် အသံအတွက် JavaScript ---
def add_button_feedback():
    components.html("""
        <script>
        const playFeedback = () => {
            if (window.navigator.vibrate) window.navigator.vibrate(50);
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
        parent.document.querySelectorAll('button').forEach(btn => {
            btn.addEventListener('click', playFeedback);
        });
        </script>
    """, height=0)

# --- [ဖြည့်စွက်ချက်] MESSENGER CHAT INTERFACE ---
def chat_interface():
    st.markdown("<h2 style='text-align:center; color:#00ff00;'>💬 BMT AI MESSENGER</h2>", unsafe_allow_html=True)
    
    # Home ပြန်ရန် ခလုတ်
    if st.button("⬅️ BACK TO HOME", use_container_width=True):
        st.session_state.page_state = 'home'
        st.rerun()
    
    st.divider()

    # Chat History သိမ်းဆည်းရန်
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Messenger ပုံစံ Chat Bubbles များ ပြသခြင်း
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            # Assistant ထံမှ အဖြေဖြစ်ပါက Copy ယူရန် code block ထည့်ပေးခြင်း
            if message["role"] == "assistant":
                st.code(message["content"], language=None)

    # စာရိုက်သည့်နေရာ (Messenger Input)
    if prompt := st.chat_input("BMT AI ကို တစ်ခုခု မေးမြန်းပါ..."):
        # User Message ကို အရင်ပြသပြီး သိမ်းဆည်းသည်
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Response (Owner ၏ LLM API နှင့် ဤနေရာတွင် ချိတ်ဆက်နိုင်သည်)
        with st.chat_message("assistant"):
            response_placeholder = st.empty()
            full_response = f"BMT AI မှ အဖြေ: {prompt} နှင့် ပတ်သက်၍ နားလည်ပါပြီ။" # ဥပမာ စာသား
            
            # စာရိုက်နေသည့် ပုံစံ (Typing effect)
            temp_resp = ""
            for chunk in full_response.split():
                temp_resp += chunk + " "
                time.sleep(0.05)
                response_placeholder.markdown(temp_resp + "▌")
            
            response_placeholder.markdown(full_response)
            st.code(full_response, language=None) # Copy ခလုတ်အတွက်
            
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# --- မူရင်း VIDEO STUDIO CODE များ (မပြောင်းလဲပါ) ---
def run_video_studio(curr):
    add_button_feedback() 

    if 'studio_view' not in st.session_state:
        st.session_state.studio_view = 'input_page'
    if 'video_gallery' not in st.session_state:
        st.session_state.video_gallery = []

    # 48hr Auto-Delete
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
    st.markdown(f"<h2 style='color:{curr['c']}; text-shadow: 0 0 15px {curr['c']}; text-align:center; margin-bottom:0;'>BMT STUDIO PRO</h2>", unsafe_allow_html=True)
    
    st.markdown(f"<div style='color:{curr['c']}; font-size:0.7rem; font-weight:bold; margin-top:10px; margin-bottom:5px;'>🔥 EXPLORE AI TRENDS</div>", unsafe_allow_html=True)
    f_col1, f_col2, f_col3 = st.columns(3)
    features = [
        {"icon": "🎄", "label": "Christmas"},
        {"icon": "❄️", "label": "Snowy AI"},
        {"icon": "🎆", "label": "2026 Art"}
    ]
    for i, f in enumerate(features):
        with [f_col1, f_col2, f_col3][i]:
            st.markdown(f"""
                <div style="background:rgba(255,255,255,0.05); padding:8px; border-radius:10px; text-align:center; border:1px solid {curr['c']}33;">
                    <div style="font-size:1.2rem;">{f['icon']}</div>
                    <div style="font-size:0.6rem; color:white;">{f['label']}</div>
                </div>
            """, unsafe_allow_html=True)

    st.write("")
    c1, c2, c3 = st.columns(3)
    with c1: duration = st.selectbox("⏱ Time", curr.get('d_list', ["5s", "8s"]))
    with c2: ratio = st.selectbox("📐 Ratio", ["16:9", "9:16", "1:1"])
    with c3: resolution = st.selectbox("📺 Res", curr.get('res', ["480p", "720p"]))

    prompt = st.text_area("DESCRIBE YOUR VISION", placeholder="Enter your idea here...", height=120)
    
    if st.button(f"🚀 START {curr['n']} GENERATE", use_container_width=True):
        if prompt:
            st.session_state.selected_duration = duration
            st.session_state.current_prompt = prompt
            st.session_state.studio_view = 'rendering_page'
            st.rerun()
        else:
            st.warning("Prompt စာသား ထည့်ပေးပါ!")

    col_back, col_gal = st.columns(2)
    with col_gal:
        if st.button("🎞 MY GALLERY", use_container_width=True):
            st.session_state.studio_view = 'gallery_page'
            st.rerun()
    with col_back:
        if st.button("⬅️ SELECTION", use_container_width=True):
            st.session_state.page_state = 'tier_selection'
            st.rerun()

def show_rendering_page(curr):
    st.markdown(f"<h3 style='color:{curr['c']}; text-align:center;'>AI GENERATING...</h3>", unsafe_allow_html=True)
    st.markdown("""<div style="background: rgba(255,255,255,0.03); border: 1px dashed #444; padding: 40px; border-radius: 15px; text-align: center; margin-bottom: 20px;"><p style="color: #888; font-size: 0.8rem;">BMT AI Sponsorship Space</p></div>""", unsafe_allow_html=True)

    duration_val = st.session_state.get('selected_duration', "5s")
    wait_time = 30 if "s" in duration_val else 60 

    prog_container = st.container()
    with prog_container:
        prog_text = st.empty()
        prog_bar = st.progress(0)
        for percent in range(101):
            time.sleep(wait_time / 100)
            prog_text.markdown(f"<h1 style='color:{curr['c']}; text-align:center; font-size:60px; text-shadow: 0 0 15px {curr['c']};'>{percent}%</h1>", unsafe_allow_html=True)
            prog_bar.progress(percent)

    new_video = {
        "id": len(st.session_state.video_gallery)+1, 
        "prompt": st.session_state.current_prompt,
        "timestamp": datetime.now()
    }
    st.session_state.video_gallery.insert(0, new_video)
    st.session_state.studio_view = 'gallery_page'
    st.rerun()

def display_gallery(curr):
    st.markdown(f"<h2 style='color:{curr['c']}; text-align:center;'>🎞 COLLECTION</h2>", unsafe_allow_html=True)
    st.info("⚠️ Videos are deleted after 48 hours.")
    
    if not st.session_state.video_gallery:
        st.write("No videos yet.")
    else:
        for idx, vid in enumerate(st.session_state.video_gallery):
            with st.container():
                st.video("https://www.w3schools.com/html/mov_bbb.mp4")
                v_info, v_menu = st.columns([0.85, 0.15])
                with v_info:
                    st.caption(f"📝 {vid['prompt'][:50]}...")
                with v_menu:
                    with st.expander("⋮", expanded=False):
                        if st.button("🗑 Del", key=f"del_{idx}", use_container_width=True):
                            st.session_state.video_gallery.pop(idx)
                            st.rerun()
                        st.button("📥 Get", key=f"dl_{idx}", use_container_width=True)
                        st.button("🔗 Sh", key=f"sh_{idx}", use_container_width=True)
                st.divider()

    if st.button("➕ CREATE NEW", use_container_width=True):
        st.session_state.studio_view = 'input_page'
        st.rerun()
