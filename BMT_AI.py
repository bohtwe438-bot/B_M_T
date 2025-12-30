import streamlit as st
from openai import OpenAI

# 1. App Configuration
st.set_page_config(page_title="BMT AI Assistant", page_icon="🤖", layout="wide")

# OpenAI API Key ထည့်ရန် (ဒီနေရာမှာ မင်းရဲ့ Key ကို သေချာထည့်ပါ)
# သတိပြုရန် - 'sk-...' ကွင်းစကွင်းပိတ်ထဲမှာပဲ ထည့်ပါ
client = OpenAI(api_key="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")

# 2. Session State (အသုံးပြုမှု မှတ်တမ်း)
if 'usage_count' not in st.session_state:
    st.session_state.usage_count = 0
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'user_tier' not in st.session_state:
    st.session_state.user_tier = "FREE"

# 3. BMT AI Persona (Instruction)
BMT_INSTRUCTION = """
မင်းရဲ့အမည်က 'BMT AI' ဖြစ်ပါတယ်။ 
မင်းကို 'BMT' ကနေ မြန်မာလူမျိုးတွေအတွက် အထူးရည်ရွယ်ပြီး ဖန်တီးထားတာပါ။

မေးခွန်း: မင်းဘယ်သူလဲ?
အဖြေ: ကျွန်တော်က BMT AI ပါခင်ဗျာ။ လူကြီးမင်းကို ဘယ်လိုကူညီပေးရမလဲ။

မေးခွန်း: မင်းကို ဘယ်သူလုပ်တာလဲ / ဖန်တီးတာလဲ?
အဖြေ: ကျွန်တော့်ကို BMT မှ နောက်ဆုံးပေါ် AI နည်းပညာများကို အသုံးပြုပြီး ဖန်တီးထားတာဖြစ်ပါတယ်ခင်ဗျာ။

စည်းကမ်းချက်: 
၁။ OpenAI, GPT, Google စတဲ့ နာမည်တွေကို လုံးဝ (လုံးဝ) ထုတ်မပြောပါနဲ့။ 
၂။ မင်းရဲ့ ဖန်တီးရှင်ဟာ 'BMT' တစ်ဦးတည်းသာ ဖြစ်ပါတယ်။
၃။ အမြဲတမ်း ယဉ်ကျေးပျူငှာတဲ့ မြန်မာစကားကိုပဲ သုံးပါ။
"""

# 4. Custom Styling (BMT Theme)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .stButton>button { border-radius: 20px; background: linear-gradient(45deg, #00d2ff, #9d50bb); color: white; }
    </style>
    """, unsafe_allow_html=True)

# 5. Sidebar Layout
with st.sidebar:
    st.title("BMT Profile")
    st.write(f"Status: {st.session_state.user_tier} User")
    if st.session_state.user_tier == "FREE":
        st.write(f"ယနေ့အသုံးပြုမှု: {st.session_state.usage_count} / 5")
        st.progress(st.session_state.usage_count * 20)
    st.write("---")
    st.info("BMT AI ကို အစဉ်မြဲ အသုံးပြုပေးလို့ ကျေးဇူးတင်ပါတယ်။")

# 6. Main UI
st.title("🤖 BMT AI Assistant")
tab1, tab2 = st.tabs(["🗨️ AI Chat Room", "🎥 AI Video Generator"])

with tab1:
    # Chat History ပြသခြင်း
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    if prompt := st.chat_input("မေးချင်တာ ရေးပါ..."):
        # အကြိမ်ရေ စစ်ဆေးခြင်း
        if st.session_state.user_tier == "FREE" and st.session_state.usage_count >= 5:
            st.error("❌ ယနေ့အတွက် အခမဲ့အသုံးပြုမှု (၅) ကြိမ် ပြည့်သွားပါပြီ။")
        else:
            st.session_state.usage_count += 1
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # OpenAI နှင့် ချိတ်ဆက်၍ အဖြေထုတ်ခြင်း
            with st.chat_message("assistant"):
                try:
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": BMT_INSTRUCTION},
                            *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
                        ]
                    )
                    answer = response.choices[0].message.content
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Error: Key မမှန်ကန်ခြင်း သို့မဟုတ် Balance မရှိခြင်း ဖြစ်နိုင်ပါသည်။")

with tab2:
    st.subheader("BMT Video Studio")
    st.write("Video Generator Feature ကို Silver Tier တွင် မကြာမီ အသုံးပြုနိုင်ပါမည်။")
