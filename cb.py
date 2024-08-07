import streamlit as st
import pandas as pd

# Initialize session state for storing contacts
if 'contacts' not in st.session_state:
    st.session_state.contacts = []

# Function to add a new contact
def add_contact(name, phone, email):
    st.session_state.contacts.append({"Name": name, "Phone": phone, "Email": email})

# Function to delete a contact
def delete_contact(index):
    del st.session_state.contacts[index]

# Custom CSS to style the app
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://static.vecteezy.com/system/resources/previews/005/263/636/non_2x/contact-us-concept-icons-such-as-mobile-phone-e-mail-address-chat-global-communication-on-dark-blue-background-for-presentation-web-banner-article-business-and-network-connection-and-company-free-vector.jpg") no-repeat center center fixed;
        background-size: cover;
    }
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: orange;
    }
    .stTextInput div, .stTextInput label, .stNumberInput div, .stNumberInput label {
        color: white;
    }
    .stTextInput input, .stNumberInput input {
        color: black;
    }
    .stButton button {
        color: white;
        background-color: red;
        border-color: red;
    }
    .stButton button:hover, .stButton button:active {
        color: black;
    }
    .stDataFrame div {
        overflow: auto;
    }
    .stDataFrame table {
        width: 100%;
        border-collapse: collapse;
    }
    .stDataFrame th, .stDataFrame td {
        padding: 10px;
        text-align: left;
        white-space: nowrap;
        color: white;
    }
    .stDataFrame thead tr {
        background-color: rgba(0, 0, 0, 0.1);
    }
    .css-1wvhkpy, .css-1wvhkpy p {
        background-color: yellow;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App
st.title("Contact Book")

# Form to add a new contact
with st.form("add_contact_form"):
    name = st.text_input("Name")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Add Contact")
    if submitted:
        add_contact(name, phone, email)
        st.success(f"Contact {name} added!")

# Display the contact list
st.subheader("Contact List")
contacts_df = pd.DataFrame(st.session_state.contacts, columns=["Name", "Phone", "Email"])
st.dataframe(contacts_df)

# Check if there are any contacts before allowing deletion
if st.session_state.contacts:
    delete_index = st.number_input("Enter the index of the contact to delete", min_value=0, max_value=len(st.session_state.contacts)-1, step=1)
    if st.button("Delete Contact"):
        delete_contact(delete_index)
        st.success("Contact deleted!")
else:
    st.info("No contacts to delete.")
