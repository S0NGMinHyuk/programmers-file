import heapq                  # heapq 모듈 사용

def solution(scoville, k):
    heapq.heapify(scoville)   # 기존 리스트를 힙으로 변환 (sort를 해주는 건 아니다)
    
    mix = 0                   # 섞는 횟수 카운트
    while scoville[0] < k:    # 스코빌의 최소값이 k보다 크면 mix 리턴
        try:                  # 섞기
            heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        except:               # 스코빌에 값이 1개밖에 없고 k 보다 작다면 
            return -1         # 만들 수 없는 경우이므로 -1 리턴

        mix += 1              # 섞은 횟수 1 증가

    return mix


s = [1, 5, 4, 3, 2]
k = 7
print(solution(s, k))# 정답 2