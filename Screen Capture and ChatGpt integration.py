import tkinter as tk
from PIL import Image, ImageTk
import pyautogui
import pytesseract
import openai

# Set the path to the Tesseract executable (replace with your path)
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Screen Capture and OCR App")

        self.label = tk.Label(root, text="Press the Capture button to take a screenshot and extract text. The screenshot will be displayed below.")
        self.label.pack(pady=10)

        self.capture_button = tk.Button(root, text="Capture", command=self.capture_and_display)
        self.capture_button.pack(pady=10)

        self.text_label = tk.Label(root, text="")
        self.text_label.pack(pady=10)

    def capture_and_display(self):
        screenshot = pyautogui.screenshot()
        screenshot_path = "screenshot.png"
        screenshot.save(screenshot_path)  # Save the screenshot to a file
        self.show_image(screenshot_path)

        extracted_text = self.extract_text_from_file(screenshot_path)
        self.text_label.config(text=f"Extracted Text: {extracted_text}")

        prompt = f"Extracted text from {screenshot_path}: {extracted_text}\nChatGPT, what can you tell me about this?"
        chatgpt_response = generate_response(prompt)
        print(chatgpt_response)

    def show_image(self, image_path):
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self.root, image=photo)
        label.image = photo
        label.pack(pady=10)

    def extract_text_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        return text

def generate_response(prompt):
    openai.api_key = 'your-api-key'  # Replace with your actual OpenAI API key
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenCaptureApp(root)
    root.mainloop()
