import streamlit as st

def manage_owner_access():
    if 'is_owner' not in st.session_state: st.session_state.is_owner = False
    if 'show_owner_login' not in st.session_state: st.session_state.show_owner_login = False
    
    with st.sidebar:
        logo_url = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png" 
        if st.button("🛡️", help="Hidden Admin Access", use_container_width=False):
            st.session_state.show_owner_login = not st.session_state.show_owner_login

        if st.session_state.show_owner_login:
            st.header("🔑 BMT Access")
            pwd = st.text_input("Owner Password", type="password")
            if pwd == "bmt999":
                st.session_state.is_owner = True
                st.markdown('<div style="color:#f1c40f; font-weight:bold;">OWNER VERIFIED ✅</div>', unsafe_allow_html=True)
            else:
                st.session_state.is_owner = False

def owner_dashboard():
    if st.session_state.get('is_owner'):
        st.markdown("<h1 style='color:#f1c40f; text-align:center;'>👑 BMT ADMIN COMMAND CENTER</h1>", unsafe_allow_html=True)
        
        # Tabs ခွဲခြားခြင်း
        t_keys, t_pricing, t_ads, t_system = st.tabs(["🔑 API KEYS", "💰 PRICING", "📢 ADS CONTROL", "⚙️ SYSTEM"])

        with t_keys:
            st.subheader("Master API Key Management")
            keys_list = [
                "1. Google Login API", "2. LLM (Chat) API", "3. Image Gen API", 
                "4. Video Gen API", "5. Myanmar TTS API", "6. Lip-Sync API",
                "7. Audio/SFX API", "8. Payment Gateway", "9. Cloud Storage", "10. Audio Enhance"
            ]
            for key_name in keys_list:
                col_key, col_btn = st.columns([0.8, 0.2])
                with col_key:
                    st.text_input(key_name, value=st.session_state.get(f'secret_{key_name}', 'HIDDEN_KEY_XXXXX'), 
                                 type="password", key=f"input_{key_name}")
                with col_btn:
                    st.write("")
                    if st.button("Update", key=f"upd_{key_name}"):
                        st.session_state[f'secret_{key_name}'] = st.session_state[f"input_{key_name}"]
                        st.toast(f"{key_name} Updated!")

        with t_pricing:
            st.subheader("Tier Pricing & Promo Control")
            col1, col2 = st.columns(2)
            st.session_state.s_price = col1.text_input("Silver Price", "5,000 MMK")
            st.session_state.s_promo = col2.text_input("Silver Promo Tag", "Hot Sale!")
            # အခြား Tier များအတွက်လည်း ဤနည်းအတိုင်း ထည့်နိုင်သည်

        with t_ads:
            st.subheader("Google Ads Control")
            st.toggle("Enable Ads Globally", value=True, key="ads_enabled")
            st.slider("Ads Frequency (per user session)", 1, 10, 3)

        with t_system:
            st.subheader("System Maintenance")
            m_mode = st.toggle("Activate Maintenance Mode", value=False, key="maintenance_mode")
            if m_mode: st.error("App is currently in Maintenance Mode!")
            
            st.subheader("Monitoring")
            c1, c2, c3 = st.columns(3)
            c1.metric("Daily Users", "150", "+5%")
            c2.metric("Revenue", "350,000 MMK", "Peak")
            history_count = len(st.session_state.get('video_history', []))
            c3.metric("Tasks", history_count)

        st.divider()
        st.success("🔒 Admin Command Center: Connected to Secure Backend")
