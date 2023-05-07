def solution(n):
    return hanoi(n, [])             # 재귀함수 호출


def hanoi(n, ans):
    if n == 1:
        return [[1, 3]]
    else:
        prior = hanoi(n-1, ans)     # 이전 하노이 배열 호출
        ans = [] 
        for p in prior:             # 이전 배열에서 2번, 3번 기둥을 서로 변경
            ans.append(change_a_and_b(p.copy(), 2, 3))
        
        ans.append([1, 3])          # 맨 아래 원판 이동

        for p in prior:             # 이전 배열에서 1번, 2번 기둥을 서로 변경
            ans.append(change_a_and_b(p.copy(), 1, 2))

    return ans


def change_a_and_b(p, a, b):        # a기둥과 <-> b기둥 변환
    if p[0] == a:
        p[0] = b
    elif p[0] == b:
        p[0] = a
    
    if p[1] == a:
        p[1] = b
    elif p[1] == b:
        p[1] = a
    
    return p
