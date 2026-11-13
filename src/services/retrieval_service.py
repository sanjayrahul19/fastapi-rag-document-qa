from src.services.embedding_service import generate_embeddings

from src.services.vector_service import collection

from src.config import TOP_K


def retrieve_chunks(question, document_id):

    # Step 1: Generate question embedding
    query_embedding = generate_embeddings([question])[0]

    # Step 2: Search only the selected document
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=TOP_K,
        where={
            "document_id": document_id
        }
    )

    # Step 3: Prepare retrieved chunks
    retrieved_chunks = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    for index, document in enumerate(documents):

        metadata = metadatas[index]

        retrieved_chunks.append({
            "text": document,
            "page": metadata["page"],
            "chunk": metadata["chunk"]
        })

    return retrieved_chunks