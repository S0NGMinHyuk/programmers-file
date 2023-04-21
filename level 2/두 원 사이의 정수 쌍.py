def solution(r1, r2):
    answer = dot_in_circle_for_big(r2) - dot_in_circle_for_small(r1)
    # 뒤의 4는 r1의 x축, y축 점 갯수
    return answer + 4


def dot_in_circle_for_big(num):
    cnt = num
    for i in range(num - 1, 0, -1):
        cnt += int((num**2 - i**2)**0.5)
        
    return cnt * 4


def dot_in_circle_for_small(num):
    cnt = num
    for i in range(num - 1, 0, -1):
        # 변경된 부분 / 점이 선 위에 있는 경우
        a = (num**2 - i**2)**0.5
        if a == int(a):
            cnt -= 1
        cnt += int(a)

    return cnt * 4


r, rr = 2, 3
print(solution(r, rr))
