while True:
    n = int(input())
    if n == -1:
        break
    A=[]
    for i in range(1,n+1):
        if n%i == 0:
            A.append(i)
    A = A[:-1]
    
    if n == sum(A):
        ans = f"{n} = "
        for a in A:
            ans+=str(a)
            ans+=" + "
        ans = ans.rstrip(" + ")
        print(ans)
        
    else:
        print(f'{n} is NOT perfect.')