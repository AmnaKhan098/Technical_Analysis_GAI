from datetime import datetime, timedelta
import finnhub
# Getting News
def Get_news(ticker):
  # Initialize the Finnhub client
  finnhub_client = finnhub.Client(api_key="d0bjakhr01qo0h63irbgd0bjakhr01qo0h63irc0")

  # Define today's date and 7 days ago
  today = datetime.today().date()
  week_ago = today - timedelta(days=7)

  # Fetch news from past week
  news = finnhub_client.company_news(ticker, _from=str(week_ago), to=str(today))

  # Store top 5 articles in a dictionary
  news_data = {}

  if news:
      for i, article in enumerate(news[:5], start=1):
          news_data[f"Article {i}"] = {
              "date": datetime.utcfromtimestamp(article['datetime']).strftime('%Y-%m-%d %H:%M:%S'),
              "headline": article['headline'],
              "url": article['url']
          }

      return news_data
  else:
      print("No news available for the selected period.")
