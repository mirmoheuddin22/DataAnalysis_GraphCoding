import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
weather = pd.read_csv(r"D:\Data set\weatherAUS.csv")
print(weather.head())
print(weather.tail(10))
print(weather.info())
print(weather.dtypes)
print(weather.shape)
print(weather.size)
print(weather.describe)
print(weather.describe(include='all').T)
print(weather.sample(n=8))
print(weather.isnull())
print(weather.isna().any())
print(weather.isnull().sum())
print(weather.nunique())
print(weather.index)
print(weather.columns)
print(weather.memory_usage())
print(weather.nsmallest(5,'Evaporation'))
print(weather.nlargest(5,'Evaporation'))
print(weather.loc[:5,['Evaporation']])
print(weather.iloc[:4,:6])
print(weather[0:4])
print(weather.sort_index(axis=1, ascending=True))
print(weather.sort_values(axis=1, ascend))
print(weather.sort_values(by='Evaporation'))
drop_cols = ['Rainfall']
weather.drop(drop_cols,axis=1,inplace=True)
print(weather)
print(weather.query('5<Rainfall<10')[:8])










