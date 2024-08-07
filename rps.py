import streamlit as st
import random

# Function to determine the winner
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Custom CSS to style the app
st.markdown(
    """
    <style>
    .stApp {
        background: url("https://static.vecteezy.com/system/resources/previews/008/014/115/non_2x/tropical-leaves-background-design-summer-leaves-flat-illustration-simple-banner-with-copy-space-free-vector.jpg") no-repeat center center fixed;
        background-size: cover;
        color: black;
    }
    .image-button {
        border: none;
        background-color: transparent;
        cursor: pointer;
    }
    .image-button:hover {
        transform: scale(1.1);
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        color: blue;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit App
st.title("Rock-Paper-Scissors Game")

# Initialize session state for player choice
if 'player_choice' not in st.session_state:
    st.session_state['player_choice'] = None

# Function to set player's choice and trigger game logic
def set_choice(choice):
    st.session_state['player_choice'] = choice
    st.session_state['play_clicked'] = True

# Display images as clickable buttons
col1, col2, col3 = st.columns(3)

# Rock Button
with col1:
    if st.button("Rock", key="rock"):
        set_choice("Rock")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1PbZsUE7x3BB1lulrWcd7F7lqh1_Djzt29Q&s", width=100)

# Paper Button
with col2:
    if st.button("Paper", key="paper"):
        set_choice("Paper")
    st.image("https://media.geeksforgeeks.org/wp-content/uploads/20210705223645/paper.jpeg", width=100)

# Scissors Button
with col3:
    if st.button("Scissors", key="scissors"):
        set_choice("Scissors")
    st.image("https://wrpsa.com/wp-content/uploads/2021/08/scissors.png", width=100)

# Play the game if player has made a choice
if 'play_clicked' in st.session_state and st.session_state['play_clicked']:
    player_choice = st.session_state['player_choice']
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    st.write(f"Your choice: {player_choice}")
    st.write(f"Computer's choice: {computer_choice}")
    result = get_winner(player_choice, computer_choice)
    st.markdown(f"<div class='result'>{result}</div>", unsafe_allow_html=True)

    # Reset the play state
    st.session_state['play_clicked'] = False
