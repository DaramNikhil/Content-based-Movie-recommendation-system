import pandas as pd
import numpy as np
import ast
import logging


#preprocess geres and keywords
def convert(data):
    """importend data preprocess by using this function extraction 

    Args:
        data (data): pd.DataFrame

    Returns:
        pd.DataFrame
    """
    my_list = []
    for i in ast.literal_eval(data):
        my_list.append(i["name"])

    return my_list


#preprocess cast
def convert_cast(data):
    my_cast = []
    value_cnt = 0

    for i in ast.literal_eval(data):
        #we can take only main 3 cast membrs only
        if value_cnt < 3:
            my_cast.append(i["name"])
            value_cnt +=1
    return my_cast


#process director
def convert_director(data):
    my_list = []

    for i in ast.literal_eval(data):
        if i["job"] == "Director":
            my_list.append(i["name"])
    return my_list



def process_data(my_data):
    """
    removing extra spaces from the features

    Args:
        my_data (pd.DataFrame): cleaned data

    Returns:
        pd.DataFrame
    """
    for i in my_data:
        my_data = i.replace(" ", "")
    return my_data 


def remove_lists(series):
    return series[~series.apply(lambda x: isinstance(x, list))]


class Data_cleaaning:

    def data_handling(self,data: pd.DataFrame) -> pd.DataFrame:
        try:

            """
                preprocess the importend data in the data frame
            
            """
            data = data[['movie_id','title','overview','genres','keywords','cast','crew']]

            data.dropna(inplace=True) # remove null values

            data["genres"] = data["genres"].apply(convert)
            # print("Data after conversion:\n",data)
            data["keywords"] = data["keywords"].apply(convert)
            # print("\nData after keywords conversion:\n",data)
            data["cast"] = data["cast"].apply(convert_cast)
            data["crew"] = data["crew"].apply(convert_director)

            return data
        except Exception as e:
            logging.error("error occured in data cleaning!")
            raise e
            


    def preprocess(self, data:pd.DataFrame) -> pd.DataFrame:

        try:

            """removing extra stuff from the feature columns"""
            data['cast'] = data['cast'].apply(process_data)
            data['crew'] = data['crew'].apply(process_data)
            data['genres'] = data['genres'].apply(process_data)
            data['keywords'] = data['keywords'].apply(process_data)


            """we can added the feature columns into list"""
            data["cast"] = data['cast'].apply(lambda x: [x])
            data["crew"] = data['crew'].apply(lambda x: [x])
            data["genres"] = data['genres'].apply(lambda x: [x])
            data["keywords"] = data['keywords'].apply(lambda x: [x])

            #overview
            data["overview"] = data["overview"].apply(lambda x:x.split())
            
            """combine the data into tags and then removing the extra stuff"""

            data['tags'] = data['overview'] + data['genres'] + data['keywords'] + data['cast'] + data['crew']

            """we can take the importet data """

            main_data = data[["movie_id","title","tags"]]

            main_data["tags"] = main_data["tags"].apply(lambda x: " ".join(str(i) for i in x) if isinstance(x, list) else x)

            main_data["tags"] = main_data["tags"].apply(lambda x:x.lower())

            return main_data
            

        except Exception as e:
            logging.error("error in preprocess function")
            raise e


    

        

        
        
        




        
        


        



        
            
            

