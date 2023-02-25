def solution(score):
    aver = [None] * len(score)      # 평균값 리스트 생성    
    for i in range(len(score)):
        aver[i] = sum(score[i]) / 2
    
    answer = [None] * len(score)    
    big = max(aver) ; rank = 1 ; mult = 0
    
    while big >= 0:
        i = aver.index(big)
        answer[i] = rank ; aver[i] = -1
        temp = max(aver)
        
        if temp == big:
            mult += 1
        else:
            rank += 1 + mult
            mult = 0
            big = temp
            
    return answer
