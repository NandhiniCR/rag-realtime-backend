from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from pathlib import Path

VECTOR_STORE_PATH = Path("data/vector_store")

def query_pdf(question: str, k: int = 3):
    # Load same embeddings used during indexing
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load FAISS index
    vector_store = FAISS.load_local(
        VECTOR_STORE_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    # Search
    docs = vector_store.similarity_search(question, k=k)

    print("\n🔍 Question:", question)
    print("=" * 60)

    for i, doc in enumerate(docs, 1):
        print(f"\n📄 Result {i}")
        print("-" * 40)
        print(doc.page_content)

if __name__ == "__main__":
    query_pdf("What is this document about?")
