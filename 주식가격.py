def solution(prices):
    answer = [] # 정답용 리스트

    for i in range(len(prices)):
        target, cnt = prices[i], 0
        # target = 값을 확인할 주식 변수
        # cnt = 몇초동안 값이 안 떨어지는지 확인할 변수

        for j in range(i +1, len(prices)):
            # prices[j] = target 이후의 주식 값들
            if target <= prices[j]:
                cnt += 1
            else:
                answer.append(cnt +1)
                break
                # 이후 주식 값이 target 보다 작으면 cnt +1 해서 answer 에 추가
                # 더이상 의미없는 반복을 피하기 위해 break 로 for 문 탈출
        else:
            answer.append(cnt)
            # for 문이 다 돌면 cnt 값을 answer 에 추가
            # break 로 탈출할 경우엔 else 문을 돌지 않는 점을 이용

    return answer

prices = [1, 2, 3, 1, 2, 3]
print(solution(prices))