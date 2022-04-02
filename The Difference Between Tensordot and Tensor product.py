#!/usr/bin/env python
# coding: utf-8

# # Tensor Dot:
# 
#     The idea with 'tensordot' simply. you input the arrays and the respective axes along which the sum-reductions are intended. The axes that take part in sum-reduction are removed in the output and all of the remaining axes from the input arrays are spread-out as different axes in the output keeping the order in which the input arrays are fed.

# In[1]:


#Assign two tensors by (.rand) as which used in arrays calculate random numbers of tensors.
import numpy as np

A = np.random.randint(2, size=(2, 3, 5))
B = np.random.randint(2, size=(3, 2, 4))

print(A)
print(B)


# In[2]:


#Two axes of sum-reduction.
np.tensordot(B, A, axes=((1,0),(0,1))).shape


# (4, 5) will be this output since;
# B : (3, 2, 4) -> reduction of axis=(1,0)
# A : (2, 3, 5) -> reduction of axis=(0,1)
# 
#    `(3, 2, 4)`, `(2, 3, 5)` ===(2,3 gone)==> `(4)` + `(5)` => `(4,5)`

# # Tensor Product:
# a numpy function that does tensor product of two matrices. That creates a 4x4 product matrix of two 2x2 matrices.

# Three common use cases are:
# 
# axes = 0 : tensor product
# axes = 1 : tensor dot product
# axes = 2 : (default) tensor double contraction

# In[3]:


A = np.array([[1,3], [4,2]])
B = np.array([[2,1], [5,4]])

print(A)
print(B)


# In[4]:


np.tensordot(A, B, axes=0)


# In[5]:


np.tensordot(A, B, axes=1)


# In[22]:


np.tensordot(A, B, axes=2)

