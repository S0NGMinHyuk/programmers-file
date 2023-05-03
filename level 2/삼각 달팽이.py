def solution(n):
    # 2차원 리스트 생성
    road = []
    for i in range(1, n+1):
        road.append([0]*i)
    
    x, y = 0, 0                             # 값을 넣을 인덱스 위치
    direct = [[0, 1], [1, 0], [-1, -1]]     # 달팽이가 진행할 방향값
    idx = 0                                 # direct 인덱스
    lap = 1                                 # 달팽이가 360도 돈 바퀴 수
    for i in range(1, (n*(n+1))//2 +1):
        road[y][x] = i 
        # 달팽이가 진행 방향을 바꾸는 경우
        if (idx % 3 == 0) and (y == n - lap): 
            idx += 1
        elif (idx % 3 == 1) and (x == y - lap + 1): 
            idx += 1
        elif (idx % 3 == 2) and (road[y-1][x-1] != 0):
            idx += 1
            lap += 1
        
        # 달팽이의 다음 인덱스 위치
        dx, dy = direct[idx % 3]
        x += dx ; y += dy

    # 2차원 리스트를 1차원으로 변경
    return sum(road, [])
