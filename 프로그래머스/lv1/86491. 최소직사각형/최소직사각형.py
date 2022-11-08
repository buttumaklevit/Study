def solution(sizes):
    A = []
    B = []
    for i in range(len(sizes)):
        sizes[i]=sorted(sizes[i])
        A.append(sizes[i][0])
        B.append(sizes[i][1])
        
    return max(A)*max(B)