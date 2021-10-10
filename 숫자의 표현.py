def solution(n):
    cnt = 0
    for i in range(1, n+1):
        sumN = 0
        for j in range(i, n+1):
            sumN += j                # 무작정 i값부터 sum에 추가
            if sumN == n:
                cnt += 1             # sum이 n과 같을 때 cnt를 하나 증가
                break                # 무의미한 반복을 피하기 위해 break
            elif sumN > n:
                break                # sum이 n보다 클 때도 무의미한 반복을 피하기 위해 break
    return cnt

print(solution(15))                  # 정답 4