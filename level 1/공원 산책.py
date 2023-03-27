def solution(park, routes):
    # 시작지점과 공원 좌우 길이 지정
    s = startPoint(park)
    h, w = len(park) - 1, len(park[0]) - 1
    direct = {
        "N" : (-1, 0),
        "S" : (1, 0),
        "E" : (0, 1), 
        "W" : (0, -1)
    }
    
    for r in routes:
        # route 동선에 따라 방향과 횟수 지정
        way, n = r.split()                        
        way = direct[way]
    
        # s 값 보존을 위해 temp 사용
        temp = list(s)
        
        for _ in range(int(n)):
            # 공원 범위를 벗어나지 않는 경우 이동
            if 0 <= temp[0] + way[0] <= h and 0 <= temp[1] + way[1] <= w:
                temp[0] += way[0] ; temp[1] += way[1]
                
                # 장애물을 만날 경우 반복문 탈출 (s 값 변화 없음)
                if park[temp[0]][temp[1]] == "X":
                    break
            # 공원 범위를 벗어나는 경우 반복문 탈출 (s 값 변화 없음)
            else: 
                break
        # 이동에 성공 시 s 값 변경
        else: 
            s = temp
    return s


# park 에서 s 위치 검색 함수
def startPoint(park):
    for i, p in enumerate(park):
        if "S" in p:
            return [i, p.index("S")]
