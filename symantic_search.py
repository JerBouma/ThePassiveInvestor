import json
import numpy as np
from openai import OpenAI
import thepassiveinvestor as pi

client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Load the JSON data with embeddings from file
with open('etf_data_with_embeddings.json', 'r') as file:
    data = json.load(file)

# Get user input
user_input = input("Enter a description of the investment strategy: ")

# Generate embedding for user input
user_input_embedding = get_embedding(user_input)

# Calculate cosine similarity between user input and each ETF
for etf in data:
    etf['similarity'] = cosine_similarity(user_input_embedding, etf['summary_embedding'])

# Sort ETFs based on similarity score
data.sort(key=lambda x: x['similarity'], reverse=True)

# # Print top 3 ETF recommendations
# print("Top 3 ETF Recommendations:")
# for i in range(3):
#     print(f"{i+1}. {data[i]['long_name']}")
#     print(f"{i+1}. {data[i]['summary']}")
#     print(f"   Similarity Score: {data[i]['similarity']}")

# Collect data from a set of ETFs and compare them
etf_comparison = pi.collect_data([data[1]['ticker'],data[2]['ticker'],data[3]['ticker']], comparison=True)

# Show the comparison
print(etf_comparison)

# Download Analysis
etf_report = [data[1]['ticker'],data[2]['ticker'],data[3]['ticker']]
pi.create_ETF_report(etf_report, 'ETF Report.xlsx')