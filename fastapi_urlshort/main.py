from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import random
import string
import os

app = FastAPI()

FILE = "urls.txt"


# Request body model
class URL(BaseModel):
    long_url: str


# Generate random code
def generate_code(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Save to file
def save_url(code, url):
    with open(FILE, "a") as f:
        f.write(f"{code},{url}\n")


# Read all URLs
# def read_urls():
#     data = {}

#     try:
#         with open(FILE, "r") as f:
#             for line in f:
#                 code, url = line.strip().split(",")
#                 data[code] = url
#     except:
#         pass

#     return data

def read_urls():

    data = {}

    if not os.path.exists(FILE):
        return data

    with open(FILE, "r") as f:
        for line in f:
            try:
                code, url = line.strip().split(",", 1)
                data[code] = url
            except:
                continue

    return data



# Create short URL
@app.post("/shorten")
def shorten(url: URL):

    code = generate_code()
    save_url(code, url.long_url)

    short_url = f"http://127.0.0.1:8000/{code}"

    return {"short_url": short_url}


# Redirect
@app.get("/{code}")
def redirect(code: str):

    urls = read_urls()

    if code not in urls:
        raise HTTPException(status_code=404, detail="URL not found")

    return RedirectResponse(urls[code])
