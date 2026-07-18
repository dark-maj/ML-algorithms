from ollama import chat
response=chat(
    model="qwen2.5:0.5b",
    messages=[
        {
            "role":"user",
            "content":"say hello in one sentence."
        }
    ]
)
print(response["message"]["content"])
