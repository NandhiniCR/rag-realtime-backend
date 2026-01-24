from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path

PDF_PATH = Path("data/raw/real_time_rag_projects.pdf")
VECTOR_DB_PATH = Path("data/vector_store")

def create_vector_store():
    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    chunks = splitter.split_documents(documents)

    print(f"📄 Pages loaded: {len(documents)}")
    print(f"✂️ Chunks created: {len(chunks)}")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_documents(chunks, embeddings)

    VECTOR_DB_PATH.mkdir(parents=True, exist_ok=True)
    vector_store.save_local(str(VECTOR_DB_PATH))

    print("✅ FAISS vector store created successfully")

if __name__ == "__main__":
    create_vector_store()


