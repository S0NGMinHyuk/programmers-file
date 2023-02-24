def solution(before, after):
    a, b = sorted(after), sorted(before)
    return 1 if a == b else 0
