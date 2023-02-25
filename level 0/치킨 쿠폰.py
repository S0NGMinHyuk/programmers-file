def solution(chicken):
    t = chicken ; c = 0
    while t >= 10:
        temp = t // 10
        c += temp
        t = t % 10 + temp
    return c
