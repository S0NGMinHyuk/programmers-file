def solution(bin1, bin2):
    b = list(reversed([int(i) for i in list(str(int(bin1) + int(bin2)))])) + [0]

    for i, n in enumerate(b): # 2진수 계산
        if n >= 2:
            b[i], b[i+1] = n % 2, b[i+1] + 1
            
    if b[-1] == 0:
        b.pop()
        
    for i in range(len(b)):
        b[i] = str(b[i])

    return "".join(reversed(b))
