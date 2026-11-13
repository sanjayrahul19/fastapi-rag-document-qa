from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    document_id: str

    question: str = Field(
        min_length=1,
        max_length=5000
    )