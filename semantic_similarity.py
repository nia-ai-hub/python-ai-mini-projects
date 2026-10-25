
from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2"
)

sentence1 = input("First sentence: ")
sentence2 = input("Second sentence: ")

embeddings = model.encode([sentence1, sentence2])

score = cos_sim(embeddings[0], embeddings[1]).item()

print("Similarity:", round(score, 3))
print("Percentage-like score:", round(score * 100, 1), "%")