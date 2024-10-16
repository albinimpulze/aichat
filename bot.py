import os
from groq import Groq
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("AI Assistant using Python")

prompt = st.text_input("Enter your prompt : ")

if st.button("Submit"):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(messages=[{"role": "user","content": "Explain the importance of fast language models",}],model="llama3-8b-8192",)

    st.write(chat_completion.choices[0].message.content)