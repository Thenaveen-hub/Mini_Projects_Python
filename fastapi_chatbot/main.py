import os
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from google import genai

# Load env
load_dotenv()

# Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

MODEL = "gemini-2.5-flash"

# Create ONE chat session (global memory)
chat_session = client.chats.create(model=MODEL)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/")
def home():
    return {"status": "Chatbot Running"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):

    try:
        # Send message with memory
        response = chat_session.send_message(req.message)

        reply = response.text

    except Exception as e:
        reply = f"Error: {str(e)}"

    return {"reply": reply}

