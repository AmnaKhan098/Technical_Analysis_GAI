from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import ChatGoogleGenerativeAI

import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
# getting ticker
def get_Ticker(user_input):


    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=api_key)
    messages = [
        ("system", """You are a financial assistant. Your task is to extract the correct ticker symbol for any stock, company, or cryptocurrency mentioned in the user's message.

    Always return ONLY the official ticker symbol (in uppercase), like:
    - Apple → AAPL
    - Bitcoin → BTC
    - Tesla → TSLA
    - Microsoft → MSFT
    - Ethereum → ETH

    If no company or asset is mentioned, return "UNKNOWN"""),
         ("human", user_input),
    ]
    return llm.invoke(messages)