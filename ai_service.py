import os
import time
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

def get_api_key():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in .env file or environment variables.")
        return None
    return api_key

def extract_text_from_image(image: Image.Image):
    api_key = get_api_key()
    if not api_key:
        return None

    client = genai.Client(api_key=api_key)
    
    # Prompt optimized for Space Rangers 2 text extraction
    prompt = """
    You are an AI assistant helping a visually impaired user play Space Rangers 2.
    Look at this screenshot. Your task is to extract the main QUEST TEXT, STORY NARRATIVE, or DIALOGUE.
    
    IGNORE:
    - UI elements (buttons, menus, "Back", "Forward", resource counts, dates)
    - Ship status panels
    - Maps or star charts
    
    FOCUS ON:
    - The main block of text describing the situation, quest, or government dialogue.
    
    Output ONLY the extracted text in Russian. Do not add "Here is the text" or markdown.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt, image]
        )
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None
