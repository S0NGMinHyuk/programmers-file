def solution(triangle): # 아래에서부터 접근
    for floor in range(len(triangle)-2, -1, -1):
        for idx in range(len(triangle[floor])):
            # 자기 아래 값 2개 중 더 큰 값을 더하기
            triangle[floor][idx] += max(triangle[floor+1][idx], triangle[floor+1][idx+1])
    
    return triangle[0][0]

t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(t))
