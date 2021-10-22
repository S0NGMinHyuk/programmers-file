def solution(n):
    for i in range(2, n):   # 1은 어차피 나머지가 0일 테니까
        if n % i == 1:      # 나머지가 1인 경우
            return i        # i 리턴