import streamlit as st
import time
from datetime import datetime, timedelta
import streamlit.components.v1 as components
from database import get_api_key
from ads_center import ads_manager

# --- ၁။ Module Safe Import ---
try:
    import google.generativeai as genai
    from groq import Groq
    from openai import OpenAI  
    HAS_LIBS = True
except ImportError:
    HAS_LIBS = False

# --- Button Feedback JavaScript ---
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
    st.markdown("""
        <style>
        .chat-header {
            text-align: center; padding: 12px; 
            background: linear-gradient(90deg, #FF4B2B, #FF416C); 
            color: white !important; border-radius: 12px; font-weight: bold; 
            font-size: 22px; margin-bottom: 25px;
        }
        .stChatMessage div p { color: #FFFFFF !important; }
        div[data-testid="stChatInput"] {
            border: 2px solid #FF416C !important;
            border-radius: 25px !important;
            margin-left: 45px !important;
            z-index: 9999 !important;
        }
        .back-btn-fixed { position: fixed; bottom: 35px; left: 10px; z-index: 10000; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="chat-header">AI CHAT</div>', unsafe_allow_html=True)

    st.markdown('<div class="back-btn-fixed">', unsafe_allow_html=True)
    if st.button("⬅️", key="chat_back_btn"):
        st.session_state.page_state = 'home'; st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    api_key = get_api_key("2. LLM (Chat) API")
    
    # --- [User Icon နေရာတွင် Owner ပေးသော BMT Logo အသုံးပြုခြင်း] ---
    # Forbidden Error ကင်းဝေးစေရန် တိုက်ရိုက် Link အဖြစ် ပြောင်းထားပါသည်
    USER_ICON = "https://raw.githubusercontent.com/BMT-AI-EMPIRE/Assets/main/BMT_Logo.png" 
    AI_ICON = "🤖"

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        avatar = USER_ICON if message["role"] == "user" else AI_ICON
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    if prompt := st.chat_input("BMT AI Chat ကို တစ်ခုခု မေးမြန်းပါ..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=USER_ICON):
            st.markdown(prompt)

        with st.chat_message("assistant", avatar=AI_ICON):
            if not api_key or api_key == "HIDDEN_KEY_XXXXX":
                st.error("Admin Panel မှာ Key အရင်ထည့်ပေးပါ Owner Bo!"); return
            
            response_placeholder = st.empty()
            try:
                system_instruction = "မင်းရဲ့အမည်က BMT AI Chat ဖြစ်ပါတယ်။ မင်းကို Bo ဆိုတဲ့သူက ဖန်တီးပေးထားတာပါ။"
                if api_key.startswith("sk-"):
                    client = OpenAI(api_key=api_key)
                    response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "system", "content": system_instruction}, {"role": "user", "content": prompt}])
                    full_response = response.choices[0].message.content
                elif api_key.startswith("gsk_"):
                    client = Groq(api_key=api_key)
                    completion = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[{"role": "system", "content": system_instruction}, {"role": "user", "content": prompt}])
                    full_response = completion.choices[0].message.content
                else:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    response = model.generate_content(f"{system_instruction}\n\nUser: {prompt}")
                    full_response = response.text

                temp_resp = ""
                for chunk in full_response.split():
                    temp_resp += chunk + " "
                    time.sleep(0.02); response_placeholder.markdown(temp_resp + "▌")
                response_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e: st.error(f"Error: {e}")

# --- Video Studio အပိုင်း ---
def run_video_studio(curr):
    add_button_feedback()
    if 'studio_view' not in st.session_state: st.session_state.studio_view = 'input_page'
    if 'video_gallery' not in st.session_state: st.session_state.video_gallery = []
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
    with c1: duration = st.selectbox("⏱ Time", curr.get('d_list', ["5s", "8s"]))
    with c2: ratio = st.selectbox("📐 Ratio", ["16:9", "9:16", "1:1"])
    with c3: resolution = st.selectbox("📺 Res", curr.get('res', ["480p", "720p"]))
    
    prompt = st.text_area("DESCRIBE YOUR VISION", placeholder="Enter idea...", height=120)
    
    if st.button(f"🚀 START GENERATE", use_container_width=True):
        if prompt:
            st.session_state.selected_duration = duration
            st.session_state.current_prompt = prompt
            st.session_state.studio_view = 'rendering_page'; st.rerun()
        else: st.warning("Prompt ထည့်ပါ!")
    
    col_back, col_gal = st.columns(2)
    with col_gal:
        if st.button("🎞 MY GALLERY", use_container_width=True):
            st.session_state.studio_view = 'gallery_page'; st.rerun()
    with col_back:
        if st.button("⬅️ BACK", use_container_width=True):
            st.session_state.page_state = 'tier_selection'; st.rerun()

def show_rendering_page(curr):
    st.markdown(f"""
        <style>
        .render-card-box {{
            background: rgba(255, 255, 255, 0.05); border: 2px solid {curr['c']};
            border-radius: 20px; padding: 40px; text-align: center;
            backdrop-filter: blur(20px); margin-top: 20px;
        }}
        .percent-text {{ font-size: 60px; font-weight: 900; color: {curr['c']}; text-shadow: 0 0 15px {curr['c']}; }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<p style='text-align:center; color:gray; font-size:10px;'>SPONSORED ADVERTISEMENT</p>", unsafe_allow_html=True)
    ads_manager()
    st.divider()

    st.markdown('<div class="render-card-box">', unsafe_allow_html=True)
    st.markdown(f"<h3 style='color:white;'>AI GENERATING...</h3>", unsafe_allow_html=True)
    
    sel_d = st.session_state.get('selected_duration', "5s").replace('s','')
    try: d_val = int(sel_d)
    except: d_val = 5
    
    wait_time = 30 if d_val <= 30 else 60 
    
    prog_bar = st.progress(0)
    percent_display = st.empty()
    
    step = wait_time / 100
    for p in range(101): 
        time.sleep(step)
        prog_bar.progress(p)
        percent_display.markdown(f'<p class="percent-text">{p}%</p>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
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
