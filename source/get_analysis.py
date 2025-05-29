from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from io import BytesIO
import base64
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")# Analysis of chart
def get_Analysis(image2):

    # Encode the image to base64

    buffered = BytesIO()
    image2.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",api_key=api_key)
    messages = [
        ("system", """Analyze the following stock chart in depth.
         Focus on technical indicators such as trend direction, support and resistance levels,
        volume analysis, moving averages, and any patterns like head and shoulders, double top/bottom, or breakouts.
        Dont use "here is the analysis".only write the analysis.Only write 150 words 
         Please provide:

         A detailed interpretation of the chart’s trend (bullish, bearish, or neutral).

        Key technical patterns or signals present.

        Insights from volume and MACD indicators (if shown).

        Potential short-term and long-term price movement predictions based on the chart.

        Use expert-level trading knowledge in your response."""),
         ("human", img_str),
    ]
    return llm.invoke(messages)