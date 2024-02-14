import pandas as pd
import numpy as np
import logging


class Data_Ingestion_Config:

    def __init__(self,data_path:str):
        """data path reading

        Args:
            data_path (str): data_path
        """
        self.data_path = data_path


    def Data_Ingest(self) -> pd.DataFrame:
        """reading the datafrane from the data_path

        Returns:
            pd.DataFrame: pd.DataFrame
        """
        return pd.read_csv(self.data_path)
    


def Data_Ingestion(data_path) -> pd.DataFrame:
    """_summary_

    Args:
        data_path (data_path): data_path

    Returns:
        pd.DataFrame: pd.DataFrame
    """
    try:
        Data_Ingestion_Config_obj = Data_Ingestion_Config(data_path)
        df = Data_Ingestion_Config_obj.Data_Ingest()
        return df
    except Exception as e:
        logging.error("Error creating data ingestion configuration")
        raise e




