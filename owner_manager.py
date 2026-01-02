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
        st.divider()
        st.subheader("📊 BMT Business Insights")
        c1, c2, c3 = st.columns(3)
        c1.metric("Daily Users", "150", "+5%")
        c2.metric("Revenue", "350,000 MMK", "Peak")
        c3.metric("Tasks", len(st.session_state.get('video_history', [])))
