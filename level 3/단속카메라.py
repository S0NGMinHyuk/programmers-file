def solution(routes):      # 탐욕 알고리즘 사용
    cameras = 0            # 필요한 카메라 개수
    routes.sort()          # 차량을 오름차순으로 정렬
    s, e = routes.pop(0)   # 가장 먼저 진입한 차량의 진입/진출 지점

    for car in routes:
        if car[0] <= e:    # 다음 차량의 진입이 진출 지점 이내일 경우
            e = car[1] if car[1] < e else e
        else:              # 다음 차량의 진입이 진출 지점 이후일 경우
            cameras += 1
            s, e = car
    
    return cameras + 1     # 마지막 차량 단속용 카메라 한 대 추가
