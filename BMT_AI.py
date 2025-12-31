import streamlit as st

# ၁။ Page Configuration
st.set_page_config(page_title="BMT", page_icon="🤖", layout="wide")

# ၂။ Advanced UI Styling (CSS)
st.markdown("""
    <style>
    /* Background တစ်ခုလုံးကို Dark & Deep ဖြစ်အောင် */
    .stApp {
        background: radial-gradient(circle at top, #1e293b 0%, #0f172a 100%);
        color: white;
    }

    /* BMT Title ကို Glow ဖြစ်အောင် */
    .bmt-header {
        font-size: 80px;
        font-weight: 900;
        text-align: center;
        margin-top: -50px;
        background: linear-gradient(180deg, #ffffff 0%, #3b82f6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(59, 130, 246, 0.5));
        letter-spacing: 10px;
    }

    /* Card Layout (Glassmorphism) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        border-radius: 30px;
        backdrop-filter: blur(20px);
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.3);
        text-align: center;
        height: 100%;
    }

    /* Chat Button Style (Cyan Gradient) */
    div.stButton > button#chat_btn {
        background: linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%);
        color: white;
        border: none;
        border-radius: 15px;
        height: 55px;
        font-size: 18px;
        font-weight: 700;
        transition: 0.4s ease;
        text-transform: uppercase;
    }

    /* Video Button Style (Purple/Pink Gradient) */
    div.stButton > button#video_btn {
        background: linear-gradient(135deg, #a855f7 0%, #ec4899 100%);
        color: white;
        border: none;
        border-radius: 15px;
        height: 55px;
        font-size: 18px;
        font-weight: 700;
        transition: 0.4s ease;
        text-transform: uppercase;
    }

    /* Hover effects for buttons */
    div.stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
        opacity: 0.9;
    }

    /* Custom Input Boxes */
    .stTextInput input {
        background: rgba(0, 0, 0, 0.2) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 12px !important;
        height: 45px;
    }
    </style>
    """, unsafe_allow_html=True)

# ၃။ Main Branding
st.markdown('<h1 class="bmt-header">BMT</h1>', unsafe_allow_html=True)
st.write("<br><br>", unsafe_allow_html=True)

# ၄။ Multi-Function Section
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("## 💬 AI CHAT")
    st.write("စမတ်ကျကျ အမေးအဖြေလုပ်ရန်")
    user_q = st.text_input("မေးခွန်းရိုက်ပါ", key="q_in", label_visibility="collapsed", placeholder="မေးချင်တာရှိရင် ဒီမှာရေးပါ...")
    st.write("<br>", unsafe_allow_html=True)
    if st.button("START CHATTING", key="chat_btn", use_container_width=True):
        st.toast("Chat Engine ပြင်ဆင်နေပါသည်...")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("## 🎥 VIDEO")
    st.write("ဗီဒီယို Script များဖန်တီးရန်")
    video_p = st.text_input("Script ရိုက်ပါ", key="v_in", label_visibility="collapsed", placeholder="ဗီဒီယိုအကြောင်းအရာ ရေးပါ...")
    st.write("<br>", unsafe_allow_html=True)
    if st.button("GENERATE VIDEO", key="video_btn", use_container_width=True):
        st.toast("Video Engine ပြင်ဆင်နေပါသည်...")
    st.markdown('</div>', unsafe_allow_html=True)

# ၅။ Sidebar Branding
with st.sidebar:
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("<h2 style='text-align: center;'>BMT</h2>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("✨ BMT Premium v1.0")
    st.caption("AI Solutions for Myanmar")

# ၆။ Footer
st.write("<br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; opacity: 0.2;'>© 2025 BMT. AUTHENTIC QUALITY.</p>", unsafe_allow_html=True)
