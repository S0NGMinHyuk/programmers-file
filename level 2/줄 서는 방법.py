def solution(n, k):
    from math import factorial 

    num = [i for i in range(1, n+1)]
    ans = []
    
    while k > 1:
        idx = 0
        f = factorial(len(num) - 1)
        while k > f:
            k -= f
            idx += 1
        ans.append(num.pop(idx))

    return ans + num
