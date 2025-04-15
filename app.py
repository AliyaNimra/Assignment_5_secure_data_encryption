# password_based_encrypt_app.py

import streamlit as st

st.title("🔐 Text Encryption with Password (No Crypto Library)")

# Convert password into a numeric shift key
def password_to_shift(password):
    return sum(ord(char) for char in password) % 26

# Encrypt the text using Caesar cipher with password-derived shift
def password_encrypt(text, password):
    shift = password_to_shift(password)
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

# UI
text = st.text_area("Enter text to encrypt:")
password = st.text_input("Enter password:", type="password")

if st.button("Encrypt"):
    if not text or not password:
        st.warning("Please enter both text and password.")
    else:
        encrypted_text = password_encrypt(text, password)
        st.success("✅ Encrypted Text:")
        st.code(encrypted_text)
        st.download_button("📄 Download Encrypted Text", encrypted_text, file_name="encrypted_text.txt")


