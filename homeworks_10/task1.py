import random
import pandas as pd


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

data['robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)

data = data.drop('whoAmI', axis = 1)

print(data.head())
