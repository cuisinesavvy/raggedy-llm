from pydantic import BaseModel

class RAGRequest(BaseModel):
    query: str

class RAGResponse(BaseModel):
    query: str
    response: str