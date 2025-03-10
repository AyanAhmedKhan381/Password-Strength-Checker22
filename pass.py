import streamlit as st
from password_strength import PasswordStats
import random

# Page Config
st.set_page_config(page_title="🔒 Password Strength Meter", page_icon="🔐", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        body, .stApp {
            background-color: #000000;
            color: white !important;
            font-family: 'Arial', sans-serif;
        }
        .title {
            font-size: 45px;
            font-weight: bold;
            text-align: center;
            color: yellow;
            text-shadow: 2px 2px 10px rgba(255, 255, 0, 0.7);
            padding-bottom: 15px;
            border-bottom: 4px solid yellow;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(255, 255, 255, 0.1);
            margin-bottom: 20px;
            text-align: center;
        }
        .stButton>button {
            background: linear-gradient(90deg, #ff8c00, #ff4500);
            color: white !important;
            font-size: 18px !important;
            padding: 12px !important;
            border-radius: 8px !important;
            border: none !important;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            transform: scale(1.08);
            box-shadow: 0px 4px 20px rgba(255, 140, 0, 0.8);
        }
        .password-input label, .stTextInput>label, .password-length-label {
            color: white !important;
            font-weight: bold;
            font-size: 18px;
        }
        .result {
            font-size: 26px;
            font-weight: bold;
            color: #00ffcc;
            text-align: center;
            text-shadow: 2px 2px 10px rgba(0, 255, 204, 0.8);
        }
        .copy-button {
            background: linear-gradient(90deg, #4CAF50, #2E8B57);
            color: white;
            border-radius: 6px;
            padding: 8px;
            margin-top: 10px;
            cursor: pointer;
        }
        .stMarkdown p {
            color: white !important;
            font-size: 16px;
            line-height: 1.6;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<h1 class="title">🔐 Secure Password Strength Checker 🔥</h1>', unsafe_allow_html=True)

# Password Input
show_password = st.checkbox("👁️ Show Password")
password = st.text_input("🔑 Enter your password:", type="text" if show_password else "password")

def generate_secure_password(length=16):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(length))

def check_password_strength(password):
    if not password:
        return 0, "⚠️ Enter a password to check strength."
    stats = PasswordStats(password)
    strength_score = stats.strength()
    return strength_score, None

# Check Strength Button
if st.button("🔍 Check Strength"):
    if password:
        strength, error_msg = check_password_strength(password)
        if strength > 0.7:
            feedback = "✅ Strong Password! 🔥🛡️"
        elif strength > 0.4:
            feedback = "⚠️ Moderate Password! Add special characters & numbers! 🛠️"
        else:
            feedback = "❌ Weak Password! Mix uppercase, numbers, and symbols! ❗🔓"
        
        st.progress(strength)
        st.markdown(f"<p class='result'>{feedback}</p>", unsafe_allow_html=True)

        with st.expander("💡 Improve Your Password"):
            st.markdown("""
            - ✅ Use at least **12+ characters**.
            - 🔠 Include **uppercase & lowercase** letters.
            - 🔢 Add **numbers** (0-9).
            - 🎯 Use **special symbols** (!@#$%^&*).
            - 🚫 Avoid **common words or predictable patterns**.
            - 🔁 Mix **random words** for better security.
            """, unsafe_allow_html=True)
        
        if strength < 0.7:
            suggested_password = generate_secure_password()
            st.markdown(f"🔑 **Try this secure password:** `{suggested_password}`")
            if st.button("📋 Copy to Clipboard", key="copy_suggestion"):
                st.write("✅ Password Copied!")
    else:
        st.error("⚠️ Please enter a password first!")

# Password Generator Section
st.markdown("<h2 style='color: white; text-align: center;'>🎲 Need a Secure Password? Generate One Below! 🔥</h2>", unsafe_allow_html=True)

if st.button("⚡ Generate Secure Password"):
    st.markdown("<p class='password-length-label'>🔢 Select Password Length:</p>", unsafe_allow_html=True)
    password_length = st.slider("", min_value=8, max_value=32, value=16)
    new_password = generate_secure_password(password_length)
    st.code(new_password, language="plaintext")
    
    if st.button("📋 Copy to Clipboard", key="copy_generated"):
        st.write("✅ Password Copied!")

st.caption("🔒 Made with ❤️ Ayan_Ahmed_Khan🌍🔐")
