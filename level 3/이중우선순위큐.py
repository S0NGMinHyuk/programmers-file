def solution(operations):
    from heapq import heappush, heappop
    big = [] ; small = [] ; cnt = 0     # 내림차순 힙, 오름차순 힙, 힙 내 원소 개수

    for op in operations:
        if op == "D 1":     # 최대 힙에서 제거, cnt 1 감소
            if cnt > 0:
                cnt -= 1
                heappop(big)
        elif op == "D -1":  # 최소 힙에서 제거, cnt 1 감소
            if cnt > 0:
                cnt -= 1
                heappop(small)
        else:
            n = int(op[2:]) # 최대, 최소 힙에 n 추가
            heappush(big, -n)
            heappush(small, n)
            cnt += 1
        
        if cnt == 0:        # cnt가 0일 경우 big, small 모두 초기화
            big = [] ; small = []

    return [-big[0], small[0]] if cnt else [0, 0]
    # cnt가 양수일 경우 [최대값, 최소값] 리턴, cnt가 0일 경우 [0, 0] 리턴
