import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from src.search import SearchService

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "notebook" / "data"
PERSIST_DIR = BASE_DIR / "faiss_store"

@st.cache_resource
def load_search_service():
    return SearchService(
        data_dir=str(DATA_DIR),
        persist_dir=str(PERSIST_DIR),
        embedding_model="all-MiniLM-L6-v2"
    )

search_service = load_search_service()

st.set_page_config(
    page_title="AlgoMentor AI",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("AlgoMentor AI")
st.markdown("An interactive Streamlit UI for interview prep and DSA search.")

with st.sidebar:
    st.header("Settings")
    top_k = st.slider("Number of results", min_value=1, max_value=10, value=5)
    st.markdown("---")
    st.subheader("Index Info")
    st.write(f"Total documents: **{len(search_service.store.metadata)}**")
    st.write("Embedding model: **all-MiniLM-L6-v2**")
    st.write("Search engine: **FAISS**")

query = st.text_input(
    "Ask a question about your documents:",
    placeholder="e.g., Explain binary search"
)

if query:
    with st.spinner("Searching..."):
        results = search_service.search(query, top_k=top_k)

    if results:
        st.success(f"Found {len(results)} relevant results")

        for idx, result in enumerate(results, start=1):
            st.markdown(f"### Result {idx}")

            st.metric(
                "Distance",
                f"{result['distance']:.4f}"
            )

            st.markdown("**Content:**")

            st.code(
                result["content"][:1600],
                language="text"
            )

    else:
        st.warning("No relevant documents found. Try a different query.")

else:
    st.info("Enter a query above to search the indexed documents.")

    st.markdown(
        """
        **Example queries:**
        - Explain binary search
        - What is a hash map?
        - Two sum problem solution
        """
    )