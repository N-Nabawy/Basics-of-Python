#!/usr/bin/env python
# coding: utf-8

# # Assignment 1

# ## Test your knowledge. 
# 
# ** Answer the following questions **

# ## Strings

# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In[152]:


s = 'hello'

# Print out 'e' using indexing
s[1]


# Reverse the string 'hello' using slicing:

# In[153]:


s ='hello'

# Reverse the string using slicing
s[::-1]


# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In[154]:


s ='hello'
# Print out the 'o'

# Method 1:
# By using the index form first to end of word

s[4]


# In[155]:


# Method 2:
# By using the index form first end to first of word (reversing index).

s[-1]


# ## Lists

# Build this list [0,0,0] two separate ways.

# In[156]:


# Method 1:
# Assign x as list by using the code list().

x=[0,0,0]
list(x)


# In[157]:


# Method 2:
# Assign list y from one variable then multiply y by 3 to get list from triple 0 items.

y=[0]
y*3


# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In[158]:


# Remove last list indexed 2 from list3 then add new nested list 

list3 = [1,2,[3,4,'hello']]

list3.remove([3,4,'hello'])
list3.extend([[3,4,'goodbye']])
print(list3)


# Sort the list below:

# In[159]:


# Sort list4 by using the code sort.

list4 = [5,3,4,6,1]

list4.sort()
print(list4)


# ## Dictionaries

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In[160]:


# Grab 'hello'
# Use dictionary d and get its key to get value of its key which is string 'hello'
d = {'simple_key':'hello'}

d['simple_key']


# In[161]:


# Grab 'hello'
# Use dictionary d its 'k1' has value its type is dictionary also which its key is 'k2' its value string 'hello'
d = {'k1':{'k2':'hello'}}

d['k1']['k2']


# In[162]:


d = {'k1':[{'nest_key':['this is deep',['hello']]}]}

#Grab hello
# Use dictionary d its key 'k1'has value of it as list inside this list a dictionary its key 'nest_key'its value list indexed list[1] inside it indexed list[0] has sting'hello'

d['k1'][0]['nest_key'][1][0]


# In[163]:


#Grab hello
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}

# Use nested dictionary until get third  insided key 'tough' which indexed list[2] get its insided string 'hello'
d['k1'][2]['k2'][1]['tough'][2][0]


# ** Given the variables:**
# 
#     planet = "Earth"
#     diameter = 12742
# 
# ** Use .format() to print the following string: **
# 
#     The diameter of Earth is 12742 kilometers.

# In[164]:


# Use the code format to get this string printed

format('The diameter of Earth is 12742 kilometers')


# ** Given this nested list, use indexing to grab the word "hello" **

# In[165]:


lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


# In[166]:


# follow index for the string 'hello' in list (lst) which has nested lists inside it.

lst[3][1][2][0]


# ** Given this nested dictionary grab the word "hello". **

# In[167]:


d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}


# In[171]:


# follow index for string 'hello' inside Dictionary 'd' which has 3 nested dictionaries inside last deeply which its key 'target' and its value as list string 'hello'indexed[3]. 
d['k1'][3]['tricky'][3]['target'][3]


# ### Write a Python program to swap two variables.
# 

# In[ ]:


x=input('swap two variables')


# ## Thanks
