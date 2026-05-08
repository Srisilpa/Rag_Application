from pathlib import Path
from typing import List, Any
from langchain_community.document_loaders import (
    PyPDFLoader, 
    TextLoader, 
    CSVLoader, 
    Docx2txtLoader,
    UnstructuredExcelLoader,
    JSONLoader
)

def load_all_documents(data_dir: str) -> List[Any]:
    """
    Load all supported files from the data directory and convert to LangChain document structures.
    Supported: PDF, TXT, CSV, Excel, Word, JSON
    """
    data_path = Path(data_dir).resolve()
    print(f"[DEBUG] Data path: {data_path}")
    documents = []

    # --- 1. PDF Files ---
    pdf_files = list(data_path.glob('**/*.pdf'))
    print(f"[DEBUG] Found {len(pdf_files)} PDF files")
    for pdf_file in pdf_files:
        try:
            loader = PyPDFLoader(str(pdf_file))
            loaded = loader.load()
            print(f"[DEBUG] Loaded {len(loaded)} pages from {pdf_file.name}")
            documents.extend(loaded)
        except Exception as e:
            print(f"[ERROR] Failed to load PDF {pdf_file}: {e}")

    # --- 2. CSV Files ---
    csv_files = list(data_path.glob('**/*.csv'))
    for csv_file in csv_files:
        try:
            loader = CSVLoader(str(csv_file), encoding='utf-8')
            documents.extend(loader.load())
            print(f"[DEBUG] Loaded {csv_file.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load CSV {csv_file}: {e}")

    # --- 3. Text Files ---
    txt_files = list(data_path.glob('**/*.txt'))
    for txt_file in txt_files:
        try:
            loader = TextLoader(str(txt_file), encoding='utf-8')
            documents.extend(loader.load())
            print(f"[DEBUG] Loaded {txt_file.name}")
        except Exception as e:
            print(f"[ERROR] Failed to load TXT {txt_file}: {e}")

    print(f"\n[SUMMARY] Total documents loaded: {len(documents)}")
    return documents

# --- EXECUTE ---
# Assuming your files are in a folder named 'data'
# all_docs = load_all_documents("./data")