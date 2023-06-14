import requests
from fastapi import FastAPI, Depends
from fastapi.openapi.models import APIKey

from auth import api_key_auth

app = FastAPI()

@app.get("/")
async def root(api_key: APIKey = Depends(api_key_auth)):
    return {"message": "Hello World"}


if __name__ == '__main__':
    # call API
    url = "http://localhost:8080/"
    headers = {
        'x-api-key': '1234'
    }

    response = requests.get(url, headers=headers)
    print(response.text)