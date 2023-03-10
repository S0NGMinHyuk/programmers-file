def check3(n):         # 3의 배수, 3 유무 확인 함수 (있으면 False 반환)
    if n % 3 == 0:
        return False
    a = list(str(n))
    for i in a:
        if int(i) == 3:
            return False
    return True


def solution(n):
    answer = 0
    for i in range(1, n+1):
        answer += 1
        while check3(answer) == False:
            answer += 1        

    return answer
