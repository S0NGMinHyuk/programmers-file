def solution(n):
    result = []
    if n % 2 == 0:                    # n이 짝수일 경우 홀수로 변경
        result.append(2)
        while n % 2 == 0:
            n = n // 2
    
    while n != 1:
        for i in range(3, n+1, 2):    # 소인수 찾기
            if n % i == 0:
                result.append(i)
                n = n // i
                break
    
    return sorted(list(set(result)))  # set 자료형을 통해 중복값 제거
