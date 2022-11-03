#Load needed libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlretrieve
#Get the data
iris_df = pd.read_csv(r"D:\Data set\Iris.csv")
print(iris_df)
#Make species group:
species_group = iris_df.groupby(["Species"])
#Get pair values
sns.set(rc={'figure.figsize':(11.7,8.27)})
#Plot
#ns.pairplot(iris_df)
#Show
plt.show()
# Heatmap for obeserving correlations
plt.figure(figsize=(10,8))
iris_heatmap = iris_df.corr()

# Ploty
sns.heatmap(iris_heatmap, annot=True, cmap='rocket').set(title = "Correlation between the data")
# Show
plt.show()
# Get the count of the species
sns.set(rc={'figure.figsize':(11.7,8.27)})

# Plot
sns.countplot(data=iris_df, x="Species", palette = "rocket").set(title =  "Frequency of the variable Species")

# Show
plt.show()
# The diversty of SEPALS between the 3 Species - PLOT 1
sns.set(rc={'figure.figsize':(11.7,8.27)})

sns.boxplot(x='SepalLengthCm',y='SepalWidthCm',data=iris_df, hue='Species', palette="rocket").set(title = "The diversity of SEPALS between the 3 Species - PLOT 1")
# Show
plt.show()
# The diversty of SEPALS between the 3 Species - PLOT 2
sns.set(rc={'figure.figsize':(11.7,8.27)})
# Plot
sns.scatterplot(data=iris_df, x="SepalLengthCm", y="SepalWidthCm", hue="Species", palette="rocket").set(title = "The diversity of SEPALS between the 3 Species - PLOT 2")
# Show
plt.show()
# The diversty of PETALS between the 3 species - PLOT 1
sns.set(rc={'figure.figsize':(11.7,8.27)})

sns.boxplot(x='PetalLengthCm',y='PetalWidthCm',data=iris_df, hue='Species', palette="rocket").set(title = "The diversity of PETALS between the 3 Species - PLOT 1")

# Show
plt.show()
# Relation between the Sepal-Length(s) &  Petal-Length(s) as a WHOLE
fig, axes = plt.subplots(1, 2)

# Plot
sns.kdeplot(x='SepalLengthCm', y='PetalLengthCm', data=iris_df, fill="True", ax=axes[0], color="salmon").set(title="Relation between the Sepal-Length(s) &  Petal-Length(s)")
sns.regplot(x='SepalLengthCm', y='PetalLengthCm', data=iris_df,ax=axes[1], color="lightblue").set(title="Relation between the Sepal-Length(s) & Petal-Length(s)")

# Show
plt.show()

# Relation between the Sepal-Length(s) &  Petal-Length(s) per Specie
sns.set(rc={'figure.figsize':(11.7,8.27)})

# Plot
g = sns.jointplot(x='PetalLengthCm', y='SepalLengthCm', data=iris_df, palette="rocket", hue="Species")
g.plot_marginals(sns.histplot, kde=True)
plt.title("Relation between the Sepal-Length(s) &  Petal-Length(s) per Specie", x=3.95)

# Show
plt.show()
# Relation between the Sepal-Width(s) &  Petal-Width(s) as a WHOLE
fig, axes = plt.subplots(1, 2)

# Plot
sns.kdeplot(x='SepalWidthCm', y='PetalWidthCm', data=iris_df, fill="True", ax=axes[0], color="salmon").set(title = "Relation between the Sepal-Width(s) &  Petal-Width(s)")
sns.regplot(x='SepalWidthCm', y='PetalWidthCm', data=iris_df,ax=axes[1], color="lightblue").set(title = "Relation between the Sepal-Width(s) &  Petal-Width(s)")

# Show
plt.show()

# Relation between the Sepal-Width(s) &  Petal-Width(s) per Specie
sns.set(rc={'figure.figsize':(11.7,10.27)})

# Plot
h = sns.jointplot(x='SepalWidthCm', y='PetalWidthCm', data=iris_df, hue="Species", palette="rocket")
h.plot_marginals(sns.boxplot) #To add a HISTOGRAM in the margins instead of a boxplot, change this line to `h.plot_marginals(sns.histplot, kde=True)`

# Set Title
plt.title("Relation between the Sepal-Width(s) &  Petal-Width(s) per Specie", x=3.85)

# Show
plt.show()

