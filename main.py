import openai
import os
import pytesseract
import pyautogui
import dotenv

dotenv.load_dotenv()

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

screenshot = pyautogui.screenshot()
extracted_text = pytesseract.image_to_string(screenshot)


openai.api_key = os.getenv('key')

messages = [
    {
        "role": "system",
        "content": "I will give screen text like \"Screentext:\\n\" and you shall explain whats happing on the screen based on the text."
    },
    {
        "role": "user",
        "content": "Screentext:\\n"+extracted_text
    }
]

def AI():
    global messages
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=messages,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
    presence_penalty=0
    )
    content = response['choices'][0]['message']
    messages.append(content)

    return content['content']

print(AI())
while True:
    messages.append(
                    {
                        "role": "user",
                        "content": input('Ask a question?: ')
                    })
    print(AI())