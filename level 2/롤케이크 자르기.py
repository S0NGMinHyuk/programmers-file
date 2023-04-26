def solution(topping):
    ans = 0  # 정답 변수
    
    # cake 딕셔너리에 토핑 별 개수 저장
    cake = dict()
    for t in topping:
        cake[t] = cake[t] + 1 if t in cake else 1

    # cut 딕셔너리에 토핑 별 개수 저장
    cut = dict()
    for t in topping:
        cut[t] = cut[t] + 1 if t in cut else 1

        # cut에 있는 토핑만큼 cake에서 감소
        # 토핑 수가 0이 되면 토핑(키) 제거
        cake[t] -= 1
        if cake[t] == 0:
            del cake[t]
        
        # cut과 cake의 토핑 수가 같은 경우
        if len(cut) == len(cake):
            ans += 1
    
    return ans
