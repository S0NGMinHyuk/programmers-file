def solution(s):
    answer = []
    dict = {}
    for i, alphabet in enumerate(s):
        if alphabet not in dict:
            answer.append(-1)
        else:
            answer.append(i - dict[alphabet])
        dict[alphabet] = i
    return answer
