import streamlit as st

def login_page():
    st.title("Login")

    # Add your login form here (for example, using email and password)
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if email and password:
            # Add your authentication logic here
            # Example: Assume login is always successful
            st.session_state["user"] = email
            st.success(f"Logged in as {email}")
            st.session_state["page"] = "home"  # Redirect back to home
            st.experimental_rerun()
        else:
            st.error("Please enter both email and password.")

if st.session_state.get("page") == "login":
    login_page()
