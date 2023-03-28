def solution(t, p):
    lp = len(p)
    cnt = 0

    for i in range(len(t) + 1 - lp):
        # 문자열 상태에서 숫자 비교 가능
        if t[i:i+lp] <= p:
            cnt += 1
            
    return cnt
