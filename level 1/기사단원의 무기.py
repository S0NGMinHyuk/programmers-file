def solution(number, limit, power):
    answer = 0
    # 각 숫자별로 약수 개수 구하기
    for n in range(1, number + 1):
        # 제곱근이 자연수일 경우 약수 개수 하나 감소
        if int(n**0.5) == n**0.5:
            cnt = -1
        else:
            cnt = 0
        # 코드 효율을 위해 제곱근까지만 반복
        for i in range(1, int(n**0.5) + 1):
            if n%i == 0:
                cnt += 2

        if cnt <= limit:
            answer += cnt
        else:
            answer += power

    return answer
