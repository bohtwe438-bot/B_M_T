import streamlit as st

# ၁။ Page Setting (Browser Tab မှာ ပေါ်မယ့်အချက်အလက်)
st.set_page_config(
    page_title="BMT AI - Chat & Video", 
    page_icon="", 
    layout="wide"
)

# ၂။ Custom CSS (App တစ်ခုလုံးကို အရောင်လှအောင် လုပ်ခြင်း)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #7f00ff;
        color: white;
        border: none;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e3b4e,#2e3b4e);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# ၃။ Sidebar (ဘေးဘား) အလှဆင်ခြင်း
with st.sidebar:
    st.title("BMT AI")
    st.image("https://img.icons8.com/clouds/100/video-call.png") # ယာယီ Icon (Founder Logo ပြန်ထည့်လို့ရသည်)
    st.info("မြန်မာနိုင်ငံ၏ ပထမဆုံး AI Chat & Video Generator")
    st.markdown("---")
    st.subheader("လုပ်ဆောင်ချက်များ")
    st.write(" AI Chat Assistant")
    st.write(" AI Video Script")
    st.write(" Video Generator (Coming Soon)")

# ၄။ Main UI (အလယ်ပိုင်း)
st.title(" BMT Ai Chat & Video Generator")
st.write("---")

# Logo နေရာအတွက် Placeholder
col1, col2, col3 = st.columns([1,2,1])
with col2:
    # Founder ရဲ့ Logo ပုံကို ဤနေရာတွင် မြင်ယောင်ကြည့်ပါ
    st.info(" Logo ပြသရန် နေရာ")

# ၅။ Key မထည့်ရသေးကြောင်း အသိပေးချက် (လှပသော Box လေးနှင့်)
if "GROQ_API_KEY" not in st.secrets:
    st.warning(" System Setup: Founder ရေ... အပြင်ပိုင်း ဒီဇိုင်းက အဆင်သင့်ဖြစ်နေပါပြီ။ စက်အင်ဂျင်နှိုးဖို့အတွက် Secrets ထဲမှာ Key ထည့်ပေးဖို့ပဲ လိုပါတော့တယ်။")
    
    # ယာယီ Chat Box ပုံစံပြသခြင်း
    st.text_input("ဘာမေးချင်လဲ Founder? (Key ထည့်ပြီးမှ အလုပ်လုပ်ပါမည်)", disabled=True)
    
    st.markdown("###  နောက်တစ်ဆင့် ဘာလုပ်မလဲ?")
    st.write("၁။ အပေါ်က Code ကို GitHub မှာ အရင် Save လုပ်ပါ။")
    st.write("၂။ App ရဲ့ ရုပ်ထွက်ကို စစ်ဆေးပါ။")
    st.write("၃။ စိတ်ကျေနပ်ပြီဆိုမှ Key ကို တစ်ကြောင်းတည်း စနစ်တကျ ထည့်ပါ။")

else:
    st.success(" အင်ဂျင်နိုးပါပြီ! Chatting စတင်နိုင်ပါပြီ။")
    # AI Chat Code များ ဤနေရာတွင် ဆက်လက်ရှိမည်
