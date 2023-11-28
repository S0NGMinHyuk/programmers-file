def solution(bandage, health, attacks):
    coolTime, heal, bonus = bandage
    maxHp = health

    previous = 0
    for time, damage in attacks:
        period = time - previous - 1    # 이전 공격과 지금 공격 사이 텀
        health += period*heal + bonus*(period//coolTime)    # period 만큼 체력 힐
        health = health if health < maxHp else maxHp        # 풀피 이상 회복하는 경우 풀피로 변경

        health -= damage
        if health <= 0:
            return -1
        
        previous = time
    
    return health
