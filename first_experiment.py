from openai import OpenAI
import os

from openai import OpenAI
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a dev ops engineer."},
    {"role": "user", "content": "Can you briefly explain what kubernetes is?"}
  ]
)

print(completion.choices[0].message)