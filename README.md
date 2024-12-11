# raggedy-llm

project/
├── app/
│   ├── __init__.py
│   ├── app.py                 # Main FastAPI entry point
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── rag_routes.py      # RAG-specific endpoints
│   ├── services/
│   │   ├── __init__.py
│   │   ├── rag_service.py     # Core logic for the RAG service
│   ├── models/
│   │   ├── __init__.py
│   │   ├── rag_models.py      # Pydantic models for requests/responses
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── database.py        # Database connection or retrieval logic
│   │   ├── embeddings.py      # Logic for handling vector embeddings
│   ├── config.py              # Configuration settings
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
├── tests/
│   ├── test_rag_service.py    # Unit tests for the RAG service