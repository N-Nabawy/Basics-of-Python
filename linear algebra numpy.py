#!/usr/bin/env python
# coding: utf-8

# ## Write a Numpy program to compute the multiplication of two given matrixes

# In[1]:


# Assign function to multiply two matrices p and Q by (.dot) to get this multiplication in new matrix x.
# Note take care with multiplication condition of sizes of matrix to do this process.

import numpy as np
p = [[1,2], [3,4]]
q = [[5,6], [7,8]]

print(p)
print(q)


# In[2]:


x= np.dot(p, q)

print(x)


# ## Write a NumPy program to compute the determinant of a given square array

# In[3]:


# Assign program for square array (2 D) then calculate determint for it.

x= np.array([[1,2], [3,4]])

print(x)


# In[4]:


np.linalg.det(x)


# ## Write a NumPy program to compute the cross product of two given vectors

# In[5]:


# Assign two vectors p and q then calculate the cross product for it by (.cross). 

p = [[0,1,2]]
q = [[3,4,5]]

print(p)
print(q)


# In[6]:


x= np.cross(p, q)
y= np.cross(q, p)

print(x)
print(y)


# ## Write a NumPy program to compute the condition number of a given matrix

# In[7]:


#Assign program to compute the condition number of A matrix by (.cond).

A= np.array([[1,0,0,0], [0,0,1,1]])
print(A)


# In[8]:


np.linalg.cond(A)


# ## Write a NumPy program to compute the inverse of a given matrix

# In[9]:


#Assign program to compute the inverse of A matrix by(.inv).

A= np.array([[1,2],[3,4]])

print(A)


# In[10]:


np.linalg.inv(A)

