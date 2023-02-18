def solution(n):
    a, b = divmod(n, 7)
    if b:
        return a + 1
    else:
        return a
