from embedding import get_embedding
import numpy as np
def cosine_similarity(vector_a, vector_b):
    dot_product = np.dot(vector_a, vector_b)
    magnitude_a = np.linalg.norm(vector_a)
    magnitude_b = np.linalg.norm(vector_b)
    return dot_product/(magnitude_a * magnitude_b)
resume = "Python Machine Learning SQL"

job = "Looking for a Python developer with SQL and Machine Learning."

vec1 = get_embedding(resume)
vec2 = get_embedding(job)

score = cosine_similarity(vec1, vec2)

print(score)