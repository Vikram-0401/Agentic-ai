from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Few shot prompting : The model is given direct tasks or question with prior examples before generating the response.
SYSTEM_PROMPT = """You should only ans coding related questions, do not ans anything else. " \
"if user asks something other than coding say sorry

Examples:
Q: Explain a + b whole square?
A: Sorry i can ans only related to maths.

Q: Give the code to add two numbers?
A: def(a, b):
    return a+b
"""

client = OpenAI(
    api_key = "AIzaSyA1VuooeR9eF99fPlvMn3Bk0opE6Qfe2zM",
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT},
        { "role": "user", "content": "Hey, i am vikram, give me a joke"}
    ]
)

print(response.choices[0].message.content)
