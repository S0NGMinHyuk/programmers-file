def solution(cards1, cards2, goal):
    # 인덱스 에러 방지를 위해 더미 요소 추가
    cards1.append("")
    cards2.append("")
    
    # 각 카드더미의 인덱스 변수
    c1, c2 = 0, 0

    for w in goal:
        if cards1[c1] == w:
            c1 += 1
        elif cards2[c2] == w:
            c2 += 1
        else:
            return "No"
    return "Yes"
