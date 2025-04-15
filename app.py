# aes_encrypt_only_app.py

import streamlit as st
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import base64

st.title("🔒 Text Encryption App (AES - Encrypt Only)")

# Function to generate key from password
def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

# Encrypt function
def encrypt(message, password):
    key = get_key(password)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted = iv + cipher.encrypt(message.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

# UI Inputs
st.subheader("Enter your text to encrypt:")
text = st.text_area("Message")

password = st.text_input("Enter password (used as encryption key):", type="password")

if st.button("Encrypt"):
    if not text or not password:
        st.warning("Please enter both message and password.")
    else:
        encrypted = encrypt(text, password)
        st.success("✅ Encrypted Text:")
        st.code(encrypted)

