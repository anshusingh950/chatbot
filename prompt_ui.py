
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

chat_model = ChatOpenAI(
    openai_api_base="https://llmfoundry.straive.com/openai/v1/",
    openai_api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFuc2h1Lmt1bWFyQGdyYW1lbmVyLmNvbSJ9.BRrvVxmYnpK6HGVzAFem9QklSyTIQUht8QScZabDv78:my-test-project",
    model="gpt-4o-mini",
)

st.header('Mychatbot')
user_ip=st.text_input('Enter Your Prompt')

if st.button("Submit"):
    result=chat_model.invoke(user_ip)
    st.write(result.content)