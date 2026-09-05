<a id="top"></a>

# ⚡ Enterprise Document Intelligence & Comparison Engine

[![Streamlit](https://img.shields.io/badge/Streamlit-1.31+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-00599C?style=for-the-badge)](https://github.com/facebookresearch/faiss)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

> **An end-to-end, privacy-centric Retrieval-Augmented Generation (RAG) platform designed to parse, analyze, visualize, and compare complex enterprise PDFs and financial reports locally—without relying on external API keys.**

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#system-architecture)
- [Project Directory Structure](#-project-directory-structure)
- [Prerequisites & Development Environment](#-prerequisites--development-environment)
- [Step-by-Step Installation](#step-by-step-installation)
- [How to Run the Application](#-how-to-run-the-application)
- [Detailed Component Breakdown](#detailed-component-breakdown)
  - [1. Executive Summary \& Question Framing Engine](#1-executive-summary--question-framing-engine)
  - [2. Dynamic Interactive Analytics Studio](#2-dynamic-interactive-analytics-studio)
  - [3. Context-Aware Vector Retrieval Q\&A](#3-context-aware-vector-retrieval-qa)
  - [4. Dual-Document Delta Comparison Engine](#4-dual-document-delta-comparison-engine)
- [Critical Pitfalls \& Things to Avoid](#️-critical-pitfalls--things-to-avoid)
- [Troubleshooting](#-troubleshooting)
- [License \& Acknowledgments](#-license--acknowledgments)

---

## 🔍 Overview

Modern corporate reports (Q3/Q4 financial updates, legal disclosures, technical whitepapers) contain critical insights spread across dense text, numerical metrics, and unstructured tables. Manually comparing two sequential reports or extracting key operational deltas is time-consuming and error-prone.

The **Enterprise Document Intelligence & Comparison Engine** addresses this challenge by providing an all-in-one local analytical workspace that:
1. Ingests PDFs into an in-memory FAISS vector index.
2. Formulates executive summaries and automated investigation questions using Google's `FLAN-T5`.
3. Extracts metrics, themes, and chunk stats to render an interactive visual analytics dashboard.
4. Synthesizes cross-document comparative insights for side-by-side delta evaluation.

---

## ✨ Key Features

#### 1. 📋 Automated Executive Summarization & Framing
* **Dynamic Abstractive Summarization:** Condenses dense text into clear, bulleted executive takeaways.
* **Smart Question Generation:** Auto-detects key themes (revenue, headcount, milestones) to formulate 3 critical questions per document upon ingestion.

#### 2. 📊 Interactive Visual Analytics Studio
* **Numerical & Financial Metric Extraction:** Automatically extracts dollar values (`$M`, `$B`), percentages, and targets into dynamic bar charts.
* **Thematic Weight Breakdown:** Categorizes text density across *Financial Performance*, *Operations & Team*, *Future Projections*, and *Tech & Product*.
* **Keyword Density Matrix:** Ranks top-frequency non-stop words across the document text.
* **Vector Chunk Distribution:** Tracks text chunk character counts to ensure uniform vector chunking.
* **Real-time Studio Controls:** Adjust top-N keyword thresholds, sort direction (asc/desc), theme filters, and chunk length boundaries on the fly.

#### 3. 🔍 Semantic Vector Retrieval Q&A
* **MiniLM Embedding Pipeline:** Vectorizes chunks using `sentence-transformers/all-MiniLM-L6-v2`.
* **FAISS In-Memory Indexing:** Conducts L2 similarity matching for instant semantic retrieval.
* **Traceable Sources:** Displays matching text chunks alongside similarity percentage scores for transparent verification.

#### 4. ⚔️ Dual-Document Delta Comparison (Side-by-Side)
* **Metadata Alignment:** Compares word counts, chunk statistics, and primary keywords across two reports.
* **Comparative Synthesis:** Queries both document indexes simultaneously to generate unified comparative takeaways (e.g., comparing Q3 vs. Q4 metrics).

---

## <a id="system-architecture"></a>🏗️ System Architecture

```text
                       +----------------------------------------+
                       |              Uploaded PDF              |
                       +-------------------+--------------------+
                                           |
                                           v
                               +-----------+-----------+
                               | PyPDF Text Extraction |
                               +-----------+-----------+
                                           |
                     +---------------------+---------------------+
                     |                                           |
                     v                                           v
          +----------+----------+                     +----------+----------+
          |  Fixed Text Chunks  |                     | Full/Truncated Text |
          +----------+----------+                     +----------+----------+
                     |                                           |
                     v                                           v
        +------------+------------+                   +----------+-------------+
        | sentence-transformers   |                   |  Google FLAN-T5 Model  |
        |  (all-MiniLM-L6-v2)     |                   | (Summary & Questions)  |
        +------------+------------+                   +----------+-------------+
                     |                                           |
                     v                                           v
        +------------+------------+                   +----------+-------------+
        |  FAISS L2 Vector Index  |                   | Pandas Data Processing |
        +------------+------------+                   +----------+-------------+
                     |                                           |
                     +---------------------+---------------------+
                                           |
                                           v
                       +-------------------+--------------------+
                       |       Streamlit Interactive UI         |
                       |  (Summary, Charts, Q&A, Comparison)    |
                       +----------------------------------------+

```

---

## 📂 Project Directory Structure

```text
enterprise-doc-intelligence-rag/
├── .github/
│   └── workflows/
│       └── ci.yml           # Automated syntax & dependency build checks
├── .streamlit/
│   └── config.toml          # Streamlit theme & file upload capacity configs
├── src/
│   └── rag_engine.py        # Core RAG pipeline, FAISS indexing & LLM logic
├── test_pdfs/
│   └── sample_maker.py      # Benchmark document generation script
├── app.py                   # Streamlit dashboard interface & user controls
├── requirements.txt         # Production dependency manifest
├── .gitignore               # Excludes virtualenvs, caches, and test artifacts
├── LICENSE                  # MIT open-source license
└── README.md                # Technical documentation & navigation index

```

---

## 💻 Prerequisites & Development Environment

```
IDE Recommendation: This project was built and optimized using PyCharm. Operating the repository through PyCharm makes it significantly easier to manage your Python virtual environment, install requirements via the built-in package manager, and run Streamlit directly from the terminal tool window.

```

Before running the application, ensure your local system meets the following requirements:

* **Operating System:** Windows 10/11, macOS, or Linux.
* **Python Version:** Python `3.9`, `3.10`, or `3.11` installed.
* **RAM:** Minimum 4 GB free system memory (8 GB recommended for smoother HuggingFace model loading).
* **Storage:** ~1.5 GB free disk space (to store model weights locally upon initial run).

---

## <a id="step-by-step-installation"></a>⚙️ Step-by-Step Installation

#### 1. Clone or Download the Repository

```bash
git clone [https://github.com/YOUR-USERNAME/enterprise-doc-intelligence-rag.git](https://github.com/YOUR-USERNAME/enterprise-doc-intelligence-rag.git)
cd enterprise-doc-intelligence-rag

```

*(If you uploaded the project directly via GitHub website, download/extract the ZIP folder and navigate into it).*

#### 2. Set Up a Virtual Environment

Creating an isolated environment prevents package conflicts:

* **Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\activate

```


* **macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```



#### 3. Upgrade Pip & Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt

```

---

## 🚀 How to Run the Application

Execute the following command in your terminal within the activated virtual environment:

```bash
python -m streamlit run app.py

```

Streamlit will initialize the environment, download model weights on the first run, and automatically open the application in your default web browser at `http://localhost:8501`.

---

## <a id="detailed-component-breakdown"></a>🛠️ Detailed Component Breakdown

#### 1. Executive Summary & Question Framing Engine

* When a PDF is loaded, `src/rag_engine.py` processes raw text into `google/flan-t5-base`.
* The model generates a concise bulleted executive overview.
* Regular expressions parse generated response strings to display clean interactive question cards.

#### 2. Dynamic Interactive Analytics Studio

* Text strings undergo regex pattern extraction to build dynamic DataFrames for:
* Financial amounts (`$M`, `$B`).
* Relative percentages and metric trends.
* Keyword frequency rankings (excluding standard English stop words).


* Users can use the **Chart Control Bar** to adjust keyword density displays, change chart sort orders, filter out specific themes, or isolate specific chunk length ranges.

#### 3. Context-Aware Vector Retrieval Q&A

* Questions submitted in **Tab 2** are transformed into vector embeddings via `all-MiniLM-L6-v2`.
* FAISS executes an L2 distance search across vector spaces to pull the top $k$ matching chunks.
* Extracted chunks provide grounded context for `FLAN-T5` to synthesize answers, minimizing hallucination risk.

#### 4. Dual-Document Delta Comparison Engine

* In **Tab 3**, uploading two documents (or clicking **🚀 Load Sample Benchmark Pair**) loads dual vector indexes.
* Queries submitted in the comparative search box evaluate both FAISS indexes simultaneously.
* Answers from both documents are processed alongside a comparative prompt to generate a consolidated delta analysis.

---

## ⚠️ Critical Pitfalls & Things to Avoid

To maintain application performance and prevent setup issues, keep the following in mind:

#### 1. Git & Version Control Hygiene (`.gitignore`)

* ❌ **DO NOT commit virtual environments (`venv/`, `env/`) or Python cache files (`__pycache__/`, `*.pyc`).** Doing so bloats your repository and can cause platform mismatches.
* ❌ **DO NOT upload secret token files (`.streamlit/secrets.toml`) or private documents** to public GitHub repositories.

#### 2. Model Caching Behavior (`@st.cache_resource`)

* Streamlit caches the heavy machine learning models in memory to avoid reloading them on every user interaction.
* ⚠️ **If you edit prompt templates, chunk sizes, or parsing logic inside `src/rag_engine.py`, you MUST restart the Streamlit server in terminal (`Ctrl + C` then rerun `python -m streamlit run app.py`).** Simply refreshing your browser tab will continue using the previously cached code instance.

#### 3. PDF Sizing & Memory Limits

* The application runs inference locally on your CPU. Ingesting massive PDFs (150+ pages) may lead to long processing times during summary generation. For optimal performance, use targeted quarterly, annual, or project status reports under 30 pages.

#### 4. Package Conflicts (`faiss-cpu` vs `faiss`)

* Ensure your `requirements.txt` specifies `faiss-cpu` rather than `faiss`. Installing the standard `faiss` package without GPU drivers configured will lead to execution crashes on standard CPU environments.

---

## 🔧 Troubleshooting

| Issue | Cause | Resolution |
| --- | --- | --- |
| **Model download takes a long time** | Hugging Face models download on the first run. | Wait for initial download to complete; subsequent launches load from local cache (`~/.cache/huggingface`). |
| **Code updates in `rag_engine.py` don't take effect** | Streamlit cached the old class in memory. | Stop Streamlit (`Ctrl + C`) in terminal and restart `python -m streamlit run app.py`. |
| **`ModuleNotFoundError: No module named 'src'`** | Python execution path issue. | Ensure you run Streamlit directly from the project root folder containing `app.py`. |
| **Out of Memory (OOM) Errors** | Insufficient RAM for holding multiple large models. | Close other resource-heavy background processes or process shorter documents. |

---

## 📄 License & Acknowledgments

* **License:** Distributed under the [MIT License](https://www.google.com/search?q=LICENSE).
* **Open-Source Technologies:**
* [Streamlit](https://streamlit.io/) for the web UI frame.
* [Hugging Face Transformers](https://huggingface.co/) for `FLAN-T5` and `Sentence-Transformers`.
* [FAISS](https://github.com/facebookresearch/faiss) by Meta AI for fast similarity search.
* [PyPDF](https://pypdf.readthedocs.io/) for document parsing.

---

<ElicitationsGroup message="Your detailed README.md is ready. Choose your next step:">
  <Elicitation label="Generate requirements.txt file contents" query="Give me the exact text needed for the requirements.txt file for this project."/>
  <Elicitation label="Deploy to Streamlit Community Cloud" query="Show me how to deploy this GitHub repository to Streamlit Community Cloud for free."/>
</ElicitationsGroup>

<p align="right"><a href="#top" onclick="scrollToTop(event)" style="text-decoration: none; font-weight: 600;">Back to Top ↑</a></p>
