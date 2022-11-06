import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlretrieve
URL = r"D:\Data set\housing.csv"
california_df = pd.read_csv(URL)
print(california_df.head(5))
print(california_df.tail(5))
print(california_df.info())
print(california_df.describe())
# Get the Null values in our dataset
print(pd.DataFrame(california_df.isnull().sum()))
# Fix the total_bedrooms, replace the NULL values with the MEAN or AVERAGE value, i.e 538
total_bedrooms_mean_value = california_df["total_bedrooms"].mean() # I could use 538 directly, but if this data gets updated somewhere in future, it could cause problems - FUTURE PROOFING
california_df["total_bedrooms"].replace(np.nan, total_bedrooms_mean_value, inplace  = True)
# Calculating mean of every column
column_count = 0
for i in california_df.columns:
  print(f"The mean value of {i} ➡️ {california_df[i].mean()}")

  # Incrementing the Counter
  column_count += 1

  # This code block is to NOT print the mean value of the ocean_proximity as it is a STRING object
  if column_count == 9: # I have used 9 because there are 10 columns
    break
# Get the count of every NEEDED column
columns_needed = ["ocean_proximity"] # You can add as many as YOU LIKE
for j in columns_needed:
  print(f"The mean value of {j} ➡️ \n{california_df[j].value_counts()}")
  print("➡️|||END|||➡️")
# Frequency of Ocean Proximity
sns.set(rc={'figure.figsize':(11.7,8.27)})

# Plot
sns.countplot(data=california_df, x="ocean_proximity",  palette="rocket").set(title = "Frequency of Ocean Proximity",xlabel = "Distance of Ocean from the House",ylabel = "Frequency")

# Show
plt.show()
# Frequency of the age of the HOUSE
sns.set(rc={'figure.figsize':(28.7,10.27)})

# Plot
sns.countplot(data=california_df, x="housing_median_age",  palette="rocket").set(title = "Frequency of the age of the HOUSE",xlabel = "Age of House")

# Show
plt.show()
# Get pair values
plt.figure(figsize=(25,15))

# Plot
sns.pairplot(california_df)

# Show
plt.show()
# Heatmap for obeserving correlations
plt.figure(figsize=(25,15))
california_heatmap = california_df.corr()

# Ploty
sns.heatmap(california_heatmap, annot=True, cmap='rocket').set(title = "Correlation between the data")

# Show
plt.xticks(rotation=360)
plt.show()
# Get the longitudinal & latitudinal graph
sns.set(rc={'figure.figsize':(11.7,8.27)})
fig, axes = plt.subplots(1, 2)

# Plot
sns.scatterplot(data=california_df, x="longitude", y="latitude", hue="population", ax=axes[0],  palette="rocket").set(title = "Graphical MAP Representation")
sns.scatterplot(data=california_df, x="longitude", y="latitude", hue="population", alpha=0.2, ax=axes[1],  palette="rocket").set(title = "Graphical Represenation to show most densly populated areas")

# Show
plt.show()
# The relation between the Ocean Proximity and Population - PLOT 1
sns.set(rc={'figure.figsize':(11.7,8.27)})

# Plot
sns.scatterplot(data=california_df, x="population", y="median_house_value", hue="ocean_proximity", palette="rocket", alpha=0.4).set(title = "How does price of house change with population and ocean proxmity - PLOT 1",xlabel = "Population",ylabel = "House Price")
# Show
plt.show()
# The most common house prices
sns.set(rc={'figure.figsize':(11.7,8.27)})

# Plot
sns.kdeplot(x='population', y='median_house_value', data=california_df, fill="True", color="salmon").set(title = "Most common house prices",xlabel = "Population",ylabel = "House Price")

# Show
plt.show()
# How does income and ocean proximity affect the house price

# Plot
m = sns.jointplot(data=california_df, x="median_income", y="median_house_value", hue="ocean_proximity", palette="rocket")
m.plot_marginals(sns.histplot, kde=True)

# Show
plt.show()
# The diversty of Ocean proximity and House Price
sns.set(rc={'figure.figsize':(11.7,8.27)})

sns.boxplot(x='ocean_proximity',y='median_house_value',data=california_df, palette="rocket").set(
    title = "The diversty of Ocean proximity and House Price",
    xlabel = "Ocean Proximity",
    ylabel = "House Price"
)

# Show
plt.show()