#!/usr/bin/env python
# coding: utf-8

# # map()
# Function will be applied to all objects of iterable, we can use as many literables as wee needed.
# 

# # filter()
# 
# Function will be applied to only those objects of iterable and added to result which item is True, we can use only one literable.

# In[1]:


#In this example; item 0 is not add in the filter function because 0 is a representation for False in some cases so it is not added to the filter and added in the map function result

def check(num):
    return num*1


nums = [0,2, 4, 6, 7, 8]
result = filter(check, nums)

print(list(result))

def check(num):
    return num*1


nums = [0,2, 4, 6, 7, 8]
result = map(check, nums)

print(list(result))


# In[2]:


# Anthor example one 
def square(num):
    return num * num

nums = [1, 2, 3, 4, 5]
mapped = map(square, nums)

print(*nums)
print(*mapped)


# In[3]:


# last example
def is_even(num):
    return num % 2 == 0


nums = [2, 4, 6, 7, 8]
filtered = filter(is_even, nums)

print(*nums)
print(*filtered)


# In[ ]:




