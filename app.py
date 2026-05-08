import os
from pathlib import Path
from flask import Flask, request, render_template_string
from dotenv import load_dotenv
from src.search import SearchService

# Load environment variables from .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "notebook" / "data"
PERSIST_DIR = BASE_DIR / "faiss_store"

app = Flask(__name__)

search_service = SearchService(
    data_dir=str(DATA_DIR),
    persist_dir=str(PERSIST_DIR),
    embedding_model="all-MiniLM-L6-v2"
)

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rag_Chatbot</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f7fb; color: #212121; margin: 0; padding: 0; }
        .container { max-width: 900px; margin: 40px auto; padding: 24px; background: white; border-radius: 12px; box-shadow: 0 10px 24px rgba(0,0,0,0.08); }
        h1 { margin-top: 0; }
        form { display: flex; gap: 10px; margin-bottom: 20px; }
        input[type=text] { flex: 1; padding: 12px 14px; border: 1px solid #d1d7e0; border-radius: 8px; font-size: 16px; }
        button { padding: 12px 20px; border: none; border-radius: 8px; background: #3f51b5; color: white; font-size: 16px; cursor: pointer; }
        button:hover { background: #3345a0; }
        .result { border: 1px solid #e1e6f1; padding: 18px; border-radius: 10px; margin-bottom: 16px; background: #fafbff; }
        .meta { color: #555; font-size: 14px; margin-bottom: 10px; }
        .snippet { white-space: pre-wrap; line-height: 1.6; }
        .status { margin-bottom: 16px; color: #333; }
        .footer { margin-top: 24px; font-size: 14px; color: #667; }
    </style>
</head>
<body>
<div class="container">
    <h1>AlgoMentor AI</h1>
    <h2>An AI-powered RAG chatbot for interview preparation,
DSA practice, and LeetCode assistance.</h2>
    <p class="status">Loaded <strong>{{ total_documents }}</strong> indexed chunks. Enter a question below and click Search.</p>
    <form method="post">
        <input type="text" name="query" placeholder="Ask a question about your documents..." value="{{ query|e }}" required>
        <button type="submit">Search</button>
    </form>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
    {% for item in results %}
    <div class="result">
        <div class="meta">Result #{{ item.rank }} | Distance: {{ '%.4f'|format(item.distance) }} | Source snippet</div>
        <div class="snippet">{{ item.content }}</div>
    </div>
    {% endfor %}
    <div class="footer">Powered by FAISS + Sentence Transformers. Use the search box to retrieve relevant passages from your dataset.</div>
</div>
</body>
</html>"""

@app.route("/", methods=["GET", "POST"])
def index():
    query = request.form.get("query", "").strip()
    results = []
    message = ""
    if query:
        results = search_service.search(query, top_k=5)
        if len(results) == 0:
            message = "No relevant documents were found for this query."
    return render_template_string(
        PAGE_TEMPLATE,
        query=query,
        results=results,
        total_documents=len(search_service.store.metadata),
        message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8500, debug=True)
