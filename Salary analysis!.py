#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Importing all needed libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[4]:


salary_data = pd.read_csv(r"D:\Data set for analysis!\Salary Dataset.csv")
# First 5 rows of data
print(salary_data.head(5))


# In[5]:


# Last 5 rows of da
salary_data.tail(5)


# In[7]:


# What is the change of salary in different locations?
sns.set(rc={'figure.figsize':(15.7,9.27)})
sns.barplot(data=salary_data, x="Location", y="Salary", hue="Employment Status")
sns.lineplot(data=salary_data, x="Location", y="Salary", hue="Employment Status", linewidth=2.5, marker='o')

# Descriptions
plt.title("Change of Salary per Location and Employment Status")
plt.show()


# In[8]:


# How does Salary change with rating and employment status?
sns.set(rc={'figure.figsize':(25.7,9.27)})
# figure_1 = sns.lineplot(data=salary_data, x="Employment Status", y="Salary", hue="Rating")
figure_1 = sns.barplot(data=salary_data, x="Employment Status", y="Salary", hue="Rating")
sns.move_legend(figure_1, "lower center", bbox_to_anchor=(.5, 1), ncol=21, title="Rating", frameon=False)

# Descriptions
plt.title("Change of Salary per Location and Employment Status")
plt.show()


# In[9]:


# Change of Salary per Job Role and Employment Status
sns.relplot(col="Job Roles", y="Salary", kind="line",x='Employment Status', data=salary_data, color="#840032")

# Descriptions
plt.title("Change of Salary per Job Role and Employment Status")
plt.show()


# In[10]:


# Frequency of Employment Status
salary_data["Employment Status"].value_counts().plot.line(color=["#00132d"], marker="o", markersize=12)
salary_data["Employment Status"].value_counts().plot.bar(color=["#3f004d", "#001e45"])

# Descriptions
plt.title("Frequency X Employment Status")
plt.xticks(rotation = 360)
plt.show()


# In[11]:


# Frequency of Location
salary_data["Location"].value_counts().plot.bar(color=["#003049", "#6B2C39"])

salary_data["Location"].value_counts().plot.line(color=["#FCBF49"], marker="o", markersize=12)

# Descriptions
plt.title("Frequency X Location")
plt.show()


# In[12]:


# Frequency of Job Roles
salary_data["Job Roles"].value_counts().plot.line(color=["#e07a5f"], marker="o", markersize=12)
salary_data["Job Roles"].value_counts().plot.bar(color=["#33032f", "#531253"])

# Descriptions
plt.title("Frequency X Job Roles")
plt.xticks(rotation = 360)
plt.show()


# In[13]:


# How does Salary change with Employment status?
sns.set(rc={'figure.figsize':(25.7,9.27)})
figure_1 = sns.lineplot(data=salary_data, x="Employment Status", y="Salary", color="#0f4c5c")
figure_1 = sns.barplot(data=salary_data, x="Employment Status", y="Salary", color="#b1a7a6")

# Descriptions
plt.title("Salary VS Employment Status")
plt.show()


# In[ ]:




