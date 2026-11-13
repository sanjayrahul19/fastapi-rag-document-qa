from fastapi import FastAPI

from src.api.routes import document_routes, chat_routes


app = FastAPI(
    title="Simple RAG API",
    description="PDF upload and question-answering using RAG",
    version="1.0.0"
)


# Register document routes
app.include_router(document_routes.router)

# Register chat routes
app.include_router(chat_routes.router)


@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "message": "RAG API is running"
    }