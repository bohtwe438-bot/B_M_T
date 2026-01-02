import streamlit as st
import time
import sys
import os

# Line 10 ဝန်းကျင် module error မတက်အောင် လမ်းကြောင်းဖွင့်ခြင်း
sys.path.append(os.path.dirname(file))

try:
    import styles as bmt_style
    # studio_engine, ads_center တို့ကိုလည်း အခုလိုမျိုး try/except နဲ့ ခေါ်ထားရင် ပိုစိတ်ချရပါတယ်
except ImportError:
    st.error("styles.py ဖိုင်ကို ရှာမတွေ့ပါဘူး Owner!")

class BMTAiEmpire:
    def init(self):
        # Line 32-34 ဝန်းကျင်က error တွေအတွက် variable တွေကို သေချာသတ်မှတ်ခြင်း
        self.ui = bmt_style.BMT_Styles()
        if 'user_session' not in st.session_state:
            st.session_state.user_session = {
                "name": "BMT User",
                "tier": "F", 
                "last_update": time.time()
            }
        self.is_owner = False

    def build_home_screen(self):
        self.ui.apply_main_css()
        st.markdown('<div class="bmt-logo">BMT AI EMPIRE</div>', unsafe_allow_html=True)
        
        # Main Buttons (Side-by-Side)
        col1, col2 = st.columns(2)
        with col1:
            if st.button(" AI SMART CHAT", use_container_width=True):
                st.info("AI Chat Engine Loading...")
        with col2:
            if st.button(" VIDEO GENERATOR", use_container_width=True):
                st.success("Video Engine Loading...")

# --- App Start ---
# အရေးကြီးဆုံးအပိုင်း (Underscore ၂ ခုစီကို သေချာစစ်ပါ)
if __name__ == "__main__":
    app = BMTAiEmpire()
    app.build_home_screen()
