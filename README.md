# AlgoMentor AI - Interview Prep & DSA Search

A simple AI-powered search tool to find answers about Data Structures, Algorithms, and technical interview questions.

## What It Does

- Fast Search: Type a question, get relevant answers instantly
- 6,800+ Documents: Interview questions + LeetCode problems indexed
- Web Interface: Easy-to-use search box in your browser
- Secure: API keys stored safely in environment variables

## Quick Setup

### 1. Install Python Packages

```bash
# Activate environment
.venv\Scripts\activate

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 2. Add Your API Key (Optional)

```bash
# Copy template
copy .env.example .env  # Windows
# cp .env.example .env  # macOS/Linux

# Edit .env and add your GEMINI_API_KEY if you want AI features
```

### 3. Run the App

```bash
streamlit run app.py
```

Opens at: **http://localhost:8501**

## Try It

Search for anything like:
- "Explain binary search"
- "What is a hash map?"
- "Two sum problem"

## How It Works

1. Load Documents → Reads CSV files from `notebook/data/`
2. Split into Chunks → Breaks documents into smaller pieces
3. Create Embeddings → Converts text to numbers (vectors)
4. Store in FAISS → Fast searchable database
5. Search → User types query → Find matching documents → Show results

## File Structure

```
rag_application/
├── app.py              ← Streamlit web server
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

API keys go in `.env` file (never in code!)  
`.env` is in `.gitignore` (won't commit secrets)  
Use `.env.example` as template

## Troubleshooting

Issue-Solution
Import errors -	Install missing packages using pip install -r requirements.txt
Dataset not loading	- Verify file paths inside notebook/data/
Encoding errors	- Use encoding="utf-8" in CSVLoader
Empty search results -	Delete faiss_store/ and restart application
Module not found	- Activate virtual environment before running

**Ready to search? Run `streamlit run app.py` now!**



Author
M. Sri Silpa
B.Tech Information Technology Student
AI & Full Stack Development Enthusiast


