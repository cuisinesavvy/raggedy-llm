from app.utils.database import retrieve_documents
from app.utils.embeddings import generate_embeddings, search_embeddings
from app.models.rag_models import RAGRequest, RAGResponse

class RAGService:
    @staticmethod
    def retrieve_and_generate(request: RAGRequest) -> RAGResponse:
        # Retrieve relevant documents based on the query
        documents = retrieve_documents(request.query)
        
        # Generate embeddings for the query
        query_embedding = generate_embeddings(request.query)
        
        # Perform vector similarity search
        relevant_docs = search_embeddings(query_embedding, documents)
        
        # Combine retrieved docs and perform generation (e.g., GPT model call)
        generated_response = f"Generated response based on: {relevant_docs[:2]}"
        
        return RAGResponse(query=request.query, response=generated_response)