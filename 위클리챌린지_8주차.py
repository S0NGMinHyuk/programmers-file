def solution(sizes):
    width = [] # 가로가 더 길도록
    height = []

    for card in sizes:
        if card[0] < card[1]:
            width.append(card[1]) ; height.append(card[0])
        else:
            width.append(card[0]) ; height.append(card[1])
    # width 에 더 큰 값을 추가

    return max(width) *max(height)

sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes)) # 정답 133