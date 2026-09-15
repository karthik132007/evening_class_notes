from openai import OpenAI

import os
key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(api_key=key,base_url="https://openrouter.ai/api/v1")
messages =[]
while True:
    message = input("Enter your message: ")
    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini",
        messages=messages,
    )
    messages.append({"role": "assistant", "content": response.choices[0].message.content})

    print(response.choices[0].message.content)
# print(response)