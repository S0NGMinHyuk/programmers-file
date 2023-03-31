def solution(ingredient):
    ing = []
    cnt = 0
    for i in ingredient:
        ing.append(i)
        if ing[-4:] == [1, 2, 3, 1]:
            cnt += 1
            # 리스트 슬라이싱보다 pop 함수가 더 빠르다
            # 리스트 슬라이싱보다 문자열 슬라이싱이 더 빠르다
            for _ in range(4):
                ing.pop()
    return cnt
