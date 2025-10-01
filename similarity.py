import numpy as np
from numpy.linalg import norm

# Embeddings hypothétiques pour démonstration
# En réalité, ces vecteurs ont des centaines de dimensions.
embeddings = {
    "chat":    np.array([0.12, -0.85, 0.43,  0.01]),
    "chien":   np.array([0.15, -0.80, 0.40,  0.05]),
    "animal":  np.array([0.10, -0.82, 0.41,  0.03]),
    "voiture": np.array([0.90,  0.10, -0.20, 0.70])
}

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

sim_chat_chien = cosine_similarity(embeddings["chat"], embeddings["chien"])
sim_chat_voiture = cosine_similarity(embeddings["chat"], embeddings["voiture"])
sim_chat_animal = cosine_similarity(embeddings["chat"], embeddings["animal"])

print(f"Similarité('chat', 'chien'): {sim_chat_chien:.4f}")
print(f"Similarité('chat', 'voiture'): {sim_chat_voiture:.4f}")
print(f"Similarité('chat', 'animal'): {sim_chat_animal:.4f}")