# 내 풀이
def solution(n, l, r):
    def get_sum(n, l, r, ans):
        if n == 1:                  # 재귀함수 종료 조건
            for i in range(l, r+1): # n이 1일 때는 1의 개수를 셀 수 있다.
                if i%5 != 3: ans += 1
            return ans

        l_share, l_rest = divmod(l, 5**(n-1))   # l과 r의 몫과 나머지를 통해 분할
        r_share, r_rest = divmod(r, 5**(n-1))
        if l_rest == 0:                         # l은 rest가 0일 경우 값 변경
            l_share -= 1 ; l_rest = 5**(n-1)

        if l_share == r_share:  # l과 r의 몫이 같으면 n을 1 줄일 수 있다.
            if l_share != 2:    # l과 r의 몫이 2인 경우, 1의 개수는 0이다.
                return get_sum(n-1, l_rest,r_rest, ans)
            else: 
                return ans


        for i in range(l_share+1, r_share):     # l과 r의 몫 사이(분할하지 않는 부분) 1의 개수는 4의 n-1승
            if i != 2: ans += 4**(n-1)     

        if l_share != 2: ans = get_sum(n-1, l_rest, 5**(n-1), ans)  # l과 r 분할
        if r_share != 2: ans = get_sum(n-1, 1 ,r_rest, ans)

        return ans
    return get_sum(n, l, r, 0)  # 재귀함수 호출


# 다른 사람의 풀이 1 (내 풀이와 비슷한 방식이지만 훨씬 코드가 간결하다.)
def solution(n, l, r):
    def get_sum(n, pos):    # 1부터 pos까지 1의 개수를 구하는 함수
        if n == 1:  return "11011"[:pos].count("1") # 종료조건 1
    
        a, b = divmod(pos, 5**(n-1))
        if a < 2:       # 몫에 따라 4^n-1을 더하고 나머지 분할재귀
            return 4**(n-1)*a + get_sum(n-1, b)
        elif a == 2:    # 종료조건 2
            return 4**(n-1)*a
        else: # a > 2
            return 4**(n-1)*(a-1) + get_sum(n-1, b)
    return get_sum(n, r) - get_sum(n, l-1)  # 1부터 r까지 1의 개수 - 1부터 l-1까지 1의 개수


# 다른 사람의 풀이 2 (완전히 다른 방식이며, 상상도 못한 방법이다.)
def solution(n, l, r):
    answer = r-l+1              # 모든 값이 1이라고 가정
    for num in range(l-1,r):    # num 값이 1인지 0인지 판별
        while num>=1:           # 반복문 탈출 = num 값이 1
            a,b=divmod(num,5)
            if b==2 or a==2:    # num 값이 0이면 ans -= 1 후 반복문 탈출
                answer-=1
                break
            num=a
    return answer
