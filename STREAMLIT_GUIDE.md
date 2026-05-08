# 🎨 Streamlit UI Guide

## Quick Start with Streamlit

Streamlit provides a beautiful, interactive web interface for your RAG search application.

## Installation

Streamlit is already added to `requirements.txt`. Install with:

```bash
uv add streamlit
```

Or if already installed, just run:

```bash
streamlit run streamlit_app.py
```

## Features

✨ **Modern Interface**
- Clean, professional design
- Gradient header with app title
- Real-time search with spinner

🎯 **Quick Access**
- Example query buttons (Binary Search, Hash Map, Two Sum)
- Adjustable number of results (1-10)
- Sidebar with index info

📊 **Rich Results**
- Rank display for each result
- Similarity score (0-1)
- Distance metric
- Content preview with syntax highlighting

⚙️ **Settings Sidebar**
- Adjust top_k (number of results)
- View index statistics
- Model and search engine info

## Running the App

### Start Server

```bash
streamlit run streamlit_app.py
```

### Browser Access

Opens automatically at: `http://localhost:8501`

If not, manually open the above URL.

## User Workflow

1. **Search**: Type or click an example button
2. **View Results**: Ranked by similarity
3. **Adjust**: Change result count in sidebar
4. **Explore**: Click through multiple queries

## Comparison: Streamlit vs Flask

| Feature | Streamlit | Flask |
|---------|-----------|-------|
| UI Design | Modern, interactive | Classic HTML |
| Setup | 1 command | 1 command |
| Customization | Limited, easy | Full control |
| Performance | Fast for data apps | Traditional web |
| Learning Curve | Very easy | Moderate |

## Deployment Options

### Local
```bash
streamlit run streamlit_app.py
```

### Streamlit Cloud
Upload to GitHub, deploy free on [share.streamlit.io](https://share.streamlit.io)

### Docker
```bash
docker run -p 8501:8501 streamlit/streamlit-docker
```

## Tips & Tricks

- **Cache Settings**: Sidebar lets you adjust results on-the-fly
- **Quick Examples**: Buttons for common searches
- **Full Content**: Scroll to see full document snippets
- **Keyboard**: Press Enter to search after typing

## Troubleshooting

### "Port 8501 already in use"
```bash
streamlit run streamlit_app.py --server.port 8502
```

### "Module not found"
```bash
uv add streamlit
```

### Slow on first load
First run builds the search index - subsequent runs are fast!

---

**Ready? Run: `streamlit run streamlit_app.py`** 🚀
