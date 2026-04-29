from langchain_community.vectorstores import FAISS


def create_vector_store(documents, embeddings):
    return FAISS.from_documents(documents, embeddings)


def search_vector_store(vector_store, query: str, top_k: int = 3):
    return vector_store.similarity_search_with_score(query, k=top_k)
