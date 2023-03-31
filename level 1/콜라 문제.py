def solution(a, b, n):
    answer = 0
    while n >= a:
        get, rest = divmod(n, a)
        answer += get * b
        n = get * b + rest
    return answer
