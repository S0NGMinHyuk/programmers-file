def solution(dirs):
    point = [0, 0] ; move = [0, 0] ; history = []
    # point = 현재 위치, move = 이동할 위치, history = 방문했던 길
    for way in dirs:
        if way == 'U':
            if point[1] < 5: # 현재 위치에서 이동이 가능한지 검사
                move[1] += 1 # 이동
                road = sorted([tuple(point), tuple(move)]) 
                # road 의 값이 변하는 것을 막고자 point 와 move 를 tuple 로 바꿔서 추가
                # 방향성 없이 갔던 길을 체크해야 하기에 현 위치와 갈 위치를 sort 해 추가
                if road not in history:
                    history.append(road)
                point = list(move)
                # road 가 history 에 없으면 처음 간 길이므로 history 에 추가
                # point(현 위치)를 move(이동한 위치)로 변경
        elif way == 'D':
            if point[1] > -5:
                move[1] -= 1
                road = sorted([tuple(point), tuple(move)])
                if road not in history:
                    history.append(road)
                point = list(move)
                # 위와 동일한 방식
        elif way == 'R':
            if point[0] < 5:
                move[0] += 1
                road = sorted([tuple(point), tuple(move)])
                if road not in history:
                    history.append(road)
                point = list(move)
                # 위와 동일한 방식
        else: # way == 'L' 일 경우
            if point[0] > -5:
                move[0] -= 1
                road = sorted([tuple(point), tuple(move)])
                if road not in history:
                    history.append(road)
                point = list(move)
                # 위와 동일한 방식
    return len(history)

# 테스트케이스, 정답 = 1
dirs = "UDU"
print(solution(dirs))