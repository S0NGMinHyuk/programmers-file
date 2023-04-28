def solution(users, emoticons):
    ans = [0, 0]            # 정답 리스트
    n = len(emoticons)      # 이모티콘 개수

    # 이모티콘 별 할인률 리스트 생성
    from itertools import product
    sales = list(product([10, 20, 30, 40], repeat=n))
    
    for s in sales:
        register, price = 0, 0    # 총 가입자, 총 구매금액
        for u in users:
            cost = 0              # 유저 별 구매금액
            for i in range(n):
                if s[i] >= u[0]:  # 할인률이 유저 기준 이상일 경우 구매
                    cost += emoticons[i] * (100 - s[i]) // 100

            if cost >= u[1]:      # 구매금액이 유저 기준 이상일 경우 가입
                register += 1
            else:                 # 구매금액이 유저 기준 이하일 경우 구매
                price += cost 
        
        # 각 할인율 별 최대한의 가입자, 최고 구매액을 계산해 ans에 추가
        if register > ans[0] or (register == ans[0] and price > ans[1]):
            ans = [register, price]
    
    return ans


u, e = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]
print(solution(u, e))
