def solution(n, s):
    if n > s or (n%2 == 1 and s%2 == 0):    # 최고의 집합 불가 조건 
        answer = [-1]
    else:   # 최고의 집합 생성
        rest = s % n
        s -= rest
        answer = [s//n for _ in range(n)]
        while rest > 0:
            answer[-rest] += 1
            rest -= 1

    return answer
