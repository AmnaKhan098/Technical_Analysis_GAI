from source.get_ticker import get_Ticker
from source.get_chart import chart_generation
from source.get_analysis import get_Analysis
from source.get_news import  Get_news

from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file

# Automatically sets GOOGLE_APPLICATION_CREDENTIALS


# user query
def process_query(query):
    # user_input=input("enter ticker:")
    ticker_symbol = get_Ticker(query).content
    chart = chart_generation(ticker_symbol)  # should return a path to image
    analysis = get_Analysis(chart).content
    # print(analysis)
    newsD = Get_news(ticker_symbol)
    # print(newsD)
    return  chart, analysis,newsD

# df2=process_query("tell me about apple")
# print(df2)