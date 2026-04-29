# Retrieval Benchmark: Strategy A vs Strategy B

Simple local RAG benchmark using mocked Vertex-style query expansion.

## Query: How does the system handle peak load?

### Strategy A (Raw Vector Search)
- chunk_id=5 score=0.7944
  - Peak load protection is reinforced through asynchronous processing
- chunk_id=3 score=1.0714
  - . During high demand periods, new instances are launched in seconds, reducing latency spikes and
- chunk_id=0 score=1.0999
  - Our platform uses horizontal autoscaling to handle sudden increases in request volume

### Strategy B (AI-Enhanced Query Expansion)
- rewritten_query: How does the system handle peak load?. Focus on: throughput burst autoscaling queue depth backpressure p95 latency.
- expanded_queries:
  - How does the system handle peak load?
  - How does the system handle peak load?. Focus on: throughput burst autoscaling queue depth backpressure p95 latency.
  - autoscaling queue lag backpressure p95 latency traffic burst
  - rate limiting load shedding admission control tail latency
- chunk_id=5 score=0.7944
  - Peak load protection is reinforced through asynchronous processing
- chunk_id=19 score=0.8386
  - . Dashboards track p95 latency, error rates, queue lag, and saturation
- chunk_id=8 score=0.9125
  - . Backpressure rules slow ingestion when queue lag grows, protecting downstream databases from

## Query: What mechanisms prevent cascading failures during outages?

### Strategy A (Raw Vector Search)
- chunk_id=22 score=0.8594
  - . This allows safe retries when transient errors happen under load
- chunk_id=16 score=0.8782
  - . If a third-party API slows down, the circuit opens to avoid cascading failures
- chunk_id=17 score=1.0516
  - . Requests may be served with stale but safe fallback data until upstream services recover.

### Strategy B (AI-Enhanced Query Expansion)
- rewritten_query: What mechanisms prevent cascading failures during outages?. Focus on: circuit breaker retry budget failover graceful degradation; circuit breaker retry budget failover graceful degradation.
- expanded_queries:
  - What mechanisms prevent cascading failures during outages?
  - What mechanisms prevent cascading failures during outages?. Focus on: circuit breaker retry budget failover graceful degradation; circuit breaker retry budget failover graceful degradation.
  - circuit breaker timeout jitter retries fallback graceful degradation
  - bulkhead isolation failover retry storm prevention
- chunk_id=22 score=0.8594
  - . This allows safe retries when transient errors happen under load
- chunk_id=16 score=0.8782
  - . If a third-party API slows down, the circuit opens to avoid cascading failures
- chunk_id=15 score=1.0200
  - The system includes circuit breakers and retry budgets for external dependencies

## Query: How is data consistency preserved when retries happen?

### Strategy A (Raw Vector Search)
- chunk_id=21 score=0.9843
  - For data consistency, writes use idempotency keys and transactional outbox patterns
- chunk_id=26 score=1.0499
  - . Recovery point objectives are maintained through continuous replication and periodic restore
- chunk_id=23 score=1.1078
  - . Event consumers apply deduplication checks so replayed events do not create duplicate records.

### Strategy B (AI-Enhanced Query Expansion)
- rewritten_query: How is data consistency preserved when retries happen?. Focus on: idempotency transactional outbox deduplication replay safety; idempotency transactional outbox deduplication replay safety.
- expanded_queries:
  - How is data consistency preserved when retries happen?
  - How is data consistency preserved when retries happen?. Focus on: idempotency transactional outbox deduplication replay safety; idempotency transactional outbox deduplication replay safety.
  - idempotency keys deduplication exactly-once semantics
  - transactional outbox replay-safe consumers processed event ids
- chunk_id=21 score=0.6034
  - For data consistency, writes use idempotency keys and transactional outbox patterns
- chunk_id=23 score=0.8202
  - . Event consumers apply deduplication checks so replayed events do not create duplicate records.
- chunk_id=26 score=0.9635
  - . Recovery point objectives are maintained through continuous replication and periodic restore
