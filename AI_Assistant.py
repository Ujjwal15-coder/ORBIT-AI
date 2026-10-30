from openai import OpenAI

client = OpenAI(
    base_url = "http://127.0.0.1:11434/v1" , #ollama server
    api_key = "ollama"
)

response = client.chat.completions.create(
    model = "qwen3:4b",
    messages = [
        {
            "role" : "user",
            "content" : "Hello LLM!"
        }
    ]
)

# print(response)
# print("LLM Response:")


#ollama gives json -> python Object (chat completion)

print(response.choices[0].message.content) #response from LLM Model : qwen3:4b