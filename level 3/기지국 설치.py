def solution(n, stations, w):
    answer = 0

    front = 0
    stations.append(n+1)    # 마지막 기지국 이후의 아파트 개수를 알기 위해 값 추가

    # gap = 기지국 사이 아파트 개수
    for i, station in enumerate(stations):
        gap = station - front - 1
        front = station

        # gap을 전파가 닿지 않는 아파트 개수로 변경
        if i == 0 or i == len(stations) - 1:
            gap -= w
        else:
            gap -= w*2
        
        # gap 범위를 커버하기 위해 필요한 회소한의 기지국 개수를 answer에 추가
        if gap > 0:
            a, b = divmod(gap, w*2 + 1)
            if b:
                answer += a + 1
            else:
                answer += a

    return answer
