from src.config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_pages(pages):

    all_chunks = []

    for page in pages:

        text = page["text"]

        start = 0

        chunk_number = 1

        while start < len(text):

            end = start + CHUNK_SIZE

            chunk = text[start:end]

            if chunk.strip():

                all_chunks.append({
                    "text": chunk,
                    "page": page["page"],
                    "chunk": chunk_number
                })

            start += CHUNK_SIZE - CHUNK_OVERLAP

            chunk_number += 1

    return all_chunks



#[
    {
        "text": "Python is a programming language...",
        "page": 1,
        "chunk": 1
    },
    {
        "text": "Python supports lists and tuples...",
        "page": 1,
        "chunk": 2
    }
#]