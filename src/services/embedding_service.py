from openai import OpenAI

from src.config import EMBEDDING_MODEL

client = OpenAI()


def generate_embeddings(texts):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts
    )

    # Keep embeddings in the same order as input texts
    ordered_data=sorted(response.data, key=lambda item: item.index)

    embeddings=[
        item.embedding
        for item in ordered_data
    ]

    return embeddings


 


    