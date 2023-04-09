def solution(elements):
    total, length = sum(elements), len(elements)
    answer = [total]

    # 슬라이싱 편의를 위해 elements 리스트를 2개 이어붙이기
    elements = elements * 2

    """ num개의 수열 합을 구하고 total에서 temp만큼 합을 빼면 
        length - num개의 수열 합을 알 수 있다.
        그래서 length의 절반만큼만 수열 합을 구하면 된다. """
    for num in range(1, length//2 + 1):
        for i in range(length):
            # num개의 수열 만큼 슬라이싱
            temp = sum(elements[i:i + num])

            answer.append(temp)
            answer.append(total - temp)

    # set 자료형을 이용해 중복값 제거
    return len(set(answer))
