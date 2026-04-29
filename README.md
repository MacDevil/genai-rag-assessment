# Final Submission (Simple Version)

This is a simple end-to-end local RAG submission aligned to the assessment:

- Strategy A: Raw vector similarity search.
- Strategy B: Query rewrite/expansion via a mocked GenerativeModel, then search.

## Project Structure

- `app/ingestion.py` - load and chunk text
- `app/mock_vertex.py` - mock TextEmbeddingModel + mock GenerativeModel behavior
- `app/retrieval.py` - embeddings, FAISS store, strategy A/B functions
- `app/benchmark.py` - run benchmark and write outputs
- `tests/test_submission.py` - basic tests

## Run

```bash
python -m app.benchmark
```

This generates:

- `outputs/benchmark_results.json`
- `retrieval_benchmark.md`

For detailed explanation and discussion points, refer to `submission_notes.md`.

## Notes

- Uses `sentence-transformers/all-MiniLM-L6-v2` for local embeddings.
- Uses cosine-friendly normalized embeddings.
- Mocking here means local deterministic logic that simulates Vertex model interfaces/behavior.

## Similarity Metric

- Cosine-style similarity is preferred for semantic retrieval because it compares vector direction.
- Euclidean can work, but cosine-aligned ranking is typically more stable for text embeddings.

## Vertex AI Migration (Production Path)

- Generate embeddings using Vertex embedding endpoints.
- Build and deploy a Vertex AI Vector Search (Matching Engine) index.
- Upsert chunk vectors + metadata and query with expanded query vectors.
- Add reranking, monitoring, and cost/latency controls.

