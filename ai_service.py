import os
import time
from google import genai
from google.genai import types
from PIL import Image

# Global variable to store the key
_API_KEY = None

def set_api_key(key):
    global _API_KEY
    _API_KEY = key

def get_api_key():
    return _API_KEY

def extract_text_from_image(image: Image.Image):
    api_key = get_api_key()
    if not api_key:
        print("Error: API Key is not set.")
        return None

    client = genai.Client(api_key=api_key)
    
    # Prompt optimized for Space Rangers 2 text extraction
    prompt = """
    You are an AI assistant helping a visually impaired user play Space Rangers 2.
    Look at this screenshot. Your task:

    1. FIRST, extract the main QUEST TEXT, STORY NARRATIVE, or DIALOGUE following these rules:
       - IGNORE UI elements (buttons, menus, "Back", "Forward", resource counts, dates)
       - IGNORE ship status panels
       - IGNORE maps or star charts
       - FOCUS ONLY on the main block of text describing the situation, quest, or government dialogue
    
    2. THEN, analyze the extracted text:
       - If it contains a QUEST, QUESTION, or TASK that requires player action
       - BRIEFLY state the SOLUTION or RECOMMENDED ACTION in 1-2 sentences
       - Keep solution concise and practical for gameplay
    
    Output format:
    - First line: Extracted text in Russian
    - If solution is needed: New line with "Решение: [brief solution in Russian]"
    - If no solution needed: Output ONLY the extracted text
    
    Do not add any other text, explanations, or markdown formatting.
    """
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[prompt, image]
        )
        return response.text
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None
