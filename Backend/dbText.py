# %%
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
from IPython.display import Markdown



# Setup Model
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv('API_KEY'),
    model_name="text-embedding-3-large"  # You can change to any of the three models
)

query = "People relation and human interaction managment opportunities for gradutate and undergraduate students"

def eventTextResponse(query):
    
    # Create Chroma Client
    chroma_client = chromadb.Client()
    
    # Create Collection
    collection = chroma_client.create_collection(name="event_collection")
    
    # Create Dataframe
    dataframe = pd.read_csv(f"Backend/data/events.csv")
    
    # Seperates data from a row to a node
    nodes = []
    for _, row in dataframe.iterrows():
        node = TextNode(
            text=row["Description"],
            metadata={
                "id": row["ID"],
                "title": row["Title"],
                "url": row["URL"],
                "type": row["Type"],
            },
        )
        nodes.append(node)

    # Creates Vector Stores
    vector_store = ChromaVectorStore(chroma_collection=collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    # Defines model
    embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    
    # Index nodes
    index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=embed_model)
    
    # Query data
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response

def ostemTextResponse(query):
    
    # Create Chroma Client
    chroma_client = chromadb.Client()
    
    # Create Collection
    collection = chroma_client.create_collection(name="ostem_collection")
    
    # Create Dataframe
    dataframe = pd.read_csv(f"Backend/data/ostems.csv")
    
    # Seperates data from a row to a node
    nodes = []
    for _, row in dataframe.iterrows():
        node = TextNode(
            text=row["Description"],
            metadata={
                "id": row["ID"],
                "title": row["Title"],
                "url": row["URL"],
                "type": row["Type"],
            },
        )
        nodes.append(node)

    # Creates Vector Stores
    vector_store = ChromaVectorStore(chroma_collection=collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    
    # Defines model
    embed_model = OpenAIEmbedding(model="text-embedding-3-small")
    
    # Index nodes
    index = VectorStoreIndex(nodes, storage_context=storage_context, embed_model=embed_model)
    
    # Query data
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return response

# %%
response = eventTextResponse(query)

# %%
response = ostemTextResponse(query)
 # %%
 
print(f"User Question: {query}")
print("-" * 50)
print(f"Chat Response: {response.response}")
print("-" * 50)

source_nodes = response.source_nodes

# Iterate through the source_nodes
for node_with_score in source_nodes:
    
    # Access the node attribute and its metadata
    node = node_with_score.node
    metadata = node.metadata
    description = node.text
    relevance = f"{(1 - node_with_score.score):.4f}"
    print(f"ID: {metadata['id']}")
    print(f"Title: {metadata['title']}")
    print(f"URL: {metadata['url']}")
    print(f"Description: {description}")
    print(f"Type: {metadata['type']}")
    print(f"Relevance: {relevance}%")
    print("-" * 50)

# %%
