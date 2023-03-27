def solution(wallpaper):
    # 파일들의 x, y 좌표 저장 리스트
    x = []
    y = []
    
    # 파일의 x, y 좌표를 각 리스트에 저장
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                x.append(j)
                y.append(i)
    
    # 정렬 후 x, y 좌표의 최대, 최소값 정제 후 리턴
    x.sort()
    y.sort()
    return [y[0], x[0], y[-1]+1, x[-1]+1]
