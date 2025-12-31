import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="BMT AI - Chat & Video",
    page_icon="🤖"
)

st.title("🤖 BMT AI Assistant")

# 2. API Connection (ဒီနေရာမှာ Key အစစ်ကို မထည့်ထားပါဘူး)
# ဒါမှ GitHub က ပိတ်မှာ မဟုတ်လို့ပါ
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except Exception:
    st.error("Setting ထဲမှာ Key ထည့်ဖို့ လိုအပ်နေပါသေးတယ်။")
    st.stop()

# 3. Chat Logic
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("ဘာမေးချင်လဲ Founder?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {"role": "system", "content": "မင်းက BMT က ဖန်တီးထားတဲ့ မြန်မာ AI Assistant ဖြစ်ပါတယ်။"},
                *st.session_state.messages
            ],
        )
        answer = response.choices[0].message.content
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
