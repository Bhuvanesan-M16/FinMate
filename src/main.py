import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Access secrets
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
INITIAL_RESPONSE = os.getenv("INITIAL_RESPONSE")
INITIAL_MSG = os.getenv("INITIAL_MSG")
CHAT_CONTEXT = os.getenv("CHAT_CONTEXT")

# Error handling if any variable is missing
if not all([GROQ_API_KEY, INITIAL_RESPONSE, INITIAL_MSG, CHAT_CONTEXT]):
    st.error("Missing one or more environment variables. Please check your .env file.")
    st.stop()

# Save the API key to the environment variable
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
