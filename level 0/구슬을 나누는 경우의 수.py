def factorial(n):
    a = 1
    for i in range(1, n+1):
        a = a*i
    return a

def solution(balls, share):
    return factorial(balls) // (factorial(share) * factorial(balls - share))
