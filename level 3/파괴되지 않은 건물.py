def solution(board, skill):     # 정확성 통과, 효율성 실패
    bldg = len(board)*len(board[0])
    for i in range(len(skill)):
        type, *location, degree = skill[i]
        if type == 1:
            for row in range(location[0], location[2]+1):
                for col in range(location[1], location[3]+1):
                    if board[row][col] > 0 and (board[row][col]-degree) <= 0:
                        bldg -= 1
                    board[row][col] -= degree
        else: # type == 2:
            for row in range(location[0], location[2]+1):
                for col in range(location[1], location[3]+1):
                    if board[row][col] <= 0 and (board[row][col]+degree) > 0:
                        bldg += 1
                    board[row][col] += degree
    return bldg

#_________________________________________________________________________________________________________________
import numpy as np  # 누적합 알고리즘 사용, 그러나 계속 효율성 실패

def make_degree(info, grid):    # skill별 누적합 2차원배열 생성 함수
    arr = grid.copy()
    # 누적합 초기값 설정
    arr[info[1]][info[2]], arr[info[3]+1][info[4]+1] = info[5], info[5]
    arr[info[1]][info[4]+1], arr[info[3]+1][info[2]] = -info[5], -info[5]

    # 행열 누적합 계산
    arr = arr.cumsum(axis=0)
    arr = arr.cumsum(axis=1)

    # 누적합 계산을 위해 만들어뒀던 잉여 행열 제거
    arr = np.delete(arr, -1, axis=0)
    arr = np.delete(arr, -1, axis=1)

    return arr  # 2차원 배열 리턴


def solution(board, skill):
    # 넘파이 배열로 변경
    board = np.array(board)
    grid = np.zeros((len(board)+1, len(board[0])+1))

    for info in skill:
        degree = make_degree(info, grid)
        
        if info[0] == 1:    # type에 따라 board 업데이트
            board = board - degree
        else:
            board = board + degree
    
    # board 내 양수값 개수 카운팅
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                cnt += 1
    
    return cnt

#_________________________________________________________________________________________________________________
def solution(board, skill):
    answer = 0

    # 누적합을 위한 2차원 배열 생성
    arr = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    # 각 skill별 누적합 초기값 설정
    for type, r1, c1, r2, c2, degree in skill:
        arr[r1][c1] += degree if type == 2 else -degree
        arr[r1][c2+1] += -degree if type == 2 else degree
        arr[r2+1][c1] += -degree if type == 2 else degree
        arr[r2+1][c2+1] += degree if type == 2 else -degree
    
    # skill별 누적합이 설정된 2차원 배열을 한꺼번에 누적합 계산 (이게 핵심)
    import numpy as np
    arr = np.array(arr)
    arr = arr.cumsum(axis=0)
    arr = arr.cumsum(axis=1)
    arr = np.delete(arr, -1, axis=0)
    arr = np.delete(arr, -1, axis=1)

    # board값에 누적합 업데이트
    board = np.array(board) + arr

    # board 내 양수값 개수 카운팅
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    
    return answer


board, skill = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]
print(solution(board, skill))
