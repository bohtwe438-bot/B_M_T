import streamlit as st

def show_login_screen():
    st.markdown("<h2 style='text-align:center;'>Welcome to BMT AI EMPIRE</h2>", unsafe_allow_html=True)
    # ဤနေရာတွင် Google Auth Logic ထည့်သွင်းမည်
    if st.button("🌐 Login with Google", use_container_width=True):
        st.session_state.logged_in = True
        st.session_state.user_data = {
            "name": "User Name", 
            "photo": "https://www.w3schools.com/howto/img_avatar.png",
            "tier": "F"
        }
        st.rerun()

def user_profile_header():
    if st.session_state.get('logged_in'):
        u = st.session_state.user_data
        # Badge အရောင် သတ်မှတ်ခြင်း
        tier_colors = {"F": "#00ff00", "S": "#bdc3c7", "G": "#f1c40f", "D": "#9b59b6"}
        t_color = tier_colors.get(u['tier'], "#fff")
        
        # UI Header (Profile + Name + Badge)
        col1, col2 = st.columns([0.2, 0.8])
        with col1:
            st.image(u['photo'], width=60)
        with col2:
            st.markdown(f"**{u['name']}**")
            st.markdown(f"<span style='background:{t_color}; color:black; padding:2px 8px; border-radius:5px; font-weight:bold;'>{u['tier']}</span>", unsafe_allow_html=True)
