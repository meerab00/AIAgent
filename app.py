
import os
import streamlit as st
from langchain_groq import ChatGroq

# ---------------------------
# API KEY
# ---------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY missing in environment variables")
    st.stop()

# ---------------------------
# LLM
# ---------------------------
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-70b-8192"
)

# ---------------------------
# Simple AI Function
# ---------------------------
def get_response(question):
    prompt = f"""
    You are a helpful AI assistant.
    Answer clearly and simply.

    User Question: {question}
    """
    response = llm.invoke(prompt)
    return response.content

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="AI Agent", page_icon="🤖")

st.title("🤖 Groq AI Assistant")

user_input = st.text_input("Ask anything:")

if st.button("Run"):
    if user_input:
        with st.spinner("Thinking..."):
            result = get_response(user_input)
        st.success(result)
    else:
        st.warning("Please enter a question")
