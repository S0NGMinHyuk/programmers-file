def solution(dots):
    a =  dots[0]
    for d in dots[1:]:
        if a[0] != d[0] and a[1] != d[1]:
            return abs((a[0] - d[0]) * (a[1] - d[1]))
