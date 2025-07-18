import streamlit as st

# --- Simple hardcoded login check ---
def login_user(username, password):
    return username == "admin" and password == "1234"

# --- Decorator for authentication check ---
def requires_authentication(func):
    def wrapper(*args, **kwargs):
        if not st.session_state.get("authenticated", False):
            st.warning("🚫 Please log in to access this feature.")
            return
        return func(*args, **kwargs)
    return wrapper

# --- Login form ---
def login_form():
    st.title("🔐 Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if login_user(username, password):
            st.session_state.authenticated = True
            st.success("✅ Logged in successfully")
        else:
            st.error("❌ Invalid credentials")

# --- Protected content ---
@requires_authentication
def view_secret():
    st.subheader("🤫 Secret Page")
    st.info("This is a secret page visible only to logged-in users!")

# --- Main App ---
def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    st.sidebar.title("Navigation")
    choice = st.sidebar.radio("Go to", ["Login", "Secret Page"])

    if choice == "Login":
        login_form()
    elif choice == "Secret Page":
        view_secret()

# --- Run App ---
if __name__ == "__main__":
    main()
