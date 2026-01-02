import streamlit as st

def manage_owner_access():
    if 'is_owner' not in st.session_state: st.session_state.is_owner = False
    if 'show_owner_login' not in st.session_state: st.session_state.show_owner_login = False
    
    with st.sidebar:
        st.markdown("---")
        # 🛡️ ခလုတ်ကို နှိပ်လိုက်ရင် Login Box ပေါ်လာမယ်
        if st.button("🛡️ ADMIN ACCESS", use_container_width=True):
            st.session_state.show_owner_login = not st.session_state.show_owner_login
            st.rerun()

        if st.session_state.show_owner_login:
            st.markdown("<h4 style='color:#f1c40f;'>🔑 BMT OWNER LOGIN</h4>", unsafe_allow_html=True)
            # Password ကို Form နဲ့ သုံးမှ Enter ခေါက်ရင် တန်းဝင်မှာပါ
            with st.form("admin_login_form"):
                pwd = st.text_input("Enter Key", type="password")
                submit = st.form_submit_button("VERIFY", use_container_width=True)
                
                if submit:
                    if pwd == "bmt999":
                        st.session_state.is_owner = True
                        st.session_state.show_owner_login = False # Login box ပြန်ဖျောက်မယ်
                        st.success("OWNER VERIFIED ✅")
                        st.rerun() # UI အသစ်ကို ချက်ချင်းပြောင်းမယ်
                    else:
                        st.error("Access Denied!")

def owner_dashboard():
    # ဒီနေရာမှာ is_owner ကို သေချာစစ်ဆေးပါတယ်
    if st.session_state.get('is_owner'):
        st.markdown("<h1 style='color:#f1c40f; text-align:center;'>👑 BMT ADMIN COMMAND CENTER</h1>", unsafe_allow_html=True)
        
        # Tabs ခွဲခြားခြင်း (Master API ၁၀ ခုလုံး ပါဝင်သည်)
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
                    # Key တွေကို Session မှာ အမြဲသိမ်းထားမယ်
                    current_val = st.session_state.get(f'secret_{key_name}', 'HIDDEN_KEY_XXXXX')
                    new_val = st.text_input(key_name, value=current_val, type="password", key=f"input_{key_name}")
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
            # Video count logic
            history_count = len(st.session_state.get('video_history', []))
            c3.metric("Tasks", history_count)

        st.divider()
        if st.button("🚪 LOGOUT ADMIN", use_container_width=True):
            st.session_state.is_owner = False
            st.rerun()
