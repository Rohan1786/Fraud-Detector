# import streamlit as st
# import pyrebase
# import os
# import firebase_admin
# from firebase_admin import credentials, auth
# import time

# # --- Page Config ---
# st.set_page_config(
#     page_title="UPI Fraud Detection | Login",
#     page_icon="🔒",
#     layout="centered"
# )

# # --- Firebase Setup ---
# if not firebase_admin._apps:
#     cred = credentials.Certificate("serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)

# firebase_config = {
#     "apiKey": "AIzaSyDmRLIlWmrG6luirX8ElFD6XXqlVF05CNk",
#     "authDomain": "ai-visualization-web-app.firebaseapp.com",
#     "projectId": "ai-visualization-web-app",
#     "storageBucket": "ai-visualization-web-app.appspot.com",
#     "messagingSenderId": "471686906282",
#     "appId": "1:471686906282:web:caf4b441312f11bd0a6bd3",
#     "measurementId": "G-NZ8TTXJL1V",
#     "databaseURL": ""
# }

# firebase = pyrebase.initialize_app(firebase_config)
# auth_fb = firebase.auth()  # Changed from auth_db to auth_fb to match your variable

# # --- UI Styles ---
# st.markdown("""
# <style>
#     .main {
#         max-width: 400px;
#         padding: 2rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         margin: 0 auto;
#     }
#     .stTextInput>div>div>input {
#         padding: 10px !important;
#     }
#     .stButton>button {
#         width: 100%;
#         padding: 0.5rem;
#         border-radius: 5px;
#     }
#     .error {
#         color: #ff4b4b;
#         font-size: 0.9rem;
#     }
# </style>
# """, unsafe_allow_html=True)

# # --- Auth Functions ---
# def handle_login(email, password):
#     try:
#         if email == "admin@gmail.com" and password == "Admin@123":
#             st.session_state.user = {"email": "admin@gmail.com", "is_admin": True}
#             st.success("Admin login successful!")
#             time.sleep(1)
#             os.system("python -m streamlit run upi_fraud.py")
#             st.stop()
#         else:
#             user = auth_fb.sign_in_with_email_and_password(email, password)  # Changed to auth_fb
#             st.session_state.user = user
#             st.success("Login successful!")
#             time.sleep(1)
#             os.system("python -m streamlit run streamlit_app.py")
#             st.stop()
#     except Exception as e:
#         st.error(f"Invalid email or password: {str(e)}")  # Added error details

# def handle_signup(email, password):
#     try:
#         auth_fb.create_user_with_email_and_password(email, password)  # Changed to auth_fb
#         st.success("Account created! Please login")
#         time.sleep(1)
#         st.session_state.current_tab = "Sign In"
#         st.rerun()
#     except Exception as e:
#         if "EMAIL_EXISTS" in str(e):
#             st.error("Email already exists. Please login instead.")
#         else:
#             st.error(f"Error creating account: {str(e)}")  # Added error details

# def show_forgot_password_page():
#     st.title("Reset Password")
#     email = st.text_input("Registered Email", placeholder="your@email.com")
#     new_password = st.text_input("New Password", type="password", placeholder="••••••••")
#     confirm_password = st.text_input("Confirm New Password", type="password", placeholder="••••••••")
    
#     if st.button("Update Password"):
#         if not all([email, new_password, confirm_password]):
#             st.error("Please fill all fields")
#         elif new_password != confirm_password:
#             st.error("Passwords don't match")
#         elif len(new_password) < 6:
#             st.error("Password must be 6+ characters")
#         else:
#             try:
#                 # Get user by email
#                 user = auth.get_user_by_email(email)
#                 # Update password
#                 auth.update_user(user.uid, password=new_password)
#                 st.success("Password updated successfully! Please login with your new password.")
#                 time.sleep(2)
#                 st.session_state.show_forgot_password = False
#                 st.rerun()
#             except Exception as e:
#                 st.error(f"Failed to update password: {str(e)}")

# # --- Main UI ---
# if st.session_state.get('show_forgot_password', False):
#     show_forgot_password_page()
# else:
#     st.title("UPI Fraud Detection")
#     st.subheader("Secure Authentication")

#     # Tab selection
#     if 'current_tab' not in st.session_state:
#         st.session_state.current_tab = "Sign In"

#     tabs = ["Sign In", "Sign Up"]
#     current_tab = st.radio("", tabs, index=tabs.index(st.session_state.current_tab), 
#                           horizontal=True, label_visibility="collapsed")

#     st.session_state.current_tab = current_tab

#     # Tab content
#     with st.container():
#         if current_tab == "Sign In":
#             email = st.text_input("Email", placeholder="Enter your email", key="login_email")
#             password = st.text_input("Password", type="password", placeholder="••••••••", key="login_password")
            
