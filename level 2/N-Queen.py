def solution(n):
    answer = 0
    row = 0

    for i in range(n):
        stack = [[row, i]]                  # 맨 윗줄 퀸 배치
        answer += put_q(n, stack, row+1, 0) # 맨 윗줄 퀸의 배치에 따른 만족 경우의 수 추가
        
    return answer


def put_q(n, stack, row, answer):
    if len(stack) == n: # 재귀함수 종료조건 (퀸이 모두 배치되었을 때)
        return answer + 1
    
    for i in range(n):
        for before in stack:    # 기존 퀸의 공격범위에 들어갈 경우 break
            if before[1] == i or row-before[0] == abs(i - before[1]):
                break
        else:   # 공격받지 않는 경우 stack에 추가 후 재귀 반복
            answer = put_q(n, stack+[[row, i]], row+1, answer)

    return answer   # 함수 종료 시 answer 반환
