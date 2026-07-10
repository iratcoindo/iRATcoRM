import streamlit as st

from database import (
    Session,
    User,
    verify_password,
    create_default_admin
)

create_default_admin()

st.set_page_config(
    page_title="iRATco Research Monitoring",
    page_icon="🧬",
    layout="centered"
)

if "login" not in st.session_state:
    st.session_state.login = False

if "user" not in st.session_state:
    st.session_state.user = None


def login_page():

    st.title("🧬 iRATco Research Monitoring")

    st.markdown("### Login")

    username = st.text_input("Username")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login", use_container_width=True):

        session = Session()

        user = session.query(User).filter_by(
            username=username
        ).first()

        if user:

            if verify_password(password, user.password):

                st.session_state.login = True
                st.session_state.user = user

                st.rerun()

            else:

                st.error("Password salah.")

        else:

            st.error("Username tidak ditemukan.")

        session.close()


def dashboard():

    st.success(
        f"Selamat datang {st.session_state.user.fullname}"
    )

    st.write("Role :", st.session_state.user.role)

    st.info("Versi 0.1")

    if st.button("Logout"):

        st.session_state.login = False

        st.session_state.user = None

        st.rerun()


if st.session_state.login:

    dashboard()

else:

    login_page()
