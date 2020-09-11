import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 =  pd.read_csv('drive/My Drive/Colab Notebooks/movies_metadata.csv')

df_fn = df1[['genres','title','original_title','overview','production_companies','release_date','runtime','tagline']]

df_fn=df_fn.fillna('')


df_fn['merged']=''

for col in df_fn:
   df_fn['merged']= df_fn['merged']+df_fn[col].map(str)
df_fn = df_fn.loc[:15000,:]
bag_of_words = pd.DataFrame(data = df_fn['merged'])

import nltk as nl
nl.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re

for i in range(0, 15001):
    inter=(re.sub('[^a-zA-Z0-9]', ' ', bag_of_words['merged'][i])).lower()
    inter = inter.split()
    ps = PorterStemmer()
    inter = [ps.stem(word) for word in inter if not word in set(stopwords.words('english'))]
    bag_of_words['merged'][i]=' '.join(inter)
    
from sklearn.feature_extraction.text import CountVectorizer
vector=CountVectorizer()
count=vector.fit_transform(bag_of_words['merged'])


from sklearn.metrics.pairwise import cosine_similarity
output=cosine_similarity(count,count)

output = pd.DataFrame(output)
output = output.set_index(df_fn['title'])
output = output.rename(columns=df_fn['title'])

movie=str(input())
result = output.loc[[movie],:]
result = result.sort_values(by=movie,ascending = False,axis =1)
Top_20 = list(result.columns)
Top_20 = Top_20[1:22]
for i in Top_20:
  print(i)
