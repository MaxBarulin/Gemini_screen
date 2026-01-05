import pyttsx3
import threading

def speak_text(text):
    if not text or not text.strip():
        return

    def _run_tts():
        try:
            engine = pyttsx3.init()
            # Optional: Configure voice here
            # voices = engine.getProperty('voices')
            # for voice in voices:
            #     if 'Russian' in voice.name:
            #         engine.setProperty('voice', voice.id)
            #         break
            
            engine.setProperty('rate', 260) # Increased speed (~1.5x)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"TTS Error: {e}")

    # Run in a separate thread to prevent blocking
    t = threading.Thread(target=_run_tts)
    t.start()

if __name__ == "__main__":
    speak_text("Привет! Это тест голосового движка.")
