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

pathway_collection = chroma_client.get_or_create_collection(
    name="pathway_collection", 
    embedding_function=openai_ef)

event_collection = chroma_client.get_or_create_collection(
    name="event_collection", 
    embedding_function=openai_ef)

solicitation_collection = chroma_client.get_or_create_collection(
    name="solicitation_collection", 
    embedding_function=openai_ef)

# Load CSV data
ostem = pd.read_csv("data/ostems.csv")
pathway = pd.read_csv("data/pathways.csv")
event = pd.read_csv("data/events.csv")
solicitation = pd.read_csv("data/solicitations.csv")

# Add documents to collection
ostem_collection.add(
    documents=ostem['Description'].tolist(),  # Use Description as the searchable text
    metadatas=[{
        "title": row['Title'],
        "type": row['Type'],
        "url": row['URL']
    } for _, row in ostem.iterrows()],  # Include metadata
    ids=[str(id) for id in ostem['ID']]  # Use ID column as unique identifier
)



# Test query
ostem_results = ostem_collection.query(
    query_texts=["biology and chemistry opportunities for students"],
    n_results=3
)



print("\nTest query results:")
for i, doc in enumerate(ostem_results['documents'][0]):
    print(f"\nResult {i+1}:")
    print(f"Title: {ostem_results['metadatas'][0][i]['title']}")
    print(f"Type: {ostem_results['metadatas'][0][i]['type']}")
    print(f"URL: {ostem_results['metadatas'][0][i]['url']}")
    
