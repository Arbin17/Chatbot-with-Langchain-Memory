import streamlit as st
from chatbot import generate_response

st.set_page_config(page_title="Sentiment-Aware Chatbot", layout="centered")
st.title("🧠 Sentiment-Aware Chatbot (Hugging Face)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Type your message:")

if st.button("Send") and user_input:
    response, sentiment = generate_response(user_input)
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", f"{response} _(Sentiment: {sentiment})_"))

# Display chat history
for sender, msg in reversed(st.session_state.chat_history):
    st.markdown(f"**{sender}:** {msg}")
