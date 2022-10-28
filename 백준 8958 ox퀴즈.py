#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = 5
A = ["OOXXOXXOOO",
"OOXXOOXXOO",
"OXOXOXOXOXOXOX",
"OOOOOOOOOO",
"OOOOXOOOOXOOOOX"]


# In[2]:


for a in A:
    cnt=0
    answer=0
    for aa in a:
        if aa=="O":
            cnt+=1
        else:
            cnt=0
        answer+=cnt
    print(answer)


# In[ ]:


N = int(input())
nl = [input() for _ in range(N)]
for n in nl:
    cnt=0
    answer=0
    for aa in n:
        if aa=="O":
            cnt+=1
        else:
            cnt=0
        answer+=cnt
    print(answer)

