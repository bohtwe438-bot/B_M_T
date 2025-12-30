import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="BMT AI ",
    page_icon="🤖"
)

st.title("🤖 BMT AI ")

# Groq client
client = Groq(api_key=st.secrets["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"])

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if prompt := st.chat_input("ဘာမေးချင်လဲ Founder?"):
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "မင်းက BMT က ဖန်တီးထားတဲ့ မြန်မာ AI Assistant ဖြစ်ပါတယ်။"
                },
                *st.session_state.messages
            ],
        )

        answer = response.choices[0].message.content
        st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
