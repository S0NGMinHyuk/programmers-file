def solution(k, d):
    # x축 위의 점 개수, +1은 (0, 0)
    dots = d//k + 1

    # x 좌표가 i 일 때 x축 제외 점의 갯수 추가
    for i in range(0, d, k):
        dots += ((d**2 - i**2)**0.5) // k

    return dots
