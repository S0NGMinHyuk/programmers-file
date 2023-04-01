def solution(X, Y):
    # X, Y 의 각 숫자 개수를 정리할 리스트 생성
    x = [0] * 10 ; y = [0] * 10

    # X, Y 의 각 숫자 개수를 정리
    x = counting(X, x)
    y = counting(Y, y)
    
    answer = ""
    num = "0123456789"
    index = 0
    # 각 인덱스의 최소 개수만큼 answer 에 추가 (0일 경우 추가 안됨)
    for a, b in zip(x, y):
        if a <= b:
            answer += num[index] * a
        else:
            answer += num[index] * b
        index += 1
    
    # 값 return 전 answer 정제 밑 예외처리
    if answer:
        answer = answer[::-1]
        if answer[0] != "0":
            return answer
        else: 
            return "0"  # answer가  "00" 같은 경우
    else:
        return "-1"     # answer가 빈 문자열일 경우


# 문자열 a의 각 숫자 개수를 리스트 l에 정리하는 함수
def counting(a, l):
    num = "0123456789"
    index = 0 ; cnt = 0
    a = sorted(a)
    for i in a:
        if i == num[index]:
            cnt += 1
        else:
            l[index] = cnt
            index = int(i) # 단순히 index += 1 하면 안된다.
            cnt = 1
    else:
        l[index] = cnt
    return l
