import streamlit as st

# Set the title of the app
st.title("Simple Calculator")

# Custom CSS to add background image
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://img.freepik.com/premium-photo/top-view-blue-calculator-notepad-color-background_260672-4055.jpg");
        background-size: cover;
        background-position: center;
        
    }
    .stTextInput input {
        font-size: 20px;
        padding: 10px;
        margin: 10px;
        
    }
    .stButton button {
        font-size: 20px;
        padding: 10px 20px;
        margin: 10px;
    }
    .stSelectbox select {
        font-size: 20px;
        padding: 10px;
        margin: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Input fields for the two numbers
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Dropdown for selecting the operation
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform the calculation based on the selected operation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed.")

# Display the result
if result is not None:
    st.success(f"The result of {operation} is: {result}")
