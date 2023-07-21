def solution(A, B):
    answer = 0

    A.sort() ; B.sort()
    aidx = 0 ; bidx = 0

    while bidx < len(B):
        if A[aidx] >= B[bidx]:
            bidx += 1
        else:
            aidx += 1
            bidx += 1
            answer += 1
    
    return answer
