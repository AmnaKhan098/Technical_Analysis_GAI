from fastapi import FastAPI
from pydantic import BaseModel
from main import process_query
from fastapi.responses import JSONResponse
import io
import base64
from PIL import Image

app = FastAPI()

# Input model
class QueryInput(BaseModel):
    query: str

@app.post("/analyze/")
def analyze_stock(input_data: QueryInput):
    try:
        # Step 1: Get the query
        query = input_data.query

        # Step 2: Process the query — returns image object (not a path), analysis text, and news dictionary
        image_fig, analysis, news_dict = process_query(query)

        # Step 3: Convert the image figure to bytes, then to base64
        # image_fig = Image.open(image_fig)
        buf = io.BytesIO()
        image_fig.save(buf, format='PNG')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.read()).decode('utf-8')
        buf.close()

        # Step 4: Return all data including the image as a base64 string
        return {
            "image_base64": image_base64,
            "analysis": analysis,
            "news": news_dict
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)


