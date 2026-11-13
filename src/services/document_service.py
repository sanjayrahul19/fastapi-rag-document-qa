import uuid

from pathlib import Path

from src.config import UPLOAD_DIR

from src.preprocessing.pdf_reader import read_pdf

from src.preprocessing.text_chunker import chunk_pages

from src.services.embedding_service import generate_embeddings

from src.services.vector_service import store_chunks


def process_document(file_path):

    # Generate unique document ID
    document_id = str(uuid.uuid4())

    # Step 1: Read PDF
    pages = read_pdf(file_path)

    if not pages:
        raise ValueError("No readable text found in PDF")

    # Step 2: Create chunks
    chunks = chunk_pages(pages)

    if not chunks:
        raise ValueError("No text chunks generated")

    # Step 3: Extract chunk text
    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    # Step 4: Generate embeddings
    embeddings = generate_embeddings(texts)

    # Step 5: Store in ChromaDB
    total_chunks = store_chunks(
        chunks,
        embeddings,
        document_id
    )

    return {
        "document_id": document_id,
        "filename": Path(file_path).name,
        "total_pages": len(pages),
        "total_chunks": total_chunks
    }