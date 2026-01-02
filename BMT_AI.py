import streamlit as st
import styles as bmt_style
import studio_engine as studio
import owner_manager as admin
import ads_center as ads

class BMTAiEmpire:
    def __init__(self):
        # Module အားလုံးကို Initialize လုပ်ပြီး ချိတ်ဆက်ခြင်း
        self.ui = bmt_style.BMT_Styles()
        self.engine = studio.StudioEngine()
        self.admin = admin.OwnerManager()
        self.ads = ads.AdsCenter()
        
        if 'user_tier' not in st.session_state:
            st.session_state.user_tier = "F" # Default Tier

    def run_app(self):
        self.ui.apply_main_css()
        # Owner Plan: Main Buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button(" AI SMART CHAT"):
                self.engine.open_chat(st.session_state.user_tier)
        with col2:
            if st.button(" VIDEO GENERATOR"):
                self.engine.open_video_gen(st.session_state.user_tier)
        
        # Ads ပြသခြင်း
        self.ads.show_banner()

if __name__ == "__main__":
    app = BMTAiEmpire()
    app.run_app()
