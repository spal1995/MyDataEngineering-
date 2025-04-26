from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAI

import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING")
os.environ["LANGSMITH_ENDPOINT"] = os.getenv("LANGSMITH_ENDPOINT")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"]= os.getenv("LANGSMITH_PROJECT")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful chat assistant. Answer the user queries correctly."),
        ("user","Question:{question}")
    ]
)

# Streamlit
st.title("Chat created using langsmith")
input_text = st.text_input("Search the topic you are interested in")

# OpenAI LLM Called
llm = ChatOpenAI(model='gpt-3.5-turbo')

# Outputparser called
output_parser = StrOutputParser()

# Langchain chain called
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
