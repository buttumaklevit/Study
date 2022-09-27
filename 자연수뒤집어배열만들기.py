#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.
입출력 예
n	return
12345	[5,4,3,2,1]
"""


# In[11]:


def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    return answer[::-1]
print(solution(12345))


# In[3]:


a=str(12345)
for i in a:
    answer.append(int(i))


# In[10]:


i=[1,2,3,4,5]
print(i[::-1])


# In[ ]:




