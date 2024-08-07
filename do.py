import streamlit as st
import pandas as pd
from PIL import Image

def todo_list():
  # Initialize a list to store tasks
  todo_list = []

  # Create a text input for adding tasks
  new_task = st.text_input("Add a new task")

  # Add a button to add the task to the list
  if st.button("Add"):
    todo_list.append(new_task)
    st.success("Task added!")

  # Display the todo list
  st.subheader("Your To-Do List")
  for task in todo_list:
    st.write(f"- {task}")

def main():
  st.set_page_config(
      page_title="Colorful Todo List",
      page_icon=image,
      layout="wide"
  )

  # Load the image (replace 'your_image.png' with your image path)
  image = Image.open('your_image.png')

  # Inline CSS
  st.markdown("""
  <style>
  body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
  }

  .stButton {
    background-color: #4CAF50;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    border: none;
    transition: background-color 0.3s ease-in-out;
  }

  .stButton:hover {
    background-color: #3e8e41;
  }

  /* Add more CSS styles for animations, colors, and layout */
  </style>
  """, unsafe_allow_html=True)

  todo_list()

if __name__ == "__main__":
  main()
