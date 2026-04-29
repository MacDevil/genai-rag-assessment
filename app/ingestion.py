from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_documents(path: str):
    loader = TextLoader(path, encoding="utf-8")
    return loader.load()


def chunk_documents(path: str, chunk_size: int = 300, chunk_overlap: int = 50):
    docs = load_documents(path)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = splitter.split_documents(docs)
    for i, doc in enumerate(chunks):
        doc.metadata["chunk_id"] = i
    return chunks

