def solution(rows, columns, queries):
    answer = [] # 정답용 리스트

    # rows*colums 2차원 리스트 만들기
    minimap = []
    temp = []
    for i in range(1, rows*columns +1):
        temp.append(i)
        if len(temp) == columns:
            minimap.append(temp)
            temp = []

    # 행렬 회전
    for grid in queries:
        x1, x2, y1, y2 = grid[0] -1, grid[1] -1, grid[2] -1, grid[3] -1 # 인덱스 번호로 다뤄야 하기에 1씩 감소
        a, b = x1, x2 # 타겟으로 할 a, b에 시작값 x1, x2 저장

        move = [minimap[x1+1][x2]] # 이동할 숫자들이 저장될 리스트 move, 첫 번째 경우를 위해 미리 minimap[x1+1][x2] 값 저장

        for _ in range((y1 +y2 -x1 -x2) *2): # 반복 횟수는 항상 (y1+y2-x1-x2)*2 만큼 반복하기 때문에 for문 사용
            move.append(minimap[a][b]) # move에 현재 a, b 인덱스의 값 추가
            minimap[a][b] = move[-2]

            # a, b 이동 (시계방향 기준으로 오른쪽, 아래, 왼쪽, 위 방향으로 이동시킬 계획)
            if a == y1 and b == x2: # 마지막 경우, a가 y1이고 b가 x2일 때 a를 감소
                a -= 1
                y1 -= 1 # y1을 같이 감소시켜야 계속 마지막 경우를 처리할 수 있음.
            elif a < y1 and b < y2: # 첫 번째 경우, b를 증가
                b += 1
            elif a < y1 and b == y2: # 두 번째 경우, a를 증가
                a += 1
            elif a == y1 and b > x2: # 세 번째 겨우, a가 y1과 같은 값일 때 b가 x2가 될 때까지 b를 감소
                b -= 1

        answer.append(min(move)) # answer에 move의 최솟값 추가

    return answer

q = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(6, 6, q)) # 정답 [8, 10, 25]