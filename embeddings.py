import json
from openai import OpenAI
from dotenv import load_dotenv
import os
client = OpenAI()

def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

# Load the JSON data from file
with open('etf_data.json', 'r') as file:
    data = json.load(file)

# Generate embeddings for each ETF
for etf in data:
    ticker = etf['ticker']
    long_name = etf['long_name']
    summary = etf['summary']
    
    long_name_embedding = get_embedding(long_name)
    summary_embedding = get_embedding(summary)
    
    etf['long_name_embedding'] = long_name_embedding
    etf['summary_embedding'] = summary_embedding

# Save the updated data with embeddings to a new JSON file
with open('etf_data_with_embeddings.json', 'w') as file:
    json.dump(data, file, indent=4)