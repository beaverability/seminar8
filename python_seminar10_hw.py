import pandas as pd
import random

# Создание DataFrame с данными
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создание новых столбцов по уникальным значениям и заполнение нулями
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаление исходного столбца 'whoAmI'
data = data.drop('whoAmI', axis=1)

data.head()

print(data.head())
