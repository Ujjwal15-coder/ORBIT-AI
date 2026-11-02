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

messages = []

messages.append(
    {
        "role":"system",
        "content":"Act as a lawyer and respond in only 30 words"
    }
)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit","bye","goodbye"]:
        print("Exiting the chat. Goodbye!")
        break

    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    response = client.chat.completions.create(
        # model = "qwen3:4b",
        model = os.getenv("MODEL"),
        messages = messages
        
)
    assistant_reply = response.choices[0].message.content
    messages.append(
            {
                "role": "assistant",
                "content": assistant_reply
            }
        )

# print(response)
# print("LLM Response:")


#ollama gives json -> python Object (chat completion)

    print("Assistant: " + assistant_reply) #response from LLM Model : qwen3:4b