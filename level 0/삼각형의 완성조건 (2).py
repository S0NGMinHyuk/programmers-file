def solution(sides):
    long = sides[0] ; short = sides[1]
    if long < short:
        long, short = short, long

    cnt = short - 1                 # 나머지 한 변이 가장 긴 변인 경우
    for i in range(long, 0, -1):    # long이 가장 긴 변인 경우
        if short + i > long:
            cnt += 1
        else:
            break
    
    return cnt
