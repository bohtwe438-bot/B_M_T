import streamlit as st

def show_login_screen():
    st.markdown("<div style='text-align:center; padding: 50px;'>", unsafe_allow_html=True)
    st.title("🌐 BMT AI EMPIRE")
    st.write("Login with your Google account to start creating.")
    
    if st.button("Login with Google", use_container_width=True):
        # ဤနေရာတွင် တကယ့် Google API နှင့် ချိတ်ဆက်မည်
        st.session_state.logged_in = True
        st.session_state.user_data = {
            "name": "User Name",
            "email": "user@gmail.com",
            "photo": "https://www.w3schools.com/howto/img_avatar.png",
            "tier": "F" # အခြေခံ Tier
        }
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def user_profile_header():
    if st.session_state.get('logged_in'):
        u = st.session_state.user_data
        
        # Tier အလိုက် Badge အရောင်များ
        tier_map = {
            "F": {"name": "FREE", "color": "#00ff00"},
            "S": {"name": "SILVER", "color": "#bdc3c7"},
            "G": {"name": "GOLD", "color": "#f1c40f"},
            "D": {"name": "DIAMOND", "color": "#9b59b6"}
        }
        t = tier_map.get(u['tier'], tier_map["F"])

        with st.sidebar:
            st.divider()
            col1, col2 = st.columns([0.3, 0.7])
            with col1:
                # Profile ပုံကို Gallery မှ ပြောင်းလဲနိုင်သော စနစ် (ထည့်သွင်းရန် အကြံပြုချက်)
                st.image(u['photo'], width=50)
            with col2:
                st.markdown(f"**{u['name']}**")
                st.markdown(f"<span style='background:{t['color']}; color:black; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:bold;'>{t['name']}</span>", unsafe_allow_html=True)
            
            if st.button("Logout", size="small"):
                st.session_state.logged_in = False
                st.rerun()
