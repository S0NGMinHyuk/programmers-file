import math as m
def solution(n):      # 내 풀이
    if n % 10 not in [2, 3, 7, 8]:
        a = int(m.sqrt(n))
        if a*a == n:
            return 1
        else:
            return 2
    else:
        return 2


def solution(n):      # 다른사람의 풀이
    if n**0.5 == int(n**0.5):
        return 1
    else:
        return 2
