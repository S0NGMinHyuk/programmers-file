def solution(a, b):
    check = 1                               # 소인수분해
    while check:                            
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                a, b = a // i, b // i
                break
        check = 0
        
    a = 2                                   # b의 소인수가 2, 5만 있는지 체크
    while 1:
        if b % a == 0:
            b = b // a
        elif a == 2:
            a = 5
        elif b == 1:
            return 1
        else:
            return 2
    
