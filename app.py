import streamlit as st
from chatbot import get_answer

st.title("Airline Customer Service Chatbot")

user_input = st.text_input("Ask your question")

if user_input:
    response = get_answer(user_input)
    st.write(response)