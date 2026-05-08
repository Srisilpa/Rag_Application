from pathlib import Path
from typing import List, Any, Dict
from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore

class SearchService:
    def __init__(self, data_dir: str, persist_dir: str = "faiss_store", embedding_model: str = "all-MiniLM-L6-v2"):
        self.data_dir = Path(data_dir).resolve()
        self.store = FaissVectorStore(persist_dir=persist_dir, embedding_model=embedding_model)
        self._ensure_index()

    def _ensure_index(self):
        self.store.load()
        if self.store.index is None or self.store.index.ntotal == 0:
            documents = load_all_documents(str(self.data_dir))
            if len(documents) == 0:
                raise RuntimeError(f"No documents found in {self.data_dir}")
            self.store.build_from_documents(documents)

    def search(self, query: str, top_k: int = 5) -> List[Dict[str, Any]]:
        results = self.store.query(query, top_k=top_k)
        formatted = []
        for rank, item in enumerate(results, start=1):
            metadata = item.get("metadata") or {}
            text = metadata.get("text", "")
            snippet = text[:1200].strip()
            formatted.append({
                "rank": rank,
                "distance": item.get("distance", 0.0),
                "content": snippet,
                "source": metadata.get("source", "unknown")
            })
        return formatted
