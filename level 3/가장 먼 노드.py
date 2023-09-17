def solution(n, vertex):
    dst = [0] * n   # 거리별 노드 개수
    visited = set() # 방문 여부 확인, 세트로 생성 시 시간복잡도 O(1)

    maps = {}
    for i in range(n+1):    # maps 딕셔너리에 각 노드별 연결된 노드 리스트와 1번 노드까지 거리 저장
        maps[i] = [[], n + 10]  # n보다 더 큰 값 아무거나 지정
    else:
        maps[1][1] = 0      # 1번 노드 거리는 0으로 변경

    for a, b in vertex:     # 각 노드별 연결된 노드 추가
        maps[a][0].append(b)
        maps[b][0].append(a)
    
    from collections import deque   # BFS 알고리즘 사용

    # 1번 노드부터 탐색하며 각 노드와 1번 노드 사이의 거리 업데이트
    queue = deque([1])
    while queue:    
        nod = queue.popleft()

        if nod in visited:  # 이미 방문했던 노드 skip
            continue

        queue += maps[nod][0]
        
        for i in maps[nod][0]:  # 거리 업데이트
            if maps[nod][1]+1 < maps[i][1]:
                maps[i][1] = maps[nod][1]+1
                dst[maps[nod][1]+1] += 1

        visited.add(nod)    # 방문했던 노드 업데이트

    for i in range(len(dst)-1, 0, -1):
        if dst[i]: return dst[i]    # 가장 먼 거리 리턴


n, vertex = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
