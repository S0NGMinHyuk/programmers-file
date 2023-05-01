# 각 방의 거리두기 여부를 리턴
def solution(places):
    ans = [0]*5
    for i, place in enumerate(places):
        ans[i] = check_place(place)
    return ans


# 방의 거리두기 여부를 판단 (지키면 1, 안지키면 0 리턴)
def check_place(place):
    idx = get_P_index(place)   # 방 내부 응시자(P)의 인덱스 리스트

    for i in range(len(idx)):
        for j in range(i+1, len(idx)):
            distance = get_distance(idx[i], idx[j])   # 응시자 사이 맨해튼 거리값

            if distance <= 2:               # 거리두기를 지키지 않고 있으면 0 리턴
                if distance == 1 or check_mans(idx[i], idx[j], place) == 0:
                    return 0
    
    return 1    # 모두가 거리두기를 지키고 있으면 1 리턴


# 방 내부 응시자(P)의 인덱스가 담긴 리스트 리턴
def get_P_index(place):
    idx = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                idx.append([i, j])
    return idx


# a, b 두 사람의 맨해튼 거리 리턴
def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# 맨해튼 거리가 2일 때 a, b 두 사람 사이 테이블 여부 판단 (있으면 0, 없으면 1 리턴)
def check_mans(a, b, place):
    if a[0] - b[0] == 0:    # 두 사람이 세로로 앉은 경우
        if place[a[0]][(a[1] + b[1]) // 2] == "O":
            return 0
    elif a[1] - b[1] == 0:  # 두 사람이 가로로 앉은 경우
        if place[(a[0] + b[0]) // 2][a[1]] == "O":
            return 0
    else:                   # 두 사람이 대각선으로 앉은 경우
        if place[a[0]][b[1]] == "O" or place[b[0]][a[1]] == "O":
            return 0

    return 1    # 두 사람 사이 파티션이 있는 경우
