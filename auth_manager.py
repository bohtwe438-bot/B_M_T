import streamlit as st
from database import get_user_tier, save_user_tier  # <--- Database ချိတ်ဆက်မှု ထည့်သွင်းခြင်း

def show_login_screen():
    st.markdown("<div style='text-align:center; padding: 50px;'>", unsafe_allow_html=True)
    st.title("🌐 BMT AI EMPIRE")
    st.write("Login with your Google account to start creating.")
    
    if st.button("Login with Google", use_container_width=True):
        # --- အသုံးပြုသူ အချက်အလက်များကို ရယူခြင်း ---
        user_email = "user@gmail.com" # အစစ်အမှန်တွင် Google Login မှရသော email ဖြစ်ရမည်
        
        # [အရေးကြီး] Database ထဲမှ ထိုအသုံးပြုသူ၏ Tier ကို ဖတ်ယူသည်
        current_tier = get_user_tier(user_email)
        
        # အကယ်၍ အသစ်စက်စက် User ဖြစ်ပါက Database ထဲတွင် FREE အဖြစ် အသေမှတ်ပေးလိုက်မည်
        if current_tier == "FREE":
            save_user_tier(user_email, "FREE")

        st.session_state.logged_in = True
        st.session_state.user_name = user_email # user_name အဖြစ် email ကိုသုံးရန် (Database Key ဖြစ်သောကြောင့်)
        
        st.session_state.user_data = {
            "name": "User Name",
            "email": user_email,
            "photo": "https://www.w3schools.com/howto/img_avatar.png",
            "tier": current_tier # Database မှရသော Tier ကို တိုက်ရိုက်အသုံးပြုသည်
        }
        
        # BMT_AI.py ရှိ session_state နှင့်လည်း ချိတ်ဆက်ပေးသည်
        st.session_state.user_tier = current_tier
        
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

def user_profile_header():
    if st.session_state.get('logged_in'):
        u = st.session_state.user_data
        
        # အမြဲတမ်း နောက်ဆုံးအခြေအနေ Tier ကို Database ထဲမှ ပြန်ဖတ်နေရန်
        updated_tier_code = get_user_tier(u['email'])
        
        tier_map = {
            "FREE": {"name": "FREE", "color": "#00ff00"}, # F မှ FREE သို့ ပြောင်းလဲထားသည်
            "SILVER": {"name": "SILVER", "color": "#bdc3c7"},
            "GOLD": {"name": "GOLD", "color": "#f1c40f"},
            "DIAMOND": {"name": "DIAMOND", "color": "#9b59b6"}
        }
        
        # Tier အချက်အလက်ကို မြေပုံနှင့် တိုက်စစ်သည်
        t = tier_map.get(updated_tier_code, tier_map["FREE"])

        with st.sidebar:
            st.divider()
            
            # --- Profile Image Display & Uploader ---
            col_img, col_txt = st.columns([0.4, 0.6])
            with col_img:
                st.image(u['photo'], width=60)
            with col_txt:
                st.markdown(f"**{u['name']}**")
                st.markdown(f"<span style='background:{t['color']}; color:black; padding:2px 6px; border-radius:4px; font-size:10px; font-weight:bold;'>{t['name']}</span>", unsafe_allow_html=True)
            
            with st.expander("🖼️ Edit Profile"):
                uploaded_file = st.file_uploader("Choose a photo", type=["jpg", "png", "jpeg"])
                if uploaded_file is not None:
                    st.session_state.user_data['photo'] = uploaded_file
                    st.success("Photo updated!")
                    st.rerun()

            st.write("") 
            if st.button("Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.is_owner = False
                st.session_state.user_name = "Guest"
                st.rerun()
