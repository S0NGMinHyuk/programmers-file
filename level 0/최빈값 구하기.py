def solution(array):
    while len(array) > 1:
        temp = set(array)
        for i in temp:
            array.remove(i)
            
    if len(array):
        return array[0]
    else:
        return -1
