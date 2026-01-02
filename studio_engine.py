import streamlit as st
import time

def run_video_studio(curr):
    # --- Ratio UI အတွက် Custom CSS ---
    st.markdown(f"""
        <style>
        /* Radio Button ကို ဖျောက်ပြီး Card ပုံစံပြောင်းခြင်း */
        div[data-testid="stMarkdownContainer"] > p {{ font-weight: bold; color: {curr['c']}; }}
        
        .ratio-container {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
        }}
        
        /* Streamlit Radio ကို horizontal ပြင်ခြင်း */
        div.row-widget.stRadio > div {{
            flex-direction: row !important;
            gap: 20px;
        }}

        div.row-widget.stRadio div[role="radiogroup"] {{
            background: rgba(255,255,255,0.05);
            padding: 15px;
            border-radius: 15px;
            border: 1px solid {curr['c']}33;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']};'>VIDEO STUDIO - {curr['n']}</h1>", unsafe_allow_html=True)
    
    col_main, col_side = st.columns([3, 1])

    with col_side:
        st.markdown(f"<h3 style='color:{curr['c']}'>⚙️ SETTINGS</h3>", unsafe_allow_html=True)
        
        duration = st.selectbox("⏱ DURATION", curr['d_list'])
        resolution = st.selectbox("📺 RESOLUTION", curr['res'])
        
        # Ratio ပိုင်းကို Icon လေးတွေနဲ့ အလှဆင်ခြင်း
        st.markdown(f"<p style='margin-bottom:-15px;'>📐 ASPECT RATIO</p>", unsafe_allow_html=True)
        aspect_ratio = st.radio("", 
            ["16:9 (Widescreen)", "9:16 (TikTok/Reels)", "1:1 (Square)"],
            horizontal=True
        )

    with col_main:
        if st.session_state.get('view') == 'gallery_page':
            display_gallery(curr)
        elif st.session_state.get('generating'):
            show_rendering_animation(curr, duration)
        elif st.session_state.get('video_done'):
            show_video_preview(curr)
        else:
            show_input_studio(curr)

    st.divider()
    if st.button("⬅️ BACK TO SELECTION", use_container_width=True):
        if 'video_done' in st.session_state: del st.session_state.video_done
        st.session_state.view = 'studio'
        st.session_state.page_state = 'tier_selection'
        st.rerun()
