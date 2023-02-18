def solution(strlist):
    answer = [None] * len(strlist)
    i = 0
    for s in strlist:
        answer[i] = len(s)
        i += 1
    return answer
