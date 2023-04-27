def solution(n, k):
    # numK 리스트에 찾을 수 있는 숫자 저장
    numk = ten_to_k(n, k).split("0")

    ans = 0
    # n이 ""인 경우를 제외하고 소수일 경우 ans값 1 증가
    for n in numk:
        if n.isdigit():
            ans += check_prime(int(n))
    
    return ans


# n을 k진수로 변환 후 문자열로 리턴
def ten_to_k(n, k):
    ans = []
    while n >= k:
        n, rest = divmod(n, k)
        ans.append(rest)
    else:
        ans.append(n)
    ans = list(map(str, ans))
    return "".join(ans[::-1])


# n이 소수인지 판별 (소수일 경우 1, 아니면 0 리턴)
def check_prime(n):
    if n <= 1:
        return 0

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 0    
    else:
        return 1


n, k = 110011, 10
print(solution(n,k))
