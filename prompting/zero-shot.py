from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Zero shot prompting : The model is given direct tasks or question without prior examples.
SYSTEM_PROMPT = "You should only ans coding related questions, do not ans anything else. " \
"if user asks something other than coding say sorry"

client = OpenAI(
    api_key = "AIzaSyA1VuooeR9eF99fPlvMn3Bk0opE6Qfe2zM",
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content": "Hey, i am vikram, give me python code for binary search"}
    ]
)

print(response.choices[0].message.content)
