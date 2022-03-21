#!/usr/bin/env python
# coding: utf-8

# # Assignment 3

# ### Write a function to count the number 4 in a given list.

# In[ ]:


# Assign function to count the number 4 in a given list and show it by return.  

lst=[1,2,3,4,4,9,6]
x=4
def count_X(lst, x):
    return lst.count(x)

print('{} has occurred {} times'.format(x, count_X(lst, x)))  
    


# ### write a  function to check whether a number is divisible by another number.

# In[12]:


#Assign function to check whether a number is divisible by another number

def div(a,b):
    if a % b ==0:
        print("True")
    else:
        print("False")


# ### write a function to find the maximum and minimum numbers from a sequence of numbers.

# In[13]:


# Assign function to find the maximum and minimum numbers through def , for in and show it by return.

def max_min(nums):
    x= nums[0]
    y= nums[0]
    for num in nums:
        if num> x:
            x = num
        elif num < y:
            y = num
    return x, y

print(max_min([0,1,3,5,7,90]))


# ### Write a Python function that takes two lists and returns True if they have at least one common member.

# In[14]:


# Assign function that takes two lists and returns True if they have at least one common member

a = [1,2,3,4]
b = [22,34,45,4]

if any(x in a for x in b):
    print(True)
else:
    print(False)


# ### Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number from the user

# In[15]:


# Assign function to calculate the factorial of a number (a non-negative integer). The function accepts the number from the user 

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(n-1)
x=int(input("Input a number to compute the factiorial"))
print(factorial(x))


# ### Write a Python function to check whether a number is in a given range.
# 
# ### The range is from 3 to 11
# 

# In[ ]:


# Assign function test_range to check whether a number is in a given range

def test_range(x):
    if x in range(3,12):
        print("true")
    else :
        print("false")
        
    return(5)


# ### Write a  program to create the multiplication table (from 1 to 10) of a number.

# In[ ]:


# use for loop to iterate 10 times
n = int(input("Input a number"))

# use for loop to iterate 10 times
for i in range(1,11):
    print(n,'x',i,'=',n*i)


# #### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers *if* both numbers are even, but returns the greater if one or both numbers are odd
#     lesser_of_two_evens(2,4) --> 2
#     lesser_of_two_evens(2,5) --> 5

# In[ ]:


# Assign a function lesser_of_two_evens that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a,b):
    if (a % 2 and b % 2) != 0:
        if b > a:
            print(b)
        if a > b:
            print(a)    
    elif (a % 2 and b % 2) == 0:
        if a < b:
            print(a)
        else:
            print(b)    
    pass


# #### ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#     animal_crackers('Levelheaded Llama') --> True
#     animal_crackers('Crazy Kangaroo') --> False

# In[ ]:


#Assign function check_letter takes a two-word string and returns True if both words begin with same lette

def check_letter(string):
# Split function splits string making an array(splits at space at this  example).
words = string.split()
# [0][0] means first element and first symbol, [1][0] - 2nd elem, 1st symbol
    if words[0][0] == words[1][0]:
        return True
    else:
        return False


# #### MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 *or* if one of the integers is 20. If not, return False
# 
#     makes_twenty(20,10) --> True
#     makes_twenty(12,8) --> True
#     makes_twenty(2,3) --> False

# In[ ]:


#Assign function with makes_twenty

def makes_twenty(NO_1,NO_2):
    if (NO_1==20 or NO_2==20 or (NO_1+NO_2)==20):
        return True
    else:
        return False


# #### ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# 
#     almost_there(90) --> True
#     almost_there(104) --> True
#     almost_there(150) --> False
#     almost_there(209) --> True
#     
# NOTE: `abs(num)` returns the absolute value of a number

# In[ ]:


#Assign function almost_there and show it through return 

def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


# #### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum  exceeds 21, return 'BUST'
#     blackjack(5,6,7) --> 18
#     blackjack(9,9,9) --> 'BUST'
#     blackjack(9,9,11) --> 19

# In[ ]:


#Assign function blackjack to make three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum exceeds 21, return 'BUST'  

def blackjack(x,y,z):
    total=int(x+y+z)
    if total < 21:
        return total
    
    elif total > 21 and x == 11 or y == 11 or z == 11:
        total_2=total-10
        return total_2
    
    else:
        return "BUST"
         
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


# In[ ]:





# In[ ]:




