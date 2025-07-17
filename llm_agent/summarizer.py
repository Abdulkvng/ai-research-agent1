

from openai import OpenAI

def summarize(text):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize this text:"},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content
