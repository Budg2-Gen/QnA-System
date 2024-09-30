from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(data):
    try:
        logging.info("Data loading...")
        loader = SimpleDirectoryReader("Data")
        documents=loader.load_data()
        logging.info("Data loading completed...")
        return documents
    except Exception as e:
        logging.info("Error in loading data...")
        raise customexception(e,sys)