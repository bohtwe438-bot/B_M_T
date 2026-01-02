import streamlit as st
from database import save_user_tier, load_db # Database ချိတ်ဆက်မှု ထည့်သွင်းခြင်း

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
                        st.session_state.user_name = "Owner_Admin" # Owner အမည်ကို မှတ်သား
                        st.session_state.page_state = 'admin_dashboard'
                        st.success("OWNER VERIFIED ✅")
                        st.rerun()
                    else:
                        st.error("Access Denied!")

def owner_dashboard():
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
                # Database ဖိုင်ထဲက Key တွေကို အရင်ဖတ်၊ မရှိမှ default value ပြပါမယ်
                db = load_db()
                current_val = db.get(f'secret_{key_name}', 'HIDDEN_KEY_XXXXX')
                st.text_input(key_name, value=current_val, type="password", key=f"input_{key_name}")
            with col_btn:
                st.write("")
                if st.button("Update", key=f"upd_{key_name}"):
                    # Database ထဲမှာ အသေသိမ်းလိုက်ပါပြီ
                    save_user_tier(f'secret_{key_name}', st.session_state[f"input_{key_name}"])
                    st.toast(f"{key_name} Saved to Database!")

    with t_pricing:
        st.subheader("Tier Pricing & Promo Control")
        db = load_db() # Database မှ လက်ရှိဈေးနှုန်းများ ဖတ်ယူ
        
        # --- SILVER ---
        st.markdown("##### ⚪ SILVER TIER")
        cs1, cs2 = st.columns(2)
        s_price_val = cs1.text_input("Silver Price", value=db.get('s_price', "5,000 MMK"), key="pr_s")
        s_promo_val = cs2.text_input("Silver Promo Tag", value=db.get('s_promo', "Hot Sale!"), key="tr_s")

        # --- GOLD ---
        st.markdown("##### 🟡 GOLD TIER")
        cg1, cg2 = st.columns(2)
        g_price_val = cg1.text_input("Gold Price", value=db.get('g_price', "15,000 MMK"), key="pr_g")
        g_promo_val = cg2.text_input("Gold Promo Tag", value=db.get('g_promo', "Most Popular!"), key="tr_g")

        # --- DIAMOND ---
        st.markdown("##### 💎 DIAMOND TIER")
        cd1, cd2 = st.columns(2)
        d_price_val = cd1.text_input("Diamond Price", value=db.get('d_price', "30,000 MMK"), key="pr_d")
        d_promo_val = cd2.text_input("Diamond Promo Tag", value=db.get('d_promo', "Ultimate Experience!"), key="tr_d")
        
        if st.button("SAVE ALL PRICING", use_container_width=True):
            # ဈေးနှုန်းအားလုံးကို Database ထဲမှာ အသေသိမ်းခြင်း
            save_user_tier('s_price', s_price_val)
            save_user_tier('s_promo', s_promo_val)
            save_user_tier('g_price', g_price_val)
            save_user_tier('g_promo', g_promo_val)
            save_user_tier('d_price', d_price_val)
            save_user_tier('d_promo', d_promo_val)
            st.success("Pricing Saved to Database!")

    with t_ads:
        st.subheader("Google Ads Control")
        db = load_db()
        ads_on = st.toggle("Enable Ads Globally", value=db.get('ads_enabled', True), key="ads_enabled")
        freq = st.slider("Ads Frequency", 1, 10, db.get('ads_freq', 3))
        
        if st.button("Save Ads Settings"):
            save_user_tier('ads_enabled', ads_on)
            save_user_tier('ads_freq', freq)
            st.success("Ads Settings Saved!")

    with t_system:
        st.subheader("System Maintenance")
        db = load_db()
        m_mode = st.toggle("Activate Maintenance Mode", value=db.get('m_mode', False), key="maintenance_mode")
        if st.button("Save System State"):
            save_user_tier('m_mode', m_mode)
            st.success("System State Updated!")
            
        st.divider()
        st.subheader("Monitoring")
        c1, c2, c3 = st.columns(3)
        c1.metric("Daily Users", "150", "+5%")
        c2.metric("Revenue", "350,000 MMK", "Peak")
        history_count = len(st.session_state.get('video_history', []))
        c3.metric("Tasks", history_count)

    st.divider()
    if st.button("🚪 LOGOUT ADMIN", use_container_width=True):
        st.session_state.is_owner = False
        st.session_state.page_state = 'home'
        st.rerun()
