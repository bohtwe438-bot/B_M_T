import streamlit as st

# Website ရဲ့ Layout ကို သတ်မှတ်ခြင်း
st.set_page_config(page_title="BMT AI Assistant", page_icon="🤖", layout="centered")

# အလှဆင်ရန် CSS Code များ
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
    }
    .main-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #00d2ff;
        text-shadow: 2px 2px 4px #000000;
    }
    .stTextInput input {
        border-radius: 20px;
        border: 2px solid #00d2ff;
    }
    </style>
    """, unsafe_allow_html=True)

# Website အပေါ်ဆုံးပိုင်း
st.markdown('<p class="main-title">🤖 BMT AI ASSISTANT</p>', unsafe_allow_html=True)
st.write("<h3 style='text-align: center;'>မြန်မာနိုင်ငံသားများအတွက် အကောင်းဆုံး AI</h3>", unsafe_allow_html=True)
st.write("---")

# Chat အကွက်
st.subheader("💬 AI Chat Room")
chat_input = st.text_input("မေးချင်တာရှိရင် ဒီမှာ ရေးပေးပါ...", placeholder="ဥပမာ- ဓာတ်ပုံဘယ်လိုပြင်ရမလဲ?")

if st.button("ပို့မည် (Send)"):
    st.success("စာသားပို့လိုက်ပါပြီ။ (AI အဖြေရဖို့ API Key ထည့်ရန် လိုအပ်သည်)")

# ဘေးဘောင် (Sidebar) မှာ အလှဆင်ခြင်း
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.title("BMT AI Settings")
    st.info("ဒီနေရာမှာ API Key တွေ ထည့်သွင်းနိုင်ပါတယ်")
