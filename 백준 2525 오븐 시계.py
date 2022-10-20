#!/usr/bin/env python
# coding: utf-8

# In[2]:


A,B = map(int,input().split())
C = int(input())
S = A*60+B+C

a, b = S//60,S%60

if a >= 24:
    a = a - 24
print(a,b)

