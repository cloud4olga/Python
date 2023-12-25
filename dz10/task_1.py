# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит
# всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?


import pandas as pd

import random
lst = ['robot'] * 10
lst += ['human'] * 10

random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head(20))


df = pd.DataFrame({'column': lst})

unique_values = df['column'].unique()
print(df.index)
print(unique_values)

one_hot_df = pd.DataFrame(0, index=df.index, columns=unique_values)

for value in unique_values:
    one_hot_df.loc[df['column'] == value, value] = 1

print(one_hot_df)

