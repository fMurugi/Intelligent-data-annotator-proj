import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth
import webbrowser

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("sch-annotator-proj-firebase-adminsdk-fbsvc-d2077b92af.json")
    firebase_admin.initialize_app(cred)

st.title("User Authentication System")

if "user" not in st.session_state:
    st.session_state["user"] = None

if st.session_state["user"] is None:
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login", key="login_button"):
        try:
            user = auth.get_user_by_email(email)
            st.session_state["user"] = user.email
            st.success(f"Welcome, {user.email}!")

            # Open local HTML file in the browser
            webbrowser.open("/home/fiona/Desktop/tuts/school_project/homePage/map_with_menu.html")

        except:
            st.error("Invalid email or password.")

else:
    st.success(f"Logged in as {st.session_state['user']}")
    
    # Logout Button
    if st.button("Logout", key="logout_button"):
        st.session_state["user"] = None
        st.experimental_rerun()






