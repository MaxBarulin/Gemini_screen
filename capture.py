import mss
from PIL import Image

def capture_screen():
    with mss.mss() as sct:
        # Get the primary monitor
        # monitor 1 is usually the primary monitor
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        
        # Convert to PIL Image
        # MSS returns BGRA, PIL needs RGB for Gemini usually, but we can convert
        img = Image.frombytes("RGB", sct_img.size, sct_img.bgra, "raw", "BGRX")
        return img

if __name__ == "__main__":
    img = capture_screen()
    img.save("test_capture.png")
    print("Screenshot saved as test_capture.png")
