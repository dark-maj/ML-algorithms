from parser import extract_text
from embedding import get_embedding
from similarity import cosine_similarity
from llm import analyze_resume

# ----------------------------
# Resume PDF Path
# ----------------------------
resume_path = "C:/Users/Admin/Desktop/RESUME(JAAHNAVI).pdf"

# ----------------------------
# Extract Resume Text
# ----------------------------
resume_text = extract_text(resume_path)

# ----------------------------
# Job Description
# ----------------------------
job_description = """
We are looking for a Python Developer with experience in:

- Python
- Machine Learning
- SQL
- Data Structures & Algorithms
- Git
- REST APIs
- Problem Solving
- Flask or FastAPI
"""

# ----------------------------
# Generate Embeddings
# ----------------------------
resume_vector = get_embedding(resume_text)
job_vector = get_embedding(job_description)

# ----------------------------
# Calculate Similarity
# ----------------------------
similarity_score = cosine_similarity(resume_vector, job_vector)

print("=" * 60)
print(f"Similarity Score : {similarity_score:.4f}")
print(f"Match Percentage : {similarity_score * 100:.2f}%")
print("=" * 60)

# ----------------------------
# AI Analysis
# ----------------------------
analysis = analyze_resume(resume_text, job_description)

print("\n🤖 AI Resume Analysis\n")
print(analysis)