from fastapi import FastAPI
from app.routes import rag_routes

app = FastAPI()

# Include RAG-specific routes
app.include_router(rag_routes.router, prefix="/rag", tags=["RAG"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI RAG Service!"}