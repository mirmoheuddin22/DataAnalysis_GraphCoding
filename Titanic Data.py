import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlretrieve
titanic_df = pd.read_csv(r"D:\Data set\titanic.csv")
print(titanic_df)
titanic_df = titanic_df.rename(columns = {'pclass':'ticket_class','ticker' : 'ticker_number','cabin' : 'cabin_number',})
titanic_df["Embarked"].replace({"C": "Cherbourg", "Q": "Queenstown", "S" : "Southampton"}, inplace=True)
titanic_df.drop("PassengerId", axis = 1, inplace = True)
print(titanic_df.head(5))
print(titanic_df.tail(5))
plt.style.use("seaborn-notebook")
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.pairplot(titanic_df)
plt.show()
titanic_mx = titanic_df.corr()
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.heatmap(titanic_mx, annot=True, cmap='rocket')
plt.show()
# Ticket Class distribution:
sns.set_theme(style="whitegrid")
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.countplot(data=titanic_df, x="Pclass", palette="seismic").set(title = "Ticket Class Distribution")
plt.show()
# Age distribution:
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.histplot(titanic_df, x="Age", bins=25).set(title = "Age Distribution")
plt.show()
# Age distribution
sns.set(rc={'figure.figsize':(10,8)})
sns.histplot(titanic_df, x="Age").set(title = "Age Distribution")
plt.show()
# Fare distribution
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.histplot(titanic_df, x="Fare", bins=20).set(title = "Fare Distribution")
plt.show()
# Sex Distribution
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.countplot(data = titanic_df, x="Sex", palette="nipy_spectral").set(title = "Sex Distribution")
plt.show()
# SibSp Distribution
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.countplot(data = titanic_df, x="SibSp", palette="prism").set(title = "SibSp Distribution")
plt.show()
# Parch Distribution
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.countplot(data = titanic_df, x="Parch", palette="gnuplot").set(title = "Parch Distribution")
plt.show()

# Embarkment Distribution
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.countplot(data = titanic_df, x="Embarked", palette="gist_earth").set(title = "Embarkment Distribution")
plt.show()
# Relationship between the fare price per gender and per embarkment
plt.style.use("fivethirtyeight")
plt.figure(figsize=(14,9))

sns.violinplot(x='Embarked',y='Fare',data=titanic_df, hue='Sex',split=True).set(title="Relationship between the fare price per gender and per embarkment", xlabel = "Embarkment",)
sns.stripplot(x='Embarked',y='Fare',data=titanic_df, jitter=True, hue='Sex', dodge=True, palette="twilight",marker="D",size=10, edgecolor="gray", alpha=.25)

# Moves legend to the best position
plt.legend(loc=0)
plt.show()
# Relationship between SibSp & Parch per gender
plt.style.use("fivethirtyeight")
plt.figure(figsize=(14,9))

sns.violinplot(x='SibSp',y='Parch',data=titanic_df, hue='Sex',split=True).set(title="Relationship between the fare price per gender and per embarkment",)
sns.stripplot(x='SibSp',y='Parch',data=titanic_df, jitter=True, hue='Sex', dodge=True, palette="twilight",marker="D",size=10, edgecolor="gray", alpha=.25)

# Moves legend to the best position
plt.legend(loc=0)
plt.show()
sns.kdeplot(x='SibSp', y='Parch', hue='Sex', data=titanic_df).set(title="Relationship between the fare price per gender and per embarkment",)
plt.show()
# Relationship between the fare price per gender and per Pclass
plt.style.use("fivethirtyeight")
plt.figure(figsize=(14,9))

sns.violinplot(x='Pclass',y='Fare',data=titanic_df, hue='Sex',split=True).set(title="Relationship between the fare price per gender and per Pclass",)
sns.stripplot(x='Pclass',y='Fare',data=titanic_df, jitter=True,hue='Sex', dodge=True, palette="twilight",marker="D",size=10, edgecolor="gray", alpha=.25)

# Moves legend to the best position
plt.legend(loc=0)
plt.show()

sns.kdeplot(x='Pclass', y='Fare', hue='Sex', data=titanic_df).set(title="Relationship between the fare price per gender and per Pclass",)

plt.show()
