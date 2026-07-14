import streamlit as st
from Modules.auth import login

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="iRATco Research Management System",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# SESSION
# ==========================

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = None

# ==========================
# LOGIN PAGE
# ==========================

def login_page():

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown("<br><br>", unsafe_allow_html=True)

        st.markdown(
            "<h1 style='text-align:center;'>🧬 iRATco RMS</h1>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<h4 style='text-align:center;color:gray;'>Research Management System</h4>",
            unsafe_allow_html=True
        )

        st.markdown("---")

        username = st.text_input(
            "Username",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            type="password",
            placeholder="Enter password"
        )

        if st.button(
            "LOGIN",
            use_container_width=True
        ):

            user = login(username, password)

            if user is not None:

                st.session_state.login = True
                st.session_state.user = user

                st.rerun()

            else:

                st.error("Username atau password salah.")

        st.markdown("---")

        st.caption("Version 1.0")
        st.caption("© 2026 iRATco Bioceuticals")

# ==========================
# DASHBOARD
# ==========================

def dashboard():

    st.sidebar.success(
        f"👤 {st.session_state.user['fullname']}"
    )

    st.sidebar.write(
        f"Role : {st.session_state.user['role']}"
    )

    st.sidebar.divider()

    if st.sidebar.button("Logout"):

        st.session_state.login = False
        st.session_state.user = None

        st.rerun()

    st.title("🏠 Dashboard")

    st.success(
        f"Welcome, {st.session_state.user['fullname']}"
    )

    st.write(
        "Selamat datang di iRATco Research Management System."
    )

# ==========================
# MAIN
# ==========================

if st.session_state.login:

    dashboard()

else:

    login_page()
