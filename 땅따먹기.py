def solution(land):                   # 다이나믹 프로그래밍(동적 계획법, aka DP)
    answer = [0, 0, 0, 0]             # 이전 행까지의 누적합중 이번 칸과 열이 다르고 가장 큰 값을 골라 이번 칸과 더해주는 방식
    for row in land:
        answer_c = answer.copy()      # answer 값 복사 (복사하지 않고 그냥 쓰면 밑의 코드가 꼬임)
        for index in range(4):        # index = answer의 인덱스 역할
            big = 0                   # 누적합 중 이번 칸과 열이 다르고 가장 큰 값
            for i in range(4):
                if (i == index):      # 누적합 중 index와 같은 열의 누적합은 쓸 수 없다
                    continue
                elif (answer[i] > big):
                    big = answer[i]
            else:
                answer_c[index] = big + row[index]  # answer_c = 인덱스에 최대 누적합 + 지금 열의 값
        else:
            answer = answer_c

    return max(answer)                # 최대값 출력


land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))                 # 정답: 16 (5+7+4)