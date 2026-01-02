import streamlit as st

def ads_manager():
    if not st.session_state.get('is_owner', False):
        st.divider()
        st.markdown("""
            <div style="background: #1e293b; padding: 15px; border-radius: 10px; border: 1px solid #3b82f6; text-align: center;">
                <h4 style="color: #3b82f6; margin:0;">BMT SPONSORED AD</h4>
                <p style="font-size: 14px; color: white;">Upgrade to Diamond for 120s Videos!</p>
            </div>
        """, unsafe_allow_html=True)
