def solution(n, k):
    # numk에 k진수 리스트 저장
    numk = ten_to_k(n, k)
    ans = 0 ; idx = 0
    # numk를 앞에서부터 탐색하며 조건에 맞는 숫자(n) 탐색
    while idx < len(numk):
        n = numk[idx]
        idx += 1
        while idx < len(numk) and numk[idx] != 0:
            n = n * 10 + numk[idx]
            idx += 1
        
        # n이 소수일 경우 ans값 1 증가
        if n > 1:
            ans += check_prime(n)
    return ans


# n을 k진수로 변환 후 리스트로 리턴
def ten_to_k(n, k):
    ans = []
    while n >= k:
        n, rest = divmod(n, k)
        ans.append(rest)
    else:
        ans.append(n)
    return ans[::-1]


# n이 소수인지 판별 (소수일 경우 1, 아니면 0 리턴)
def check_prime(n):
    if n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0
    return 1
