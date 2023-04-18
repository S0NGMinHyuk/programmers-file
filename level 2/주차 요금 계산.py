def solution(fees, records):
    # records 리스트 가공 
    # (시각, 차량번호, 내역 분리 & 차량번호, 시간 순으로 정렬)
    r = [i.split() for i in records]
    r.sort(key=lambda x : (x[1], x[0]))
    
    parking = dict() # 입차 시간 체크용 딕셔너리
    price = dict()   # 주차 시간 체크용 딕셔너리
    stack = []       # 출차 여부 체크용 리스트

    for car in r:
        # 입차인 경우
        if car[1] not in parking:
            parking[car[1]] = car[0]   # 입차 시간 추가
            stack.append(car[1])       # 차량 입차
            if car[1] not in price:    # 처음 온 경우 주차시간 추가
                price[car[1]] = 0
        # 출차인 경우
        else:
            h, m = map(int, parking[car[1]].split(":"))   # 입차 시간 정보 h, m
            h2, m2 = map(int, car[0].split(":"))          # 출차 시간 정보 h, m
            price[car[1]] += (h2 - h) * 60 + (m2 - m)     # 총 주차 시간 계산
            del parking[car[1]]                           # 차량 출차
            stack.pop()

    # 오늘 출차하지 않은 차량의 경우
    while stack:
        car = stack.pop()
        h, m = map(int, parking[car].split(":"))
        price[car] += (23 - h) * 60 + (59 - m)

    # 주차 시간에 따른 요금 계산
    from math import ceil       # 올림을 사용하기 위해 import
    ans = []                    # 정답 리스트
    for p in price.values():    # (이미 values() 리스트는 정렬되어 있기 때문에 순서대로 계산)
        ans.append(fees[1])     # 기본 요금 부과
        if p > fees[0]:         # 기본 시간 초과 주차 시 추가 요금 부과
            ans[-1] += ceil((p - fees[0]) / fees[2]) * fees[3]
    
    return ans
