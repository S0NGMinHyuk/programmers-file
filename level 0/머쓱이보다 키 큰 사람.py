def solution(array, height):
    array.sort()
    for i in range(len(array)):
        if array[i] > height:
            return len(array) - i
    return 0
