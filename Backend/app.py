from fastapi import APIRouter, Depends, HTTPException
from app.models.document import DocumentCreate, Document, SearchQuery, SearchResult
from app.services.document_service import DocumentService
from app.api.dependencies import get_document_service

router = APIRouter()

@router.post("/documents/", response_model=Document)
async def create_document(
    document: DocumentCreate,
    service: DocumentService = Depends(get_document_service)
):
    return service.create_document(document)

@router.get("/documents/{document_id}", response_model=Document)
async def get_document(
    document_id: str,
    service: DocumentService = Depends(get_document_service)
):
    document = service.get_document(document_id)
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@router.post("/search/", response_model=SearchResult)
async def search_documents(
    query: SearchQuery,
    service: DocumentService = Depends(get_document_service)
):
    return service.search_documents(query)
