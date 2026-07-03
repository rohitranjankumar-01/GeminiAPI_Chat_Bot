import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

gclient = genai.Client(api_key = api_key)

try:
    with open("prompt.txt", "r") as f:
        my_prompt = f.read()
except FileNotFoundError:
    print("Error: prompt.txt not found. Please create the file.")

def ChatBot(text):
    resp = gclient.models.generate_content(
    model="gemini-2.5-flash",
    contents=text,
    )
    
    print(resp.text)


ChatBot(my_prompt)