def solution(line):
    dots = []
    # line의 선분에 따라 정수 좌표 교점을 dots에 추가
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            dot = get_dot(line[i], line[j])
            if dot:
                dots.append(dot)

    # 배열 생성에 필요한 변수 가공
    minX, maxX, minY, maxY = get_min_max(dots)          # X, Y축의 최대/최소값
    X, Y = maxX - minX, maxY - minY                     # x, y축의 길이
    meanX, meanY = (maxX + minX)//2, (maxY + minY)//2   # X, Y축의 중심 좌표

    # 정답 배열 생성, dot에 따라 ans배열에 별 찍기
    # 작업 편의를 위해 거꾸로된 배열로 계산
    ans = ["."*(X + 1) for _ in range(Y + 1)] 
    for dot in dots:
        temp = list(ans[dot[0] + Y//2 - meanY])
        temp[dot[1] + X//2 - meanX] = "*"
        ans[dot[0] + Y//2 - meanY] = "".join(temp)
    
    # 배열 뒤집어 리턴
    return ans[::-1]


# 선분 a, b의 교점을 구하는 함수 ( [y, x]로 리턴 ) / 교점이 정수 좌표가 아닐 경우 False 리턴
def get_dot(a, b):
    A, B, E = a ; C, D, F = b

    # 두 선분이 평행하는 경우
    if (A*D - B*C) == 0:
        return False
    
    x = (B*F - E*D) / (A*D - B*C)
    y = (E*C - A*F) / (A*D - B*C)
    if x % 1 == 0 and y % 1 == 0: 
        return [int(y), int(x)]
    else: # 교점에 정수 좌표가 아닐 경우
        return False


# x, y 좌표의 최대/최소값을 구하는 함수
def get_min_max(dots):
    ans = [None] * 4    # [minX, maxX, minY, maxY]

    for dot in dots:
        if ans[0] == None or ans[0] > dot[1]:
            ans[0] = dot[1]
        if ans[1] == None or ans[1] < dot[1]:
            ans[1] = dot[1]
        if ans[2] == None or ans[2] > dot[0]:
            ans[2] = dot[0]
        if ans[3] == None or ans[3] < dot[0]:
            ans[3] = dot[0]

    return ans
