import keyboard
import time
import os
import sys
from capture import capture_screen
from ai_service import extract_text_from_image
from tts_service import speak_text

# Hotkey configuration
CAPTURE_HOTKEY = 'ctrl+l' 
EXIT_HOTKEY = 'ctrl+shift+q'

def on_trigger():
    print("\n--- Triggered! Capturing screen... ---")
    try:
        # 1. Capture
        image = capture_screen()
        print("Screen captured.")
        
        # 2. Analyze
        print("Sending to Gemini...")
        text = extract_text_from_image(image)
        
        # 3. Speak
        if text:
            print(f"Extracted Text:\n{text}")
            speak_text(text)
        else:
            print("No text extracted or error occurred.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    print("--- Done. Waiting for hotkey... ---")

def main():
    print("==========================================")
    print("Space Rangers 2 AI Screen Reader")
    print("==========================================")
    print(f"Hotkey: {CAPTURE_HOTKEY} to read screen")
    print(f"Exit:   {EXIT_HOTKEY} (or Ctrl+C in terminal)")
    print("==========================================")
    print("Ensure .env file has GEMINI_API_KEY")
    
    keyboard.add_hotkey(CAPTURE_HOTKEY, on_trigger)
    
    try:
        keyboard.wait(EXIT_HOTKEY)
    except KeyboardInterrupt:
        pass
    print("\nExiting...")

if __name__ == "__main__":
    main()