#             if st.button("Login", type="primary", key="login_btn"):
#                 if email and password:
#                     handle_login(email, password)
#                 else:
#                     st.error("Please fill all fields")
                    
#             if st.button("Forgot Password?", key="forgot_btn"):
#                 st.session_state.show_forgot_password = True
#                 st.rerun()
            
#         else:  # Sign Up
#             email = st.text_input("Email", placeholder="your@email.com", key="signup_email")
#             password = st.text_input("Password", type="password", placeholder="Create password (min 6 chars)", key="signup_password")
#             confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter password", key="confirm_password")
            
#             if st.button("Create Account", type="primary", key="signup_btn"):
#                 if not all([email, password, confirm]):
#                     st.error("Please fill all fields")
#                 elif password != confirm:
#                     st.error("Passwords don't match")
#                 elif len(password) < 6:
#                     st.error("Password must be 6+ characters")
#                 else:
#                     handle_signup(email, password)

# # Status message area
# if 'auth_message' in st.session_state:
#     st.info(st.session_state.auth_message)
#     del st.session_state.auth_message


# import streamlit as st
# import pyrebase
# import os
# import firebase_admin
# from firebase_admin import credentials, auth
# import time
# import webbrowser
# from urllib.parse import urlparse, parse_qs

# # --- Page Config ---
# st.set_page_config(
#     page_title="UPI Fraud Detection | Login",
#     page_icon="🔒",
#     layout="centered"
# )

# # --- Firebase Setup ---
# if not firebase_admin._apps:
#     cred = credentials.Certificate("serviceAccountKey.json")
#     firebase_admin.initialize_app(cred)

# firebase_config = {
#     "apiKey": "AIzaSyDmRLIlWmrG6luirX8ElFD6XXqlVF05CNk",
#     "authDomain": "ai-visualization-web-app.firebaseapp.com",
#     "projectId": "ai-visualization-web-app",
#     "storageBucket": "ai-visualization-web-app.appspot.com",
#     "messagingSenderId": "471686906282",
#     "appId": "1:471686906282:web:caf4b441312f11bd0a6bd3",
#     "measurementId": "G-NZ8TTXJL1V",
#     "databaseURL": ""
# }

# firebase = pyrebase.initialize_app(firebase_config)
# auth_fb = firebase.auth()

# # --- UI Styles ---
# st.markdown("""
# <style>
#     .main {
#         max-width: 400px;
#         padding: 2rem;
#         border-radius: 10px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
#         margin: 0 auto;
#     }
#     .stTextInput>div>div>input {
#         padding: 10px !important;
#     }
#     .stButton>button {
#         width: 100%;
#         padding: 0.5rem;
#         border-radius: 5px;
#         margin: 0.25rem 0;
#     }
#     .google-btn {
#         background-color: #4285F4 !important;
#         color: white !important;
#     }
#     .error {
#         color: #ff4b4b;
#         font-size: 0.9rem;
#     }
#     .divider {
#         display: flex;
#         align-items: center;
#         text-align: center;
#         margin: 1rem 0;
#     }
#     .divider::before, .divider::after {
#         content: "";
#         flex: 1;
#         border-bottom: 1px solid #ddd;
#     }
#     .divider-text {
#         padding: 0 10px;
#     }
# </style>
# """, unsafe_allow_html=True)

# # --- Auth Functions ---
# def handle_login(email, password):
#     try:
#         if email == "admin@gmail.com" and password == "Admin@123":
#             st.session_state.user = {"email": "admin@gmail.com", "is_admin": True}
#             st.success("Admin login successful!")
#             time.sleep(1)
#             os.system("python -m streamlit run upi_fraud.py")
#             st.stop()
#         else:
#             user = auth_fb.sign_in_with_email_and_password(email, password)
#             st.session_state.user = user
#             st.success("Login successful!")
#             time.sleep(1)
#             os.system("python -m streamlit run streamlit_app.py")
#             st.stop()
#     except Exception as e:
#         st.error(f"Invalid email or password: {str(e)}")

# def handle_signup(email, password):
#     try:
#         auth_fb.create_user_with_email_and_password(email, password)
#         st.success("Account created! Please login")
#         time.sleep(1)
#         st.session_state.current_tab = "Sign In"
#         st.rerun()
#     except Exception as e:
#         if "EMAIL_EXISTS" in str(e):
#             st.error("Email already exists. Please login instead.")
#         else:
#             st.error(f"Error creating account: {str(e)}")

# def handle_google_signin():
#     try:
#         # This is a simplified approach - in production, use Firebase UI or proper OAuth flow
#         auth_url = f"https://{firebase_config['authDomain']}/__/auth/handler"
#         webbrowser.open_new_tab(auth_url)
#         st.info("Please complete Google Sign-In in the browser window that opened")
#     except Exception as e:
#         st.error(f"Google Sign-In failed: {str(e)}")

