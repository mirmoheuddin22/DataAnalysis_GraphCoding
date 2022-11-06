import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from urllib.request import urlretrieve
import seaborn as sns
dataset = r"D:\Data set\netflix_titles.csv"
netflix_df = pd.read_csv(dataset)
print(netflix_df)
# Some stats/info on the dataset
netflix_df.info()
# Get some description of the data - ONLY release_year is NUMBER(S) VALUE(S)
print(netflix_df.describe())
# Columns in the dataset
print(netflix_df.columns)
# Shape of The data frame
print(netflix_df.shape) # 12 Columns and 8807 Rows
# How many years of Data (1966-2021)
print(netflix_df["release_year"].value_counts())
# MOVIES vs TV SHOWS
print(netflix_df["type"].value_counts()) # MORE MOVIES
# Check for null values in all columns of dataset
print(pd.DataFrame(netflix_df.isnull().sum()))
# Replace NAN value(s) with TV-MA
netflix_df['rating'].replace(np.nan, 'TV-MA',inplace  = True)
# Replace NAN value(s) with United States
netflix_df['country'].replace(np.nan, 'United States',inplace = True)
# Rename the Column "listed_in" to "genre"
#print(netflix_df.rename(columns={'listed_in': 'genre'},inplace=True, errors='raise'))
sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
print(netflix_df["release_year"].value_counts().mean())
plt.title('Netflix Release Years')
netflix_df["release_year"].value_counts().plot.barh(figsize=(30,20), color="#32a883")
plt.show()
# TV SHOW VS MOVIES On NETFLIX - BAR CHART
plt.figure(figsize=(10,5))
plt.title('Type of shows on Netflix')
sns.barplot(x=netflix_df['type'], y=netflix_df.index)
plt.show()
plt.title('Type of shows on Netflix')
netflix_df['type'].value_counts().plot.pie(autopct='%1.1f%%',figsize=(15,10))
plt.show()
plt.figure(figsize = (15,8))
plt.title('Netflix Ratings Distribution')
sns.countplot(x='rating', data = netflix_df)
plt.show()
plt.figure(figsize = (15,8))
plt.title('Netflix ratings distribution seperated by type of release')

# Unique category labels: 'Diet', 'MOD-PA'...
color_labels = netflix_df['rating'].unique()

# List of color palette to use
rgb_values = sns.color_palette("Set2", 6)

# Map label to color palette
color_map = dict(zip(color_labels, rgb_values))

# Plotting The CountPLOT
sns.countplot(x='rating', data=netflix_df, hue="type", palette=netflix_df['rating'].map(color_map))
plt.show()
plt.figure(figsize=(15,10))
plt.title('Top 5 Netflix Countries')
colors = sns.color_palette("husl", 9)
netflix_df["country"].value_counts().nlargest(n=5).plot.pie(autopct='%1.1f%%',figsize=(15,10), colors=colors)
plt.show()
plt.figure(figsize=(10,5))
plt.title('Top 5 Netflix Countries')
netflix_df["country"].value_counts().nlargest(n=5).plot.barh(figsize=(15,10), color="#42c2f5")
plt.show()
plt.figure(figsize = (15,8))
plt.title('Top 5 Netflix country distribution seperated by type of release')
sns.countplot(x='country', data=netflix_df, hue='type', order=netflix_df.country.value_counts().iloc[:5].index, color="salmon")
plt.show()

