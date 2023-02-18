def solution(A, B):
    for i in range(0, len(A) + 1):
        if A == B:
            return i
        A = A[-1] + A[:-1]
    return -1
