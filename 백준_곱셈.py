# -*- coding: utf-8 -*-
"""백준 곱셈.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CxsMhlXt-89lQsl8GWv7YVm_oSJtNMwo
"""



A = int("472")
B = "385"
C = []
for b in B:
    C.append(A*int(b))
C = C[::-1]
print(C[0])
print(C[1])
print(C[2])
print(C[0]+C[1]*10+C[2]*100)