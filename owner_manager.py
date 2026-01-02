import streamlit as st

def manage_owner_access():
    # Session state initialization
    if 'is_owner' not in st.session_state: st.session_state.is_owner = False
    if 'show_owner_login' not in st.session_state: st.session_state.show_owner_login = False
    
    with st.sidebar:
        st.markdown("---")
        # အကယ်၍ Owner Login ဝင်မထားရသေးရင် Admin Access ခလုတ်ပြမယ်
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
                        st.session_state.page_state = 'admin_dashboard' # တန်းပြီး Dashboard ပို့မယ်
                        st.success("OWNER VERIFIED ✅")
                        st.rerun()
                    else:
                        st.error("Access Denied!")

def owner_dashboard():
    # အရေးကြီးသည်- Dashboard စာမျက်နှာတွင် Sidebar Menu ကိုပါ မြင်ရစေရန် st.stop() မသုံးတော့ပါ
    st.markdown("<h1 style='color:#f1c40f; text-align:center;'>👑 BMT ADMIN COMMAND CENTER</h1>", unsafe_allow_html=True)
    
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
                current_val = st.session_state.get(f'secret_{key_name}', 'HIDDEN_KEY_XXXXX')
                st.text_input(key_name, value=current_val, type="password", key=f"input_{key_name}")
            with col_btn:
                st.write("")
                if st.button("Update", key=f"upd_{key_name}"):
                    st.session_state[f'secret_{key_name}'] = st.session_state[f"input_{key_name}"]
                    st.toast(f"{key_name} Updated!")

    with t_pricing:
        st.subheader("Tier Pricing & Promo Control")
        
        # --- SILVER ---
        st.markdown("##### ⚪ SILVER TIER")
        cs1, cs2 = st.columns(2)
        st.session_state.s_price = cs1.text_input("Silver Price", "5,000 MMK", key="pr_s")
        st.session_state.s_promo = cs2.text_input("Silver Promo Tag", "Hot Sale!", key="tr_s")
        st.divider()

        # --- GOLD ---
        st.markdown("##### 🟡 GOLD TIER")
        cg1, cg2 = st.columns(2)
        st.session_state.g_price = cg1.text_input("Gold Price", "15,000 MMK", key="pr_g")
        st.session_state.g_promo = cg2.text_input("Gold Promo Tag", "Most Popular!", key="tr_g")
        st.divider()

        # --- DIAMOND ---
        st.markdown("##### 💎 DIAMOND TIER")
        cd1, cd2 = st.columns(2)
        st.session_state.d_price = cd1.text_input("Diamond Price", "30,000 MMK", key="pr_d")
        st.session_state.d_promo = cd2.text_input("Diamond Promo Tag", "Ultimate Experience!", key="tr_d")
        
        if st.button("SAVE ALL PRICING", use_container_width=True):
            st.success("All Tiers Updated Successfully!")

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
    if st.sidebar.button("🚪 LOGOUT ADMIN", use_container_width=True):
        st.session_state.is_owner = False
        st.session_state.page_state = 'home'
        st.rerun()
