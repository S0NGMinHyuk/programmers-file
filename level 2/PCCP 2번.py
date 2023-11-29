def solution(land):
    # 각 위치마다 뽑을 수 있는 석유량
    answer = [0] * len(land[0])

    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1:                         # land 탐색하다가 석유칸 도착
                fuel, width, land = dig(land, i, j)     # 해당 석유칸과 이어진 석유칸 시추 
                answer = getAnswer(answer, width, fuel) # answer 리스트 업데이트

    return max(answer)


def dig(land, i, j):    
    width = set([j])    # 석유에 접근할 수 있는 위치(인덱스)
    fuel = 0            # 총 석유 매장량

    from collections import deque       # BFS 알고리즘 사용

    q = deque([[i, j]]) 
    while q:
        spot = q.popleft()
        if land[spot[0]][spot[1]] != 1: # 이미 시추한 경우 스킵
            continue

        land[spot[0]][spot[1]] = 2  # 현재 석유칸 시추 (2로 표시)
        fuel += 1                   # 총 석유 매장량 증가

        # 현재 석유칸의 상하좌우 탐색 후 석유칸이 있으면 q에 추가
        di, dj = [0, 1, 0, -1], [-1, 0, 1, 0]
        for n in range(4):
            if spot[0]+di[n] >= 0 and spot[0]+di[n] < len(land) and spot[1]+dj[n] >= 0 and spot[1]+dj[n] < len(land[0]) and land[spot[0]+di[n]][spot[1]+dj[n]] == 1:
                q.append([spot[0]+di[n], spot[1]+dj[n]])
                width.add(spot[1]+dj[n])
            else:
                None
    
    return fuel, width, land    # 총 석유 매장량, 접근 가능 인덱스, land 업데이트


def getAnswer(answer, width, fuel):
    for i in width:
        answer[i] += fuel
    return answer
