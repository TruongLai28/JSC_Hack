import chromadb
import pandas as pd
import chromadb.utils.embedding_functions as embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="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",
    model_name="text-embedding-3-large"  # You can change to any of the three models
)

# Initialize ChromaDB client
chroma_client = chromadb.Client()

# Get existing collection or create new one
collection = chroma_client.get_or_create_collection(
    name="ostem_collection", 
    embedding_function=openai_ef)

# Load CSV data
ostem = pd.read_csv("data/ostems.csv")

# Add documents to collection
collection.add(
    documents=ostem['Description'].tolist(),  # Use Description as the searchable text
    metadatas=[{
        "title": row['Title'],
        "type": row['Type'],
        "url": row['URL']
    } for _, row in ostem.iterrows()],  # Include metadata
    ids=[str(id) for id in ostem['ID']]  # Use ID column as unique identifier
)

# Test query
results = collection.query(
    query_texts=["biology and chemistry opportunities for students"],
    n_results=3
)

print("\nTest query results:")
for i, doc in enumerate(results['documents'][0]):
    print(f"\nResult {i+1}:")
    print(f"Title: {results['metadatas'][0][i]['title']}")
    print(f"Type: {results['metadatas'][0][i]['type']}")
    print(f"URL: {results['metadatas'][0][i]['url']}")