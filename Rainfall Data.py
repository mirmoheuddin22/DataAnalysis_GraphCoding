import pandas as pd
import os
weather_df = pd.read_csv(r"D:\Data set\weatherAUS.csv")
#print(weather_df.info())
weather_df.dropna(subset=['RainToday', 'RainTomorrow'], inplace=True)
print(weather_df)
