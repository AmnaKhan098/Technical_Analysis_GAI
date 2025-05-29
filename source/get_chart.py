import requests
from PIL import Image
from io import BytesIO
import json
from dotenv import load_dotenv
import os

load_dotenv()

x_api_key = os.getenv("X_API_Key")
url2=os.getenv("URL")
# Generating charts

def chart_generation(ticker):
    url = url2
    headers = {
        "x-api-key":x_api_key ,
        "content-type": "application/json"
    }

    data = {
        "theme": "dark",
        "interval": "1W",
        "symbol": f"NASDAQ:{ticker}",
        "override": {
            "showStudyLastValue": False
        },
        "studies": [
            {
                "name": "Volume",
                "forceOverlay": True
            },
            {
                "name": "MACD",
                "override": {
                    "Signal.linewidth": 2,
                    "Signal.color": "rgb(255,65,129)"
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    # Open an image file
    image = Image.open(BytesIO(response.content))

    # Display the image
    return image

