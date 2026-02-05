import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_llm(prompt, system="You are a helpful AI"):
    # print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))  # debug
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )
    print("Response raw:", response)
    return response.choices[0].message.content