# def show_forgot_password_page():
#     st.title("Reset Password")
#     email = st.text_input("Registered Email", placeholder="your@email.com")
#     new_password = st.text_input("New Password", type="password", placeholder="••••••••")
#     confirm_password = st.text_input("Confirm New Password", type="password", placeholder="••••••••")
    
#     if st.button("Update Password"):
#         if not all([email, new_password, confirm_password]):
#             st.error("Please fill all fields")
#         elif new_password != confirm_password:
#             st.error("Passwords don't match")
#         elif len(new_password) < 6:
#             st.error("Password must be 6+ characters")
#         else:
#             try:
#                 user = auth.get_user_by_email(email)
#                 auth.update_user(user.uid, password=new_password)
#                 st.success("Password updated successfully! Please login with your new password.")
#                 time.sleep(2)
#                 st.session_state.show_forgot_password = False
#                 st.rerun()
#             except Exception as e:
#                 st.error(f"Failed to update password: {str(e)}")

# # --- Main UI ---
# if st.session_state.get('show_forgot_password', False):
#     show_forgot_password_page()
# else:
#     st.title("UPI Fraud Detection")
#     st.subheader("Secure Authentication")

#     # Tab selection
#     if 'current_tab' not in st.session_state:
#         st.session_state.current_tab = "Sign In"

#     tabs = ["Sign In", "Sign Up"]
#     current_tab = st.radio("", tabs, index=tabs.index(st.session_state.current_tab), 
#                           horizontal=True, label_visibility="collapsed")

#     st.session_state.current_tab = current_tab

#     # Tab content
#     with st.container():
#         if current_tab == "Sign In":
#             email = st.text_input("Email", placeholder="Enter your email", key="login_email")
#             password = st.text_input("Password", type="password", placeholder="••••••••", key="login_password")
            
#             if st.button("Login", type="primary", key="login_btn"):
#                 if email and password:
#                     handle_login(email, password)
#                 else:
#                     st.error("Please fill all fields")
                    
#             if st.button("Forgot Password?", key="forgot_btn"):
#                 st.session_state.show_forgot_password = True
#                 st.rerun()
            
#             # Google Sign-In Button
#             st.markdown('<div class="divider"><span class="divider-text">OR</span></div>', unsafe_allow_html=True)
#             if st.button("Sign in with Google", key="google_btn", type="secondary", help="Sign in using your Google account"):
#                 handle_google_signin()
            
#         else:  # Sign Up
#             email = st.text_input("Email", placeholder="your@email.com", key="signup_email")
#             password = st.text_input("Password", type="password", placeholder="Create password (min 6 chars)", key="signup_password")
#             confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter password", key="confirm_password")
            
#             if st.button("Create Account", type="primary", key="signup_btn"):
#                 if not all([email, password, confirm]):
#                     st.error("Please fill all fields")
#                 elif password != confirm:
#                     st.error("Passwords don't match")
#                 elif len(password) < 6:
#                     st.error("Password must be 6+ characters")
#                 else:
#                     handle_signup(email, password)

# # Status message area
# if 'auth_message' in st.session_state:
#     st.info(st.session_state.auth_message)
#     del st.session_state.auth_message

import streamlit as st
import pyrebase
import os
import firebase_admin
from firebase_admin import credentials, auth
import time
import webbrowser
from urllib.parse import urlparse, parse_qs

# --- Page Config ---
st.set_page_config(
    page_title="UPI Fraud Detection | Login",
    page_icon="🔒",
    layout="centered"
)

# --- Firebase Setup ---
if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

firebase_config = {
    "apiKey": "AIzaSyDmRLIlWmrG6luirX8ElFD6XXqlVF05CNk",
    "authDomain": "ai-visualization-web-app.firebaseapp.com",
    "projectId": "ai-visualization-web-app",
    "storageBucket": "ai-visualization-web-app.appspot.com",
    "messagingSenderId": "471686906282",
    "appId": "1:471686906282:web:caf4b441312f11bd0a6bd3",
    "measurementId": "G-NZ8TTXJL1V",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebase_config)
auth_fb = firebase.auth()

