import streamlit as st
from chatbot import climate_chatbot
import os

st.set_page_config(page_title="Climate Action AI Chatbot", layout="wide")

st.title("🍃 Climate Action AI Chatbot")
st.markdown("🌱 Ask anything about climate science!")

user_input = st.text_input("Your Question:")

if st.button("Ask"):
    if not os.getenv("API_KEY"):
        st.error("API Key missing! Add API_KEY in Render dashboard.")
    elif user_input.strip() != "":
        with st.spinner("AI is thinking..."):
            answer = climate_chatbot(user_input)
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**AI:** {answer}")
    else:
        st.warning("Please enter a question.")
