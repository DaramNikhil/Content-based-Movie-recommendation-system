import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging
import pickle

def model_train(data: pd.DataFrame):

    try:
        cv = CountVectorizer(max_features=5000,stop_words='english')
        """we can convert the features into vector format"""
        vector = cv.fit_transform(data['tags']).toarray()

        #finging the similarity between the features
        similarity = cosine_similarity(vector)
        index = data[data['title'] == 'Avatar'].index[0]
        distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])


        """store the data into pickel files for later uses"""
        #movies 
        pickle.dump(data,open('D:\my projects\movie-recommendation-system\movies.pkl','wb'))

        #similarity
        pickle.dump(similarity,open('D:\my projects\movie-recommendation-system\similarity.pkl','wb'))

        """we have taken the top 5 similer movies"""
        for i in distances[1:6]:
            print(data.iloc[i[0]].title)

    except Exception as e:
        logging.error("error in model training")
        raise e