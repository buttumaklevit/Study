#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 문제를 풀었지만 아래의 배열인 경우에는 1개만 제거되어서 오답으로 된다.
# 1을 모두 제거해야하는데 1개만 제거함
arr = [3,2,1,1,1]
def solution(arr):
    answer = []
    if len(arr) <= 1:
        answer.append(-1)
    else:
        a=min(arr)
        arr.pop(arr.index(min(arr)))
        for i in arr:
            answer.append(i)
    return answer

solution(arr)

