from ollama import embeddings

# response=embeddings(
#     model="nomic-embed-text",
#     prompt="Python Machine Learning SQL"
# )
# vector=response["embedding"]
# print(len(vector))
# print(vector[:10])

def get_embedding(resume_text):
    response =embeddings(
        model="nomic-embed-text",
        prompt=resume_text
    )
    
    vector=response["embedding"]
    return vector

#