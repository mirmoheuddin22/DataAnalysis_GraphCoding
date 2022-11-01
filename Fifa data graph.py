import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fifa = pd.read_csv(r"D:\Data set\fifa_data.csv")
print(fifa.head())
#Histograms:
bins = [40, 50, 60, 70, 80, 90, 100]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(fifa.Overall, bins = bins, color = '#abcdef')
plt.xticks(bins)
plt.xlabel('Number of Players')
plt.ylabel('Skill Level')
plt.title('Distribution of Player Skills in FIFA 2018')
plt.show()
#Pie Charts:
left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
labels = ['Left', 'Right']
colors = ['#abcdef', '#aabbcc']
plt.pie([left, right], labels = labels, colors=colors, autopct='%.2f')
plt.show()
print(left)
#Extra coding