def solution(N, road, K):
    graph = [[] for _ in range(N+1)]    # 마을 번호 = 인덱스 번호
    for a, b, t in road:                # 각 마을별로 리스트 자료형에 (이어진 마을, 이동 시간) 저장
        graph[a].append((b, t))
        graph[b].append((a, t))

    from heapq import heappop, heappush # 다익스트라 알고리즘 + 힙 알고리즘 사용

    heap = [(0, 1)]             # 최단거리 마을부터 계산하기 위해 힙 사용
    lst = [500001] * (N+1)      # 1번 마을에서부터 각 마을까지의 최소 배달 시간 리스트
    while heap: 
        time, now = heappop(heap)
        if time < lst[now]:     # 지금 마을까지 배달시간이 최소시간일 경우
            lst[now] = time     # lst 값 변경
            for next_town, next_time in graph[now]:     # 지금 마을에서 이어진 다른 마을을 heap에 추가
                heappush(heap, (time+next_time, next_town))
        else:
            None
    
    ans = 0 
    for i in range(1,N+1):      # K 시간 이내로 배달 가능한 마을 갯수 카운팅
        if lst[i] <= K:
            ans += 1
    
    return ans
