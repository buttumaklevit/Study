#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(array, commands):
    answer = []
    i = commands[0][0]
    j = commands[0][1]
    array[i,j]
    for com in commands:
        
    return answer


# In[9]:


answer = []
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
for com in range(len(commands)):
    i = commands[com][0]
    j = commands[com][1]
    k = commands[com][2]
    a = sorted(array[i-1:j])
    answer.append(a[k-1])
print(answer)

