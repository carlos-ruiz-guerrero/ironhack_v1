#!/usr/bin/env python
# coding: utf-8

# # Foreword

# The intention of this project is providing a thorough analysis of a dataset regarding it-related job offerings, where we analyse relevant aspects such as the job title, location and gross average salary. 
# 
# Due to time constraints, and the technical difficulties encountered in previous web scraping attempts, it has been withdrawn the option to scrap data from infojobs, since the general T&C of the website do not allow for web scrapping, plus, they have controls in place to block any web scrapping action. 
# 
# We insted take the data from a .csv dataset obtained from kaggle, whose link is provided in the initial section. 

# 1. the project consists of an analysis of IT industry job openings from a kaggle datasets that has a sample size of 3,755 elements
# 2. we provide information on the gross salary, irrespective of other benefits (contributions to pensions schema, health insurance, travel allowances, etc.)
# 3. we do not take into account the inflation effect / consumer price index (6,1% in the Eurozone as of June 2023) 
# 4. this dataset provides information as of April 2023 

# Sources: digitalocean.com, kaggle, datacamp, geeks for geeks, eurostat, medium.com, towardsdatascience.com 

# 
# 
# 

# # Dataset 

# 1. Read the data

# Data source: https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023

# In[1]:


import pandas as pd                   
import numpy as np   

import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


# In[2]:


dataset = pd.read_csv('ds_salaries (1).csv')
dataset.head()


# 2. Analyse dataset 

# In[3]:


dataset.shape


# In[4]:


dataset.info()


# In[ ]:





# 3. Get num and cat variables 

# In[5]:


num = dataset.select_dtypes(include=np.number)
num


# In[6]:


cat = dataset.select_dtypes(include=np.object)
cat


# In[7]:


for column in cat.columns:
    unique_values = cat[column].unique()
    print(f"Unique values '{column}': {unique_values}")


# In[8]:


print(dataset.isnull().sum())


# In[ ]:





# In[9]:


dataset['job_title'].unique()


# In[10]:


item_counts = dataset["job_title"].value_counts(normalize=True)
print(item_counts)


# In[11]:


dataset['company_location'].unique()
item_counts = dataset["company_location"].value_counts(normalize=True)
print(item_counts)


# 4. Descriptive statistics 

#   

# In[12]:


dataset.describe()


# In[13]:


for column in cat.columns:
    plt.figure()  # Create a new figure for each plot
    sns.countplot(data=cat, x=column)
    plt.title(f"Countplot of {column}")
    plt.show()


# We provide a countplot for categorical variables, we do it initially with a for loop, just to get an overview, and then we do it individually to provide a detailed description of the selected charts to get a better data interpretation from a cleaner graph. 

# In[14]:


sns.countplot(dataset['work_year']).unique()


# In[15]:


sns.countplot(dataset['experience_level']).unique()


# In[16]:


sns.countplot(dataset['employment_type']).unique()


# In[17]:


sns.countplot(dataset['company_size']).unique()


# In[20]:


sns.pairplot(dataset, height=1.5)


# In[18]:


sns.pairplot(
    dataset,
    plot_kws=dict(marker="+", linewidth=1),
    diag_kws=dict(fill=False),
)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# 

# # Ideas for sql querying

# Eventhough we are going to be dealing with this in the corresponding section of the project, we provide an advance of some sql queries that we may perform once we create the sql db from the dataset being analysed

# 1. calculate the average gross salary, in usd, for middle and senior experience level
# 2. calculate the average gross salary for a Data Scientist and a Machine Learning Engineer 
# 3. calculate the average gross salary for a Deep Learning Engineer in the US 
# 4. calculate the average gross salary for a Machine Learning Engineer in Spain in 2022 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




