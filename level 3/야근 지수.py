def solution(n, works):
    # 남은 작업량이 남은 근무시간보다 적은 경우 0 리턴
    if sum(works) <= n: return 0

    # 힙 모듈 사용
    from heapq import heappush, heappop

    # works의 값을 음수로 변경해 최대힙 생성
    heap = []
    for w in works:
        heappush(heap, -w)
    
    # n번동안 최대값을 1 줄이기
    for _ in range(n):
        heappush(heap, heappop(heap)+1)

    # 근무시간동안 줄이고 남은 값의 제곱을 모두 더하기
    answer = 0
    for num in heap:
        answer += num**2

    return answer


works, n = [10, 5, 7], 7
print(solution(n, works))
