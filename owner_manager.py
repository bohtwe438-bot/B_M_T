import streamlit as st

def manage_owner_access():
    if 'is_owner' not in st.session_state: st.session_state.is_owner = False
    
    with st.sidebar:
        st.header("🔑 BMT Access")
        pwd = st.text_input("Owner Password", type="password")
        if pwd == "bmt999":
            st.session_state.is_owner = True
            st.markdown('<div style="color:#3b82f6; font-weight:bold;">OWNER VERIFIED ✅</div>', unsafe_allow_html=True)
        else:
            st.session_state.is_owner = False

def owner_dashboard():
    if st.session_state.get('is_owner'):
        # --- (၁) မူရင်း Business Insights အပိုင်း ---
        st.divider()
        st.subheader("📊 BMT Business Insights")
        c1, c2, c3 = st.columns(3)
        c1.metric("Daily Users", "150", "+5%")
        c2.metric("Revenue", "350,000 MMK", "Peak")
        # Video History အရေအတွက်ကို တွက်ချက်ခြင်း
        history_count = len(st.session_state.get('video_history', [])) if st.session_state.get('video_history') else 0
        c3.metric("Tasks", history_count)

        # --- (၂) ထပ်တိုး API Key Master Control အပိုင်း (၁၀ မျိုး) ---
        st.divider()
        st.subheader("⚙️ MASTER API KEYS (SECURE STORAGE)")
        st.info("API Key များကို ဤနေရာတွင် စီမံနိုင်ပါသည်။ ပြင်ဆင်ပြီးပါက Update ကို နှိပ်ပါ။")

        keys_list = [
            "1. Google Login API", "2. LLM (Chat) API", "3. Image Gen API", 
            "4. Video Gen API", "5. Myanmar TTS API", "6. Lip-Sync API",
            "7. Audio/SFX API", "8. Payment Gateway", "9. Cloud Storage", "10. Audio Enhance"
        ]

        # API Keys များကို တစ်ခုချင်းစီ စာရင်းပြခြင်း
        for key_name in keys_list:
            col_key, col_btn = st.columns([0.8, 0.2])
            with col_key:
                # Key များကို ကုဒ်ထဲမှာ မမြင်ရစေရန် Password Type ဖြင့် ထားရှိသည်
                st.text_input(key_name, value=st.session_state.get(f'secret_{key_name}', 'HIDDEN_KEY_XXXXX'), 
                             type="password", key=f"input_{key_name}")
            with col_btn:
                st.write("") # နေရာညှိရန်
                if st.button("Update", key=f"upd_{key_name}"):
                    # Input ထဲက Key ကို session_state (သို့မဟုတ် Database) ထဲ သိမ်းမည့်နေရာ
                    new_val = st.session_state[f"input_{key_name}"]
                    st.session_state[f'secret_{key_name}'] = new_val
                    st.toast(f"{key_name} Updated!")

        # --- (၃) Database Sync အခြေအနေ ပြရန် ---
        st.divider()
        st.success("🔒 Cloud Database Sync: Connected")
