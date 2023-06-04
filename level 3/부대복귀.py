def solution(n, roads, sources, destination):   # 다익스트라 알고리즘 풀이
    graph = [[] for _ in range(n+1)]    # 지역별로 이어진 지역 정보가 담긴 리스트 생성
    for a, b in roads:
        graph[a].append(b) ; graph[b].append(a)
    
    time = [-1] * (n+1)     # 각 지역에서 destination까지 최소시간 리스트
    time[destination] = 0   # destination은 0으로 변경

    from collections import deque   # 큐 라이브러리 사용

    q = deque([destination])    # destination에서부터 이어진 지역의 최소 시간 찾기
    while q:
        now = q.popleft()       # now = 현재 지역
        for i in graph[now]:    # 현재 지역에서 이어진 지역 최소시간을 "현재 지역 최소시간 +1"로 변경 후 q에 추가
            if (time[i] == -1) or (time[i] > time[now]+1):
                time[i] = time[now]+1
                q.append(i)

    return [time[i] for i in sources]   # sources 지역의 최소시간 리턴
