from fastapi import APIRouter, HTTPException

from src.api.schemas.chat_schema import ChatRequest

from src.services.retrieval_service import retrieve_chunks

from src.services.generation_service import generate_answer

from src.services.vector_service import collection


router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post("/query")
def ask_question(request: ChatRequest):

    # Step 1: Check whether document exists
    existing_document = collection.get(
        where={
            "document_id": request.document_id
        },
        limit=1
    )

    if not existing_document["ids"]:

        raise HTTPException(
            status_code=404,
            detail="Document not found. Upload the document first."
        )

    # Step 2: Retrieve relevant chunks
    retrieved_chunks = retrieve_chunks(
        request.question,
        request.document_id
    )

    if not retrieved_chunks:

        raise HTTPException(
            status_code=404,
            detail="No relevant document content found"
        )

    # Step 3: Generate answer
    answer = generate_answer(
        request.question,
        retrieved_chunks
    )

    # Step 4: Prepare source information
    sources = []

    for chunk in retrieved_chunks:

        sources.append({
            "page": chunk["page"],
            "chunk": chunk["chunk"]
        })

    # Step 5: Return response
    return {
        "question": request.question,
        "answer": answer,
        "sources": sources
    }