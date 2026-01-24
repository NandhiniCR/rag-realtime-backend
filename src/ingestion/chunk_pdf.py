from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

PDF_PATH = Path("data/raw/real_time_rag_projects.pdf")

def chunk_pdf():
    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    print(f"✅ Total pages loaded: {len(documents)}")
    print(f"✅ Total chunks created: {len(chunks)}")

    return chunks

if __name__ == "__main__":
    chunk_pdf()
