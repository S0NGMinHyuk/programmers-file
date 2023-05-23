def solution(m, n, board):
    ans = 0
    board = [list(board[i]) for i in range(m)]  # 값 변경을 위해 2차원 리스트로 변경
    while 1:
        board, cnt = change_board(m, n, board)  # 사라지는 블록 체크 
        if cnt: # 사라지는 블록이 있다면 ans에 개수 추가
            ans += cnt
        else:   # 더이상 사라지는 블록이 없다면 ans 리턴
            return ans


def change_board(m, n, board):  # 보드 변경 함수
    blocks = [] # 사라지는 블록 인덱스 리스트
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] != "0" and (board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]):
                blocks = add_idx(blocks, i, j)  # blocks에 2×2 형태 블록 인덱스 추가

    board = refresh(m, n, board, blocks)    # blocks에 따라 board 갱신

    return board, len(blocks)   # 갱신된 board와 사라지는 블록 개수 리턴


def add_idx(blocks, i, j):  # blocks 리스트에 중복값이 없도록 추가하는 함수
    for a in range(i, i+2):
        for b in range(j, j+2):
            if (a, b) not in blocks:
                blocks.append((a, b))
    return blocks


def refresh(m, n, board, blocks):
    for i, j in blocks: # 사라지는 블록값을 "0"으로 변경
        board[i][j] = "0"

    for j in range(n):  # 각 열마다 가장 아래 행부터 올라오며 "0" 값을 가장 처음 만나는 알파벳과 변경
        for i in range(m-1, -1, -1):
            idx = 1

            if board[i][j] == "0":
                while board[i-idx][j] == "0":   # 가장 처음 나오는 알파벳의 인덱스 찾기
                    idx += 1
                    if idx > m:
                        break
                
                if i-idx >= 0:
                    board[i][j], board[i-idx][j] = board[i-idx][j], board[i][j] # "0"과 알파벳 자리 변경 (알파벳 내리기)
    
    return board
