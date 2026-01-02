import streamlit as st
import time
from datetime import datetime, timedelta
import streamlit.components.v1 as components
from database import get_api_key

# --- ၁။ Module Error မတက်အောင် Safe Import လုပ်ခြင်း ---
try:
    import google.generativeai as genai
    from groq import Groq
    HAS_LIBS = True
except ImportError:
    HAS_LIBS = False

# --- Button Feedback JavaScript (မူရင်းအတိုင်း) ---
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

# --- MESSENGER CHAT INTERFACE ---
def chat_interface():
    st.markdown("<h2 style='text-align:center; color:#00ff00;'>💬 BMT AI MESSENGER</h2>", unsafe_allow_html=True)
    api_key = get_api_key("2. LLM (Chat) API")
    
    if st.button("⬅️ BACK TO HOME", use_container_width=True):
        st.session_state.page_state = 'home'
        st.rerun()
    
    st.divider()

    if not HAS_LIBS:
        st.error("⚠️ Error: Library များ မသွင်းရသေးပါ။ Terminal တွင် 'pip install google-generativeai groq' ကို ရိုက်ထည့်ပေးပါ။")
        return

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("BMT AI ကို တစ်ခုခု မေးမြန်းပါ..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            if not api_key:
                st.error("Admin Panel မှာ Key အရင်ထည့်ပေးပါ Owner!")
                return
            
            response_placeholder = st.empty()
            try:
                if api_key.startswith("gsk_"):
                    client = Groq(api_key=api_key)
                    completion = client.chat.completions.create(
                        model="llama-3.3-70b-versatile",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    full_response = completion.choices[0].message.content
                else:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(prompt)
                    full_response = response.text

                # Typing Effect
                temp_resp = ""
                for chunk in full_response.split():
                    temp_resp += chunk + " "
                    time.sleep(0.03)
                    response_placeholder.markdown(temp_resp + "▌")
                response_placeholder.markdown(full_response)
                st.code(full_response, language=None)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"Error: {e}")

# --- VIDEO STUDIO CODE (Syntax Error များကို ပြင်ဆင်ပြီး) ---
def run_video_studio(curr):
    add_button_feedback()
    if 'studio_view' not in st.session_state:
        st.session_state.studio_view = 'input_page'
    if 'video_gallery' not in st.session_state:
        st.session_state.video_gallery = []

    now = datetime.now()
    st.session_state.video_gallery = [v for v in st.session_state.video_gallery if now - v.get('timestamp', now) < timedelta(hours=48)]

    if st.session_state.studio_view == 'input_page': show_input_page(curr)
    elif st.session_state.studio_view == 'rendering_page': show_rendering_page(curr)
    elif st.session_state.studio_view == 'gallery_page': display_gallery(curr)

def show_input_page(curr):
    st.markdown(f"<h2 style='color:{curr['c']}; text-align:center;'>BMT STUDIO PRO</h2>", unsafe_allow_html=True)
    
    f_col1, f_col2, f_col3 = st.columns(3)
    features = [{"icon": "🎄", "label": "Christmas"}, {"icon": "❄️", "label": "Snowy AI"}, {"icon": "🎆", "label": "2026 Art"}]
    for i, f in enumerate(features):
        with [f_col1, f_col2, f_col3][i]:
            st.markdown(f"<div style='background:rgba(255,255,255,0.05); padding:8px; border-radius:10px; text-align:center; border:1px solid {curr['c']}33;'>{f['icon']}<br><small>{f['label']}</small></div>", unsafe_allow_html=True)

    st.write("")
    c1, c2, c3 = st.columns(3)
    # Syntax Error ဖြစ်နေသော နေရာများကို ပြင်ဆင်ပြီး (ကွင်းစ ကွင်းပိတ် နှင့် စာလုံးပေါင်း)
    with c1: duration = st.selectbox("⏱ Time", curr.get('d_list', ["5s", "8s"]))
    with c2: ratio = st.selectbox("📐 Ratio", ["16:9", "9:16", "1:1"])
    with c3: resolution = st.selectbox("📺 Res", curr.get('res', ["480p", "720p"]))

    prompt = st.text_area("DESCRIBE YOUR VISION", placeholder="Enter idea...", height=120)
    
    if st.button(f"🚀 START GENERATE", use_container_width=True):
        if prompt:
            st.session_state.selected_duration = duration
            st.session_state.current_prompt = prompt
            st.session_state.studio_view = 'rendering_page'
            st.rerun()
        else: st.warning("Prompt ထည့်ပါ!")

    col_back, col_gal = st.columns(2)
    with col_gal:
        if st.button("🎞 MY GALLERY", use_container_width=True):
            st.session_state.studio_view = 'gallery_page'; st.rerun()
    with col_back:
        if st.button("⬅️ BACK", use_container_width=True):
            st.session_state.page_state = 'tier_selection'; st.rerun()

def show_rendering_page(curr):
    st.markdown(f"<h3 style='color:{curr['c']}; text-align:center;'>AI GENERATING...</h3>", unsafe_allow_html=True)
    prog_bar = st.progress(0)
    for p in range(101):
        time.sleep(0.1); prog_bar.progress(p)
    
    st.session_state.video_gallery.insert(0, {"id": len(st.session_state.video_gallery)+1, "prompt": st.session_state.current_prompt, "timestamp": datetime.now()})
    st.session_state.studio_view = 'gallery_page'; st.rerun()

def display_gallery(curr):
    st.markdown(f"<h2 style='color:{curr['c']}; text-align:center;'>🎞 COLLECTION</h2>", unsafe_allow_html=True)
    if not st.session_state.video_gallery: st.write("No videos yet.")
    else:
        for idx, vid in enumerate(st.session_state.video_gallery):
            st.video("https://www.w3schools.com/html/mov_bbb.mp4")
            if st.button(f"🗑 Del {idx}", use_container_width=True):
                st.session_state.video_gallery.pop(idx); st.rerun()
    if st.button("➕ CREATE NEW", use_container_width=True):
        st.session_state.studio_view = 'input_page'; st.rerun()
