import streamlit as st

# --- Simple hardcoded login check ---
def login_user(username, password):
    return username == "admin" and password == "1234"

# --- Decorator for authentication check ---
def requires_authentication(func):
    def wrapper(*args, **kwargs):
        if not st.session_state.get("authenticated", False):
            st.warning("🚫 Please log in to access this feature.")
            return  # Block access
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

# --- Logout button ---
def logout_button():
    if st.sidebar.button("🚪 Logout"):
        st.session_state.authenticated = False
        st.success("🔓 Logged out successfully")

# --- Protected content ---
@requires_authentication
def view_secret():
    st.subheader("🤫 Secret Page")
    st.info("This is a secret page visible only to logged-in users!")

    st.write("🎉 Welcome, admin! You made it.")
    
    # Example: secret image or file
    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", caption="Top Secret Fun")
    st.download_button("📄 Download Secret File", data="Top secret content inside.", file_name="secret.txt")

# --- Main App ---
def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    st.sidebar.title("🔧 Navigation")
    choice = st.sidebar.radio("Go to", ["Login", "Secret Page"])

    if st.session_state.authenticated:
        logout_button()

    if choice == "Login":
        login_form()
    elif choice == "Secret Page":
        view_secret()

# --- Run App ---
if __name__ == "__main__":
    main()
