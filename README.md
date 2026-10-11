# 🔬 Autonomous Research & Knowledge Agent

> A self-managing multi-agent system that researches any topic thoroughly, analyzes findings critically, and produces high-quality knowledge reports — with persistent memory and a clean web interface.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## What This System Does

This is not a simple chatbot. It is a **self-directed research team** consisting of specialized agents:

| Agent | Role |
|-------|------|
| **Researcher** | Searches the web, finds sources, scrapes key pages |
| **Analyst** | Critically evaluates findings, spots contradictions & gaps |
| **Writer** | Synthesizes everything into a clean, structured report |

The system:
- Conducts multi-source research automatically
- Stores knowledge in a persistent vector memory (ChromaDB)
- Saves polished Markdown reports
- Offers both CLI and beautiful Streamlit web interface
- Supports scheduled autonomous runs

---

## Quick Start

### 1. Clone & Setup

```bash
git clone https://github.com/shabanihamidu19-cell/autonomous-research-knowledge-agent.git
cd autonomous-research-knowledge-agent

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

```env
OPENAI_API_KEY=sk-your-key-here
MODEL_NAME=gpt-4o-mini        # or gpt-4o for higher quality
```

### 3. Run Your First Research

**Command Line:**
```bash
python run_agent.py "Impact of autonomous AI agents on software engineering"
```

**With depth control:**
```bash
python run_agent.py "Quantum error correction advances" --depth deep
python run_agent.py "Latest LLM benchmarks" --depth quick
```

**Interactive mode:**
```bash
python run_agent.py
```

**Web Interface (recommended):**
```bash
streamlit run app/streamlit_app.py
```

---

## Features

- **Multi-Agent Collaboration** — Researcher → Analyst → Writer pipeline
- **Web Search + Scraping** — DuckDuckGo search + intelligent page scraping
- **Persistent Memory** — ChromaDB vector store remembers past research
- **Three Depth Levels** — `quick` / `standard` / `deep`
- **Beautiful Reports** — Structured Markdown with Executive Summary, Key Findings, Analysis, Open Questions, and Sources
- **Streamlit Dashboard** — Clean web UI with history and download
- **Scheduler** — Optional daily/weekly autonomous research jobs
- **CLI Tools** — List past topics, view stats

---

## Project Structure

```
autonomous-research-agent/
├── agents/               # Specialized agents
│   ├── researcher.py
│   ├── analyst.py
│   ├── writer.py
│   └── supervisor.py
├── tools/                # Agent tools
│   ├── web_search.py     # DuckDuckGo search + news
│   └── web_scraper.py    # Clean page content extraction
├── memory/
│   └── vector_store.py   # ChromaDB persistent memory
├── core/
│   ├── crew.py           # Main orchestration logic
│   ├── config.py         # Settings & paths
│   └── scheduler.py      # Optional autonomous scheduling
├── app/
│   └── streamlit_app.py  # Web interface
├── data/
│   ├── knowledge/        # Generated Markdown reports
│   └── logs/
├── run_agent.py          # CLI entry point
├── requirements.txt
└── README.md
```

---

## Usage Examples

```bash
# Basic research
python run_agent.py "The future of multi-agent systems"

# Deep research
python run_agent.py "CRISPR gene editing clinical trials 2024-2026" --depth deep

# List all past research topics
python run_agent.py --list

# Show memory stats
python run_agent.py --stats
```

---

## Optional: Autonomous Scheduling

You can make the agent research topics on a schedule:

```python
from core.scheduler import ResearchScheduler

scheduler = ResearchScheduler()
scheduler.add_daily_research(
    topic="Latest developments in AI agents",
    hour=7,
    minute=30,
    depth="standard"
)
scheduler.start()
```

Or run the example:
```bash
python -m core.scheduler
```

---

## Requirements

- Python 3.11+
- OpenAI API key (GPT-4o-mini recommended for cost efficiency)
- Internet connection (for web search & scraping)

---

## Roadmap / Future Improvements

- [ ] Add local LLM support (Ollama / LM Studio)
- [ ] PDF report generation
- [ ] Multi-language support
- [ ] Source credibility scoring
- [ ] Automatic follow-up research on open questions
- [ ] GitHub Action for scheduled research
- [ ] Discord / Telegram notification on completion

---

## License

MIT License. Use freely, modify, and build upon it.

---

**Built with the mindset of creating systems that work for you — not the other way around.**
