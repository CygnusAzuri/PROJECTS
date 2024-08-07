import streamlit as st
import random
import string

# Function to generate password
def generate_password(length, include_uppercase, include_numbers, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit App
st.title("Password Generator")

length = st.slider("Select password length", min_value=6, max_value=30, value=12)
include_uppercase = st.checkbox("Include uppercase letters", value=True)
include_numbers = st.checkbox("Include numbers", value=True)
include_special = st.checkbox("Include special characters", value=True)

if st.button("Generate Password"):
    password = generate_password(length, include_uppercase, include_numbers, include_special)
    st.success(f"Generated Password: {password}")

