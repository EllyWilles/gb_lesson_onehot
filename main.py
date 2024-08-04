import pandas as pd
import random


lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})


data_one_hot = pd.DataFrame()

for category in data['whoAmI'].unique():
    data_one_hot[category] = (data['whoAmI'] == category).astype(int)

print(data_one_hot.head())
