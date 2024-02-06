import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# data = pd.read_csv('california_housing_train.csv')
# print(df.head())
# sns.scatterplot(df, x='households', y='population')
# sns.histplot(data=data, x='housing_median_age')
# plt.show()

penguins = pd.read_csv('penguins.csv')
print(penguins.head())
# print(penguins.columns)
# print(penguins.info)
# print(penguins.describe())
# print(penguins.isnull().sum())
# penguins.dropna(inplace=True)
# print(penguins.head())
# sns.scatterplot(data=penguins, x='species', y='body_mass_g', hue='sex')
# plt.show()
