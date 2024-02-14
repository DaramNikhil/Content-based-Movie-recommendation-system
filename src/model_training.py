import pandas as pd
from data_dev.model_train import model_train


def model_training_pipeline(data: pd.DataFrame):
    
    model = model_train(data)

    return model