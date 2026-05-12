import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool

# ---------------------------
# GROQ API KEY (Set in Streamlit secrets or env)
# ---------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Please set GROQ_API_KEY in environment variables")
    st.stop()

# ---------------------------
# LLM (Groq Model)
# ---------------------------
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-70b-8192"  # stable current model
)

# ---------------------------
# Simple Tool Example (Calculator Tool)
# ---------------------------
def calculator_tool(query):
    try:
        return str(eval(query))
    except:
        return "Invalid calculation"

tools = [
    Tool(
        name="Calculator",
        func=calculator_tool,
        description="Use for math calculations"
    )
]

# ---------------------------
# AI Agent
# ---------------------------
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="AI Agent", page_icon="🤖")
st.title("🤖 My AI Agent (LangChain + Groq)")

user_input = st.text_input("Enter your query:")

if st.button("Run Agent"):
    if user_input:
        with st.spinner("Thinking..."):
            response = agent.run(user_input)
        st.success(response)
    else:
        st.warning("Please enter a query")
