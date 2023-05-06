def solution(n):
    # 피보나치 수열을 사용
    num = [0] * 2000
    num[1], num[2] = 1, 2           # 피보나치 수열 초기 설정값
    idx = 3                         # index 3부터 시작
    while idx <= n:                 # 피보나치 수열 따라 num 채워가기
        num[idx] = (num[idx - 1] + num[idx - 2]) % 1234567
        idx += 1
    
    return num[n]                   # n번째 피보나치 수열 값 리턴
