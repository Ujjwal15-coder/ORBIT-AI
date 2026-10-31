from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

client = OpenAI(
    # base_url = "http://127.0.0.1:11434/v1" , #ollama server
    # api_key = "ollama"

    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)
while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit","bye","goodbye"]:
        print("Exiting the chat. Goodbye!")
        break

    response = client.chat.completions.create(
        # model = "qwen3:4b",
        model = os.getenv("MODEL"),
        messages = [
            {
            "role" : "user",
            "content" : user_input
        }
    ]
)

# print(response)
# print("LLM Response:")


#ollama gives json -> python Object (chat completion)

print("Assistant: " + response.choices[0].message.content) #response from LLM Model : qwen3:4b