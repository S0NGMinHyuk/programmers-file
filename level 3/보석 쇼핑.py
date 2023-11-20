def solution(gems):
    # 투포인터 알고리즘
    answer = []

    data = {}       # 현재 포함하는 보석 개수를 세기 위한 딕셔너리
    for gem in set(gems):
        data[gem] = 0
    n = len(data)

    s, e, cnt = 0, -1, 0
    while e < len(gems):
        if cnt < n:                 # 모든 보석을 포함하지 못한 경우, e 증가 (보석 추가)
            e += 1
            if e == len(gems):          # gems의 끝을 넘었다면 answer 리턴
                return answer
            data[gems[e]] += 1
            if data[gems[e]] == 1:      # 포함하지 않던 보석일 경우 cnt 증가
                cnt += 1
        else:                       # 모든 보석을 포함할 경우, answer 조건에 맞게 변경
            if answer == [] or (e-s < answer[1]-answer[0]):
                answer = [s+1, e+1]
            data[gems[s]] -= 1          # 최소한의 보석만 포함하기 위해 가장 먼저 담은 보석 빼기
            if data[gems[s]] == 0:      # 빠진 보석을 포함하고 있지 않을 경우 cnt 감소
                cnt -= 1
            s += 1
        
    return answer
