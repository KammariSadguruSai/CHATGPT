import streamlit as st
import google.generativeai as genai
import os

# Configure the API key securely
genai_api_key = os.getenv("GENAI_API_KEY")
if not genai_api_key:
    st.error("API key for Generative AI is not set.")
    st.stop()

genai.configure(api_key=genai_api_key)

# Initialize the Generative Model
try:
    llm = genai.GenerativeModel("models/gemini-1.5-flash")
    chatbot = llm.start_chat(history=[])
except Exception as e:
    st.error(f"Failed to initialize the model: {e}")
    st.stop()

# Streamlit App Interface
st.title("Welcome to the Chatbot")

st.chat_message("ai").write("Hi there! I am a helpful AI Assistant. How can I help you today?")

# User Input
human_prompt = st.chat_input("Say Something...")

if human_prompt:
    # Display user message
    st.chat_message("human").write(human_prompt)

    # Generate AI Response
    try:
        response = chatbot.send_message(human_prompt)
        st.chat_message("ai").write(response)
    except Exception as e:
        st.error(f"Failed to get a response: {e}")
