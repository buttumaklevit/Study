def solution(my_str, n):
    answer = []

    while my_str:
        if len(my_str)>=n:
            answer.append(my_str[:n])
            my_str=my_str[n:]
        elif len(my_str)<n:
            answer.append(my_str)
            my_str=[]
    return answer