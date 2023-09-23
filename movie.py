import pandas as pd
import pickle
import requests
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from io import BytesIO
movies_list=pickle.load(open('model/movies_dict.pkl','rb'))
similarity=pickle.load(open('model/resimilar.pkl','rb'))

new_df=pd.DataFrame(movies_list)
movie_title=new_df['title'].values
mv=list(movies_list)
def fetch_poster(imdb_id):
    api_key = 'f63a16f0'
    url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    poster_url = data['Poster']
    return poster_url

def recommend(movie):
    ind=new_df[new_df['title']==movie].index[0]
    v=similarity[ind]
    recommend_movie=[]
    poster=[]
    for i in range(10):
        ind=v[i][0]
        imdb_id=new_df['api_imdbId'][ind]
        poster.append(fetch_poster(imdb_id))
        recommend_movie.append(new_df['title'][ind])
    return poster, recommend_movie


if __name__=="__main__":
    val=recommend('Batman')
    print(val)

