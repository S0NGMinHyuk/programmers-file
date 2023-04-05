def solution(picks, minerals):
    hp = []
    for slicing in range(sum(picks)):
        # 광물을 5개씩 슬라이싱 후 돌곡괭이 기준 피로도로 변경
        m = minerals[slicing * 5:slicing * 5 + 5]
        for i in range(len(m)):
            if m[i] == "diamond":
                m[i] = 25
            elif m[i] == "iron":
                m[i] = 5
            else:
                m[i] = 1
        
        # 5개씩 나눠져 있는 피로도를 각 곡괭이로 캘 때의 피로도로 치환
        # hp 리스트에 [stone, iron, diamond] 리스트 추가
        if m:
            stone = sum(m)
            iron = 0
            for i in m:
                if i == 1:
                    iron += 1
                else:
                    iron += i//5
            hp.append([stone, iron, len(m)])
        # m이 빈 리스트인 경우는 주어진 곡괭이에 비해 캘 광물이 적은 경우
        # 슬라이싱 반복문 탈출
        else:
            break
    
    # 돌곡괭이 피로도 기준으로 내림차순 정렬
    hp.sort(key=lambda x : x[0], reverse=True)

    # 주어진 곡괭이(picks) 중 사용할 곡괭이 계산
    can_use = len(hp)
    for i in range(len(picks)):
        if can_use:
            if picks[i] <= can_use:
                can_use -= picks[i]
            else:
                picks[i] = can_use
                can_use = 0
        else:
            picks[i] = 0

    # 낮은 품질의 곡괭이부터 사용
    answer = 0
    for i, num in enumerate(reversed(picks)):
        for _ in range(num):
            answer += hp.pop()[i]
            
    return answer
