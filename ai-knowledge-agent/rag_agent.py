from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def ask_agent(query):

    query_embedding = model.encode(query)

    # search using Endee
    results = endee.search(query_embedding)

    context = " ".join(results)

    answer = llm.generate(
        f"Answer using context:\n{context}\nQuestion:{query}"
    )

    return answer
