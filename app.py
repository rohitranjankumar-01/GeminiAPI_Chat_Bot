import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

with open("prompt.txt", "r") as f:
    my_prompt = f.read()

def ChatBot(text):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=text,
    )
    print(response.text)

if __name__ == "__main__":
    ChatBot(my_prompt)

