import streamlit as st
from utils.ui import ensure_session_keys, init_once
from utils.auth import signup, login

st.set_page_config(page_title="NeuroLearn Software", layout="wide")
init_once()
ensure_session_keys()

st.title("NeuroLearn — Software Edition")
st.caption("Secure login, saved progress, and modular learning tools.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Login")
    with st.form("login_form"):
        email = st.text_input("Email", placeholder="you@example.com")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
    if submitted:
        user = login(email, password)
        if user:
            st.session_state.user = user
            st.session_state.authed = True
            st.success(f"Welcome back, {user['name']}! Go to pages from the sidebar.")
        else:
            st.error("Invalid email or password.")

with col2:
    st.subheader("Sign Up")
    with st.form("signup_form"):
        name = st.text_input("Full Name")
        email2 = st.text_input("Email (new)")
        pw1 = st.text_input("Password", type="password")
        pw2 = st.text_input("Confirm Password", type="password")
        ok = st.form_submit_button("Create Account")
    if ok:
        if not name or not email2 or not pw1:
            st.error("Please fill all fields.")
        elif pw1 != pw2:
            st.error("Passwords do not match.")
        else:
            res = signup(name, email2, pw1)
            if res == "OK":
                st.success("Account created. Please login on the left.")
            else:
                st.error(res)

st.divider()
if st.session_state.authed and st.session_state.user:
    st.info("You're logged in. Use the sidebar to open learning pages (TTS, Quiz, Visuals, Dashboard).")
    if st.button("Logout"):
        st.session_state.user = None
        st.session_state.authed = False
        st.success("Logged out.")
else:
    st.info("New here? Create an account on the right, then login and explore the pages from the sidebar.")
