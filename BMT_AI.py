import streamlit as st
from groq import Groq

st.set_page_config(page_title="BMT AI Assistant", page_icon="🤖")
st.title("🤖 BMT AI Assistant")

# Secrets ထဲက Groq Key ကို ယူမယ်
client = Groq(api_key=st.secrets["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"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("ဘာမေးချင်လဲ Founder?"):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "မင်းက BMT က ဖန်တီးထားတဲ့ မြန်မာ AI ဖြစ်ပါတယ်။"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        msg = response.choices[0].message.content
        st.markdown(msg)

    st.session_state.messages.append(
        {"role": "assistant", "content": msg}
    )
