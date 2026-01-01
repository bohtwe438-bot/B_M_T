import streamlit as st
from groq import Groq
import time

import streamlit as st

# ==========================================
# ၁။ အလှအပ (ULTRA-PREMIUM UI DESIGN)
# ==========================================
def apply_bmt_style():
    # Page Setting (Cloud အတွက် အကောင်းဆုံးဖြစ်အောင်)
    st.set_page_config(page_title="BMT AI EMPIRE", layout="wide", initial_sidebar_state="collapsed")
    
    st.markdown("""
        <style>
        /* Streamlit ၏ မလိုအပ်သော Header များကို ဖျောက်ခြင်း */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Deep Space Moving Background */
        .stApp {
            background: radial-gradient(circle at 50% 50%, #0f172a 0%, #020617 100%);
            background-size: 200% 200%;
            animation: spaceMove 15s ease-in-out infinite;
            color: #e2e8f0;
            font-family: 'Inter', sans-serif;
        }

        @keyframes spaceMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        /* Metallic BMT Title with Glow */
        .bmt-title {
            font-size: clamp(35px, 8vw, 85px);
            font-weight: 900;
            text-align: center;
            background: linear-gradient(to bottom, #ffffff 40%, #3b82f6 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 0 15px rgba(59, 130, 246, 0.6));
            letter-spacing: clamp(5px, 2vw, 15px);
            margin: 20px 0 5px 0;
            text-transform: uppercase;
        }

        .bmt-sub {
            text-align: center;
            font-size: clamp(12px, 2vw, 18px);
            color: #60a5fa;
            letter-spacing: 5px;
            margin-bottom: 50px;
            text-transform: uppercase;
            opacity: 0.8;
        }

        /* Glassmorphism Tier Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(15px);
            padding: 30px;
            border-radius: 25px;
            border: 1px solid rgba(59, 130, 246, 0.2);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-align: center;
            margin-bottom: 15px;
        }

        .glass-card:hover {
            transform: translateY(-10px) scale(1.02);
            border: 1px solid rgba(59, 130, 246, 0.6);
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.3);
        }

        /* Gold Tag for Limits */
        .tier-tag {
            color: #facc15;
            font-weight: 800;
            border: 1px solid #facc15;
            padding: 6px 15px;
            border_radius: 10px;
            display: inline-block;
            margin-top: 15px;
            font-size: 0.85rem;
            box-shadow: 0 0 10px rgba(250, 204, 21, 0.2);
        }

        /* Premium Buttons */
        div.stButton > button {
            background: rgba(59, 130, 246, 0.1);
            color: #3b82f6;
            border: 1px solid #3b82f6;
            border-radius: 15px;
            padding: 12px 20px;
            width: 100%;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: 0.3s;
        }

        div.stButton > button:hover {
            background: #3b82f6 !important;
            color: white !important;
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.5);
        }
        </style>
        """, unsafe_allow_html=True)

