import chromadb
import pandas as pd
import os
import chromadb.utils.embedding_functions as embedding_functions

from dotenv import load_dotenv
from llama_index.core.schema import TextNode
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.openai import OpenAIEmbedding
from fastapi import FastAPI
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv('API_KEY'),
    model_name="text-embedding-3-large"  # You can change to any of the three models
)

   
# Defines model for llama inde
embed_model = OpenAIEmbedding(model="text-embedding-3-large")
    

# Initialize ChromaDB client
chroma_client = chromadb.PersistentClient(path="./chroma_db")

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
    documents=[f"{row['Title']}. {row['Description']}" for _, row in ostem.iterrows()],  # Combine title and description
    metadatas=[{
        "title": row['Title'],
        "type": row['Type'],
        "url": row['URL']
    } for _, row in ostem.iterrows()],
    ids=[str(id) for id in ostem['ID']]
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
    documents=[f"{row['Title']}. {row['Description']}" for _, row in ostem.iterrows()],  # Combine title and description
    metadatas=[{
        "title": row['Title'],
        "type": row['Type'],
        "url": row['URL']
    } for _, row in ostem.iterrows()],
    ids=[str(id) for id in ostem['ID']]
)

solicitation_collection.add(
    documents=solicitation['Solicitation Title'].tolist(),  # Use Title as the searchable text
    metadatas=[{
        "status": row['Status'],
        "solicitation_id": row['Solicitation ID'],
        "url": row['URL']
    } for _, row in solicitation.iterrows()],  
    ids=[str(id) for id in solicitation['ID']]  # Use ID column as unique identifier
)



@app.get("/")
async def root():
    return {"message": "Hello FastAPI!"}

# Define the expected request model
class SearchRequest(BaseModel):
    query: str
    num_results: int = 3  # Optional, defaults to 3

