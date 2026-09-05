import io
import re
from collections import Counter
import faiss
import numpy as np
import pandas as pd
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from transformers import T5Tokenizer, T5ForConditionalGeneration


class MultiDocRAG:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.tokenizer = T5Tokenizer.from_pretrained('google/flan-t5-base', legacy=False)
        self.model = T5ForConditionalGeneration.from_pretrained('google/flan-t5-base')
        self.docs = {}

    def _extract_dynamic_chart_data(self, raw_text):
        """Extracts numerical metrics and thematic topic distributions for automated chart generation."""
        # 1. Extract Numerical Metrics & Financial Quantities
        metric_matches = []

        # Currency pattern ($X.XM or $XX,XXX)
        currencies = re.findall(r'(\$[0-9\.]+\s*(?:Million|M|Billion|B|k|K)?)', raw_text)
        for val in currencies[:4]:
            num_clean = re.sub(r'[\$,]', '', val).lower()
            scale = 1.0
            if 'm' in num_clean:
                num_clean = num_clean.replace('million', '').replace('m', '').strip()
                scale = 1.0  # in Millions
            elif 'k' in num_clean:
                num_clean = str(float(num_clean.replace('k', '').strip()) / 1000)
            try:
                metric_matches.append(("Extracted Amount ($M)", float(num_clean) * scale))
            except ValueError:
                pass

        # Percentage pattern (e.g. 18.5%)
        percentages = re.findall(r'([0-9\.]+\%)', raw_text)
        for pct in percentages[:3]:
            try:
                metric_matches.append((f"Metric Ratio ({pct})", float(pct.replace('%', ''))))
            except ValueError:
                pass

        # Fallback metric chart data if document has few numbers
        if not metric_matches:
            metric_matches = [("Section A Density", 45), ("Section B Density", 70), ("Key Insights Count", 12)]

        df_metrics = pd.DataFrame(metric_matches, columns=["Metric Target", "Extracted Value"]).drop_duplicates(
            subset=["Metric Target"])

        # 2. Content Theme Distribution Breakdown
        lowered = raw_text.lower()
        financial_count = sum(
            lowered.count(w) for w in ['revenue', 'profit', 'expenses', 'budget', 'dollar', 'cost', 'financial'])
        operations_count = sum(
            lowered.count(w) for w in ['team', 'engineers', 'hiring', 'launch', 'users', 'operational', 'project'])
        strategy_count = sum(
            lowered.count(w) for w in ['target', 'projected', 'future', 'q4', '2027', 'goal', 'milestone'])
        tech_count = sum(lowered.count(w) for w in ['ai', 'cloud', 'system', 'research', 'vector', 'model', 'alpha'])

        total_hits = max(1, financial_count + operations_count + strategy_count + tech_count)
        theme_data = {
            "Theme Focus": ["Financial Performance", "Operations & Team", "Future Projections", "Tech & Product"],
            "Weight Share (%)": [
                round((financial_count / total_hits) * 100, 1) or 25.0,
                round((operations_count / total_hits) * 100, 1) or 25.0,
                round((strategy_count / total_hits) * 100, 1) or 25.0,
                round((tech_count / total_hits) * 100, 1) or 25.0
            ]
        }
        df_themes = pd.DataFrame(theme_data)

        return df_metrics, df_themes

    def ingest_pdf(self, pdf_file, doc_id="Doc 1"):
        if isinstance(pdf_file, bytes):
            pdf_file = io.BytesIO(pdf_file)

        reader = PdfReader(pdf_file)
        raw_text = ""
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                raw_text += extracted + "\n"

        chunks = [raw_text[i:i + 300] for i in range(0, len(raw_text), 250)]
        embeddings = self.embedder.encode(chunks)

        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(np.array(embeddings).astype('float32'))

        # 1. Executive Summary Generation
        summary_prompt = f"Summarize key financial and operational findings in bullet points:\n\n{raw_text[:1200]}"
        input_ids = self.tokenizer.encode(summary_prompt, return_tensors="pt", max_length=512, truncation=True)
        summary_outputs = self.model.generate(input_ids, max_new_tokens=150)
        summary_text = self.tokenizer.decode(summary_outputs[0], skip_special_tokens=True)

        # 2. Automated Question Framing Engine
        q_prompt = f"Ask 3 specific questions about the revenue, operations, and targets in this report:\n\n{raw_text[:1000]}"
        q_input_ids = self.tokenizer.encode(q_prompt, return_tensors="pt", max_length=512, truncation=True)
        q_outputs = self.model.generate(q_input_ids, max_new_tokens=120)
        q_raw = self.tokenizer.decode(q_outputs[0], skip_special_tokens=True)

        parsed_qs = [q.strip() for q in re.split(r'\?|\n|\d+\.', q_raw) if len(q.strip()) > 10]
        suggested_questions = [q if q.endswith("?") else f"{q}?" for q in parsed_qs]

        if len(suggested_questions) < 3:
            suggested_questions = [
                f"What are the main financial results and revenue metrics recorded in {doc_id}?",
                f"What operational developments or team expansions occurred in {doc_id}?",
                f"What key targets, forecasts, or future milestones are specified in {doc_id}?"
            ]

        # 3. Dynamic Chart Analytics Data Extraction
        df_metrics, df_themes = self._extract_dynamic_chart_data(raw_text)

        # Keyword Extraction
        words = re.findall(r'\b[a-zA-Z]{3,}\b', raw_text.lower())
        stop_words = {'the', 'and', 'for', 'that', 'with', 'this', 'was', 'are', 'from', 'has', 'have', 'total',
                      'reached'}
        filtered_words = [w for w in words if w not in stop_words]
        top_keywords = Counter(filtered_words).most_common(10)

        chunk_stats = [{"chunk_id": i, "char_len": len(c), "word_count": len(c.split())} for i, c in enumerate(chunks)]

        doc_meta = {
            "doc_id": doc_id,
            "pages": len(reader.pages),
            "total_chunks": len(chunks),
            "total_words": len(raw_text.split()),
            "summary": summary_text,
            "suggested_questions": suggested_questions[:3],
            "df_metrics": df_metrics,
            "df_themes": df_themes,
            "top_keywords": top_keywords,
            "chunk_stats": chunk_stats,
            "raw_text": raw_text,
            "index": index,
            "chunks": chunks
        }

        self.docs[doc_id] = doc_meta
        return doc_meta

    def query_doc(self, doc_id, question, top_k=3):
        if doc_id not in self.docs:
            return None

        doc = self.docs[doc_id]
        q_embed = self.embedder.encode([question])
        distances, indices = doc["index"].search(np.array(q_embed).astype('float32'), top_k)

        retrieved_items = []
        combined_text = ""

        for dist, idx in zip(distances[0], indices[0]):
            if idx < len(doc["chunks"]):
                text_content = doc["chunks"][int(idx)]
                similarity = round(float(1 / (1 + dist)) * 100, 2)
                retrieved_items.append({
                    "chunk_id": int(idx),
                    "text": text_content,
                    "similarity": similarity,
                    "word_count": len(text_content.split())
                })
                combined_text += " " + text_content

        prompt = f"Context: {combined_text}\n\nQuestion: {question}\n\nAnswer:"
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
        outputs = self.model.generate(input_ids, max_new_tokens=80)
        answer = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return {
            "answer": answer.strip() if answer.strip() else "No direct answer found.",
            "retrieved_items": retrieved_items
        }

    def compare_documents(self, doc1_id, doc2_id, topic_question):
        res1 = self.query_doc(doc1_id, topic_question)
        res2 = self.query_doc(doc2_id, topic_question)

        comp_prompt = f"Compare these two document findings concisely.\n\nDocument 1 ({doc1_id}): {res1['answer'] if res1 else 'N/A'}\n\nDocument 2 ({doc2_id}): {res2['answer'] if res2 else 'N/A'}\n\nComparison Summary:"
        input_ids = self.tokenizer.encode(comp_prompt, return_tensors="pt")
        outputs = self.model.generate(input_ids, max_new_tokens=120)
        comp_summary = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return {
            "doc1_answer": res1["answer"] if res1 else "N/A",
            "doc2_answer": res2["answer"] if res2 else "N/A",
            "comparison": comp_summary,
            "doc1_items": res1["retrieved_items"] if res1 else [],
            "doc2_items": res2["retrieved_items"] if res2 else []
        }