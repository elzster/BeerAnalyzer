# Import Libraries
import pandas as pd
import numpy as np
# from pyspark.sql import SparkSession
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#LoadSmaller CSV File
# df_5000 = pd.read_csv('static/df500.csv')
import os
cd = os.getcwd()
df_5000 = pd.read_csv(cd+"/beer/static/df500.csv")

# Helper function to get the title from the index
def get_title_from_index (index):
    return df_5000[df_5000.index == index]["beer_name"].values[0]

# # Helper function to get the index from the title
def get_index_from_title(beer_name):
    return df_5000[df_5000.beer_name == beer_name]["index"].values[0]

def similarity_model(parameter):
    cd = os.getcwd()
    df_5000 = pd.read_csv(cd+"/beer/static/df500.csv")
    count_matrix = CountVectorizer().fit_transform(df_5000["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    cosine_sim.shape
    beer_user_likes = (parameter)
    beer_index = get_index_from_title(beer_user_likes)
    similar_beers = list( enumerate(cosine_sim[beer_index]) )
    sorted_similar_beers = sorted(similar_beers,key = lambda x:x[1], reverse = True)[1:]
    i=0
    beer_dict = []
    sim_score = []
    print(f"The top 5 beers similar to {beer_user_likes} are: ")
    for i in range(len(sorted_similar_beers)):
        beer_dict.append(get_title_from_index(sorted_similar_beers[i][0]))
        sim_score.append(sorted_similar_beers[i][1])
        if i>=4:
            break
    result = (dict(zip(beer_dict, sim_score)))

def print_statement(parameter):
    i=0
    print(f"The top 5 beers similar to {beer_user_likes} are: ")
    for i in range( len(sorted_similar_beers)):
        print('Beer Name:',get_title_from_index(sorted_similar_beers[i][0]), ', Similarity Score: ', sorted_similar_beers[i][1] )
        i=i+1
        if i>=5:
            break


# Convert a collection of text to a matrix of token counts
count_matrix = CountVectorizer().fit_transform(df_5000["combined_features"])

# Get the cosine similarity matrix from the count matrix
cosine_sim = cosine_similarity(count_matrix)

# Get the number of rows and columns in cosine_sim
cosine_sim.shape

# Get the title of the beer that the user likes
beer_user_likes = "Wachusett Larry"
# beer_user_likes = input("Beer Name: ")

# Find that movies index
beer_index = get_index_from_title(beer_user_likes)

# Enumerate through all the similarity scores of the beer_user_likes to make
similar_beers = list( enumerate(cosine_sim[beer_index]) )

# Sort the list of silimar movies sccording to the similarity scores in decending order
sorted_similar_beers = sorted(similar_beers,key = lambda x:x[1], reverse = True)[1:]


i=0
beer_dict = []
sim_score = []
print(f"The top 5 beers similar to {beer_user_likes} are: ")
for i in range(len(sorted_similar_beers)):
    beer_dict.append(get_title_from_index(sorted_similar_beers[i][0]))
    sim_score.append(sorted_similar_beers[i][1])
    if i>=4:
        break
# print(beer_dict)
# print(sim_score)
mydict = dict(zip(beer_dict, sim_score))
print(mydict)

