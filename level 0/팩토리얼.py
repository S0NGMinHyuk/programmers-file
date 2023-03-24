def solution(n):
    num = 1 ; a = 1
    while 1:
        num = num * a
        if num <= n:
            a += 1
        else:
            return a - 1
