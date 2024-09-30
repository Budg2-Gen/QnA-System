from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, GPTVectorStoreIndex
from llama_index.llms.gemini import Gemini
from IPython.display import Markdown, display
from llama_index.core import ServiceContext
from llama_index.core import Settings
from llama_index.core import StorageContext, load_index_from_storage
import google.generativeai as genai
from llama_index.embeddings.gemini import GeminiEmbedding

from QAWithPDF.data_ingestion import load_data
from QAWithPDF.model_api import load_model

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model,document):
    try:
        logging.info("")
        gemini_embed_model=genai.embed_content(model="models/text-embedding-004", content="../Data")
        Settings.llm = model
        Settings.embed_model = GeminiEmbedding(model="gemini_embed_model")
        Settings.chunk_size=800
        Settings.chunk_overlap=20
        
        logging.info("")      
        index = VectorStoreIndex.from_documents(document)
        #index.embed_model = gemini_embed_model
        #index.llm = model
        index.storage_context.persist()
        
        logging.info("")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e,sys)