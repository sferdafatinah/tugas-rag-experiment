from chunker import chunk_pages
from config import BRIEF_TOP_K, TOP_K 
from embeddings import (
    embed_text,
    embed_texts,
)
from llm import generate_text
from pdf_loader import extract_pdf_pages
from vector_store import (
    search_chunks,
    store_chunks,
)

def ingest_pdf(
    file_path: str,
    source: str,
):
    pages = extract_pdf_pages(
        file_path
    )
    chunks = chunk_pages(
        pages,
        source,
    )
    if not chunks:
        raise ValueError(
            "No readable text was found in the PDF."
        )
    texts = [
        chunk["text"]
        for chunk in chunks
    ]
    vectors = embed_texts(texts)
    stored = store_chunks(
        chunks,
        vectors,
    )
    
    # --- INFO CHUNKS STORED SAAT UPLOAD ---
    print(f"\n[INFO INGESTION] Total Chunks Stored: {stored} chunks (dari {len(pages)} halaman)\n", flush=True)
    # --------------------------------------
    
    return {
        "source": source,
        "pages_read": len(pages),
        "chunks_stored": stored,
    }

def retrieve(
    query: str,
    limit: int = TOP_K,
):
    from config import CHUNK_SIZE, CHUNK_OVERLAP
    query_vector = embed_text(
        query
    )
    results = search_chunks(
        query_vector,
        limit,
    )
    
    # --- HEADER TERMINAL LENGKAP (CHUNK_SIZE, CHUNK_OVERLAP, TOP_K) ---
    print(f"\n=== EKSPERIMEN RAG ===", flush=True)
    print(f"Parameter  -> CHUNK_SIZE = {CHUNK_SIZE} | CHUNK_OVERLAP = {CHUNK_OVERLAP} | TOP_K = {limit}", flush=True)
    print(f"Hasil      -> Total Chunk yang ditarik (Retrieved): {len(results)} chunks", flush=True)
    for i, result in enumerate(results):
        score = result.get("score", 0.0)
        page = result.get("page", "Tidak diketahui")
        print(f"  Rank {i+1} | Score: {score:.4f} | Halaman: {page}", flush=True)
    print("==================================================================================\n", flush=True)
    # ------------------------------------------------------------------
    
    return results

def build_context(
    results: list[dict],
):
    blocks = []
    for result in results:
        blocks.append(
            f"[{result['source']} | Page: {result['page']}]\n"
            f"{result['text']}"
        )
    return "\n\n---\n\n".join(blocks)

def build_sources(
    results: list[dict],
):
    seen = set()
    sources = []
    for result in results:
        key = (
            result["source"],
            result["page"],
        )
        if key in seen:
            continue
        seen.add(key)
        sources.append({
            "source": result["source"],
            "page": result["page"],
            "score": result["score"],
        })
    return sources

async def ask_question(
    question: str,
):
    results = retrieve(
        question,
        TOP_K,
    )
    context = build_context(
        results
    )
    system_prompt = """
You are a RAG assistant.
Answer only using the provided context.
If the context does not contain enough information,
say that the answer was not found in the uploaded documents.
Keep the answer concise.
Mention the source and page when useful.
"""
    user_prompt = f"""
QUESTION:
{question}
CONTEXT:
{context}
"""
    answer = await generate_text(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )
    return {
        "answer": answer,
        "sources": build_sources(results),
    }

async def create_brief(
    topic: str,
):
    results = retrieve(
        topic,
        BRIEF_TOP_K,
    )
    context = build_context(
        results
    )
    system_prompt = """
You create concise topic briefs from retrieved documents.
Use only the provided context.
Structure the response as:
1. Summary
2. Key Points
3. Source References
Do not invent information that is not present in the context.
"""
    user_prompt = f"""
TOPIC:
{topic}
CONTEXT:
{context}
"""
    brief = await generate_text(
        system_prompt=system_prompt,
        user_prompt=user_prompt,
    )
    return {
        "topic": topic,
        "brief": brief,
        "sources": build_sources(results),
    }