# --- UI Styles ---
st.markdown("""
<style>
    .main {
        max-width: 400px;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 0 auto;
    }
    .stTextInput>div>div>input {
        padding: 10px !important;
    }
    .stButton>button {
        width: 100%;
        padding: 0.5rem;
        border-radius: 5px;
        margin: 0.25rem 0;
    }
    .google-btn {
        background-color: #4285F4 !important;
        color: white !important;
    }
    .error {
        color: #ff4b4b;
        font-size: 0.9rem;
    }
    .divider {
        display: flex;
        align-items: center;
        text-align: center;
        margin: 1rem 0;
    }
    .divider::before, .divider::after {
        content: "";
        flex: 1;
        border-bottom: 1px solid #ddd;
    }
    .divider-text {
        padding: 0 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- Auth Functions ---
def handle_login(email, password):
    try:
        if email == "admin@gmail.com" and password == "Admin@123":
            st.session_state.user = {"email": "admin@gmail.com", "is_admin": True}
            st.success("Admin login successful!")
            time.sleep(1)
            os.system("python -m streamlit run upi_fraud.py")
            st.stop()
        else:
            user = auth_fb.sign_in_with_email_and_password(email, password)
            st.session_state.user = user
            st.success("Login successful!")
            time.sleep(1)
            os.system("python -m streamlit run streamlit_app.py")
            st.stop()
    except Exception as e:
        st.error(f"Invalid email or password: {str(e)}")

def handle_signup(email, password, username):
    try:
        # Create user with email and password
        user = auth_fb.create_user_with_email_and_password(email, password)
        
        # Get the UID of the newly created user
        uid = user['localId']
        
        # Update the user's display name with the username
        auth.update_user(uid, display_name=username)
        
        st.success("Account created successfully! Please login")
        time.sleep(1)
        st.session_state.current_tab = "Sign In"
        st.rerun()
    except Exception as e:
        if "EMAIL_EXISTS" in str(e):
            st.error("Email already exists. Please login instead.")
        else:
            st.error(f"Error creating account: {str(e)}")

def handle_google_signin():
    try:
        # This is a simplified approach - in production, use Firebase UI or proper OAuth flow
        auth_url = f"https://{firebase_config['authDomain']}/__/auth/handler"
        webbrowser.open_new_tab(auth_url)
        st.info("Please complete Google Sign-In in the browser window that opened")
    except Exception as e:
        st.error(f"Google Sign-In failed: {str(e)}")

def show_forgot_password_page():
    st.title("Reset Password")
    email = st.text_input("Registered Email", placeholder="your@email.com")
    new_password = st.text_input("New Password", type="password", placeholder="••••••••")
    confirm_password = st.text_input("Confirm New Password", type="password", placeholder="••••••••")
    
    if st.button("Update Password"):
        if not all([email, new_password, confirm_password]):
            st.error("Please fill all fields")
        elif new_password != confirm_password:
            st.error("Passwords don't match")
        elif len(new_password) < 6:
            st.error("Password must be 6+ characters")
        else:
            try:
                user = auth.get_user_by_email(email)
                auth.update_user(user.uid, password=new_password)
                st.success("Password updated successfully! Please login with your new password.")
                time.sleep(2)
                st.session_state.show_forgot_password = False
                st.rerun()
            except Exception as e:
                st.error(f"Failed to update password: {str(e)}")

# --- Main UI ---
if st.session_state.get('show_forgot_password', False):
    show_forgot_password_page()
else:
    st.title("UPI Fraud Detection")
    st.subheader("Secure Authentication")

    # Tab selection
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "Sign In"

    tabs = ["Sign In", "Sign Up"]
    current_tab = st.radio("", tabs, index=tabs.index(st.session_state.current_tab), 
                          horizontal=True, label_visibility="collapsed")

    st.session_state.current_tab = current_tab

    # Tab content
    with st.container():
        if current_tab == "Sign In":
            email = st.text_input("Email", placeholder="Enter your email", key="login_email")
            password = st.text_input("Password", type="password", placeholder="••••••••", key="login_password")
            
            if st.button("Login", type="primary", key="login_btn"):
                if email and password:
                    handle_login(email, password)
                else:
                    st.error("Please fill all fields")
                    
            if st.button("Forgot Password?", key="forgot_btn"):
                st.session_state.show_forgot_password = True
                st.rerun()
            
            # Google Sign-In Button
            st.markdown('<div class="divider"><span class="divider-text">OR</span></div>', unsafe_allow_html=True)
            if st.button("Sign in with Google", key="google_btn", type="secondary", help="Sign in using your Google account"):
                handle_google_signin()
            
        else:  # Sign Up
            username = st.text_input("Username", placeholder="Enter your username", key="signup_username")
            email = st.text_input("Email", placeholder="your@email.com", key="signup_email")
            password = st.text_input("Password", type="password", placeholder="Create password (min 6 chars)", key="signup_password")
            confirm = st.text_input("Confirm Password", type="password", placeholder="Re-enter password", key="confirm_password")
            
            if st.button("Create Account", type="primary", key="signup_btn"):
                if not all([username, email, password, confirm]):
                    st.error("Please fill all fields")
                elif password != confirm:
                    st.error("Passwords don't match")
                elif len(password) < 6:
                    st.error("Password must be 6+ characters")
                else:
                    handle_signup(email, password, username)

# Status message area
if 'auth_message' in st.session_state:
    st.info(st.session_state.auth_message)
    del st.session_state.auth_message