import streamlit as st

def apply_bmt_style():
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}
        .stApp {
            background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
            background-size: 200% 200%;
            animation: spaceMove 15s ease-in-out infinite;
            color: #e2e8f0; font-family: 'Inter', sans-serif;
        }
        @keyframes spaceMove { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
        .bmt-title {
            font-size: clamp(35px, 8vw, 85px); font-weight: 900; text-align: center;
            background: linear-gradient(to bottom, #ffffff 40%, #3b82f6 100%);
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 15px rgba(59, 130, 246, 0.6));
            letter-spacing: clamp(5px, 2vw, 15px); margin: 20px 0 5px 0; text-transform: uppercase;
        }
        .bmt-sub { text-align: center; font-size: clamp(12px, 2vw, 18px); color: #60a5fa; letter-spacing: 5px; margin-bottom: 50px; text-transform: uppercase; opacity: 0.8; }
        .glass-card {
            background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(15px);
            padding: 30px; border-radius: 25px; border: 1px solid rgba(59, 130, 246, 0.2);
            text-align: center; margin-bottom: 15px; transition: 0.4s;
        }
        .tier-tag { color: #facc15; font-weight: 800; border: 1px solid #facc15; padding: 6px 15px; border-radius: 10px; display: inline-block; margin-top: 15px; font-size: 0.85rem; }
        </style>
    """, unsafe_allow_html=True)
