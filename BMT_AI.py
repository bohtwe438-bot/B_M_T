import streamlit as st
import traceback

# ၁။ Error ကို Screen ပေါ်မှာ ဖမ်းပြမယ့်စနစ်
try:
    # Page Config ကို အပေါ်ဆုံးမှာ ထားရပါမယ်
    st.set_page_config(page_title="BMT AI EMPIRE", layout="wide")

    # ၂။ Sidebar မှာ Status ပြပေးခြင်း
    st.sidebar.title(" BMT System Status")
    st.sidebar.success("Engine: Online")
    st.sidebar.info("Plan: 10,000 Lines Project")

    # ၃။ Main UI
    st.markdown("<h1 style='text-align: center; color: #00F3FF;'> BMT AI EMPIRE</h1>", unsafe_allow_html=True)
    st.write("---")

    # ၄။ Owner ရဲ့ Plan အတိုင်း Buttons များ
    st.subheader("BMT Main Services")
    col1, col2 = st.columns(2)
    with col1:
        st.button(" AI SMART CHAT", use_container_width=True)
    with col2:
        st.button(" VIDEO GENERATOR", use_container_width=True)

    # ၅။ Tier Selection
    st.write("---")
    st.subheader("Tier Selection")
    t1, t2, t3, t4 = st.columns(4)
    tiers = [(" F Tier", "Free"), (" S Tier", "Silver"), (" G Tier", "Gold"), (" D Tier", "Diamond")]
    cols = [t1, t2, t3, t4]
    
    for i, col in enumerate(cols):
        with col:
            if st.button(tiers[i][0], use_container_width=True):
                st.toast(f"{tiers[i][1]} Activated!")

    st.write("---")
    st.info("Owner ရေ... ဒီ UI ပေါ်လာပြီဆိုရင် ကျွန်တော်တို့ Line 10,000 ဆီ သွားဖို့ အသင့်ဖြစ်ပါပြီ!")

except Exception as e:
    # Error တက်ရင် အဖြူရောင်ကြီး ဖြစ်မနေဘဲ ဒီစာသားတွေ ပေါ်လာပါလိမ့်မယ်
    st.error(" BMT AI Error တက်နေပါတယ် Owner!")
    st.code(traceback.format_exc()) # Error ဖြစ်တဲ့ နေရာကို အတိအကျပြပေးမယ်
