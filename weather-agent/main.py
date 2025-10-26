from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = "AIzaSyA1VuooeR9eF99fPlvMn3Bk0opE6Qfe2zM",
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

def main():
    user_query = input("> ")
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            { "role": "user", "content": "user_query"}
        ]
    )

    print(f": {response.choices[0].message.content}")

main()