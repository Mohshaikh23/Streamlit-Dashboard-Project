import streamlit as st

def get_session_state():
    if "uploaded_data" not in st.session_state:
        st.session_state.uploaded_data = None
    return st.session_state
