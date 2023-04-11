def solution(storey):
    cnt = 0
    while storey:
        storey, rest = divmod(storey, 10)

        if rest >= 6:
            cnt += 10 - rest ; storey += 1 
        elif rest <= 4:
            cnt += rest
        else: # rest == 5
            # 앞의 자리 값이 5 이상일 경우
            if storey % 10 >= 5:
                cnt += rest ; storey += 1
            else:
                cnt += rest
    
    return cnt
