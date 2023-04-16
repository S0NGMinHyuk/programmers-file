def solution(want, number, discount):
    # 구매할 10가지 품목 리스트 생성
    temp = []
    for w, n in zip(want, number):
        for _ in range(n):
            temp.append(w)
    want = sorted(temp)

    # discount 리스트에서 차례대로 10개씩 탐색
    ans = 0
    for i in range(len(discount) - 9):
        temp = sorted(discount[i:i+10])
        if temp == want:
            ans += 1
    
    return ans
