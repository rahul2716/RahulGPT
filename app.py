import streamlit as st
import google.generativeai as genai

# Set page configuration with title and icon
st.set_page_config(page_title="Rahul's GPT Chatbot", page_icon="🤖")

# Add a sidebar with a brief description
st.sidebar.title("🤖 Rahul's GPT")
st.sidebar.info("This is a chatbot powered by Gemini GPT. Enter your question below and receive a response.")

# Configure the API key
genai.configure(api_key="AIzaSyB7Fkodq4VqovGlGJwxPQqdGk5KpoRH3Yg")

# Title of the app
st.title("Welcome to Rahul's GPT Chatbot")
st.subheader("Ask me anything and get instant answers!")

# Adding a visual divider
st.markdown("---")

# Text input from the user
text = st.text_input("Enter Your Question:")

# Adding some instructions
st.write("Click the button to get a response from the chatbot.")

# Adding an empty space for visual appeal
st.write("")

# Initialize the model with the correct model name
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Send the message and get the response
if st.button("Ask GPT"):
    if text:
        response = chat.send_message(text)
        # Display the response in a styled container
        st.markdown(f"**Response:** {response.text}")
    else:
        st.warning("Please enter a question to ask!")


