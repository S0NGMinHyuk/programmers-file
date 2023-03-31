def solution(k, score):
    result = []
    h = []
    for s in score:
        h.append(s)
        h.sort(reverse=True)
        if len(h) > k:
            h.pop()
        result.append(h[-1])
    return result
