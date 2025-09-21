import streamlit as st
from .db import init_db

def ensure_session_keys():
    if "user" not in st.session_state:
        st.session_state.user = None
    if "authed" not in st.session_state:
        st.session_state.authed = False

def require_auth():
    ensure_session_keys()
    if not st.session_state.authed:
        st.warning("Please log in from Home page to access this section.")
        st.stop()

def init_once():
    init_db()
