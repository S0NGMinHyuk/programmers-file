def solution(i, j, k):
    a = "".join([str(i) for i in range(i, j+1)])
    return a.count(str(k))
