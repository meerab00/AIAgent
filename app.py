
import os
import streamlit as st
from groq import Groq

# API KEY
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY missing")
    st.stop()

client = Groq(api_key=GROQ_API_KEY)

# ---------------------------
# AI RESPONSE FUNCTION
# ---------------------------
def get_response(user_input):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"

# ---------------------------
# STREAMLIT UI
# ---------------------------
st.title("🤖 Groq AI Assistant")

user_input = st.text_input("Ask anything:")

if st.button("Run"):
    if user_input:
        st.write(get_response(user_input))
    else:
        st.warning("Enter a question")
