# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-gMwL7jQrZAILwVbr8r0dP1QeC7WfBjn
"""

T = int(input())
for i in range(1,len(T)+1):
  A, B = map(int,input().split())
  print("Case #{}: {} + {} = {}".format(i, A, B, A+B))