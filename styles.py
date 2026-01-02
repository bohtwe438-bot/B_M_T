import streamlit as st
import streamlit.components.v1 as components

def apply_bmt_style():
    # ၁။ Button Feedback (တုန်ခါမှုနှင့် အသံ) အတွက် JavaScript Logic
    components.html("""
        <script>
        const playBMTFeedback = () => {
            // Vibration (Mobile အတွက်)
            if (window.navigator.vibrate) window.navigator.vibrate(40);
            
            // Synthetic Click Sound
            const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            osc.type = 'sine';
            osc.frequency.setValueAtTime(450, audioCtx.currentTime);
            gain.gain.setValueAtTime(0.05, audioCtx.currentTime);
            osc.start();
            osc.stop(audioCtx.currentTime + 0.04);
        };

        // Button အားလုံးကို Event ပတ်ခြင်း
        setInterval(() => {
            const buttons = parent.document.querySelectorAll('button');
            buttons.forEach(btn => {
                if (!btn.dataset.bmtListener) {
                    btn.addEventListener('click', playBMTFeedback);
                    btn.dataset.bmtListener = 'true';
                }
            });
        }, 500);
        </script>
    """, height=0)

    # ၂။ UI Styling Logic
    is_admin = st.session_state.get('is_owner', False)
    title_color = "linear-gradient(to bottom, #f1c40f 40%, #926600 100%)" if is_admin else "linear-gradient(to bottom, #ffffff 40%, #3b82f6 100%)"
    glow_color = "rgba(241, 196, 15, 0.6)" if is_admin else "rgba(59, 130, 246, 0.6)"
    accent = "#f1c40f" if is_admin else "#3b82f6"

    st.markdown(f"""
        <style>
        #MainMenu {{visibility: hidden;}} footer {{visibility: hidden;}} header {{visibility: hidden;}}
        .stApp {{
            background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
            background-size: 200% 200%;
            animation: spaceMove 15s ease-in-out infinite;
            color: #e2e8f0; font-family: 'Inter', sans-serif;
        }}
        @keyframes spaceMove {{ 0% {{ background-position: 0% 50%; }} 50% {{ background-position: 100% 50%; }} 100% {{ background-position: 0% 50%; }} }}
        
        /* Title Glow */
        .bmt-title {{
            font-size: clamp(35px, 8vw, 85px); font-weight: 900; text-align: center;
            background: {title_color};
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 15px {glow_color});
            letter-spacing: clamp(5px, 2vw, 15px); margin: 20px 0 5px 0; text-transform: uppercase;
        }}

        /* Button Neon Glow & Animation */
        .stButton>button {{
            width: 100%;
            border-radius: 12px;
            background: rgba(255, 255, 255, 0.05) !important;
            border: 1px solid {accent} !important;
            color: white !important;
            font-weight: bold;
            transition: all 0.3s ease;
            text-transform: uppercase;
            box-shadow: 0 0 5px {accent}44;
        }}
        .stButton>button:hover {{
            box-shadow: 0 0 15px {accent};
            background: {accent}22 !important;
            transform: translateY(-2px);
        }}
        .stButton>button:active {{
            transform: scale(0.95) !important;
        }}

        .stTabs [data-baseweb="tab-list"] {{ gap: 10px; }}
        .stTabs [data-baseweb="tab"] {{
            background-color: rgba(255,255,255,0.05); border-radius: 10px 10px 0 0;
            padding: 10px 20px; color: {accent};
        }}
        .bmt-sub {{ text-align: center; font-size: clamp(12px, 2vw, 18px); color: #60a5fa; letter-spacing: 5px; margin-bottom: 50px; text-transform: uppercase; opacity: 0.8; }}
        .glass-card {{
            background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px);
            padding: 30px; border-radius: 25px; border: 1px solid rgba(59, 130, 246, 0.2);
            text-align: center; margin-bottom: 15px; transition: 0.4s;
        }}
        .tier-tag {{ color: #facc15; font-weight: 800; border: 1px solid #facc15; padding: 6px 15px; border-radius: 10px; display: inline-block; margin-top: 15px; font-size: 0.85rem; }}
        </style>
    """, unsafe_allow_html=True)
