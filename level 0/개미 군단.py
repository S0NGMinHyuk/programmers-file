def solution(hp):
    ant = hp // 5   # 장군개미 수
    hp = hp % 5
    
    if hp >= 3:
        ant += 1    # 병정개미 수 추가
        hp -= 3     # 일개미 수
    
    return ant + hp
