#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[4]:


st = 'Print only the words that start with s in this sentence'


# In[ ]:


# Assign function for this syntax by using tools(for,split code, if )

st=input('the words that start with s in this sentence\n')
x=st.split()
for word in x:
    if word[0]=='s':
        print(word)
 
     
    
    


# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[ ]:


# Assign range code and use through function (for in)

for i in range(0,11):
    if i % 2==0:
        print(i)


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[ ]:


# Assign list and use it through lambda.

lst1=range(1,51)
lst2=list(filter(lambda i:(i%3==0),lst1))
   
print(lst2)
        


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[ ]:


st = 'Print every word in this sentence that has an even number of letters'


# In[ ]:


# Assign lst variable and use it through for statment.

lst=['Print every word in this sentence that has an even number of letters']
x=lst
for x in lst:
    if lst==x%2:
        print('even')


# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[ ]:


#Assign i variable through range code and implement if statments

for i in range(1,101):
    if i%3==0:
        print("Frizz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("FizzBuzz")
        
    else:
        print(i)


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[ ]:


st = 'Create a list of the first letters of every word in this string'


# In[ ]:


# Assign input code and through split code and indexing first letters of every word in the string by (for in) 

st=input('Create a list of the first letters of every word in this string')

x=st.split()
x=['letter'[0]for words in x]
print(x)


# ### Great Job!
