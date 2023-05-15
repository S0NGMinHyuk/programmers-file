def solution(n, l, r):
    return get_sum(n, l, r, 0)  # 재귀함수 호출


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
