#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
문제 설명
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

제한 사항
n은 1이상, 50000000000000 이하인 양의 정수입니다.
입출력 예
n	return
121	144
3	-1
입출력 예 설명
입출력 예#1
121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.

입출력 예#2
3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.
"""


# In[11]:


def solution(n):
    answer = 0
    for i in range(n):
        i=i+1
        if n%i==0:
            if i**2==n:
                return (i+1)**2
            else:
                continue
        else:
            continue
    return -1


# In[13]:


print(solution(3))


# In[18]:


def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'


# In[17]:


def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));


# In[20]:


def nextSqure(n):
    sqrt = pow(n, 0.5)
    return pow(sqrt + 1, 2) if sqrt == int(sqrt) else 'no'

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(nextSqure(121)));
    


# In[ ]:


import math
def solution(n):
    answer = 0
    tmp = int(math.sqrt(n))
    mul = tmp*tmp
    if mul == n:
        answer = (tmp+1)*(tmp+1)
    else:
        answer =-1
    return answer

