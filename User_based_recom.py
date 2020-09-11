import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fuzzywuzzy import process

def recommender(name,mod,data):
  abc = pd.read_csv('movies_metadata.csv')
  abc=abc[['title','id']]
 # print(abc)
  mod.fit(data)
  idx = process.extractOne(name,abc['title'])[2]
  print(idx)
  dist,ind = mod.kneighbors(data[idx],n_neighbors = 20)
  print(ind)
  print(dist)
  for i in ind:
    print(abc['title'][i].where(i!=idx))   
 
df = pd.read_csv('ratings_small.csv')
df=df[['userId','movieId','rating']]
new=df.pivot(index='userId',columns='movieId',values='rating').fillna(0)

new = np.asmatrix(new)

from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(metric='cosine')
model.fit(new)

recommender('batman',model,new)
