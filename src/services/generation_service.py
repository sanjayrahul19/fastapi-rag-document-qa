from openai import OpenAI

from src.config import LLM_MODEL


client = OpenAI()


def generate_answer(question, retrieved_chunks):

    # Step 1: Combine retrieved chunks
    context = "\n\n".join(
        chunk["text"]
        for chunk in retrieved_chunks
    )

    # Step 2: Create prompt
    prompt = f"""
You are a helpful document assistant.

Answer the user's question using only the context below.

If the answer is not available in the context,
say that you could not find the answer in the document.

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

    # Step 3: Call Responses API
    response = client.responses.create(
        model=LLM_MODEL,
        input=prompt
    )

    return response.output_text