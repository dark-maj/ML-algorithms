from ollama import embeddings
response=embeddings(
    model="nomic-embed-text",
    prompt="Python Machine Learning SQL"
)
vector=response["embedding"]
print(len(vector))
print(vector[:10])