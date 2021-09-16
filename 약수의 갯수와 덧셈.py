def solution(left, right):
    answer = 0 # 정답용 변수

    for number in range(left, right +1):
        cnt = 0 # 약수 개수 체크용 변수
        for i in range(1, number +1):
            if number %i == 0:
                cnt += 1
            # i 가 약수면 cnt 1 증가
            
        if cnt %2 == 0:
            answer += number
        else:
            answer -= number
        # cnt 가 짝수면 덧셈, 홀수면 뺄셈

    return answer