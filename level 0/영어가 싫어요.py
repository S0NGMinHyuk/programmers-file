def solution(numbers):
    a = "zero one two three four five six seven eight nine"
    a = a.split()
    
    for i, eng in enumerate(a):
        numbers = numbers.replace(eng, str(i))
    return int(numbers)
