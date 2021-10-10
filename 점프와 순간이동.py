def solution(n):
    ans = 0                 # 사용한 에너지량
    while n > 0:
        if n % 2 == 0:      # n이 짝수일 경우 텔레포트를 사용, 에너지가 들지 않음
            n = n//2
        else:               # n이 홀수일 경우 점프를 사용, 에너지를 1 사용
            n -= 1
            ans += 1
    return ans

print(solution(5000))       # 정답 5