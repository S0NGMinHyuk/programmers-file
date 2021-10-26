import itertools

def solution(k, dungeons):          # 무지성 완전탐색
    # 던전을 도는 모든 경우의 수가 담긴 리스트 생성
    orders = list(itertools.permutations(dungeons, len(dungeons)))
    answer = 0

    for order in orders:            # order = 던전을 도는 경우의 수 중 하나
        mana = k ; cnt = 0          # mana = 현재 피로도, cnt = 탐험한 던전 수
        for work in order:  
            if mana >= work[0]:     # 현재 피로도가 필요 피로도보다 크거나 같으면
                mana -= work[1]     # 현재 피로도가 소모 피로도만큼 감소
                cnt += 1
            else:                   # 현재 피로도가 필요 피로도보다 작으면 반복문 탈출
                break

        if cnt > answer:            # cnt 값이 더 크면 answer 값 변경
            answer = cnt

    return answer


dungeons = [[80,20],[50,40],[30,10]]
k = 80
print(solution(k, dungeons))    # 정답 3