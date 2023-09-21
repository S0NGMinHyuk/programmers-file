def solution(sticker):
    if len(sticker) == 1:   # 스티커가 1장일 경우
        return sticker[0]
    
    dp1 = sticker[:-1]  # 첫 번째 스티커 사용
    dp2 = sticker[1:]   # 첫 번째 스티커 미사용

    return max(getBig(dp1), getBig(dp2))


def getBig(array):
    for i in range(1, len(array)):
        if i == 1:
            array[i] = max(array[0], array[i])
        else:
            array[i] = max(array[i-1], array[i-2]+array[i])
#                         안뽑는 경우,      뽑는 경우

    return array[-1]
