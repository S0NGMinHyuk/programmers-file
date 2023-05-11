def solution(x, y, n):  # BFS 알고리즘 풀이
    from collections import deque
    queue = deque([[y, 0]])

    while queue:    # y 값에서 x 값으로 내려가며 탐색
        y, cnt = queue.popleft()
        if y == x: return cnt

        for i in range(3):  # 2로 나누는 경우, 3으로 나누는 경우, n을 빼는 경우 3가지 탐색
            if i == 0 and (y/2)%1 == 0 and y//2 >= x:   # 나누는 경우, 나눠진 값이 정수가 아니면 스킵
                queue.append([y//2, cnt+1])
            elif i == 1 and (y/3)%1 == 0 and y//3 >= x:
                queue.append([y//3, cnt+1])
            elif i == 2 and y-n >= x:
                queue.append([y-n, cnt+1])
    
    return -1   # while 문을 탈출하는 경우 = x를 y로 변경하지 못하는 경우
