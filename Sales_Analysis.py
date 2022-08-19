#!/usr/bin/env python
# coding: utf-8

# # Data Analysis Via Pandas and Matplotlib Libraries:
# #### This project is part of a learning process that I am attempting in order to understand some of the basic elements of data analysis within a buisness setting.
# 
# We will use Pyhton Pandas and Matplotlib to analyze and answer buisness-driven questions about a year long worth of sales. Our data contains hundreds of thousands of electronic devices store purchases broken down by: month, product type, cost, purchase address, quantity, etc.

# #### Import Essential Libraries:

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import os
from functools import reduce


# #### Import Data For 12 Months

# In[2]:


df1 = pd.read_csv("Untitled folder 1/Sales_January_2019.csv")
df2 = pd.read_csv("Untitled folder 1/Sales_February_2019.csv")
df3 = pd.read_csv("Untitled folder 1/Sales_March_2019.csv")
df4 = pd.read_csv("Untitled folder 1/Sales_April_2019.csv")
df5 = pd.read_csv("Untitled folder 1/Sales_May_2019.csv")
df6 = pd.read_csv("Untitled folder 1/Sales_June_2019.csv")
df7 = pd.read_csv("Untitled folder 1/Sales_July_2019.csv")
df8 = pd.read_csv("Untitled folder 1/Sales_August_2019.csv")
df9 = pd.read_csv("Untitled folder 1/Sales_September_2019.csv")
df10 = pd.read_csv("Untitled folder 1/Sales_October_2019.csv")
df11 = pd.read_csv("Untitled folder 1/Sales_November_2019.csv")
df12 = pd.read_csv("Untitled folder 1/Sales_December_2019.csv")


# #### Segment data by each year quarter and merge into 4 distinct dataframes:
# 
# * Data for an entire year has been uploaded into the Jupyter Notebook.We will use 1st, 2nd, 3rd, and 4th quarters to reduce the size of the overall dataframe, which could not be implemeted in the jupyter notebook to to size limitations.

# In[3]:


df_1st_quarter = [df1, df2, df3] # 1st Quarter of 2019
df_2nd_quarter = [df4, df5, df6] # 2nd Quarter of 2019
df_3rd_quarter = [df7, df8, df9] # 3rd Quarter of 2019
df_4th_quarter = [df10, df11, df12] # 4th Quarter of 2019

df_merged1= reduce(lambda left,right: pd.merge(left, right, how = 'outer'), df_1st_quarter)
df_merged2= reduce(lambda left,right: pd.merge(left, right, how = 'outer'), df_2nd_quarter)
df_merged3= reduce(lambda left,right: pd.merge(left, right, how = 'outer'), df_3rd_quarter)
df_merged4= reduce(lambda left,right: pd.merge(left, right, how = 'outer'), df_4th_quarter)


# In[4]:


df_merged1.head() # Pull-up 1st five rows of the dataframe


# In[5]:


df_merged1.head()


# In[6]:


print("Data For First Quarter: \n")
print(df_merged1.count())
print("Data For Second Quarter: \n")
print(df_merged2.count())
print("Data For Thrid Quarter: \n")
print(df_merged3.count())
print("Data For Fourth Quarter: \n")
print(df_merged4.count())


# ### Cleaning Data:

# #### Drop rows of NaN from each dataframe:

# In[7]:


nan_df1 = df_merged1[df_merged1.isna().any(axis=1)]
nan_df1.head()

df_merged1 = df_merged1.dropna(how = 'all')
df_merged1.head()


# In[8]:


nan_df2 = df_merged2[df_merged2.isna().any(axis=1)]
nan_df1.head()

df_merged2 = df_merged2.dropna(how = 'all')
df_merged2.head()


# In[9]:


nan_df3 = df_merged3[df_merged3.isna().any(axis=1)]
nan_df3.head()

df_merged3 = df_merged3.dropna(how = 'all')
df_merged3.head()


# In[10]:


nan_df4 = df_merged4[df_merged4.isna().any(axis=1)]
nan_df4.head()

df_merged4 = df_merged4.dropna(how = 'all')
df_merged4.head()


# #### Find 'Or' and delete it from each dataframe:

# In[11]:


df_merged1 = df_merged1[df_merged1["Order Date"].str[0:2] != 'Or']
df_merged2 = df_merged2[df_merged2["Order Date"].str[0:2] != 'Or']
df_merged3 = df_merged3[df_merged3["Order Date"].str[0:2] != 'Or']
df_merged4 = df_merged4[df_merged4["Order Date"].str[0:2] != 'Or']


# ### Make columns of correct type:

# In[12]:


# Convert Columns Data Types to Correct Data Types for Each DataFrame:

