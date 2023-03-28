def solution(keymap, targets):
    board = {}
    # 각 알파벳의 최소 클릭 수 지정
    for k in keymap:
        for i, a in enumerate(k):
            if a not in board:
                board[a] = i + 1
            else:
                if board[a] > i + 1:
                    board[a] = i + 1
    
    result = []
    for t in targets:
        cnt = 0
        # 알파벳의 최소 클릭 수 덧셈, 없다면 -1로 종료 
        for w in t:
            if w in board.keys():
                cnt += board[w]
            else:
                result.append(-1)
                break
        else:
            result.append(cnt)
            
    return result
