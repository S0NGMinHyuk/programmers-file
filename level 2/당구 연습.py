def solution(m, n, startX, startY, balls):
    result = []
    for ball in balls:
        ans, sp = 0, get_SP(m, n, startX, startY, ball)     # 최소 거리값 / x, y 좌표의 대칭점
        for start in sp:
            distance = get_distace(start, ball)             # 각 대칭점과 ball좌표 사이를 구해 최소값 추가
            ans = distance if ans == 0 or ans > distance else ans
        result.append(ans)                  # 공이 꼭짓점에 튕기는 경우는 최소값이 될 수 없으므로 구하지 않음
    return result

# x, y 좌표와 상하좌우 벽 사이 대칭점 리스트 리턴
def get_SP(m, n, x, y, ball):
    ans = [(x, 2*n - y), (x, -y), (2*m - x, y), (-x, y)]
    # x, y와 대칭점 사이 ball좌표가 있으면 해당 대칭점 삭제
    if x == ball[0]:
        idx = 0 if y < ball[1] else 1
        ans.pop(idx)
    elif y == ball[1]:
        idx = 2 if x < ball[0] else 3
        ans.pop(idx)
    return ans

# start좌표와 ball좌표 사이 거리값 리턴
def get_distace(start, ball):
    return (ball[0] - start[0])**2 + (ball[1] - start[1])**2


m, n, x, y, ball = 10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]
print(solution(m, n, x, y, ball))
