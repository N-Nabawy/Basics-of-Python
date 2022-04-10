#!/usr/bin/env python
# coding: utf-8

# # Titanic project ( Numpy & Pandas)

# In[1]:


# Import libariries for exploring data.
# Numpy for linear algebra & Panadas for statistics.

import numpy as np 
import pandas as pd 


# In[2]:


# Import csv file of Data and read it.
# Assign Titanic_Data as Data Frame.

Titanic_Data = pd.read_csv('titanic dataset.csv')


# In[3]:


# Getting the number of rows and columns in the dataset

Titanic_Data.shape


# ### Description of Data Shape & Variablies:
# 
# Data is 891 observations of 12 variables. Description of these variables as follows:
# 
# PassengerId: unique id number to each passenger.
# Survived: passenger Survived (1) or died (0).
# Pclass: Passenger's class.
# Name: Passenger's name.
# Sex: Passenger's sex.
# Age: Passenger's age.
# SibSp: Number of siblings/spouses aboard.
# Parch: Number of parents/children aboard.
# Ticket: Ticket number.
# Fare: Amount of money spent on ticket.
# Cabin: Cabin Category.
# Embarked: Port of passenger embarkation(C = Cherbourg, Q = Queenstown, S = Southampton). 

# In[4]:


# Assign .info() for knowing more information about Data.

Titanic_Data.info()


# In[5]:


# Showing first 5 indexes of Data.

Titanic_Data.head()


# In[6]:


# Showing last 5 indexes of Data.

Titanic_Data.tail()


# previously cell obvious some essential information about the variables.
# 
# An numeric variable is one with values of integers or real numbers while a categorical variable is a variable that can take on one of a limited, and usually fixed, number of possible values.

# ### Sex 
#  from this colume will explore and calculate percentage of Female(women) and Male(men) who survived.

# In[7]:


# Number of people of each gender. 

Titanic_Data['Sex'].value_counts()


# In[8]:


# Number of people survived.

Titanic_Data['Survived'].value_counts()


# In[9]:


#percentage of women who survived by ratio_women equation.

women = Titanic_Data.loc[Titanic_Data.Sex == 'female']["Survived"]
ratio_women = sum(women)/len(women)

print("percentage of women who survived:", ratio_women)


# In[10]:


#percentage of men who survived by ratio_men equation.

men = Titanic_Data.loc[Titanic_Data.Sex == 'male']["Survived"]
ratio_men = sum(men)/len(men)

print("percentage of men who survived:", ratio_men)


# ### More Explore for  Whole Data  

# In[11]:


#Assign .describe() for Essential statistical Data. 

Titanic_Data.describe()


# Notice especially what type of variable each is, how many observations there are and some of the variable values.
# 
# An interesting observation could for example be the minimum age 0.42, do you know why this is?

# ### Dealing & Handling Missing Data

# In[12]:


# Calculating Missing value of whole Data.
Titanic_Data.isnull().sum()


# There are missing values for Age, Cabin and Embarked features. Deeply, there are many missing values for Age and Cabin features.

# Firstly dealing with Cabin snice there is relationship between cabin and survival ratio.

# In[13]:


Titanic_Data['Cabin'].isnull().sum()


# In[14]:


Titanic_Data['Cabin'].unique()


# All Missing values are 866. Deeply, This is used to determine whether the cabin is owned or not calculate percentage of it.

# In[15]:


# The percentage of missing values cabin column. 
percent=(687/891)*100
print("The percentage of missing values in 'Cabin' column is", round(percent, 2), '%')


# Not just dropping the column because a column with many missing values does not mean that it can't provide the model with very useful information.
# 
# Firstly glance the most significant columns are Pclass, Sex, Age, SibSp, Parch, Fare and maybe Embarked. PassengerId is irrelevant and the column Ticket doesn't seem to play a significant role because 5-7 digits numbers on tickets and letters seem to be random and not relevant to a specific class or some other column.
# 
# Another thought is that moral code dictates that the physically weaker passengers should have been protected by the young male adults so we expect to see a higher survival rate to women, children and older people and a lower survival rate to young male adults.

# Cabin has missing value but it because many people would be sharing the dorm area of the ship. We can mark such data with our represention of dorm. lets marks it with Z0,
# Z -> room, 0 -> No Room.

# In[16]:



Adjust_Cabin=Titanic_Data.Cabin.isna()
Titanic_Data.loc[Titanic_Data[Adjust_Cabin].index, ['Cabin']] = 'Z0'
Titanic_Data.Cabin.isna().sum()


# In[17]:


Adjust_Cabin= Titanic_Data.Age.isna()
Titanic_Data[Adjust_Cabin]


# In[18]:


# Conclusion - Missing age data has children(Master), younger Female(Miss), Female(Mrs), Male(Mr,Dr) 

Titanic_Data[Adjust_Cabin]['Name'].apply(lambda x : x.split(',')[1].split('.')[0].strip()).value_counts()


# In[19]:


# Conclusion- these are passanger count as per title. I will use this for age imputation.

Titanic_Data['NameTitle'] = Titanic_Data.Name.apply(lambda x : x.split(',')[1].split('.')[0].strip())
Titanic_Data.NameTitle.value_counts()


# Handling this missing after filtering separately it with median which is more accurate than mean since it littel sensitive with outliers.

# In[20]:


# Age up to master

filter_master = (Titanic_Data.NameTitle == 'Master')
master_age= Titanic_Data[filter_master].Age.median()
master_age


# In[21]:


# Age up to Mr

filter_mr = (Titanic_Data.NameTitle == 'Mr')
mr_age = Titanic_Data[filter_mr].Age.median()
mr_age


# In[22]:


# Age up to Mrs

filter_mrs = (Titanic_Data.NameTitle == 'Mrs')
mrs_age = Titanic_Data[filter_mrs].Age.median()
mrs_age


# In[23]:


# Age up to Miss

filter_miss = (Titanic_Data.NameTitle == 'Miss')
miss_age = Titanic_Data[filter_miss].Age.median()
miss_age


# In[24]:


# Age up to dr

filter_dr = (Titanic_Data.NameTitle == 'dr')
dr_age = Titanic_Data[filter_dr].Age.median()
dr_age


# In[25]:


Titanic_Data.loc[Titanic_Data[(Titanic_Data.Age.isna() ) & (filter_master) ].index, 'Age' ] = master_age
Titanic_Data.loc[Titanic_Data[(Titanic_Data.Age.isna() ) & (filter_mr) ].index, 'Age' ] = mr_age
Titanic_Data.loc[Titanic_Data[(Titanic_Data.Age.isna() ) & (filter_mrs) ].index, 'Age' ] = mrs_age
Titanic_Data.loc[Titanic_Data[(Titanic_Data.Age.isna() ) & (filter_miss) ].index, 'Age' ] = miss_age
Titanic_Data.loc[Titanic_Data[(Titanic_Data.Age.isna() ) & (filter_dr) ].index, 'Age' ] = dr_age


# Finally as much as possible Core missing values of Cabin and Age handeled.
