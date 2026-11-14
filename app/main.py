"""
Production Enterprise Agentic RAG Platform
High-throughput knowledge retrieval and generation service with OpenTelemetry observability.
"""
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import List, Optional
import os
import asyncio
import json

from app.engine.rag import HybridRAGEngine

app = FastAPI(
    title="Enterprise Agentic RAG Platform",
    description="Scalable Hybrid Search, Cross-Encoder Reranking, and Generative AI Knowledge Service",
    version="1.0.0"
)

rag_engine = HybridRAGEngine()

class QueryRequest(BaseModel):
    query: str = Field(..., description="User search query or prompt")
    top_k: int = Field(5, description="Number of context documents to retrieve")
    rerank: bool = Field(True, description="Enable cross-encoder reranking")
    stream: bool = Field(False, description="Enable token streaming response")

class DocumentCitation(BaseModel):
    id: str
    score: float
    text: str
    metadata: dict

class QueryResponse(BaseModel):
    query: str
    answer: str
    citations: List[DocumentCitation]
    latency_ms: float

@app.get("/healthz")
def health():
    return {"status": "healthy", "service": "enterprise-rag-platform", "version": "1.0.0"}

@app.post("/api/v1/rag/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    try:
        response = await rag_engine.query(
            query_str=request.query,
            top_k=request.top_k,
            rerank=request.rerank
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
