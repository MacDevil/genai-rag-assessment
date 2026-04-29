def get_embeddings_with_mock_text_embedding_model(embedding_backend, texts: list[str]) -> list[list[float]]:
    """
    Mock of vertexai.language_models.TextEmbeddingModel.get_embeddings.
    """
    return embedding_backend.embed_documents(texts)


def rewrite_query_with_mock_generative_model(query: str) -> str:
    """
    Mock of vertexai.generative_models.GenerativeModel for query expansion.
    """
    lowered = query.lower()

    rules = {
        "peak load": "throughput burst autoscaling queue depth backpressure p95 latency",
        "traffic spikes": "throughput burst autoscaling queue depth backpressure p95 latency",
        "spikes": "throughput burst autoscaling queue depth backpressure p95 latency",
        "slowing": "tail latency saturation queue lag autoscaling",
        "outages": "circuit breaker retry budget failover graceful degradation",
        "cascading failures": "circuit breaker retry budget failover graceful degradation",
        "dependency": "circuit breaker timeout jitter retries graceful degradation",
        "taking down everything": "cascading failures bulkhead isolation fallback",
        "consistency": "idempotency transactional outbox deduplication replay safety",
        "retries": "idempotency transactional outbox deduplication replay safety",
        "duplicate writes": "idempotency keys deduplication exactly-once transactional outbox",
    }

    extras = []
    for k, v in rules.items():
        if k in lowered:
            extras.append(v)

    if not extras:
        extras.append("capacity planning saturation observability resilience")

    return f"{query}. Focus on: {'; '.join(extras)}."


def expand_query_with_mock_generative_model(query: str) -> list[str]:
    """
    Return multiple rewritten variants to simulate stronger AI-assisted query expansion.
    """
    rewritten = rewrite_query_with_mock_generative_model(query)
    lowered = query.lower()

    variants = [query, rewritten]

    if "spikes" in lowered or "peak" in lowered or "slowing" in lowered:
        variants.append("autoscaling queue lag backpressure p95 latency traffic burst")
        variants.append("rate limiting load shedding admission control tail latency")

    if "dependency" in lowered or "outage" in lowered or "cascading" in lowered:
        variants.append("circuit breaker timeout jitter retries fallback graceful degradation")
        variants.append("bulkhead isolation failover retry storm prevention")

    if "duplicate writes" in lowered or "retry" in lowered or "consistency" in lowered:
        variants.append("idempotency keys deduplication exactly-once semantics")
        variants.append("transactional outbox replay-safe consumers processed event ids")

    deduped = []
    seen = set()
    for v in variants:
        key = v.strip().lower()
        if key and key not in seen:
            seen.add(key)
            deduped.append(v)
    return deduped
