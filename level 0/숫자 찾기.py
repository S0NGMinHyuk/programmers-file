def solution(num, k):
    num, k = list(str(num)), str(k)
    if k in num:
        return num.index(k) + 1
    else:
        return -1