# DataFrame for First Yearly Quarter:
df_merged1["Quantity Ordered"] = df_merged1["Quantity Ordered"].astype("int32")
df_merged1["Price Each"] = df_merged1["Price Each"].astype("float")

df_merged1["Sales"] = df_merged1["Quantity Ordered"] * df_merged1["Price Each"]

df_merged1.head()


# In[13]:


# DataFrame for Second Yearly Quarter:
df_merged2["Quantity Ordered"] = df_merged2["Quantity Ordered"].astype("int32")
df_merged2["Price Each"] = df_merged2["Price Each"].astype("float")

df_merged2["Sales"] = df_merged2["Quantity Ordered"] * df_merged2["Price Each"]

# DataFrame for Third Yearly Quarter:
df_merged3["Quantity Ordered"] = df_merged3["Quantity Ordered"].astype("int32")
df_merged3["Price Each"] = df_merged3["Price Each"].astype("float")

df_merged3["Sales"] = df_merged3["Quantity Ordered"] * df_merged3["Price Each"]

# DataFrame for Fourth Yearly Quarter:
df_merged4["Quantity Ordered"] = df_merged4["Quantity Ordered"].astype("int32")
df_merged4["Price Each"] = df_merged4["Price Each"].astype("float")

df_merged4["Sales"] = df_merged4["Quantity Ordered"] * df_merged4["Price Each"]

df_merged4.head()


# ## Augment data with additional month columns:

# In[14]:


df_merged1["Month"] = df_merged1["Order Date"].str[0:2] # e.g. date 01/27/2019 pick 01 and so on for each Month column
df_merged2["Month"] = df_merged2["Order Date"].str[0:2]
df_merged3["Month"] = df_merged3["Order Date"].str[0:2]
df_merged4["Month"] = df_merged4["Order Date"].str[0:2]


df_merged1["Month"] = df_merged1["Month"].astype("int32") # Covert Month column to integer data type
df_merged2["Month"] = df_merged2["Month"].astype("int32")
df_merged3["Month"] = df_merged3["Month"].astype("int32")
df_merged4["Month"] = df_merged4["Month"].astype("int32")


# In[15]:


df_merged4.head()


# #### Add a city column:

# In[16]:


# Let's use .apply()
# Consider cities with duplicate names i.e look-up states as well:

def get_city(address):
    return address.split(",")[1] # Get city name

def get_state(address):
    return address.split(",")[2].split(' ')[1] # Get state and delete ZipCode

df_merged1["City"] = df_merged1["Purchase Address"].apply(lambda x: 
                                f"{get_city(x)} ({get_state(x)})")


df_merged1.head()


# In[17]:


def get_city(address):
    return address.split(",")[1]

def get_state(address):
    return address.split(",")[2].split(' ')[1]

df_merged2["City"] = df_merged2["Purchase Address"].apply(lambda x:
                                f"{get_city(x)} ({get_state(x)})")

df_merged2.head()


# In[18]:


def get_city(address):
    return address.split(",")[1]
def get_state(address):
    return address.split(",")[2].split(' ')[1]

df_merged3["City"] = df_merged3["Purchase Address"].apply(lambda x: 
                                f"{get_city(x)} ({get_state(x)})")

df_merged3.head()


# In[19]:


def get_city(address):
    return address.split(",")[1]

def get_state(address):
    return address.split(",")[2].split(' ')[1]

df_merged4["City"] = df_merged4["Purchase Address"].apply(lambda x: 
                                    f"{get_city(x)} ({get_state(x)})")

df_merged4.head()


# # Data Exploration!

# #### Q1: What was the best month for sales? How much was earned that month?

# ##### Adding a sales column:

# In[20]:


df_merged1.dtypes


# In[21]:


df_merged3.head()


# In[22]:


print(df_merged1.groupby("Month").sum())
print(df_merged2.groupby("Month").sum())
print(df_merged3.groupby("Month").sum())
print(df_merged4.groupby("Month").sum())


# ##### We see that December was the best month for sales with about 4.6 million US Dollars... Let us visualize the sales result for each month in the year 2019:

# In[23]:


results_Q1 = df_merged1.groupby("Month").sum()
results_Q2 = df_merged2.groupby("Month").sum()
results_Q3 = df_merged3.groupby("Month").sum()
results_Q4 = df_merged4.groupby("Month").sum()


# In[24]:


firstQ = range(1,5)

plt.bar(firstQ, results_Q1["Sales"])
plt.xticks(firstQ)
plt.ylabel("Sales in USD ($)")
plt.xlabel("Month Number")
plt.show()


# In[25]:


secondQ = range(4, 8)

