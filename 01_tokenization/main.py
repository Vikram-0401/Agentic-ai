import tiktoken

enc = tiktoken.encoding_for_model("gpt-4")

text = "hey there! my name is vikram"
tokens = enc.encode(text)

print("Tokens: ", tokens) 

dec = enc.decode([36661, 1070, 0, 856, 836, 374, 348, 1609, 2453])

print("Decoded: ", dec)