def solution(k, ranges):
    # dic 자료형에 x 좌표에 따른 y 값 저장
    x = 0 ; dic = { x : k }
    while k != 1:
        k = k // 2 if k % 2 == 0 else k * 3 + 1
        x += 1 ; dic[x] = k
    

    answer = []
    for spot in ranges:
        # 정적분 시작 x 좌표, 끝 x 좌표
        start, end = spot[0], len(dic) + spot[1] - 1

        # start, end의 값에 따라 예외처리
        if start > end:
            answer.append(-1.0) ; continue
        elif start == end:
            answer.append(0.0) ; continue

        # 정적분 값 구하는 식
        ans = (dic[start] + dic[end]) / 2
        for i in range(start + 1, end):
            ans += dic[i]
        answer.append(ans)

    return answer
