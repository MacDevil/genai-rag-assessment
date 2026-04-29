# Submission Notes: Retrieval Benchmark POC

This submission is a proof of concept (POC) for comparing:

- Strategy A: Raw vector similarity search
- Strategy B: Query expansion before vector search

## Observations from This Assignment

In this dataset, there are no major differences between Strategy A and Strategy B outputs. The overlap in top retrieved chunks is still high. This is expected because the provided corpus is small and not very complex.

Query expansion is still a strong retrieval technique, but its impact is usually more visible in larger and noisier corpora with broader vocabulary spread, deeper domain language, and multiple competing contexts.

## How I Apply This in Real Projects

My production-style approach is slightly different from this simplified assessment setup:

- I typically add an LLM rewrite layer to generate multiple expanded queries.
- I run vector retrieval for each expanded query.
- I union/merge the retrieved results and then rank/filter them.

This multi-query expansion pattern usually improves recall more than a single rewrite.

## Embedding Model Choice

For this POC, I used a local Hugging Face embedding model.

In regular project work, I more commonly use:

- Amazon Bedrock Titan Embeddings (for AWS-focused deployments)
- OpenAI embeddings (for personal/smaller projects)

Embedding provider selection depends on cost, latency, compliance, and deployment environment.

## Similarity Metric Choice (Cosine vs Euclidean)

For semantic text retrieval, Cosine similarity is generally preferred because it compares vector direction (semantic meaning) rather than raw magnitude. This is usually more stable across sentence lengths and token count variation.

Euclidean distance can work, especially when embeddings are carefully normalized, but in most practical text-retrieval pipelines Cosine-aligned behavior is easier to reason about and typically gives more reliable ranking quality.

In this POC, embeddings are normalized, so the retrieval behaves in a cosine-friendly way.

## Migration to Vertex AI Vector Search (Matching Engine)

A production migration path to Vertex AI would be:

- Generate embeddings with Vertex embedding model endpoints.
- Build and deploy a Matching Engine index with chosen distance metric.
- Upsert chunk vectors + metadata.
- Query index with expanded query vectors.
- Add optional reranking and response synthesis layers.
- Add monitoring for latency, recall quality, and cost.

I have not yet worked hands-on with Vertex AI Matching Engine in production.

In my current production environment, I use:

- Titan embeddings
- Azure OpenAI GPT-4o model
- PostgreSQL with PGVector extension for production-scale vector retrieval

This stack supports strong scaling and operational control in my current projects. If helpful, we can discuss future migration design tradeoffs between Vertex AI and this architecture.

## Final Note

This submission demonstrates the method and code structure clearly as a local POC. The retrieval delta is limited here due to dataset size and complexity, not due to invalidity of the approach.

I am happy to discuss deeper production considerations in the interview, including:

- query expansion strategy design
- reranking layers
- chunking tradeoffs
- evaluation metrics and benchmark methodology
- migration path to managed vector systems
