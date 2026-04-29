from langchain_community.embeddings import HuggingFaceEmbeddings
from app.mock_vertex import (
    expand_query_with_mock_generative_model,
    get_embeddings_with_mock_text_embedding_model,
    rewrite_query_with_mock_generative_model,
)
from app.storage import create_vector_store, search_vector_store


def build_embeddings(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True},
    )


def build_vector_store(documents, embeddings):
    return create_vector_store(documents, embeddings)


def run_strategy_a(vector_store, query: str, top_k: int = 3):
    hits = search_vector_store(vector_store, query, top_k=top_k)
    return format_hits(hits)


def run_strategy_b(vector_store, query: str, top_k: int = 3):
    rewritten_query = rewrite_query_with_mock_generative_model(query)
    expanded_queries = expand_query_with_mock_generative_model(query)

    merged = {}
    for q in expanded_queries:
        hits = search_vector_store(vector_store, q, top_k=top_k)
        for doc, score in hits:
            chunk_id = doc.metadata.get("chunk_id")
            if chunk_id not in merged or score < merged[chunk_id][1]:
                merged[chunk_id] = (doc, score)

    hits = sorted(merged.values(), key=lambda x: x[1])[:top_k]
    return {
        "rewritten_query": rewritten_query,
        "expanded_queries": expanded_queries,
        "top_3": format_hits(hits),
    }


def format_hits(hits):
    rows = []
    for doc, score in hits:
        rows.append(
            {
                "chunk_id": doc.metadata.get("chunk_id"),
                "score": float(score),
                "text": doc.page_content,
            }
        )
    return rows


def get_embeddings_for_mock_api(embeddings, texts: list[str]) -> list[list[float]]:
    """
    Helper to demonstrate mocked TextEmbeddingModel usage.
    """
    return get_embeddings_with_mock_text_embedding_model(embeddings, texts)

