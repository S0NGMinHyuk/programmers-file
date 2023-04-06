def solution(players, callings):
    # 선수별 순위 정보 딕셔너리 생성
    dic = {}
    for i, p in enumerate(players):
        dic[p] = i

    # dic에서 인덱스를 바로 찾고, dic와 players에서 앞의 선수와 값 변경
    for c in callings:
        i = dic[c]
        dic[c], dic[players[i -1]] = dic[players[i -1]], dic[c]
        players[i], players[i - 1] = players[i - 1], players[i]
        
    return players
