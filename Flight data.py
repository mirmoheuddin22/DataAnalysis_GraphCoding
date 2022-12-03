#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing all needed libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


flight_data = pd.read_csv(r"D:\Data set for analysis!\flights_data.csv")
# First 5 rows of data
flight_data.head(5)


# In[3]:


# Last 5 rows of data
flight_data.tail(5)


# In[4]:


# Last 5 rows of data
flight_data.tail(5)


# In[5]:


# Remove IN-DATA `index` column
flight_data.drop(columns=['index'], axis=1, inplace=True)
flight_data.tail(5)


# In[6]:


# Get some info about the data
flight_data.info()


# In[7]:


# Get some description about the data
flight_data.describe()


# In[11]:


# 1. What are the airlines in the dataset, accompanied by thier frequencies?
plt.title("Airlines X Frequencies")
plt.xlabel("Number of Flights")
plt.ylabel("Airlines")
flight_data["airline"].value_counts().plot.barh(color=["lightblue", "blue"])

plt.show()


# In[12]:


# 2. Departure time against Arrival time.
plt.rcParams["figure.figsize"] = [13.50, 5.50]
plt.rcParams["figure.autolayout"] = True

plt.subplot(1, 2, 1)
plt.bar(flight_data["departure_time"].value_counts().index, flight_data["departure_time"].value_counts(), color=["salmon", "lightblue"])
plt.title("Departure Time")


plt.subplot(1, 2, 2)
plt.bar(flight_data["arrival_time"].value_counts().index, flight_data["arrival_time"].value_counts(),color=["salmon", "lightblue"])
plt.title("Arrival Time")

plt.show()


# In[13]:


# 3. Source city against Destination city.
plt.rcParams["figure.figsize"] = [13.50, 5.50]
plt.rcParams["figure.autolayout"] = True

plt.subplot(1, 2, 1)
plt.bar(flight_data["source_city"].value_counts().index, flight_data["source_city"].value_counts(), color=["salmon", "lightblue"])
plt.title("Departing City")

plt.subplot(1, 2, 2)
plt.barh(flight_data["destination_city"].value_counts().index, flight_data["destination_city"].value_counts(),color=["salmon", "lightblue"])
plt.title("Destination City")



plt.show()


# In[14]:


# 4. Does price vary with Airlines?
sns.catplot(x='airline',y='price',kind='bar',hue='class',palette='rocket',data=flight_data)
plt.show()


# In[15]:


# 5. Does ticket price change based on the departure time and arrival time?
sns.relplot(col="departure_time", y="price", kind="line",x='arrival_time', data=flight_data)
plt.show()


# In[16]:


# 6. How the price changes with change in Source and Destination?
sns.relplot(col="source_city", y="price", kind="line",x='destination_city', data=flight_data)
plt.show()


# In[ ]:




