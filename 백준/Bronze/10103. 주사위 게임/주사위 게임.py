n = int(input())
C = 100
S = 100

for _ in range(n):
    c,s = map(int, input().split())
    if c > s:
        S -= c
    elif c < s:
        C -= s
print(C)
print(S)