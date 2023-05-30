def solution(n):
    # 문제 풀이 점화식 -> f(n) = f(n-2)*4 - f(n-4)
    lst = [0] * 5001    # n이 5000 이하의 자연수
    lst[2] = 3          # 점화식 초기값 설정
    lst[4] = 11

    if n%2 == 0:        
        for i in range(6, n+1, 2):
            lst[i] = (lst[i-2]*4 - lst[i-4] + 1000000007) % 1000000007  # 점화식 과정에서 음수 값 방지
    
    return lst[n]       # 시간복잡도 O(N/2) = O(N)
