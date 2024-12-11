from fastapi import APIRouter, HTTPException
from app.services.rag_service import RAGService
from app.models.rag_models import RAGRequest, RAGResponse

router = APIRouter()

@router.post("/generate", response_model=RAGResponse)
def generate_response(request: RAGRequest):
    try:
        response = RAGService.retrieve_and_generate(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))