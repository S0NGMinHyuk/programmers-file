def solution(order):
    cnt = 0
    for i in [3, 6, 9]:
        if str(i) in str(order):
            cnt += str(order).count(str(i))
    return cnt
