import torch
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load multilingual model optimized for sentence embeddings
model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# Sample French texts to embed
texts = [
    "un chat.",
    "un chien.",
    "une automobile."
]

def get_embeddings(texts, model):
    """Generate embeddings using sentence-transformers model"""
    return model.encode(texts)

# Generate embeddings
embeddings = get_embeddings(texts, model)

# Calculate similarities
similarities = cosine_similarity(embeddings)

print("Similarity matrix:")
print("Texts:", texts)
print("\nSimilarity scores:")
for i, text1 in enumerate(texts):
    for j, text2 in enumerate(texts):
        if i < j:  # Only show upper triangle
            print(f"'{text1}' vs '{text2}': {similarities[i][j]:.4f}")

# Find most similar pair
max_sim = 0
best_pair = None
for i in range(len(texts)):
    for j in range(i+1, len(texts)):
        if similarities[i][j] > max_sim:
            max_sim = similarities[i][j]
            best_pair = (texts[i], texts[j])

print(f"\nMost similar pair: '{best_pair[0]}' and '{best_pair[1]}' (similarity: {max_sim:.4f})")

# Test with a query
print("\n--- Query Test ---")
query = "Cet animal mange des souris"
query_embedding = get_embeddings([query], model)[0]

# Calculate similarity with each text
query_similarities = cosine_similarity([query_embedding], embeddings)[0]

print(f"Query: '{query}'")
for i, text in enumerate(texts):
    print(f"Similarity with '{text}': {query_similarities[i]:.4f}")

# Find most similar text to query
best_match_idx = np.argmax(query_similarities)
print(f"\nBest match for '{query}': '{texts[best_match_idx]}' (similarity: {query_similarities[best_match_idx]:.4f})")

# Clear model from memory to prevent safetensors saving
del model
torch.cuda.empty_cache() if torch.cuda.is_available() else None