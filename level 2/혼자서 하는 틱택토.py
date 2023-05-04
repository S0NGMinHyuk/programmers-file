def solution(board):
    o_cnt, o_win = check_eng("O", board)
    x_cnt, x_win = check_eng("X", board)

    # 정상 틱택토 경우의 수
    if o_win and not x_win and o_cnt - x_cnt == 1:
        return 1
    elif x_win and not o_win and o_cnt - x_cnt == 0:
        return 1
    elif not x_win and not o_win and 0 <= o_cnt - x_cnt <= 1:
        return 1
    
    return 0


# a가 몇 번 뒀는지, 이겼는지 리턴
def check_eng(a, board):
    cnt = 0                  # a의 개수
    for i in range(3):
        for j in range(3):
            if board[i][j] == a:
                cnt += 1
    win = False             # a가 이겼는지 졌는지 확인
    if cnt >= 3:
        if (board[0][0] == board[1][0] == board[2][0] == a      # 세로빙고
            or board[0][1] == board[1][1] == board[2][1] == a
            or board[0][2] == board[1][2] == board[2][2] == a
            or board[0][0] == board[0][1] == board[0][2] == a   # 가로빙고
            or board[1][0] == board[1][1] == board[1][2] == a
            or board[2][0] == board[2][1] == board[2][2] == a 
            or board[0][0] == board[1][1] == board[2][2] == a   # 대각선빙고
            or board[0][2] == board[1][1] == board[2][0] == a):
            win = True

    return cnt, win
