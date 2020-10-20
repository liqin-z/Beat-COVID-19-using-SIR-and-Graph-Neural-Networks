import pandas as pd
import numpy as np

df=pd.read_json('data.json')
#print(df)
print(df['day'])
print(df[df['day']==1.26])
print(df[df['country']!= '中国'])
