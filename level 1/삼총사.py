def solution(number):
    # 함수 안에서 모듈 호출 가능
    from itertools import combinations

    answer = 0
    for i in list(combinations(number, 3)):
        if sum(i) == 0:
            answer += 1
            
    return answer
