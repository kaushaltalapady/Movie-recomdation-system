import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 =  pd.read_csv('movies_metadata.csv')


df_new = df1[['popularity']]

for i,row in df1.iterrows():
    a=row['popularity']
    if type(a) is float:
        continue
    else:
       df_fn=df1.drop(i)
       
df_new = df_fn['popularity']      
df_new=df_new.fillna(0)
#df_fn=df1.drop(35586)
#df_new= df_new.drop(35586)

df_new = pd.DataFrame(df_new)

df_new= df_new.set_index(df_fn['title'])

df_new = df_new.replace(to_replace = 'Beware Of Frost Bites' ,value=0)

df_new['popularity'] = df_new['popularity'].map(float)

df_new = df_new.sort_values(by=['popularity'],ascending = False,axis =0)
Top_20 = list(df_new.index)
Top_20 = Top_20[0:21]
for i in Top_20:
  print(i)
