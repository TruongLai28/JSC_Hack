import chromadb
import pandas as pd
import chromadb.utils.embedding_functions as embedding_functions


openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=API_KEY,
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

pathway_collection.add(
    documents=pathway['Majors'].tolist(),  # Use Majors as the searchable text since it contains detailed field information
    metadatas=[{
        "title": row['Title'],
        "education_level": row['Education Level'],
        "url": row['URL']
    } for _, row in pathway.iterrows()],  # Include metadata
    ids=[str(id) for id in pathway['ID']]  # Use ID column as unique identifier
)

event_collection.add(
    documents=event['Description'].tolist(),  # Use Description as the searchable text
    metadatas=[{
        "title": row['Title'],
        "type": row['Type'],
        "url": row['URL']
    } for _, row in event.iterrows()],  # Include metadata
    ids=[str(id) for id in event['ID']]  # Use ID column as unique identifier
)

solicitation_collection.add(
    documents=solicitation['Solicitation Title'].tolist(),  # Use Title as the searchable text
    metadatas=[{
        "status": row['Status'],
        "solicitation_id": row['Solicitation ID'],
        "url": row['URL']
    } for _, row in solicitation.iterrows()],  # Include metadata
    ids=[str(id) for id in solicitation['ID']]  # Use ID column as unique identifier
)

# Test query
ostem_results = ostem_collection.query(
    query_texts=["biology and chemistry opportunities for students"],
    n_results=3
)

pathway_results = pathway_collection.query(
    query_images=["biology and chemistry opportunities for students"],
    n_results=3
)

event_results = event_collection.query(
    query_texts=["biology and chemistry opportunities for students"],
    n_results=3
)

solicitation_results = solicitation_collection.query(
    query_texts=["research opportunities"],
    n_results=3
)

print("\nTest query results:")
for i, doc in enumerate(ostem_results['documents'][0]):
    print(f"\nResult {i+1}:")
    print(f"Title: {ostem_results['metadatas'][0][i]['title']}")
    print(f"Type: {ostem_results['metadatas'][0][i]['type']}")
    print(f"URL: {ostem_results['metadatas'][0][i]['url']}")
    
for i, doc in enumerate(pathway_results['documents'][0]):
    print(f"\nResult {i+1}:")
    print(f"Title: {pathway_results['metadatas'][0][i]['title']}")
    print(f"Education Level: {pathway_results['metadatas'][0][i]['education_level']}")  # Changed from 'Education Level' to 'education_level'
    print(f"Majors: {doc}")
    print(f"URL: {pathway_results['metadatas'][0][i]['url']}")
    
for i, doc in enumerate(event_results['documents'][0]):
    print(f"\nResult {i+1}:")
    print(f"Title: {event_results['metadatas'][0][i]['title']}")
    print(f"Type: {event_results['metadatas'][0][i]['type']}")
    print(f"URL: {event_results['metadatas'][0][i]['url']}")
    
for i, doc in enumerate(solicitation_results['documents'][0]):
    print(f"\nResult {i+1}:")
    print(f"Title: {doc}")
    print(f"Status: {solicitation_results['metadatas'][0][i]['status']}")
    print(f"Solicitation ID: {solicitation_results['metadatas'][0][i]['solicitation_id']}")
    print(f"URL: {solicitation_results['metadatas'][0][i]['url']}")