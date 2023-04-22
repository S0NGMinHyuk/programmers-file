def solution(n, k, enemy):
    # 힙 모듈 사용
    import heapq as hq
    heap = []

    # 차례대로 적을 상대하기
    for i, e in enumerate(enemy):
        n -= e
        hq.heappush(heap, (e * -1))

        # 병사 수가 부족한 경우
        if n < 0:
            if k:   # 그동안 상대했던 적 중 가장 큰 적에게 무적권 사용 후 병사 수 증가
                k -= 1
                n -= hq.heappop(heap)
            else:   # 무적권이 없으면 리턴
                return i
            
    else:           # 모든 적을 상대한 경우
        return len(enemy)