plt.bar(secondQ, results_Q2["Sales"])
plt.xticks(secondQ)
plt.ylabel("Sales in USD ($)")
plt.xlabel("Month Number")
plt.show()


# In[26]:


thirdQ = range(8, 12)

plt.bar(thirdQ, results_Q3["Sales"])
plt.xticks(thirdQ)
plt.ylabel("Sales in USD ($)")
plt.xlabel("Month Number")
plt.show()


# In[27]:


fourthQ = range(9, 13)

plt.bar(fourthQ, results_Q4["Sales"])
plt.xticks(fourthQ)
plt.ylabel("Sales in USD ($)")
plt.xlabel("Month Number")
plt.show()


# #### Q2. Which US city had the highest number of sales:

# In[28]:


city_results_Q1 = df_merged1.groupby("City").sum()
city_results_Q2 = df_merged2.groupby("City").sum()
city_results_Q3 = df_merged3.groupby("City").sum()
city_results_Q4 = df_merged4.groupby("City").sum()


# In[29]:


Rresult = [city_results_Q1, city_results_Q2, city_results_Q3, city_results_Q4]
Rresult


# In[30]:


city_results_Q1


# In[31]:


city_results_Q4


# SAN FRANCISCO (CA) seems be the city with the highest number of sales with over 2.7 Million US Dollars in 4th quarter of the year 2019, but let's make sure of our result by using bar graphs:

# In[32]:


keys = [city for city, df in df_merged1.groupby(['City'])]

plt.bar(keys,df_merged1.groupby(['City']).sum()['Sales'])
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.xticks(keys, rotation='vertical', size=8)
plt.show()


# In[33]:


keys = [city for city, df in df_merged2.groupby(['City'])]

plt.bar(keys,df_merged2.groupby(['City']).sum()['Sales'])
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.xticks(keys, rotation='vertical', size=8)
plt.show()


# In[34]:


keys = [city for city, df in df_merged3.groupby(['City'])]

plt.bar(keys,df_merged3.groupby(['City']).sum()['Sales'])
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.xticks(keys, rotation='vertical', size=8)
plt.show()


# In[41]:


keys = [city for city, df in df_merged4.groupby(['City'])]

plt.bar(keys,df_merged4.groupby(['City']).sum()['Sales'])
plt.ylabel('Sales in USD ($)')
plt.xlabel('Month number')
plt.xticks(keys, rotation='vertical', size=8)

plt.show()


# #### Q3. What time should we display advertisements to maximize likelihood of customer's buying product?

# #### 1st Quarter:

# In[46]:


# Use to_datetime to convert Order Date to datetime formate

df_merged1['Hour'] = pd.to_datetime(df_merged1['Order Date']).dt.hour
df_merged1['Minute'] = pd.to_datetime(df_merged1['Order Date']).dt.minute
df_merged1['Count'] = 1
df_merged1.head()


# In[57]:


keys = [pair for pair, df in df_merged1.groupby(["Hour"])]

plt.plot(keys, df_merged1.groupby(['Hour']).count()['Count'])
plt.xticks(keys)
plt.grid()
plt.show()

# Observe Peaks and Make Probable Conclusions


# #### 2nd Quarter:

# In[50]:


df_merged2['Hour'] = pd.to_datetime(df_merged2['Order Date']).dt.hour
df_merged2['Minute'] = pd.to_datetime(df_merged2['Order Date']).dt.minute
df_merged2['Count'] = 1
df_merged2.head()


# In[54]:


keys = [pair for pair, df in df_merged2.groupby(["Hour"])]

plt.plot(keys, df_merged2.groupby(['Hour']).count()['Count'])
plt.xticks(keys)
plt.grid()
plt.show()


# #### 3rd Quarter:

# In[52]:


df_merged3['Hour'] = pd.to_datetime(df_merged3['Order Date']).dt.hour
df_merged3['Minute'] = pd.to_datetime(df_merged3['Order Date']).dt.minute
df_merged3['Count'] = 1
df_merged3.head()


# In[53]:


keys = [pair for pair, df in df_merged3.groupby(["Hour"])]

plt.plot(keys, df_merged3.groupby(['Hour']).count()['Count'])
plt.xticks(keys)
plt.grid()
plt.show()


# #### 4th Quarter:

# In[55]:


df_merged4['Hour'] = pd.to_datetime(df_merged4['Order Date']).dt.hour
df_merged4['Minute'] = pd.to_datetime(df_merged4['Order Date']).dt.minute
df_merged4['Count'] = 1
df_merged4.head()


# In[56]:


keys = [pair for pair, df in df_merged4.groupby(["Hour"])]

plt.plot(keys, df_merged4.groupby(['Hour']).count()['Count'])
plt.xticks(keys)
plt.grid()
plt.show()

