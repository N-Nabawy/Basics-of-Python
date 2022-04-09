#!/usr/bin/env python
# coding: utf-8

# # SF Salaries Exercise 
# 
# 

# ** Import pandas as pd.**

# In[1]:


import pandas as pd


# ** Read Salaries.csv as a dataframe called sal.**

# In[2]:


# Assign data frame as sal and read this csv file from home of jupter.

sal= pd.read_csv('Salaries.csv')


# In[3]:


# This for showing indexes and colums vice versa
sal.transpose()


# ** Check the head of the DataFrame. **

# In[4]:


# Function of .head() for first 5 indexes.
sal.head()


# ** Use the .info() method to find out how many entries there are.**

# In[5]:


# Function of .info() for showing more detials widely of Data inside csv file.
sal.info()


# **What is the average BasePay ?**

# In[6]:


#Assign function of .mean() for calculating average of 'BasePay' colume.

sal['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[7]:


#Assign function of .max()for calculating the highest amount of 'OvertimePay' colume.

sal['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[8]:


# Assign conditional data frame to know the job title of JOSEPH DRISCOLL and taking care about name whole word is uppercase letters.

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[14]:


# Assign conditional data frame to know TotalPayBenefits of JOSEPH DRISCOLL.

sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']


# ** What is the name of highest paid person (including benefits)?**

# In[18]:


# Assign data frame x to know the name of highest paid person by using .idxmax() function.

x= sal['TotalPayBenefits'].idxmax()
sal.loc[x]['EmployeeName']


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[19]:


# Assign data frame x to know the name of lowest paid person by using .idxmin() function.

x= sal['TotalPayBenefits'].idxmin()
sal.iloc[x]


# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[20]:


# Assign groupby method to group rows of data together in year and call aggregate functions.
#for calculating the average of BasePay icluding all employees per year between 2011 to 2014 by use .mean().

sal.groupby('Year').mean()['BasePay']


# ** How many unique job titles are there? **

# In[22]:


# Assign function .nunique() for calculating number of unique values of 'JobTitle'. 

sal['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[23]:


# Assign function .value_counts() for counting values of 'JobTitle'. 
# Assign also .head() for persenting the top 5 most common jobs.
    
sal['JobTitle'].value_counts().head()


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[24]:


#Assign conditional data frame to know Job Titles use .sum() were represented by only one person in 2013 .value_counts()==1.

(sal[sal['Year']==2013]['JobTitle'].value_counts()==1).sum()


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[25]:


#Assign data frame and .apply() to function .sum() for calculating number of the word Chief as string x in their job title.

sal['JobTitle'].apply(lambda x :('chief' in str(x).lower())).sum()


# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[27]:


#Assign data frame as 'title_len' use .apply(len) then .corr between'title_len' and 'TotalPayBenefits' for calculating correlation between them. 

sal['title_len'] = sal['JobTitle'].apply(len)


# In[28]:


sal[['title_len','TotalPayBenefits']].corr()


# There is no corrlation between 'title_len' and 'TotalPayBenefits'.

# # Great Job!
