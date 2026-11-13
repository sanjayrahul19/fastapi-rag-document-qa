import chromadb

from src.config import COLLECTION_NAME,CHROMA_DB_DIR

# Create persistent ChromaDB database
chroma_client = chromadb.PersistentClient(path=CHROMA_DB_DIR)

# Create or load collection
collection = chroma_client.get_or_create_collection(name=COLLECTION_NAME,metadata={"hnsw:space": "cosine"})

def store_chunks(chunks,embeddings,document_id):

    ids=[]

    documents=[]

    metadatas=[]

    for index,chunk in enumerate(chunks):

        ids.append(f"{document_id}_{index}")

        documents.append(chunk['text'])

        metadatas.append({
            "document_id": document_id,
            "page": chunk["page"],
            "chunk": chunk["chunk"]
        })

    collection.upsert(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )
        
    print(f"Stored {len(documents)} chunks in ChromaDB")

    return len(documents)
        








