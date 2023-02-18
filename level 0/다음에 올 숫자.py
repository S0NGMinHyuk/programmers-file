def solution(common):
    answer = common[-1]
    if common[1] * 2 == common[0] + common[2]:   # 등차수열일 경우
        answer += common[1] - common[0]
    else:                                        # 등비수열일 경우
        answer *= common[1] // common[0]
    return answer
