def solution(array, n):
    gap, answer = 100, 0
    for a in array:
        if abs(a - n) < gap:
            gap, answer = abs(a - n), a
        elif abs(a - n) == gap:
            answer = a if a < answer else answer
    return answer
