
# coding: utf-8

# # Data Workflow Lab 1
#
# Clean and summarize Project 3 data.
#
# ### Learning Objectives
#
# * Practice text cleaning techniques
# * Practice datatype conversion
# * Practice filling in missing values with either 0 or the average in the column
# * Practice categorical data techniques
# * Transform data into usable quantities
#

# In[2]:
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
import datetime
import numpy as np
import pandas as pd


# In[6]:

# Load the data

location =  "Iowa_Liquor_Sales_reduced.csv"

df = pd.read_csv(location, low_memory = False)
print df.columns
print df.dtypes

df.head()


# In[19]:

#I actually want to know the columns and their data types now.

df.dtypes


# ## Clean the data
#
# Let's practice our data cleaning skills on the Project 3 dataset. If you don't remember how to do any of these tasks, look back at your work from the previous weeks or search the internet. There are many blog articles and Stack Overflow posts that cover these topics.
#
# You'll want to complete at least the following tasks:
# * Remove redundant columns
# * Remove "$" prices from characters and convert values to floats.
# * Convert dates to pandas datetime objects
# * Convert category floats to integers
# * Drop or fill in bad values

# In[25]:

# Remove redundant columns

#County Number and County seem to match exactly, so will remove one.
#Category and Category name do not. I wonder if I could map category name to category, and also to mean retail price...

print len(df['Category'].unique())
print len(df['Category Name'].unique())

#Checking if there is any meaningful difference in Category Name and Category.

print pd.pivot_table(df, index = ['Category Name', 'Category'], values = ['Bottle Volume (ml)'])


#df2 = df.drop()


# In[5]:

# Remove $ from certain columns


# In[ ]:

# Convert dates


# In[ ]:

# Drop or replace bad values

# Convert integers


# ## Filter the Data
#
# Some stores may have opened or closed in 2015. These data points will heavily skew our models, so we need to filter them out or find a way to deal with them.
#
# You'll need to provide a summary in your project report about these data points. You may also consider using the monthly sales in your model and including other information (number of months or days each store is open) in your data to handle these unusual cases.
#
# Let's record the first and last sales dates for each store. We'll save this information for later when we fit our models.

# In[ ]:

# Determine which stores were open all of 2015
# Find the first and last sales date.


# Filter out stores that opened or closed throughout the year
# You may want to save this step until you start modelling


# ## Compute New Columns and Tables
#
# Since we're trying to predict sales and/or profits, we'll want to compute some intermediate data. There are a lot of ways to do thisand good use of pandas is crucial. For example, for each transaction we may want to know:
# * margin, retail cost minus bottle cost
# * price per bottle
# * price per liter
#
# We'll need to make a new dataframe that indexes quantities by store:
# * sales per store for all of 2015
# * sales per store for Q1 2015
# * sales per store for Q1 2016
# * total volumes sold
# * mean transaction revenue, gross margin, price per bottle, price per liter, etc.
# * average sales per day
# * number of days open
#
# Make sure to retain other variables that we'll want to use to build our models, such as zip code, county number, city, etc. We recommend that you spend some time thinking about the model you may want to fit and computing enough of the suggested quantities to give you a few options.
#
# Bonus tasks:
# * Restrict your attention to stores that were open for all of 2015 and Q1 2016. Stores that opened or closed in 2015 will introduce outliers into your data.
# * For each transaction we have the item category. You may be able to determine the store type (primarily wine, liquor, all types of alcohol, etc.) by the most common transaction category for each store. This could be a useful categorical variable for modelling.

# In[ ]:

# Margin and Price per liter


# In[ ]:

# Sales per store, 2015

# Filter by our start and end dates
df.sort_values(by=["Store Number", "Date"], inplace=True)
start_date = pd.Timestamp("20150101")
end_date = pd.Timestamp("20151231")
mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
sales = df[mask]

# Group by store name
sales = sales.groupby(by=["Store Number"], as_index=False)
# Compute sums, means
sales = sales.agg({"Sale (Dollars)": [np.sum, np.mean],
                   "Volume Sold (Liters)": [np.sum, np.mean],
                   "Margin": np.mean,
                   "Price per Liter": np.mean,
                   "Zip Code": lambda x: x.iloc[0], # just extract once, should be the same
                   "City": lambda x: x.iloc[0],
                   "County Number": lambda x: x.iloc[0]})
# Collapse the column indices
sales.columns = [' '.join(col).strip() for col in sales.columns.values]
# Rename columns

# Quick check
sales.head()


# In[ ]:

# Q1 sales, may want to also use aggregate as above to have more columns (means, etc.)

# Sales 2015  Q1

# Sales 2016 Q1


# Proceed with any calculations that you need for your models, such as grouping
# sales by zip code, most common vendor number per store, etc. Once you have finished adding columns, be sure to save the dataframe.

# In[ ]:

# Compute more things
# ...


# In[ ]:

# Save this dataframe

# Let's add the dates computed above to this data.
sales["First Date"] = dates['Date amin']
sales["Last Date"] = dates['Date amax']

sales.to_csv("sales.csv")
