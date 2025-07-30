


def ask_question(context, question):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Answer the question based on this context:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
