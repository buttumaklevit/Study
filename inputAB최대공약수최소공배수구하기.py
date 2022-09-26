#!/usr/bin/env python
# coding: utf-8

# In[9]:


def solution( n , m):
    answer=[]
    n_a = [i for i in range(1,n+1) if n%i==0] # n의 약수
    m_a = [i for i in range(1,m+1) if m%i==0] # m의 약수
    m_b = list(filter(lambda x : x > n, m_a)) # 공약수를 제외한 m의 약수
#     print(n_a)
#     print(m_a)
#     print(m_b)
    print()
    # 공약수 찾기
    list_A = [] # n과 m의 공약수
    for i in n_a:
        for j in m_a:
            if i == j:
                list_A.append(i)
    
    
    
    # 최대공약수
    answer.append(max(list_A))
    # 최소공배수
    answer.append(m*n//max(list_A))
#     if m%n==0:
#         answer.append(max(n_a)*min(m_b))
        
#     else:
#         answer.append(max(n_a)*min(m_b))
    return answer


# In[10]:


print(solution(3,12))
print()
print(solution(2,5))

