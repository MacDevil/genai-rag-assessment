import json
from pathlib import Path

from app.ingestion import chunk_documents
from app.retrieval import build_embeddings, build_vector_store, run_strategy_a, run_strategy_b


def run_benchmark():
    docs = chunk_documents("data/knowledge_base.txt")
    embeddings = build_embeddings("sentence-transformers/all-MiniLM-L6-v2")
    vector_store = build_vector_store(docs, embeddings)

    queries = [
        "How does the system handle peak load?",
        "What mechanisms prevent cascading failures during outages?",
        "How is data consistency preserved when retries happen?",
    ]

    results = []
    for query in queries:
        strategy_a = {
            "query": query,
            "rewritten_query": None,
            "top_3": run_strategy_a(vector_store, query, top_k=3),
        }
        strategy_b_result = run_strategy_b(vector_store, query, top_k=3)
        strategy_b = {
            "query": query,
            "rewritten_query": strategy_b_result["rewritten_query"],
            "expanded_queries": strategy_b_result["expanded_queries"],
            "top_3": strategy_b_result["top_3"],
        }
        results.append(
            {
                "query": query,
                "strategy_a": strategy_a,
                "strategy_b": strategy_b,
            }
        )

    return results


def write_outputs(results):
    Path("outputs").mkdir(parents=True, exist_ok=True)
    Path("outputs/benchmark_results.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )

    lines = [
        "# Retrieval Benchmark: Strategy A vs Strategy B",
        "",
        "Simple local RAG benchmark using mocked Vertex-style query expansion.",
        "",
    ]

    for row in results:
        lines.append(f"## Query: {row['query']}")
        lines.append("")

        lines.append("### Strategy A (Raw Vector Search)")
        for hit in row["strategy_a"]["top_3"]:
            lines.append(f"- chunk_id={hit['chunk_id']} score={hit['score']:.4f}")
            lines.append(f"  - {hit['text']}")
        lines.append("")

        lines.append("### Strategy B (AI-Enhanced Query Expansion)")
        lines.append(f"- rewritten_query: {row['strategy_b']['rewritten_query']}")
        lines.append("- expanded_queries:")
        for eq in row["strategy_b"]["expanded_queries"]:
            lines.append(f"  - {eq}")
        for hit in row["strategy_b"]["top_3"]:
            lines.append(f"- chunk_id={hit['chunk_id']} score={hit['score']:.4f}")
            lines.append(f"  - {hit['text']}")
        lines.append("")

    Path("retrieval_benchmark.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    benchmark_rows = run_benchmark()
    write_outputs(benchmark_rows)
    print(json.dumps(benchmark_rows, indent=2))

