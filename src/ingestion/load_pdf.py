from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

PDF_PATH = Path("data/raw/real_time_rag_projects.pdf")

def load_pdf():
    loader = PyPDFLoader(str(PDF_PATH))
    documents = loader.load()
    print(f"✅ Total pages loaded: {len(documents)}")
    return documents

if __name__ == "__main__":
    load_pdf()

