from itertools import combinations

def checkIncline(dA, dB):   # 기울기 반환 함수
    return (dB[1] - dA[1]) / (dB[0] - dA[0])


def solution(dots):
    order = list(combinations([0, 1, 2, 3], 2))
    index = 0

    while index < len(order):
        iA = order[index]
        iB = list(set([0, 1, 2, 3]) - set(iA))
        a = checkIncline(dots[iA[0]], dots[iA[1]])  
        b = checkIncline(dots[iB[0]], dots[iB[1]])
        if a == b:
            return 1
        else:
            index += 1
    return 0
