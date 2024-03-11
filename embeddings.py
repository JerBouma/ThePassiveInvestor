import os
import json
import pandas as pd
from openai import OpenAI

client = OpenAI()

def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding

# Load the JSON data
with open('paste.txt', 'r') as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

# Generate embeddings
df['long_name_embedding'] = df.long_name.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
df['summary_embedding'] = df.summary.apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))

# Save DataFrame with embeddings
df.to_csv('etf_data_with_embeddings.csv', index=False)