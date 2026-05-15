import google.generativeai as genai
from dotenv import load_dotenv
import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from verify import get_current_user
from database import get_db
import google.generativeai as genai
from models import Chatbot

load_dotenv(dotenv_path=".env")

genai.configure(api_key=os.getenv("Gemini_API_Key_1"))

for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"Model Name: {model.name}")
        
model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are an agricultural assistant chatbot.

Your job is to help farmers with:
- crops
- fertilizers
- irrigation
- plant diseases
- pesticides
- soil problems
- agriculture tips

Rules:
- Only answer agriculture-related questions.
- If the question is outside agriculture, politely refuse.
- Answer in simple english.
- Keep answers short and practical.
"""

router = APIRouter()
@router.post("/chatbot")
async def chat(
    data: Chatbot,
    db: Session = Depends(get_db),
    user = Depends(get_current_user),
):

    prompt = f"""
    {SYSTEM_PROMPT}
    User Question:
    {data.message}
    """
    response = model.generate_content(prompt)
    return {
        "reply": response.text
    }
