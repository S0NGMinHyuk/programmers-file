def solution(n):
    dict = { 1 : 1, 2 : 2 } 
    for i in range(3, n+1):
        dict[i] = (dict[i-1] + dict[i-2]) % 1000000007
    return dict[n]


def solution(n):
    a, b = 1, 1
    for _ in range(1, n):
        a, b = b, (a+b) % 1000000007
    return b
