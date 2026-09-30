import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from promptt import prompt

load_dotenv()

def chatbot():

    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
         api_key = st.secrets["GOOGLE_API_KEY"]
    
    client = genai.Client(api_key=api_key)

    question = st.text_input("", placeholder="Ask about Shubham Patil")
    
    if st.button("Ask"):

        

     if question:
        st.chat_message("user").write(question)
        input=prompt(question)
    
        try:
            with st.spinner("Thinking..."):
                interaction = client.interactions.create(
                    model="gemini-3.8-flash",
                    input=input,
                    generation_config={
                                    "thinking_level": "low"
                                }
            )

            st.chat_message("assistant").write(interaction.output_text)

        except Exception as e:
            st.error(f"to many questions ask after some time")