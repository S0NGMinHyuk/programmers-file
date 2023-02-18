def solution(dot):
    l = [1, 4] if dot[0] > 0 else [2, 3]
    answer = l[0] if dot[1] > 0 else l[1]
    return answer
