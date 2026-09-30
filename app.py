import streamlit as st
from chatbott import chatbot


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Shubham AI Assistant",
    page_icon="🤖",
    layout="centered"
)


# -----------------------------
# Page UI
# -----------------------------
st.title("🤖 Shubham AI Assistant")

st.write(
    "Ask me about Shubham's skills, education, projects, or professional background."
)


chatbot()