@app.post("/search/ostem")
async def search_ostem(request: SearchRequest):
    try:
        results = ostem_collection.query(
            query_texts=[request.query],
            n_results=request.num_results,
            include=['metadatas', 'documents', 'distances']  # Add distances
        )
        
        formatted_results = []
        for i in range(len(results['documents'][0])):
            similarity_score = (1 - (results['distances'][0][i] / 2)) * 100 +30
            formatted_results.append({
                "Result": i + 1,
                "Title": results['metadatas'][0][i]['title'],
                "Type": results['metadatas'][0][i]['type'],
                "URL": results['metadatas'][0][i]['url'],
                "Description": results['documents'][0][i],
                "Similarity": f"{round(similarity_score, 1)}%"
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

@app.post("/search/pathway")
async def search_pathway(request: SearchRequest):
    try:
        results = pathway_collection.query(
            query_texts=[request.query],
            n_results=request.num_results,
            include=['metadatas', 'documents', 'distances']  # Add distances
        )
        
        formatted_results = []
        for i in range(len(results['documents'][0])):
            similarity_score = (1 - (results['distances'][0][i] / 2)) * 100 +30
            formatted_results.append({
                "Result": i + 1,
                "Title": results['metadatas'][0][i]['title'],
                "Education_Level": results['metadatas'][0][i]['education_level'],
                "URL": results['metadatas'][0][i]['url'],
                "Majors": results['documents'][0][i],
                "Similarity": f"{round(similarity_score, 1)}%"
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

@app.post("/search/event")
async def search_event(request: SearchRequest):  # Fixed function name from search_ostem
    try:
        results = event_collection.query(
            query_texts=[request.query],
            n_results=request.num_results,
            include=['metadatas', 'documents', 'distances']  # Add distances
        )
        
        formatted_results = []
        for i in range(len(results['documents'][0])):
            similarity_score = (1 - (results['distances'][0][i] / 2)) * 100 +30
            formatted_results.append({
                "Result": i + 1,
                "Title": results['metadatas'][0][i]['title'],
                "Type": results['metadatas'][0][i]['type'],
                "URL": results['metadatas'][0][i]['url'],
                "Description": results['documents'][0][i],
                "Similarity": f"{round(similarity_score, 1)}%"
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

@app.post("/search/research")
async def search_solicitation(request: SearchRequest):
    try:
        results = solicitation_collection.query(
            query_texts=[request.query],
            n_results=request.num_results,
            include=['metadatas', 'documents', 'distances']  # Add distances
        )
        
        formatted_results = []
        for i in range(len(results['documents'][0])):
            similarity_score = (1 - (results['distances'][0][i] / 2)) * 100 +30
            formatted_results.append({
                "Result": i + 1,
                "Title": results['documents'][0][i],
                "Status": results['metadatas'][0][i]['status'],
                "Solicitation_ID": results['metadatas'][0][i]['solicitation_id'],
                "URL": results['metadatas'][0][i]['url'],
                "Similarity": f"{round(similarity_score, 1)}%"
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

@app.post("/event")
async def searchEvent(request: SearchRequest):
    try:
        # Convert rows to nodes
        nodes = [
            TextNode(
                text=row["Description"],
                metadata={
                    "id": row["ID"],
                    "title": row["Title"],
                    "url": row["URL"],
                    "type": row["Type"],
                },
            )
            for _, row in event.iterrows()
        ]

        # Create a vector store
        vector_store = ChromaVectorStore(chroma_collection=event_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # Create an index and query engine
        index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=embed_model)
        query_engine = index.as_query_engine()

        # Query the engine
        response = query_engine.query(request.query)

        # Prepare results
        results = []
        for node_with_score in response.source_nodes:
            node = node_with_score.node
            metadata = node.metadata
            description = node.text
            relevance = 1 - node_with_score.score

            results.append({
                "id": metadata["id"],
                "title": metadata["title"],
                "url": metadata["url"],
                "description": description,
                "type": metadata["type"],
                "relevance": relevance,
            })

        # Return all data
        return {
            "status": "success",
            "query": request.query,
            "response": response.response,
            "results": results,
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
        
@app.post("/ostem")
async def searchOstem(request: SearchRequest):
    try:
        # Convert rows to nodes
        nodes = [
            TextNode(
                text=row["Description"],
                metadata={
                    "id": row["ID"],
                    "title": row["Title"],
                    "url": row["URL"],
                    "type": row["Type"],
                },
            )
            for _, row in ostem.iterrows()
        ]

        # Create a vector store
        vector_store = ChromaVectorStore(chroma_collection=ostem_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # Create an index and query engine
        index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=embed_model)
        query_engine = index.as_query_engine()

        # Query the engine
        response = query_engine.query(request.query)

        # Prepare results
        results = []
        for node_with_score in response.source_nodes:
            node = node_with_score.node
            metadata = node.metadata
            description = node.text
            relevance = 1 - node_with_score.score

            results.append({
                "id": metadata["id"],
                "title": metadata["title"],
                "url": metadata["url"],
                "description": description,
                "type": metadata["type"],
                "relevance": relevance,
            })

        # Return all data
        return {
            "status": "success",
            "query": request.query,
            "response": response.response,
            "results": results,
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
        
@app.post("/pathway")
async def searchPathway(request: SearchRequest):
    try:
        # Convert rows to nodes
        nodes = [
            TextNode(
                text=row["Title"],
                metadata={
                    "id": row["ID"],
                    "education_level": row["Education Level"],
                    "url": row["URL"],
                    "majors": row["Majors"],
                },
            )
            for _, row in pathway.iterrows()
        ]

        # Create a vector store
        vector_store = ChromaVectorStore(chroma_collection=pathway_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # Create an index and query engine
        index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=embed_model)
        query_engine = index.as_query_engine()

        # Query the engine
        response = query_engine.query(request.query)

        # Prepare results
        results = []
        for node_with_score in response.source_nodes:
            node = node_with_score.node
            metadata = node.metadata
            title = node.text
            relevance = 1 - node_with_score.score

            results.append({
                "id": metadata["id"],
                "title": title,
                "education_level": metadata["education_level"],
                "url": metadata["url"],
                "majors":metadata["majors"],
                "relevance": relevance,
            })

        # Return all data
        return {
            "status": "success",
            "query": request.query,
            "response": response.response,
            "results": results,
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


@app.post("/research")
async def searchResearch(request: SearchRequest):
    try:
        # Convert rows to nodes
        nodes = [
            TextNode(
                text=row["Solicitation Title"],
                metadata={
                    "id": row["ID"],
                    "status": row["Status"],
                    "url": row["URL"],
                    "solicitation_id": row["Solicitation ID"],
                },
            )
            for _, row in solicitation.iterrows()
        ]

        # Create a vector store
        vector_store = ChromaVectorStore(chroma_collection=solicitation_collection)
        storage_context = StorageContext.from_defaults(vector_store=vector_store)

        # Create an index and query engine
        index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=embed_model)
        query_engine = index.as_query_engine()

        # Query the engine
        response = query_engine.query(request.query)

        # Prepare results
        results = []
        for node_with_score in response.source_nodes:
            node = node_with_score.node
            metadata = node.metadata
            title = node.text
            relevance = 1 - node_with_score.score

            results.append({
                "id": metadata["id"],
                "title": title,
                "status": metadata["status"],
                "url": metadata["url"],
                "solicitation_id":metadata["solicitation_id"],
                "relevance": relevance,
            })

        # Return all data
        return {
            "status": "success",
            "query": request.query,
            "response": response.response,
            "results": results,
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }
