import streamlit as st
from chatbot import climate_chatbot

st.set_page_config(page_title="Climate Action AI Chatbot", layout="wide")

st.title("🍃 Climate Action AI Chatbot")
st.markdown("🌱 Ask anything about climate science!")

# Input box
user_input = st.text_input("Your Question:")

# When user submits
if st.button("Ask"):
    if user_input.strip() != "":
        with st.spinner("AI is thinking..."):
            answer = climate_chatbot(user_input)
        st.markdown(f"**You:** {user_input}")
        st.markdown(f"**AI:** {answer}")
