# AlgoMentor AI - Interview Prep & DSA Search

A simple AI-powered search tool to find answers about Data Structures, Algorithms, and technical interview questions.

## What It Does

- 🔍 **Fast Search**: Type a question, get relevant answers instantly
- 📚 **6,800+ Documents**: Interview questions + LeetCode problems indexed
- 🌐 **Web Interface**: Easy-to-use search box in your browser
- 🔐 **Secure**: API keys stored safely in environment variables

## Quick Setup

### 1. Install Python Packages

```bash
# Activate environment
.venv\Scripts\activate

# Install dependencies
uv add -r requirements.txt
```

### 2. Add Your API Key (Optional)

```bash
# Copy template
cp .env.example .env

# Edit .env and add your GEMINI_API_KEY if you want AI features
```

### 3. Run the App

```bash
python app.py
```

Open: **http://127.0.0.1:8500**

## Try It

Search for anything like:
- "Explain binary search"
- "What is a hash map?"
- "Two sum problem"

## How It Works

1. **Load Documents** → Reads CSV files from `notebook/data/`
2. **Split into Chunks** → Breaks documents into smaller pieces
3. **Create Embeddings** → Converts text to numbers (vectors)
4. **Store in FAISS** → Fast searchable database
5. **Search** → User types query → Find matching documents → Show results

## File Structure

```
rag_application/
├── app.py              ← Flask web server
├── src/
│   ├── search.py       ← Search logic
│   ├── embedding.py    ← Vector generation
│   ├── vectorstore.py  ← FAISS database
│   └── data_loader.py  ← Load documents
├── notebook/data/      ← Your documents (CSV files)
├── faiss_store/        ← Search index (auto-created)
├── .env.example        ← API key template
└── requirements.txt    ← Python packages
```

## Adding More Documents

1. Place `.csv`, `.pdf`, or `.txt` files in `notebook/data/`
2. Restart the app
3. Index rebuilds automatically

## Security

✅ API keys go in `.env` file (never in code!)  
✅ `.env` is in `.gitignore` (won't commit secrets)  
✅ Use `.env.example` as template

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Import errors | Run: `.venv\Scripts\python.exe -m pip install langchain-community` |
| No documents found | Check files exist: `ls notebook/data/` |
| Empty search index | Delete `faiss_store/` folder and restart app |

## Need More Info?

See `QUICKSTART.md` for quick reference.

---

**Ready to search? Run `python app.py` now!** 🚀


