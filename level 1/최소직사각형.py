def solution(sizes):
    width = [] # 가로가 더 길도록
    height = []

    for card in sizes:
        if card[0] < card[1]:
            width.append(card[1]) ; height.append(card[0])
        else:
            width.append(card[0]) ; height.append(card[1])

    return max(width) *max(height)
