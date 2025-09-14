import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("Missing GEMINI_API_KEY in .env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash-latest")

def ask_gemini(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API Error: {e}"
