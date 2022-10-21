#!/usr/bin/env python
# coding: utf-8

# In[ ]:


A,B = map(int,input().split())

C = (A*60+B)-45
A = C//60
B = C%60
if A < 0:
    A = 23
print(A,B)

