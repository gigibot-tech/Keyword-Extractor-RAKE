import uvicorn
from fastapi import FastAPI
from keywords import extract_keywords
import json

app = FastAPI()

@app.get('/')
def keywords(text: str):
    return json.dumps({"keywords": extract_keywords(text)})

"""
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
"""
