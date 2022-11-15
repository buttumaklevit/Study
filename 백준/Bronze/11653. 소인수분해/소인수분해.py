N = int(input())
n = 2
while n <= N:
    if N%n==0:
        print(n)
        N=N/n
    else:
        n+=1