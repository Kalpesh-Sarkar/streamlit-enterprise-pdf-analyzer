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
- [System Architecture](#-system-architecture)
- [Project Directory Structure](#-project-directory-structure)
- [Prerequisites](#-prerequisites)
- [Step-by-Step Installation](#-step-by-step-installation)
- [How to Run the Application](#-how-to-run-the-application)
- [Detailed Component Breakdown](#-detailed-component-breakdown)
  - [1. Executive Summary \& Question Framing Engine](#1-executive-summary--question-framing-engine)
  - [2. Dynamic Interactive Analytics Studio](#2-dynamic-interactive-analytics-studio)
  - [3. Context-Aware Vector Retrieval Q\&A](#3-context-aware-vector-retrieval-qa)
  - [4. Dual-Document Delta Comparison Engine](#4-dual-document-delta-comparison-engine)
- [⚠️ Critical Pitfalls \& Things to Avoid](#️-critical-pitfalls--things-to-avoid)
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

### 1. 📋 Automated Executive Summarization & Framing
* **Dynamic Abstractive Summarization:** Condenses dense text into clear, bulleted executive takeaways.
* **Smart Question Generation:** Auto-detects key themes (revenue, headcount, milestones) to formulate 3 critical questions per document upon ingestion.

### 2. 📊 Interactive Visual Analytics Studio
* **Numerical & Financial Metric Extraction:** Automatically extracts dollar values (`$M`, `$B`), percentages, and targets into dynamic bar charts.
* **Thematic Weight Breakdown:** Categorizes text density across *Financial Performance*, *Operations & Team*, *Future Projections*, and *Tech & Product*.
* **Keyword Density Matrix:** Ranks top-frequency non-stop words across the document text.
* **Vector Chunk Distribution:** Tracks text chunk character counts to ensure uniform vector chunking.
* **Real-time Studio Controls:** Adjust top-N keyword thresholds, sort direction (asc/desc), theme filters, and chunk length boundaries on the fly.

### 3. 🔍 Semantic Vector Retrieval Q&A
* **MiniLM Embedding Pipeline:** Vectorizes chunks using `sentence-transformers/all-MiniLM-L6-v2`.
* **FAISS In-Memory Indexing:** Conducts L2 similarity matching for instant semantic retrieval.
* **Traceable Sources:** Displays matching text chunks alongside similarity percentage scores for transparent verification.

### 4. ⚔️ Dual-Document Delta Comparison (Side-by-Side)
* **Metadata Alignment:** Compares word counts, chunk statistics, and primary keywords across two reports.
* **Comparative Synthesis:** Queries both document indexes simultaneously to generate unified comparative takeaways (e.g., comparing Q3 vs. Q4 metrics).

---

## 🏗️ System Architecture

```text
               +----------------------------------------+
               |              Uploaded PDF              |
               +-------------------+--------------------+
                                   |
                                   v
                       +-----------+-----------+
                       |   PyPDF Text Extraction|
                       +-----------+-----------+
                                   |
             +---------------------+---------------------+
             |                                           |
             v                                           v
  +----------+----------+                     +----------+----------+
  |   Fixed Text Chunks  |                     |  Full/Truncated Text    |
  +----------+----------+                     +----------+----------+
             |                                           |
             v                                           v
+------------+------------+                   +----------+----------+
| sentence-transformers    |                   | Google FLAN-T5 Model    |
| (all-MiniLM-L6-v2)      |                   | (Summary & Questions)   |
+------------+------------+                   +----------+----------+
             |                                           |
             v                                           v
+------------+------------+                   +----------+----------+
|  FAISS L2 Vector Index  |                   | Pandas Data Processing  |
+------------+------------+                   +----------+----------+
             |                                           |
             +---------------------+---------------------+
                                   |
                                   v
               +-------------------+--------------------+
               |       Streamlit Interactive UI         |
               | (Summary, Charts, Q&A, Comparison)     |
               +----------------------------------------+
```
## 📂 Project Directory Structure

enterprise-doc-intelligence-rag/
├── app.py                  # Main Streamlit application UI & reactive state handling
├── requirements.txt        # Python dependency specifications
├── README.md               # Complete project documentation
└── src/
    ├── __init__.py         # Package initialization
    └── rag_engine.py       # Core RAG engine: Embeddings, FAISS, Summaries & Comparisons

## 💻 Prerequisites

Before running the application, ensure your local system meets the following requirements:

- Operating System: Windows 10/11, macOS, or Linux.

- Python Version: Python 3.9, 3.10, or 3.11 installed.

- RAM: Minimum 4 GB free system memory (8 GB recommended for smoother HuggingFace model loading).

- Storage: ~1.5 GB free disk space (to store model weights locally upon initial run).

## ⚙️ Step-by-Step Installation

1. Clone or Download the Repository

git clone [https://github.com/YOUR-USERNAME/enterprise-doc-intelligence-rag.git](https://github.com/YOUR-USERNAME/enterprise-doc-intelligence-rag.git)
cd enterprise-doc-intelligence-rag
