
import os
import streamlit as st

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ---------------------------
# API KEY
# ---------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY missing in environment variables")
    st.stop()

# ---------------------------
# LLM (Groq)
# ---------------------------
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.1-8b-instant"   # ✅ working model
)

# ---------------------------
# Prompt Template
# ---------------------------
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant. Give simple and clear answers."),
    ("user", "{input}")
])

# ---------------------------
# Chain (LangChain modern style)
# ---------------------------
chain = prompt | llm | StrOutputParser()

# ---------------------------
# STREAMLIT UI
# ---------------------------
st.set_page_config(page_title="LangChain AI Agent", page_icon="🤖")

st.title("🤖 LangChain + Groq AI Agent")

user_input = st.text_input("Ask anything:")

if st.button("Run"):
    if user_input:
        with st.spinner("Thinking..."):
            response = chain.invoke({"input": user_input})
        st.success(response)
    else:
        st.warning("Please enter a question")
