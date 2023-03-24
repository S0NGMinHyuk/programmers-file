def findPrime(n):
    if n < 4:
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False

    return True
        


def solution(n):
    cnt = 0
    for i in range(4, n + 1):
        if findPrime(i) == False:
            cnt += 1
    return cnt
