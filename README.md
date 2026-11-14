# 🧠 Production Enterprise Agentic RAG Platform

[![RAG Engine](https://img.shields.io/badge/RAG-Hybrid_Search_%26_Rerank-00D2FF?style=for-the-badge&logo=openai&logoColor=white)](#)
[![Vector Store](https://img.shields.io/badge/Vector_DB-Qdrant_%7C_Chroma-red?style=for-the-badge&logo=qdrant&logoColor=white)](#)
[![Kubernetes HPA](https://img.shields.io/badge/Kubernetes-Autoscaling_HPA-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](#)
[![OpenTelemetry](https://img.shields.io/badge/Telemetry-OpenTelemetry-black?style=for-the-badge&logo=opentelemetry&logoColor=white)](#)

> **High-throughput, production-ready Retrieval-Augmented Generation (RAG) platform** engineered for enterprise scale, featuring sparse BM25 + dense vector hybrid search, cross-encoder reranking, FastAPI streaming API, and autoscaled Kubernetes deployment.

---

## 🏛️ System Architecture

```mermaid
flowchart TD
    UserQuery["Client Query / Prompt"] --> API["FastAPI Knowledge Gateway\n(OpenTelemetry Tracing)"]
    
    subgraph RetrievalLayer["1. Hybrid Search Retrieval Engine"]
        API --> Dense["Dense Vector Search\n(Cosine Similarity / Embeddings)"]
        API --> Sparse["Sparse Lexical Search\n(BM25 Keyword Matching)"]
        Dense & Sparse --> Fusion["Reciprocal Rank Fusion (RRF)"]
    end

    subgraph RerankLayer["2. Cross-Encoder Re-Ranking"]
        Fusion --> Reranker["Cross-Encoder Reranker\n(ms-marco / bge-reranker)"]
        Reranker --> TopK["Top-K Precision Citations"]
    end

    subgraph SynthesisLayer["3. Contextual Synthesis & Serving"]
        TopK --> LLM["LLM Generation Engine\n(Streaming Tokens + Citations)"]
    end

    subgraph Orchestration["4. Cloud Infrastructure"]
        direction LR
        K8s["Kubernetes Deployment"]
        HPA["Horizontal Pod Autoscaler (HPA)"]
        VectorDB["Qdrant / Chroma Cluster"]
        K8s --- HPA
        K8s --- VectorDB
    end

    SynthesisLayer --> Orchestration
```

---

## ⚡ Key Capabilities

* **Hybrid Retrieval (Dense + Sparse)**: Combines semantic nuance with exact keyword matching to eliminate hallucinations.
* **Cross-Encoder Re-ranking**: Second-stage scoring maximizes context relevance before injecting into LLM context windows.
* **OpenTelemetry Instrumentation**: Full distributed tracing of latency, vector query times, and token generation rates.
* **Production Kubernetes Topology**: Includes Deployment specs, liveness/readiness probes, and Horizontal Pod Autoscaling (HPA) up to 10 replicas.
* **Hardened Security**: Non-root UID `10001` containerized runtime following zero-trust standards.

---

## 🚀 API Specification & Local Execution

### 1. Run with Docker
```bash
docker build -t enterprise-rag-platform:latest .
docker run -p 8000:8000 enterprise-rag-platform:latest
```

### 2. Query the Hybrid RAG API
```bash
curl -X POST "http://localhost:8000/api/v1/rag/query" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are Azure Landing Zone CAF standards for networking?",
    "top_k": 3,
    "rerank": true
  }'
```

### 3. Deploy to Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
```

---

## 👨💻 Author

**Ashu Dixit (Ashu02412)**  
*Senior DevSecOps & AI Platform Engineer*  
- GitHub: [@Ashu02412](https://github.com/Ashu02412)  
- Email: [ashu.dixit024@gmail.com](mailto:ashu.dixit024@gmail.com)
