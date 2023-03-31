def solution(k, m, score):
    # 제일 최상품인 사과 순서로 m개씩 포장
    score.sort(reverse=True)
    box = [score[i:i+m] for i in range(0, len(score), m)]

    # 박스의 사과 개수가 m개라면 price에 가격 추가
    price = 0
    for b in box:
        if len(b) == m:
            price += min(b) * len(b)
    
    return price
