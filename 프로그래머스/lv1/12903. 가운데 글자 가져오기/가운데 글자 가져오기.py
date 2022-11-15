def solution(s):
    N = len(s)//2
    if len(s)%2:
        answer = (s[N])
    else:
        answer = (s[N-1:N+1])
    return answer