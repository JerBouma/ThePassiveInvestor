import json
import openai
import numpy as np
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load the data from the JSON file
with open('etf_data.json', 'r') as file:
    etf_data = json.load(file)

# Create a list of summaries from the ETF data
summaries = [etf['summary'] for etf in etf_data]

# Generate embeddings for the summaries using OpenAI API
embeddings = []
for summary in summaries:
    response = openai.Embedding.create(
        input=summary,
        model="text-embedding-ada-002"
    )
    embedding = response['data'][0]['embedding']
    embeddings.append(embedding)

# Search through the ETF summaries
def search_etfs(query, n=3):
    query_embedding = openai.Embedding.create(
        input=query,
        model="text-embedding-ada-002"
    )['data'][0]['embedding']

    similarities = []
    for embedding in embeddings:
        similarity = np.dot(embedding, query_embedding) / (np.linalg.norm(embedding) * np.linalg.norm(query_embedding))
        similarities.append(similarity)

    # Sort ETFs based on similarity scores
    sorted_indices = np.argsort(similarities)[::-1]

    # Print the top n matching ETFs
    for i in range(n):
        index = sorted_indices[i]
        etf = etf_data[index]
        print(f"Top {i+1} match:")
        print("Long Name:", etf['long_name'])
        print("Summary:", etf['summary'])
        print("Similarity Score:", similarities[index])
        print()

# Ask for user input
user_query = input("Enter your search query: ")

# Search for the most similar ETFs
search_etfs(user_query)