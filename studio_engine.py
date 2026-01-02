import streamlit as st
import time

def video_rendering_logic(curr):
    st.markdown(f"<h3 style='color:{curr['c']}; text-align:center;'>RENDERING VIDEO...</h3>", unsafe_allow_html=True)
    prog_bar = st.progress(0)
    for percent in range(101):
        time.sleep(0.1) # ချိန်ညှိနိုင်သည်
        prog_bar.progress(percent)
    st.session_state.generating = False
    st.session_state.video_done = True
    st.rerun()

def chat_interface():
    st.markdown("<h1>BMT AI CHAT</h1>", unsafe_allow_html=True)
    if st.button("BACK TO EMPIRE"):
        st.session_state.page_state = 'home'
        st.rerun()
    st.chat_input("မေးမြန်းလိုသည်များကို ရိုက်ထည့်ပါ...")
