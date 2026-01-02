import streamlit as st

def manage_owner_access():
    if 'is_owner' not in st.session_state: st.session_state.is_owner = False
    if 'show_owner_login' not in st.session_state: st.session_state.show_owner_login = False
    
    with st.sidebar:
        st.markdown("---")
        if not st.session_state.is_owner:
            if st.button("🛡️ ADMIN ACCESS", use_container_width=True):
                st.session_state.show_owner_login = not st.session_state.show_owner_login
                st.rerun()

        if st.session_state.show_owner_login:
            st.markdown("<h4 style='color:#f1c40f;'>🔑 BMT OWNER LOGIN</h4>", unsafe_allow_html=True)
            with st.form("admin_login_form"):
                pwd = st.text_input("Enter Key", type="password")
                submit = st.form_submit_button("VERIFY", use_container_width=True)
                
                if submit:
                    if pwd == "bmt999":
                        st.session_state.is_owner = True
                        st.session_state.show_owner_login = False
                        st.session_state.page_state = 'admin_dashboard'
                        st.success("OWNER VERIFIED ✅")
                        st.rerun()
                    else:
                        st.error("Access Denied!")

def owner_dashboard():
    # Admin Dashboard စာမျက်နှာ
    st.markdown("<h1 style='color:#f1c40f; text-align:center;'>👑 BMT ADMIN COMMAND CENTER</h1>", unsafe_allow_html=True)
    
    t_keys, t_pricing, t_ads, t_system = st.tabs(["🔑 API KEYS", "💰 PRICING", "📢 ADS CONTROL", "⚙️ SYSTEM"])

    with t_keys:
        st.subheader("Master API Key Management")
        keys_list = ["1. Google Login API", "2. LLM (Chat) API", "3. Image Gen API", "4. Video Gen API", "5. Myanmar TTS API", "6. Lip-Sync API", "7. Audio/SFX API", "8. Payment Gateway", "9. Cloud Storage", "10. Audio Enhance"]
        for key_name in keys_list:
            col_key, col_btn = st.columns([0.8, 0.2])
            with col_key:
                current_val = st.session_state.get(f'secret_{key_name}', 'HIDDEN_KEY_XXXXX')
                st.text_input(key_name, value=current_val, type="password", key=f"input_{key_name}")
            with col_btn:
                st.write("")
                if st.button("Update", key=f"upd_{key_name}"):
                    st.session_state[f'secret_{key_name}'] = st.session_state[f"input_{key_name}"]
                    st.toast(f"{key_name} Updated!")

    with t_pricing:
        st.subheader("Tier Pricing & Promo Control")
        # SILVER, GOLD, DIAMOND
        for tier_name, key_id in [("SILVER", "s"), ("GOLD", "g"), ("DIAMOND", "d")]:
            st.markdown(f"##### {tier_name} TIER")
            c1, c2 = st.columns(2)
            st.session_state[f'{key_id}_price'] = c1.text_input(f"{tier_name} Price", value=st.session_state.get(f'{key_id}_price', "5,000 MMK"), key=f"pr_{key_id}")
            st.session_state[f'{key_id}_promo'] = c2.text_input(f"{tier_name} Promo Tag", value=st.session_state.get(f'{key_id}_promo', "Promo!"), key=f"tr_{key_id}")
            st.divider()
        
        if st.button("SAVE ALL PRICING", use_container_width=True):
            st.success("All Tiers Updated Successfully!")

    with t_ads:
        st.subheader("Google Ads Control")
        st.toggle("Enable Ads Globally", value=True, key="ads_enabled")
        st.slider("Ads Frequency", 1, 10, 3)

    with t_system:
        st.subheader("Monitoring")
        c1, c2 = st.columns(2)
        c1.metric("Daily Users", "150")
        c2.metric("Revenue", "350,000 MMK")
        st.divider()
        # Logout ကို Dashboard ထဲမှာပဲ ထည့်လိုက်ပါမယ် (Error ကင်းအောင်)
        if st.button("🚪 LOGOUT ADMIN", use_container_width=True):
            st.session_state.is_owner = False
            st.session_state.page_state = 'home'
            st.rerun()
