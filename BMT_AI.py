import streamlit as st

# ၁။ Page Layout & Style
st.set_page_config(page_title="BMT AI Assistant", page_icon="", layout="wide")

# ၂။ Advanced CSS Customization
st.markdown("""
    <style>
    /* တစ်ခုလုံးရဲ့ နောက်ခံအရောင် */
    .stApp {
        background: linear-gradient(180deg, #0f172a 0%, #1e293b 100%);
        color: white;
    }
    
    /* Card Style - စာသားတွေ စုစည်းဖို့ */
    .main-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    /* ခေါင်းစဉ်ကြီး */
    .main-title {
        font-size: 45px;
        font-weight: 800;
        text-align: center;
        background: linear-gradient(90deg, #00d2ff, #3a7bd5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    
    /* Button အလှဆင်ခြင်း */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 30px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }
    div.stButton > button:hover {
        transform: scale(1.02);
        box-shadow: 0px 4px 15px rgba(0, 210, 255, 0.4);
    }

    /* Input Box */
    .stTextInput input {
        background-color: #1e293b !important;
        color: white !important;
        border-radius: 15px !important;
        border: 1px solid #334155 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ၃။ Sidebar (ဘေးဘောင်)
with st.sidebar:
    # logo.png ကို GitHub မှာ တင်ထားရင် ဒါက အလိုလိုပေါ်မယ်
    try:
        st.image("logo.png", width=200)
    except:
        st.write(" BMT AI PROJECT")
    
    st.markdown("---")
    st.title(" Control Panel")
    st.info("BMT AI ကို အသုံးပြုပြီး Video Script များနှင့် Chatting လုပ်ဆောင်နိုင်ပါသည်။")
    st.markdown("---")
    st.caption("Developed with  for Myanmar")

# ၄။ Main Content အပိုင်း
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    # Logo နဲ့ ခေါင်းစဉ်
    st.markdown('<p class="main-title">BMT AI ASSISTANT</p>', unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: #94a3b8;'>Smart AI Chat & Video Generator</h5>", unsafe_allow_html=True)
    st.write("<br>", unsafe_allow_html=True)
    
    # စာရိုက်မည့် ဧရိယာကို Card ထဲထည့်ခြင်း
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        
        st.subheader(" AI Chat Room")
        user_input = st.text_input("ဘာမေးချင်လဲ Founder?", placeholder="ဥပမာ- Video Script ရေးပေးပါ...")
        
        c1, c2, c3 = st.columns([1, 1, 1])
        with c2:
            send_btn = st.button("Send Message")
        
        if send_btn:
            if user_input:
                st.success("စာသားပို့လိုက်ပါပြီ။ အင်ဂျင်နိုးရန် Key ထည့်ဖို့ လိုအပ်ပါသည်။")
            else:
                st.warning("စာသား အရင်ရေးပေးပါဦး။")
                
        st.markdown('</div>', unsafe_allow_html=True)

# ၅။ Footer အပိုင်း
st.write("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569;'> 2025 BMT AI. Billion Level Vision.</p>", unsafe_allow_html=True)
