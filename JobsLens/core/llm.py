from ollama import chat
from prompt import build_prompt

def analyze_resume(resume_text, job_description):

    prompt = build_prompt(resume_text, job_description)

    response = chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]