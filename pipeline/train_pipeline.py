import pandas as pd
import numpy as np
from src.ingestion import Data_Ingestion
import logging
from src.preprocess import Data_transform
from src.model_training import model_training_pipeline
import ast

def train_pipeline(data_path: str):
    try:
        """Train the data pipeline using a given dataset path."""
        # Step 1: Load and preprocess the raw data
        data = Data_Ingestion(data_path)
        credits = pd.read_csv(r"D:\my projects\movie-recommendation-system\data\tmdb_5000_credits.csv")
        movie = Data_transform(data, credits)

        #similarity  
        similaritys = model_training_pipeline(movie)

        print(similaritys)        

    except Exception as e:
        logging.error("error occurred in train_pipeline")
        raise e
    

