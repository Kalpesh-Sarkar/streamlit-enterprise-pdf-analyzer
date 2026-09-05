# Multimodal Document RAG Pipeline (`multimodal-doc-rag`)

[![Kaggle Notebook](https://img.shields.io/badge/Kaggle-View_Notebook-blue?logo=kaggle)](https://www.kaggle.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview
A lightweight PDF Document Retrieval-Augmented Generation (RAG) pipeline built using FAISS, HuggingFace Sentence Transformers, Google FLAN-T5, and Streamlit.

## Architecture
```mermaid
graph LR
    A[PDF Upload] --> B[pypdf Chunking]
    B --> C[all-MiniLM Embeddings]
    C --> D[FAISS Vector Store]
    D --> E[FLAN-T5 Answer Generation]