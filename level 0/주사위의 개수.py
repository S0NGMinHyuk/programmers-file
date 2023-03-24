def solution(box, n):
    width, length, height = box
    return (width // n) * (length // n) * (height // n)
