import streamlit as st

def manage_owner_access():
    if 'is_owner' not in st.session_state: st.session_state.is_owner = False
    if 'show_owner_login' not in st.session_state: st.session_state.show_owner_login = False
    
    with st.sidebar:
        # Logo ကို နှိပ်လျှင် Password Box ပေါ်လာစေရန် (Hidden Trigger)
        # အောက်က URL မှာ Owner ရဲ့ Logo link ပြောင်းထည့်နိုင်ပါတယ်
        logo_url = "https://cdn-icons-png.flaticon.com/512/3135/3135715.png" 
        if st.button("🛡️", help="Hidden Admin Access", use_container_width=False):
            st.session_state.show_owner_login = not st.session_state.show_owner_login

        if st.session_state.show_owner_login:
            st.header("🔑 BMT Access")
            pwd = st.text_input("Owner Password", type="password")
            if pwd == "bmt999":
                st.session_state.is_owner = True
                st.markdown('<div style="color:#3b82f6; font-weight:bold;">OWNER VERIFIED ✅</div>', unsafe_allow_html=True)
            else:
                st.session_state.is_owner = False

def owner_dashboard():
    # --- မူရင်း Dashboard ကုဒ်များ (Business Insights + API Keys) အားလုံး ဤနေရာတွင် ဆက်ရှိနေမည် ---
    if st.session_state.get('is_owner'):
        st.divider()
        st.subheader("📊 BMT Business Insights")
        c1, c2, c3 = st.columns(3)
        c1.metric("Daily Users", "150", "+5%")
        c2.metric("Revenue", "350,000 MMK", "Peak")
        history_count = len(st.session_state.get('video_history', [])) if st.session_state.get('video_history') else 0
        c3.metric("Tasks", history_count)

        st.divider()
        st.subheader("⚙️ MASTER API KEYS (SECURE STORAGE)")
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
        
        st.divider()
        st.success("🔒 Cloud Database Sync: Connected")
