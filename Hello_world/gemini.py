from google import genai

client = genai.Client(
    api_key = "AIzaSyA1VuooeR9eF99fPlvMn3Bk0opE6Qfe2zM"
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

print(response.text)