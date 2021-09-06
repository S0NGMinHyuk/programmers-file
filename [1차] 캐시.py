def solution(cacheSize, cities): # 캐시교체 알고리즘 LRU(Least Recently Used) 사용 문제
    time = 0 ; cache = []
    # time = 총 실행 시간, cache = 캐시 리스트

    for city in cities:
        city = city.upper()
        # city 이름을 통일하기 위해 대문자로 변경

        if city not in cache: # (Miss 의 경우)
            if len(cache) == cacheSize:
                try:
                    cache.pop(0)
                except:
                    return len(cities) *5
            # cache 리스트 안에 cacheSize 만큼 요소가 있으면 제일 오래된 것을 pop
            # cacheSize 가 0일 경우 time 이 무조건 len(cities)*5 이므로 바로 return 
            
            cache.append(city)
            time += 5
            # cache 에 city 를 추가, time 에 5 추가

        else: # (Hit 의 경우)
            cache.pop(cache.index(city))
            cache.append(city)
            time += 1
            # cache 내 city 를 제거하고 다시 추가, time 에 1 추가

    return time

size = 2
city = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(size, city))