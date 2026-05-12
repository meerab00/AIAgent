
import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

# ---------------------------
# API KEY
# ---------------------------
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("GROQ_API_KEY missing")
    st.stop()

# ---------------------------
# LLM
# ---------------------------
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama3-70b-8192"
)

# ---------------------------
# Tool
# ---------------------------
@tool
def calculator(query: str) -> str:
    """Simple calculator tool"""
    try:
        return str(eval(query))
    except:
        return "Invalid expression"

tools = [calculator]

# ---------------------------
# Prompt (ReAct Agent)
# ---------------------------
prompt = hub.pull("hwchase17/react")

# ---------------------------
# Agent
# ---------------------------
agent = create_react_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🤖 AI Agent (Groq + LangChain)")

user_input = st.text_input("Enter query:")

if st.button("Run"):
    if user_input:
        result = agent_executor.invoke({"input": user_input})
        st.write(result["output"])
    else:
        st.warning("Enter something")
