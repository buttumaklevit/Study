A, B = input().split()

A_r = ""
B_r = ""

for i in range(2,-1,-1):
    A_r += A[i]
    B_r += B[i]

A_r = int(A_r)
B_r = int(B_r)

if A_r > B_r:
    print(A_r)
else:
    print(B_r)