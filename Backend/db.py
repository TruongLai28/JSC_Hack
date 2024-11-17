import chromadb
import pandas as pd
import chromadb.utils.embedding_functions as embedding_functions
import os
from dotenv import load_dotenv

load_dotenv()

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv('API_KEY'),
    model_name="text-embedding-3-large"  # You can change to any of the three models
)

# Initialize ChromaDB client
chroma_client = chromadb.Client()

# Get existing collection or create new one
ostem_collection = chroma_client.get_or_create_collection(
    name="ostem_collection", 
    embedding_function=openai_ef)

# Load CSV data
ostem = pd.read_csv("data/ostems.csv")
pathway = pd.read_csv("data/pathways.csv")
event = pd.read_csv("data/events.csv")
solicitation = pd.read_csv("data/solicitations.csv")

# Add documents to collection
ostem_collection.add(
    documents=[f"{row['Title']}. {row['Description']}" for _, row in ostem.iterrows()],  # Combine title and description
    metadatas=[{
        "title": row['Title'],
        "type": row['Type'],
        "url": row['URL']
    } for _, row in ostem.iterrows()],
    ids=[str(id) for id in ostem['ID']]
)


# Test query
ostem_results = ostem_collection.query(
    query_texts=["Mechanical Engineering opportunities for students"],
    n_results=3,
    include=['metadatas', 'documents', 'distances']  # Add distances to the returned results
)

print("\nTest query results:")
for i, doc in enumerate(ostem_results['documents'][0]):
    # Calculate similarity score from distance
    # ChromaDB returns euclidean distance, convert to cosine similarity
    # Cosine similarity = 1 - (euclidean_distance² / 2)
    similarity_score = 1 - (ostem_results['distances'][0][i] / 2)
    
    print(f"\nResult {i+1}:")
    print(f"Title: {ostem_results['metadatas'][0][i]['title']}")
    print(f"Type: {ostem_results['metadatas'][0][i]['type']}")
    print(f"URL: {ostem_results['metadatas'][0][i]['url']}")
    print(f"Similarity Score: {similarity_score:.3f}")  # Display similarity score rounded to 4 decimal places
    
    
#0.90-1.00: Near identical meaning
#0.70-0.90: Very similar meaning
#0.50-0.70: Related concepts
#0.30-0.50: Somewhat related
#Below 0.30: Likely unrelated    
