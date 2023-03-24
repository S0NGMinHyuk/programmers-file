def solution(numbers, direction):
    if direction == "right":
        temp = numbers.pop()
        return [temp] + numbers
    else:           # left
        temp = numbers.pop(0)
        return numbers + [temp]
