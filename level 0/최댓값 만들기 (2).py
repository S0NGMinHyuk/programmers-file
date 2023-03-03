def solution(numbers):
    n = sorted(numbers)
    a = n[0] * n[1]
    b = n[-1] * n[-2]
    return a if a > b else b
