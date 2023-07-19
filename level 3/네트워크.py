def solution(n, computers):
    # 각 컴퓨터마다 연결된 컴퓨터 리스트를 가진 딕셔너리 생성
    info = {}
    for i, computer in enumerate(computers):
        temp = []
        for j in range(n):
            if computer[j] == 1: 
                temp.append(j)
        info[i] = temp

    # 연결된 컴퓨터 리스트 , 연결된 네트워크 개수
    visit = [] ; answer = 1

    # i가 연결된 컴퓨터 리스트에 없다면 i와 연결된 컴퓨터 리스트를 구하고 visit에 추가
    # 추가한 후 visit 리스트의 길이가 n이라면 answer 리턴
    for i in range(n):
        if i not in visit:
            result = checkLink(i, info)
            visit = visit + result

            if len(visit) == n:
                break
            else:
                answer += 1

    return answer


# i와 연결된 컴퓨터 리스트 생성 함수
def checkLink(i, info):
    # deque 라이브러리 사용
    from collections import deque
    
    q = deque([i])  # 탐색할 컴퓨터 리스트
    visit = [i]     # 연결된 컴퓨터 리스트

    while q:
        # idx와 연결된 컴퓨터 리스트를 q와 visit에 추가
        for idx in info[q.popleft()]:
            if idx not in visit:
                visit.append(idx)
                q.append(idx)
    
    return visit



n, computers = 3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
