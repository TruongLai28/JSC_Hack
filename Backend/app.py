from fastapi import FastAPI, Body
from pydantic import BaseModel
import chromadb
import pandas as pd
import chromadb.utils.embedding_functions as embedding_functions
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

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

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/home")
async def Home():
    return {"message": "This is home page"}

# Define the expected request model
class SearchRequest(BaseModel):
    query: str
    num_results: int = 3  # Optional, defaults to 3

@app.post("/search/ostem")
async def search_ostem(request: SearchRequest):
    try:
        results = ostem_collection.query(
            query_texts=[request.query],
            n_results=request.num_results
        )
        
        formatted_results = []
        for i in range(len(results['documents'][0])):
            formatted_results.append({
                "Result": i + 1,
                "Title": results['metadatas'][0][i]['title'],
                "Type": results['metadatas'][0][i]['type'],
                "URL": results['metadatas'][0][i]['url']
            })
            
        return {
            "status": "success",
            "results": formatted_results
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }




