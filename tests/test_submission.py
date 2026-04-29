import json

from app.mock_vertex import rewrite_query_with_mock_generative_model


def test_rewrite_query_expands_peak_load():
    query = "How does the system handle peak load?"
    rewritten = rewrite_query_with_mock_generative_model(query)
    assert "autoscaling" in rewritten.lower()
    assert query in rewritten


def test_rewrite_query_has_default_expansion_for_unknown_query():
    query = "Tell me about deployment"
    rewritten = rewrite_query_with_mock_generative_model(query)
    assert "capacity planning" in rewritten.lower()


def test_json_serializable_shape():
    sample = {
        "query": "q",
        "strategy_a": {"query": "q", "rewritten_query": None, "top_3": []},
        "strategy_b": {"query": "q", "rewritten_query": "q2", "expanded_queries": ["q", "q2"], "top_3": []},
    }
    json.dumps([sample])

