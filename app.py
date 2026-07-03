import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")


gclient = genai.Client(api_key = api_key)


def ChatBot(text):
    resp = gclient.models.generate_content(
    model="gemini-2.5-flash",
    contents=text,
    )
    
    print(resp.text)


while True:
    input_text = input("Enter Your Prompt (Type 'exit' to quit): ")
    if input_text.lower() == "exit":
        break
    ChatBot(input_text)