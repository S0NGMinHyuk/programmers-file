def solution(array):   # 내 풀이
    cnt = 0
    for num in array:
        for n in str(num):
            if n == "7":
                cnt  += 1
    return cnt


def solution(array):    # 다른사람의 풀이
    return str(array).count("7")
