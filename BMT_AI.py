import styles as bmt_style # အသေးပြောင်းထားသည်
import time
import streamlit as st

class BMTAiEmpire:
    def init(self): # init ဟု ပြင်ထားသည်
        self.ui = bmt_style.BMT_Styles() # Class နာမည် ညှိထားသည်
        if 'user_session' not in st.session_state:
            st.session_state.user_session = {
                "name": "BMT User",
                "tier": "F", 
                "last_update": 0 
            }
        self.is_owner = False

    def google_auth_system(self):
        st.write("BMT AI EMPIRE: Connected via Google.")

    def build_home_screen(self):
        # Master Plan အရ UI ကို ဒီမှာ ဆက်ရေးပါမည်
        st.title("BMT AI EMPIRE")
        col1, col2 = st.columns(2)
        with col1: st.button(" AI SMART CHAT", use_container_width=True)
        with col2: st.button(" VIDEO GENERATOR", use_container_width=True)

# App Start (Syntax အမှန်ပြင်ထားသည်)
if name == "main":
    app = BMTAiEmpire()
    app.google_auth_system()
    app.build_home_screen()
