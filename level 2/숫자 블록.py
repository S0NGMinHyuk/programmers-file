# 내 풀이
def solution(begin, end):
    answer = []
    for num in range(begin, end + 1):
        if num % 2 == 0 or num == 1:    # 짝수, 1인 경우 2로 나눈 값 추가
            answer.append(num // 2 if num < 20000000 else 10000000)
            continue
        
        for n in range(2, int(num**0.5) + 1):
            if num % n == 0 and num // n <= 10**7:
                answer.append(num//n)   # 홀수인 경우 가장 처음 나눠지는 값 추가 (10^7 이하)
                break
        else:
            answer.append(1)            # 홀수이며 소수인 경우 1 추가

    return answer


# 다른 사람의 풀이
def solution(begin, end):
    ans = []
    for n in range(begin, end + 1):
        k = 0 if n == 1 else 1
        for i in range(2, int(n**0.5) + 1): # 2부터 시작하므로 처음 나오는 n//i가 두번째로 큰 약수
            if n%i == 0 and n//i <= 10**7:  # 이미 1에서 다 나눠졌을 것이기 때문
                k = n//i
                break
        ans.append(k)
    return ans