# ==========================================
# ၂။ APP MAIN INTERFACE
# ==========================================
def main():
    apply_bmt_style()

    # Branding
    st.markdown('<div class="bmt-title">BMT AI EMPIRE</div>', unsafe_allow_html=True)
    st.markdown('<div class="bmt-sub">The Future of AI Video Generation</div>', unsafe_allow_html=True)

    # Tier Selection Logic (စာလုံးနေရာမှန်အောင် ပြင်ဆင်ထားသည်)
    # col1, col2 ကို ၂ ခုပဲ ခွဲပြီး ၂ တန်း စီရင် ပိုလှပါတယ်
    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    tiers = [
        {"id": "FREE", "name": "FREE TIER", "limit": "8 SECONDS", "col": row1_col1},
        {"id": "SILVER", "name": "SILVER TIER", "limit": "30 SECONDS", "col": row1_col2},
        {"id": "GOLD", "name": "GOLD TIER", "limit": "60 SECONDS", "col": row2_col1},
        {"id": "DIAMOND", "name": "DIAMOND TIER", "limit": "UNLIMITED", "col": row2_col2}
    ]

    for t in tiers:
        with t["col"]:
            # Card ထဲက စာလုံးတွေကို အလယ်ဗဟိုကျအောင်နဲ့ မကျပ်အောင် ပြင်ထားသည်
            st.markdown(f"""
                <div class="glass-card">
                    <h3 style="margin-bottom: 10px; font-size: 1.5rem; letter-spacing: 2px;">{t['name']}</h3>
                    <p style="color: #94a3b8; font-size: 0.8rem; margin-bottom: 15px;">AI POWERED GENERATION</p>
                    <div class="tier-tag" style="font-size: 0.7rem; width: 100%;">{t['limit']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # ခလုတ်ကို ကတ်နဲ့ ကပ်မနေအောင် spacer လေး ခံပေးပါ
            st.write("") 
            if st.button(f"ENTER {t['id']}", key=t['id'], use_container_width=True):
                st.session_state.tier = t['id']
                st.toast(f"Welcome to {t['name']}!")

# ==========================================
# ၂။ ပိုင်ရှင် KEY များ (OWNER KEYS & API)
# ==========================================
def manage_owner_keys():
    # Initialize Keys in Session State
    if 'api_keys' not in st.session_state:
        st.session_state.api_keys = {"groq": "", "video": "", "voice": ""}
    if 'is_owner' not in st.session_state:
        st.session_state.is_owner = False

    with st.sidebar:
        st.header(" BMT Access")
        pwd = st.text_input("Owner Password", type="password")
        if pwd == "bmt999": # ဗိုလ်ချုပ် စိတ်ကြိုက်ပြောင်းနိုင်သည်
            st.session_state.is_owner = True
            st.markdown('<div class="owner-tag">OWNER VERIFIED </div>', unsafe_allow_html=True)
            st.divider()
            st.subheader(" API Configuration")
            st.session_state.api_keys["groq"] = st.text_input("Groq AI Key", value=st.session_state.api_keys["groq"], type="password")
            st.session_state.api_keys["video"] = st.text_input("Video Engine Key", value=st.session_state.api_keys["video"], type="password")
            st.session_state.api_keys["voice"] = st.text_input("Voice Key", value=st.session_state.api_keys["voice"], type="password")
        else:
            st.session_state.is_owner = False

# ==========================================
# ၃။ AI CHAT & VIDEO GENERATOR (CORE LOGIC)
# ==========================================
def ai_studio_module():
    # ၁။ စာမျက်နှာ အခြေအနေ မှတ်သားခြင်း [cite: 2026-01-01]
    if 'page_state' not in st.session_state:
        st.session_state.page_state = 'home'

    # --- CSS: Tier အလိုက် မတူညီသော အရောင်နှင့် Scanner Effect များ --- [cite: 2026-01-01]
    st.markdown("""
        <style>
        .stApp { background: #0a0e14; color: white; }
        /* Glassmorphism Buttons [cite: 2026-01-01] */
        div.stButton > button {
            border-radius: 12px; border: 1px solid rgba(255,255,255,0.1);
            background: rgba(255,255,255,0.05); backdrop-filter: blur(10px);
            font-weight: bold; transition: 0.3s;
        }
        /* Scanner Animation [cite: 2026-01-01] */
        @keyframes scan { 0% { top: 0; } 100% { top: 100%; } }
        .scanner-box { 
            position: relative; overflow: hidden; height: 60px; 
            border: 1px solid #00f2ff; background: rgba(0,242,255,0.05);
            display: flex; align-items: center; justify-content: center;
        }
        .scanner-line {
            position: absolute; width: 100%; height: 2px;
            background: #00f2ff; box-shadow: 0 0 15px #00f2ff;
            animation: scan 2s linear infinite;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- ၂။ HOME PAGE (SIDE-BY-SIDE RECTANGLE) --- [cite: 2026-01-01]
    if st.session_state.page_state == 'home':
        st.markdown("<div style='text-align:center; padding: 40px 0;'><h1 style='font-size:100px; letter-spacing:20px; margin:0;'>BMT</h1></div>", unsafe_allow_html=True)
        
        col_chat, col_vid = st.columns(2)
        with col_chat:
            if st.button("\n\nAI SMART CHAT", key="home_chat", use_container_width=True):
                st.session_state.page_state = 'chat_page'; st.rerun()
        with col_vid:
            if st.button("\n\nVIDEO GENERATOR", key="home_vid", use_container_width=True):
                st.session_state.page_state = 'tier_selection'; st.rerun()

    # --- ၃။ TIER SELECTION PAGE (F, S, G, D) --- [cite: 2026-01-01]
    elif st.session_state.page_state == 'tier_selection':
        st.markdown("<h2 style='text-align:center; padding: 20px;'>SELECT YOUR TIER</h2>", unsafe_allow_html=True)
        t1, t2, t3, t4 = st.columns(4)
        # ခလုတ်တစ်ခုစီတွင် မတူညီသော အရောင် Glow များ ထည့်သွင်းမည် [cite: 2026-01-01]
        if t1.button("F (FREE)"): st.session_state.page_state = 'f_page'; st.rerun()
        if t2.button("S (SILVER)"): st.session_state.page_state = 's_page'; st.rerun()
        if t3.button("G (GOLD)"): st.session_state.page_state = 'g_page'; st.rerun()
        if t4.button("D (DIAMOND)"): st.session_state.page_state = 'd_page'; st.rerun()
        if st.button(" BACK"): st.session_state.page_state = 'home'; st.rerun()

    # --- ၄။ INDIVIDUAL VIDEO PAGES (F, S, G, D) ---
    elif st.session_state.page_state in ['f_page', 's_page', 'g_page', 'd_page']:
        configs = {
            'f_page': {'bg': '#021202', 'c': '#00ff00', 'n': 'FREE', 'd_list': ["5s", "8s"], 'res': ["480p", "720p"]},
            's_page': {'bg': '#121212', 'c': '#bdc3c7', 'n': 'SILVER', 'd_list': ["10s", "20s"], 'res': ["720p", "1080p"]},
            'g_page': {'bg': '#141101', 'c': '#f1c40f', 'n': 'GOLD', 'd_list': ["30s", "60s"], 'res': ["1080p", "2k"]},
            'd_page': {'bg': '#0d0114', 'c': '#9b59b6', 'n': 'DIAMOND', 'd_list': ["30s", "60s", "90s", "120s"], 'res': ["1080p", "2k", "4k"]}
        }
        curr = configs[st.session_state.page_state]

        # Background CSS
        st.markdown(f"""
            <style>
            [data-testid="stAppViewContainer"] {{ background-color: {curr['bg']} !important; }}
            [data-testid="stHeader"] {{ background-color: rgba(0,0,0,0) !important; }}
            </style>
        """, unsafe_allow_html=True)

        # (က) အပေါ်ပိုင်း - GOOGLE ADS SECTION
        st.markdown(f'<div style="border:1px solid {curr["c"]}; border-radius:10px; padding:10px; margin-bottom:20px; background:rgba(0,0,0,0.3);">', unsafe_allow_html=True)
        
        ad_mode = 'long' if st.session_state.page_state == 'd_page' else 'short'
        ads_manager()
        
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(f"<h1 style='color:{curr['c']}; text-shadow: 0 0 20px {curr['c']};'>VIDEO STUDIO - {curr['n']}</h1>", unsafe_allow_html=True)
        
        col_main, col_side = st.columns([3, 1])


        # --- (၁) Sidebar Settings အပိုင်း (ညာဘက်ခြမ်း) ---
        with col_side:
            st.markdown(f"<h3 style='color:{curr['c']}'> SETTINGS</h3>", unsafe_allow_html=True)
            duration = st.selectbox(" DURATION", curr['d_list'])
            resolution = st.selectbox(" RESOLUTION", curr['res'])
            aspect_ratio = st.radio(" RATIO", ["16:9", "9:16", "1:1"])

        # --- (၂) & (ဂ) INTEGRATED STUDIO & GALLERY SYSTEM ---
        with col_main:
            # စာမျက်နှာ View နှင့် အခြေအနေများကို ထိန်းချုပ်ရန်
            if 'view' not in st.session_state: st.session_state.view = 'studio'
            if 'generating' not in st.session_state: st.session_state.generating = False
            if 'ad_done' not in st.session_state: st.session_state.ad_done = False

            # --- 🖼️ (ဂ) GALLERY VIEW MODE (စာမျက်နှာအသစ် လုံးဝပြောင်းသွားမည့်အပိုင်း) ---
            if st.session_state.view == 'gallery_page':
                gallery_page_container = st.empty()
                with gallery_page_container.container():
                    st.markdown(f"""
                        <div style="text-align: center; padding: 10px;">
                            <h2 style="color:{curr['c']}; text-shadow: 0 0 10px {curr['c']}55;">🎞️ VIDEO GALLERY</h2>
                            <p style="color: #888; font-size: 13px;">Manage your created masterpieces</p>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    if not st.session_state.get('gallery'):
                        st.info("No videos in gallery yet.")
                    else:
                        # ဗီဒီယိုများကို ၂ ခုစီ စီပြခြင်း
                        g_cols = st.columns(2)
                        for i, item in enumerate(reversed(st.session_state.gallery)):
                            with g_cols[i % 2]:
                                # ဗီဒီယို Player ကို စတုဂံဘောင်လေးဖြင့်
                                st.markdown(f'<div style="border:1px solid {curr["c"]}44; border-radius:10px; padding:5px; background:#000; margin-bottom:5px;">', unsafe_allow_html=True)
                                st.video(item['url'])
                                st.markdown('</div>', unsafe_allow_html=True)
                                
                                # ⋮ Dot-3 Popover Options (အရောင်စုံ ခလုတ်များဖြင့်)
                                with st.popover("⋮ OPTIONS"):
                                    # 🔵 Download (Blue Gradient)
                                    st.markdown(f'<style>div.stButton > button[key="dl_{i}"] {{ background: linear-gradient(90deg, #00C6FF, #0072FF) !important; color: white !important; border:none !important; border-radius:4px !important; }}</style>', unsafe_allow_html=True)
                                    st.button(f"📥 Download", key=f"dl_{i}", use_container_width=True)
                                    
                                    # 🟢 Share (Green Gradient)
                                    st.markdown(f'<style>div.stButton > button[key="sh_{i}"] {{ background: linear-gradient(90deg, #11998e, #38ef7d) !important; color: white !important; border:none !important; border-radius:4px !important; }}</style>', unsafe_allow_html=True)
                                    st.button(f"📤 Share", key=f"sh_{i}", use_container_width=True)
                                    
                                    # 🔴 Delete (Red Gradient)
                                    st.markdown(f'<style>div.stButton > button[key="del_{i}"] {{ background: linear-gradient(90deg, #FF4B2B, #FF416C) !important; color: white !important; border:none !important; border-radius:4px !important; }}</style>', unsafe_allow_html=True)
                                    if st.button(f"🗑️ Delete", key=f"del_{i}", use_container_width=True):
                                        st.session_state.gallery.pop(-(i+1))
                                        st.rerun()
                    
                    st.write("---")
                    # 🔙 BACK TO STUDIO BUTTON (စတုဂံပုံစံ)
                    st.markdown(f"""
                        <style>
                        div.stButton > button.back-to-st {{height: 55px !important; background: transparent !important;
                            color: {curr['c']} !important; border: 2px solid {curr['c']} !important;
                            border-radius: 4px !important; font-weight: bold !important; font-size: 16px !important;
                        }}
                        div.stButton > button.back-to-st:hover {{ background: {curr['c']} !important; color: black !important; }}
                        </style>
                    """, unsafe_allow_html=True)
                    if st.button("⬅️ BACK TO STUDIO", key="back-to-st", use_container_width=True):
                        st.session_state.view = 'studio'
                        st.rerun()
                st.stop() # Gallery ပြနေချိန် ကျန်တာတွေ မပြရန်

            # --- 🎥 (၂) STUDIO VIEW (ဗီဒီယို Studio နှင့် Input) ---
            else:
                # Header နှင့် Gallery Button ကို ဘေးချင်းယှဉ်ပြခြင်း
                h_col1, h_col2 = st.columns([0.6, 0.4])
                with h_col1:
                    st.markdown(f"<h3 style='color:{curr['c']}'>Video studio-{curr['n']}</h3>", unsafe_allow_html=True)
                with h_col2:
                    if st.button("🖼️ MY GALLERY", use_container_width=True):
                        st.session_state.view = 'gallery_page'
                        st.rerun()

                # --- ⏳ (က) GENERATING MODE ---
                if st.session_state.generating:
                    main_placeholder = st.empty()
                    with main_placeholder.container():
                        wait_time = 60 if ("min" in duration or "60s" in duration) else 30
                        ad_img = "https://img.freepik.com/free-vector/horizontal-banner-template-online-streaming-service_23-2148902804.jpg"
                        
                        st.markdown(f"""
                            <div style="text-align: center; margin-bottom: 30px; background: #000; padding: 15px; border-bottom: 2px solid {curr['c']};">
                                <p style="color: #666; font-size: 10px; letter-spacing: 2px;">GOOGLE ADS SPONSOR</p>
                                <img src="{ad_img}" style="width: 100%; max-width: 450px; border-radius: 8px; margin-top:10px;">
                            </div>
                        """, unsafe_allow_html=True)

                        prog_text = st.empty()
                        prog_bar = st.empty()

                        for percent in range(101):
                            time.sleep(wait_time / 100)
                            ad_msg = "UPGRADE FOR 4K QUALITY" if percent < 50 else "ENJOY AD-FREE EXPERIENCE"
                            prog_text.markdown(f"""
                                <div style="text-align: center;">
                                    <h1 style="color: {curr['c']}; font-size: 75px; font-weight: 900; margin: 0; text-shadow: 0 0 20px {curr['c']}CC;">{percent}%</h1>
                                    <p style="color: #888; letter-spacing: 5px; font-size: 12px;">RENDERING VIDEO...</p>
                                    <p style="color: {curr['c']}; font-size: 14px;">{ad_msg}</p>
                                </div>
                            """, unsafe_allow_html=True)
                            prog_bar.markdown(f"""
                                <div style="width: 90%; background: #111; border-radius: 50px; height: 12px; margin: 20px auto; border: 1px solid #333; padding: 2px;">
                                    <div style="width: {percent}%; height: 100%; border-radius: 50px; background: linear-gradient(90deg, {curr['c']}, #fff); box-shadow: 0 0 10px {curr['c']}; transition: width 0.3s;"></div>
                                </div>
                            """, unsafe_allow_html=True)

                    st.session_state.generating = False
                    st.session_state.video_done = True
                    st.session_state.view = 'studio' # ပြီးရင် Studio မှာပဲ Preview ပြရန်
                    st.rerun()# --- ✅ (ခ) PREVIEW SUCCESS (ဗီဒီယိုထွက်လာသည့်အချိန်) ---
                elif st.session_state.get('video_done'):
                    st.markdown(f"<h3 style='color:{curr['c']}; text-align:center;'>🎯 PREVIEW SUCCESS</h3>", unsafe_allow_html=True)
                    st.markdown(f'<div style="border:2px solid {curr["c"]}; border-radius:12px; padding:10px; background:#000; margin-bottom:20px;">', unsafe_allow_html=True)
                    st.video("https://www.w3schools.com/html/mov_bbb.mp4")
                    st.markdown('</div>', unsafe_allow_html=True)

                    col_dl, col_sh = st.columns(2)
                    col_dl.button("📥 DOWNLOAD VIDEO", use_container_width=True)
                    col_sh.button("📤 SHARE VIDEO", use_container_width=True)

                    if st.button("⬅️ BACK TO CREATE", use_container_width=True):
                        del st.session_state.video_done
                        st.session_state.ad_done = True 
                        st.rerun()

                # --- 📝 (1) INPUT MODE (စာရိုက်သည့်အချိန်) ---
                else:
                    prompt = st.text_area("WRITE YOUR SCRIPT", height=250)
                    st.markdown(f"""
                        <style>
                        div.stButton > button.start-gen-btn {{
                            width: 100% !important; height: 60px !important;
                            background: transparent !important; color: {curr['c']} !important;
                            border: 2px solid {curr['c']} !important; border-radius: 4px !important;
                            font-weight: bold !important; font-size: 18px !important;
                        }}
                        div.stButton > button.start-gen-btn:hover {{ background: {curr['c']} !important; color: black !important; box-shadow: 0 0 20px {curr['c']}; }}
                        </style>
                    """, unsafe_allow_html=True)

                    if st.button(f"🚀 START {curr['n']} GENERATE", key="start-gen-btn"):
                        st.session_state.generating = True
                        st.rerun()
            # (ခ) အောက်ပိုင်း - % PROGRESS BAR
            if st.session_state.generating:
                wait_time = 60 if ad_mode == 'long' else 30
                st.markdown(f'<div class="scanner-box" style="border-color:{curr["c"]}"><div class="scanner-line" style="background:{curr["c"]}"></div><span style="color:{curr["c"]}">AI RENDERING...</span></div>', unsafe_allow_html=True)
                
                bar_placeholder = st.progress(0)
                percent_text = st.empty()
                
                for p in range(101):
                    time.sleep(wait_time / 100)
                    bar_placeholder.progress(p)
                    percent_text.markdown(f"<h2 style='text-align:center; color:{curr['c']};'>{p}%</h2>", unsafe_allow_html=True)
                
                st.session_state.generating = False
                st.session_state.video_done = True
                st.rerun()

            # ---  (ဂ) FINAL BACK (COLOR FIXED & NO ADS) ---
            # CSS Selector ကို အတိအကျ ပြင်ထားပါတယ်
            st.markdown(f"""
                <style>
                div.stButton > button:first-child {{
                    background-color: transparent !important;
                    color: {curr['c']} !important;
                    border: 1px solid {curr['c']} !important;
                    border-radius: 4px !important;
                    width: 150px !important;
                    height: 40px !important;
                    display: block !important;
                    margin: 30px auto !important;
                    font-weight: bold !important;
                }}
                div.stButton > button:first-child:hover {{
                    background-color: {curr['c']} !important;
                    color: black !important;
                    border: 1px solid {curr['c']} !important;
                }}
                </style>
            """, unsafe_allow_html=True)

            # ခလုတ်ကို နှိပ်လိုက်လျှင် လုပ်ဆောင်မည့် Logic
            if st.button(" BACK "):
                # ၁။ ကြော်ငြာကို အတင်းကျော်ရန် (ad_done ကို True ပေးရမည်)
                st.session_state.ad_done = True 
                
                # --- ၂။ Owner Dashboard Check (Line 501 မှစတင်၍ ပြင်ရန်) --- [cite: 2026-01-01]
    if 'admin_mode' in st.session_state:
        # ဒီအောက်က စာကြောင်းတွေကို ရှေ့ကို Space ၄ ချက်စီ ပုတ်ပေးထားပါတယ်
        st.session_state.admin_mode = False 
        st.session_state.generating = False 
        st.session_state.page_state = 'tier_selection'
        st.rerun()

# --- ဤနေရာတွင် Studio Page ကို ထည့်သွင်းနိုင်ပါသည် --- [cite: 2026-01-01]
    elif st.session_state.page_state == 'studio':
        # စာရိုက်သည့်နေရာ
        prompt = st.text_area("ENTER YOUR SCRIPT")
        # ၎င်းအောက်တွင် Setting Bar ထားရှိခြင်း [cite: 2026-01-01]
        st.write("Settings: Duration, Res, Ratio")

# --- ၅။ AI CHAT PAGE (မူရင်း Line 514 အပိုင်း) --- [cite: 2026-01-01]
    elif st.session_state.page_state == 'chat_page':
        st.markdown("<h1>BMT AI CHAT</h1>", unsafe_allow_html=True)
        # ... ကျန်တာများကို မူရင်းအတိုင်း ထားပါ ...
        if st.button(" BACK TO EMPIRE"): st.session_state.page_state = 'home'; st.rerun()
        st.chat_input("မေးမြန်းလိုသည်များကို ရိုက်ထည့်ပါ...")

# ==========================================
# ၄။ ကြော်ငြာ (ADVERTISEMENTS)
# ==========================================
def ads_manager():
    if not st.session_state.is_owner:
        st.divider()
        st.markdown("""
            <div style="background: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; text-align: center;">
                <h4 style="color: #3b82f6; margin:0;">BMT SPONSORED AD</h4>
                <p style="font-size: 14px;">Upgrade to Diamond for 120s Videos!</p>
            </div>
        """, unsafe_allow_html=True)

# ==========================================
# ၅။ ပိုင်ရှင်ကြည့်ရန် (OWNER DASHBOARD)
# ==========================================
def owner_dashboard():
    if st.session_state.is_owner:
        st.divider()
        st.subheader(" BMT Business Insights")
        c1, c2, c3 = st.columns(3)
        c1.metric("Daily Users", "150", "+5%")
        c2.metric("Revenue", "350,000 MMK", "Peak")
        c3.metric("Video Tasks", len(st.session_state.video_history))

# ==========================================
# ၆။ အစီအစဉ်ကျ RUN ခြင်း (MAIN EXECUTION)
# ==========================================
if 'messages' not in st.session_state: st.session_state.messages = []
if 'video_history' not in st.session_state: st.session_state.video_history = []

apply_bmt_style()       # ၁။ အလှပြင်
manage_owner_keys()     # ၂။ Key စစ်/ထည့်
ai_studio_module()      # ၃။ Chat & Video
ads_manager()           # ၄။ ကြော်ငြာ
owner_dashboard()       # ၅။ ပိုင်ရှင်ကြည့်ရန်
