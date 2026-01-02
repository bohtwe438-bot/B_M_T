import streamlit as st

def show_login_screen():
    st.markdown("<div style='text-align:center; padding: 50px;'>", unsafe_allow_html=True)
    st.title("🌐 BMT AI EMPIRE")
    st.write("Login with your Google account to start creating.")
    
    if st.button("Login with Google", use_container_width=True):
        st.session_state.logged_in = True
        st.session_state.user_data = {
            "name": "User Name",
            "email": "user@gmail.com",
            "photo": "https://www.w3schools.com/howto/img_avatar.png",
            "tier": "F" 
        }
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def user_profile_header():
    if st.session_state.get('logged_in'):
        u = st.session_state.user_data
        
        tier_map = {
            "F": {"name": "FREE", "color": "#00ff00"},
            "S": {"name": "SILVER", "color": "#bdc3c7"},
            "G": {"name": "GOLD", "color": "#f1c40f"},
            "D": {"name": "DIAMOND", "color": "#9b59b6"}
        }
        t = tier_map.get(u['tier'], tier_map["F"])

        with st.sidebar:
            st.divider()
            
            # --- Profile Image Display & Uploader ---
            col_img, col_txt = st.columns([0.4, 0.6])
            with col_img:
                st.image(u['photo'], width=60)
            with col_txt:
                st.markdown(f"**{u['name']}**")
                st.markdown(f"<span style='background:{t['color']}; color:black; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:bold;'>{t['name']}</span>", unsafe_allow_html=True)
            
            # ပုံပြောင်းရန်အတွက် Expander လေးနဲ့ ဝှက်ထားပေးပါမယ် (Clean ဖြစ်အောင်)
            with st.expander("🖼️ Edit Profile"):
                uploaded_file = st.file_uploader("Choose a photo", type=["jpg", "png", "jpeg"])
                if uploaded_file is not None:
                    # ပုံအသစ်ကို session_state ထဲမှာ အစားထိုးခြင်း
                    st.session_state.user_data['photo'] = uploaded_file
                    st.success("Photo updated!")
                    st.rerun()

            st.write("") # နေရာလွတ်လေးခြားရန်
            # Error တက်ခဲ့သည့် button နေရာကို ပြင်ထားပါသည် (size attribute ကို ဖြုတ်ထားပါသည်)
            if st.button("Logout", use_container_width=True):
                st.session_state.logged_in = False
                # Logout လုပ်ချိန်တွင် Owner state ပါ ဖျက်သိမ်းရန်
                st.session_state.is_owner = False
                st.rerun()
