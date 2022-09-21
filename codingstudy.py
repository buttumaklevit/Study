# 1일차 짝수와 홀수
# 나의 답안
def solution(num):
    answer=""
    if num%2==0:
        answer="Even"
    elif num%2==1:
        answer="Odd"
    else:
        answer="Even"
    return answer

# 다른 사람 답안 참고할만 한 것
def evenOrOdd():
    if (num%2):
        return "Odd"
    else:
        return "Even"
    # 0=False 1=True 라는 특징을 활용해서 홀짝을 구분

def evenOrOdd():
    return ["Even","Odd"][num&1]
    # 비트연산자를 활용해서 리스트의 인덱스의 값을 출력

def solution(num):
    return["Even","Odd"].pop(num%2)
    #pop()함수를 활용