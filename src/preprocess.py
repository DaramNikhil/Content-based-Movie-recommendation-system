import pandas as pd
import numpy as np
import logging
from data_dev.clean_data import Data_cleaaning




def Data_transform(data1, data2):
    try:
        data_merge = data1.merge(data2,on='title')
        data_cleaning_obj = Data_cleaaning()
        preprocess_data = data_cleaning_obj.data_handling(data_merge)
        cleaned_data = data_cleaning_obj.preprocess(preprocess_data)
        return cleaned_data

    except Exception as e:
        raise e